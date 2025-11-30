from enum import Enum

from .entity_type import EntityType
from .siso_ref_010.enums.entity_vprecord_change_indicator import EntityVPRecordChangeIndicator
from .siso_ref_010.enums.variable_parameter_record_type import VariableParameterRecordType

class EntityTypeVP( object ):
    """Association or disassociation of two entities.  Section 6.2.94.5"""

    def __init__(self):
        """ Initializer for EntityTypeVP"""
        # /** The identification of the Variable Parameter record. uid 56 */
        self.recordType = VariableParameterRecordType.entity_type

        # /** Indicates if this VP has changed since last issuance uid 320 */
        self.changeIndicator = EntityVPRecordChangeIndicator.default

        """ """
        self.entityType = EntityType()
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ padding"""
        self.padding1 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "VariableParameterRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "EntityVPRecordChangeIndicator : " + self.changeIndicator.get_description + "(" + (str(int(self.changeIndicator))) + ")" + "\n"
        outputString += "EntityType :" + "\n" + self.entityType.to_string() + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
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
        self.serialize_enum(self.changeIndicator,outputStream)
        self.entityType.serialize(outputStream)
        outputStream.write_short(int(self.padding))
        outputStream.write_int(int(self.padding1))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = VariableParameterRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.changeIndicator = EntityVPRecordChangeIndicator.get_enum(self.parse_enum(self.changeIndicator,inputStream))
        self.entityType.parse(inputStream)
        self.padding = inputStream.read_short()
        self.padding1 = inputStream.read_int()

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



