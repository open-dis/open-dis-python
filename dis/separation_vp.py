from enum import Enum

from .named_location_identification import NamedLocationIdentification
from .siso_ref_010.enums.separation_vpreasonfor_separation import SeparationVPReasonforSeparation
from .siso_ref_010.enums.separation_vppre_entity_indicator import SeparationVPPreEntityIndicator
from .siso_ref_010.enums.variable_parameter_record_type import VariableParameterRecordType
from .entity_id import EntityID

class SeparationVP( object ):
    """Physical separation of an entity from another entity.  Section 6.2.94.6"""

    def __init__(self):
        """ Initializer for SeparationVP"""
        # /** The identification of the Variable Parameter record. Enumeration from EBV uid 56 */
        self.recordType = VariableParameterRecordType.separation

        # /** Reason for separation. EBV uid 282 */
        self.reasonForSeparation = SeparationVPReasonforSeparation.default

        # /** Whether the entity existed prior to separation EBV uid 283 */
        self.preEntityIndicator = SeparationVPPreEntityIndicator.default

        """ padding"""
        self.padding1 = 0
        """ ID of parent"""
        self.parentEntityID = EntityID()
        """ padding"""
        self.padding2 = 0
        """ Station separated from"""
        self.stationLocation = NamedLocationIdentification()

    def to_string(self) ->str:
        outputString = ""
        outputString += "VariableParameterRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "SeparationVPReasonforSeparation : " + self.reasonForSeparation.get_description + "(" + (str(int(self.reasonForSeparation))) + ")" + "\n"
        outputString += "SeparationVPPreEntityIndicator : " + self.preEntityIndicator.get_description + "(" + (str(int(self.preEntityIndicator))) + ")" + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "ParentEntityID :" + "\n" + self.parentEntityID.to_string() + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "StationLocation :" + "\n" + self.stationLocation.to_string() + "\n"
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
        self.serialize_enum(self.reasonForSeparation,outputStream)
        self.serialize_enum(self.preEntityIndicator,outputStream)
        outputStream.write_byte(int(self.padding1))
        self.parentEntityID.serialize(outputStream)
        outputStream.write_short(int(self.padding2))
        self.stationLocation.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = VariableParameterRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.reasonForSeparation = SeparationVPReasonforSeparation.get_enum(self.parse_enum(self.reasonForSeparation,inputStream))
        self.preEntityIndicator = SeparationVPPreEntityIndicator.get_enum(self.parse_enum(self.preEntityIndicator,inputStream))
        self.padding1 = inputStream.read_byte()
        self.parentEntityID.parse(inputStream)
        self.padding2 = inputStream.read_short()
        self.stationLocation.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 7

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



