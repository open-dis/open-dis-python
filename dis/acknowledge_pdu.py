from enum import Enum

from .simulation_management_family_pdu import SimulationManagementFamilyPdu
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.acknowledge_acknowledge_flag import AcknowledgeAcknowledgeFlag
from .siso_ref_010.enums.acknowledge_response_flag import AcknowledgeResponseFlag

class AcknowledgePdu( SimulationManagementFamilyPdu ):
    """7.5.6 Acknowledges the receipt of a Start/Resume PDU, Stop/Freeze PDU, Create Entity PDU, or Remove Entity PDU. See 5.6.5.6."""

    def __init__(self):
        """ Initializer for AcknowledgePdu"""
        super().__init__()
        # /** type of message being acknowledged uid 69 */
        self.acknowledgeFlag = AcknowledgeAcknowledgeFlag.default

        # /** Whether or not the receiving entity was able to comply with the request uid 70 */
        self.responseFlag = AcknowledgeResponseFlag.default

        """ Request ID that is unique"""
        self.requestID = 0
        self.pduType = DisPduType.acknowledge

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "AcknowledgeAcknowledgeFlag : " + self.acknowledgeFlag.get_description + "(" + (str(int(self.acknowledgeFlag))) + ")" + "\n"
        outputString += "AcknowledgeResponseFlag : " + self.responseFlag.get_description + "(" + (str(int(self.responseFlag))) + ")" + "\n"
        outputString += "RequestID : " + str(self.requestID) + "\n"
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
        super( AcknowledgePdu, self ).serialize(outputStream)
        self.serialize_enum(self.acknowledgeFlag,outputStream)
        self.serialize_enum(self.responseFlag,outputStream)
        outputStream.write_int(int(self.requestID))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( AcknowledgePdu, self).parse(inputStream)
        self.acknowledgeFlag = AcknowledgeAcknowledgeFlag.get_enum(self.parse_enum(self.acknowledgeFlag,inputStream))
        self.responseFlag = AcknowledgeResponseFlag.get_enum(self.parse_enum(self.responseFlag,inputStream))
        self.requestID = inputStream.read_int()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 3

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



