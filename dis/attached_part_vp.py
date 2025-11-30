from enum import Enum

from .entity_type import EntityType
from .siso_ref_010.enums.attached_part_detached_indicator import AttachedPartDetachedIndicator
from .siso_ref_010.enums.variable_parameter_record_type import VariableParameterRecordType
from .siso_ref_010.enums.attached_parts import AttachedParts

class AttachedPartVP( object ):
    """Removable parts that may be attached to an entity.  Section 6.2.93.3"""

    def __init__(self):
        """ Initializer for AttachedPartVP"""
        # /** The identification of the Variable Parameter record. Enumeration from EBV uid 56 */
        self.recordType = VariableParameterRecordType.attached_part

        # /** 0 = attached, 1 = detached. See I.2.3.1 for state transition diagram uid 415 */
        self.detachedIndicator = AttachedPartDetachedIndicator.default

        """ The identification of the articulated part to which this articulation parameter is attached. This field shall be specified by a 16-bit unsigned integer. This field shall contain the value zero if the articulated part is attached directly to the entity."""
        self.partAttachedTo = 0
        # /** The location or station to which the part is attached uid 57 */
        self.parameterType = AttachedParts.default

        """ The definition of the 64-bits shall be determined based on the type of parameter specified in the Parameter Type field """
        self.attachedPartType = EntityType()

    def to_string(self) ->str:
        outputString = ""
        outputString += "VariableParameterRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "AttachedPartDetachedIndicator : " + self.detachedIndicator.get_description + "(" + (str(int(self.detachedIndicator))) + ")" + "\n"
        outputString += "PartAttachedTo : " + str(self.partAttachedTo) + "\n"
        outputString += "AttachedParts : " + self.parameterType.get_description + "(" + (str(int(self.parameterType))) + ")" + "\n"
        outputString += "AttachedPartType :" + "\n" + self.attachedPartType.to_string() + "\n"
        return outputString

    def __str__(self):
        return self.to_string()

    def serialize_enum(self, enumValue, outputStream):
        enumSize = enumValue.get_marshaled_size()
        marshallers = {8 : 'byte', 16 : 'short', 32 : 'int'}
        marshalFunction = getattr(outputStream, 'write_unsigned_' + marshallers[enumSize])
        result = marshalFunction(int(enumValue))

    def parse_enum(self, enumValue, intputStream) -> int:
        enumSize = enumValue.get_marshaled_size()
        marshallers = {8 : 'byte', 16 : 'short', 32 : 'int'}
        marshalFunction = getattr(intputStream, 'read_unsigned_' + marshallers[enumSize])
        return marshalFunction()

    def serialize(self, outputStream):
        """serialize the class """
        self.serialize_enum(self.recordType,outputStream)
        self.serialize_enum(self.detachedIndicator,outputStream)
        outputStream.write_short(int(self.partAttachedTo))
        self.serialize_enum(self.parameterType,outputStream)
        self.attachedPartType.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = VariableParameterRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.detachedIndicator = AttachedPartDetachedIndicator.get_enum(self.parse_enum(self.detachedIndicator,inputStream))
        self.partAttachedTo = inputStream.read_short()
        self.parameterType = AttachedParts.get_enum(self.parse_enum(self.parameterType,inputStream))
        self.attachedPartType.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 5

    def get_attribute_count(self) -> int:
        attrList = list()
        for attr in dir(self):
            if not callable(getattr(self, attr)):
                if not attr.startswith("__"):
                    if not hasattr(self.__class__.__base__(), attr):
                        attrList.append(attr)
        return len(attrList)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def diff(self,other) -> set:
        diffs = set()
        for key, value in self.__dict__.items():
            value2 = other.__dict__[key]
            if (value != value2):
                if type(value) is list:
                    diffs.add((key, str(value)))
                    diffs.add((key, str(value2)))
                elif (type(value).__module__ == "builtins"):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, Enum)):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, object)):
                    diffs.update(value.diff(value2))
                else:
                    diffs.add((key, value))
                    diffs.add((key, value2))
        return(diffs)



