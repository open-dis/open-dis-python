from enum import Enum

from .siso_ref_010.enums.disprotocol_version import DISProtocolVersion
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.disprotocol_family import DISProtocolFamily

class Pdu( object ):
    """Base class of PduBase and LiveEntityPdu"""

    def __init__(self):
        """ Initializer for Pdu"""
        # /** The version of the protocol. 5=DIS-1995, 6=DIS-1998, 7=DIS-2012 uid 3 */
        self.protocolVersion = DISProtocolVersion.ieee_12781_2012

        """ Exercise ID provides a unique identifier"""
        self.exerciseID = 0
        # /** Type of pdu, unique for each PDU class uid 4 */
        self.pduType = DisPduType.default

        # /** value that refers to the protocol family, eg SimulationManagement, et uid 5 */
        self.protocolFamily = DISProtocolFamily.default

        """ Timestamp value, int representing number of 1.675 microseconds as interval past hour"""
        self.timestamp = 0
        """ Length, in bytes, of the PDU"""
        self.length = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "DISProtocolVersion : " + self.protocolVersion.get_description + "(" + (str(int(self.protocolVersion))) + ")" + "\n"
        outputString += "ExerciseID : " + str(self.exerciseID) + "\n"
        outputString += "DisPduType : " + self.pduType.get_description + "(" + (str(int(self.pduType))) + ")" + "\n"
        outputString += "DISProtocolFamily : " + self.protocolFamily.get_description + "(" + (str(int(self.protocolFamily))) + ")" + "\n"
        outputString += "Timestamp : " + str(self.timestamp) + "\n"
        outputString += "Length : " + str(self.length) + "\n"
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
        self.serialize_enum(self.protocolVersion,outputStream)
        outputStream.write_byte(int(self.exerciseID))
        self.serialize_enum(self.pduType,outputStream)
        self.serialize_enum(self.protocolFamily,outputStream)
        outputStream.write_int(int(self.timestamp))
        outputStream.write_short(int(self.length))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.protocolVersion = DISProtocolVersion.get_enum(self.parse_enum(self.protocolVersion,inputStream))
        self.exerciseID = inputStream.read_byte()
        self.pduType = DisPduType.get_enum(self.parse_enum(self.pduType,inputStream))
        self.protocolFamily = DISProtocolFamily.get_enum(self.parse_enum(self.protocolFamily,inputStream))
        self.timestamp = inputStream.read_int()
        self.length = inputStream.read_short()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 6

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



