from enum import Enum

from .siso_ref_010.enums.variable_record_type import VariableRecordType

class StandardVariableRecord( object ):
    """Section 6.2.83"""

    def __init__(self):
        """ Initializer for StandardVariableRecord"""
        # /**  uid 66 Variable Record Type values are defined by VariableRecordType enumerations */
        self.recordType = VariableRecordType.default

        self.recordLength = 0
        self.recordSpecificFields =  []
        self.padding = [0] * 64

    def to_string(self) ->str:
        outputString = ""
        outputString += "VariableRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "RecordSpecificFields : " + "\n"
        for idx in range(0, len(self.recordSpecificFields)):
            outputString += str(self.recordSpecificFields[idx])

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
        outputStream.write_short(int(self.recordLength))
        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.recordSpecificFields[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = VariableRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.recordLength = inputStream.read_short()
        self.recordSpecificFields = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.recordSpecificFields[  idx  ] = val


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 4

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



