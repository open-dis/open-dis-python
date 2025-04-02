from enum import Enum

from .iorecord import IORecord
from .siso_ref_010.enums.iocomms_node_record_comms_node_type import IOCommsNodeRecordCommsNodeType
from .siso_ref_010.enums.variable_record_type import VariableRecordType
from .communications_node_id import CommunicationsNodeID

class IOCommsNodeRecord( IORecord ):
    """6.2.48.2"""

    def __init__(self):
        """ Initializer for IOCommsNodeRecord"""
        super().__init__()
        # /**  uid 66 Variable Record Type values are defined by VariableRecordType enumerations */
        self.recordType = VariableRecordType.io_communications_node

        self.recordLength = 0
        # /**  uid 294 */
        self.commsNodeType = IOCommsNodeRecordCommsNodeType.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        # commsNodeId is an undescribed parameter... 
        self.commsNodeId = CommunicationsNodeID()

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "VariableRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "IOCommsNodeRecordCommsNodeType : " + self.commsNodeType.get_description + "(" + (str(int(self.commsNodeType))) + ")" + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "CommsNodeId :" + "\n" + self.commsNodeId.to_string() + "\n"
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
        super( IOCommsNodeRecord, self ).serialize(outputStream)
        self.serialize_enum(self.recordType,outputStream)
        outputStream.write_short(int(self.recordLength))
        self.serialize_enum(self.commsNodeType,outputStream)
        outputStream.write_byte(int(self.padding))
        self.commsNodeId.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( IOCommsNodeRecord, self).parse(inputStream)
        self.recordType = VariableRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.recordLength = inputStream.read_short()
        self.commsNodeType = IOCommsNodeRecordCommsNodeType.get_enum(self.parse_enum(self.commsNodeType,inputStream))
        self.padding = inputStream.read_byte()
        self.commsNodeId.parse(inputStream)

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



