from enum import Enum

from .siso_ref_010.enums.variable_record_type import VariableRecordType

class RecordSpecificationElement( object ):
    """Synthetic record, made up from section 6.2.73. This is used to achieve a repeating variable list element.<p>recordLength, recordCount and recordValues must be set by hand so the."""

    def __init__(self):
        """ Initializer for RecordSpecificationElement"""
        # /** The data structure used to convey the parameter values of the record for each record. 32-bit enumeration. uid = 66 */
        self.recordID = VariableRecordType.default

        """ The serial number of the first record in the block of records"""
        self.recordSetSerialNumber = 0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """  the length, in bits, of the record. Note, bits, not bytes."""
        self.recordLength = 0
        """  the number of records included in the record set """
        self.recordCount = 0
        """ The concatenated records of the format specified by the Record ID field. The length of this field is the Record Length multiplied by the Record Count, in units of bits."""
        self.recordValues =  []
        """ used if required to make entire record size an even multiple of 8 bytes"""
        self.padTo64 =  []

    def to_string(self) ->str:
        outputString = ""
        outputString += "VariableRecordType : " + self.recordID.get_description + "(" + (str(int(self.recordID))) + ")" + "\n"
        outputString += "RecordSetSerialNumber : " + str(self.recordSetSerialNumber) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "RecordCount : " + str(self.recordCount) + "\n"
        outputString += "RecordValues : " + "\n"
        for idx in range(0, len(self.recordValues)):
            outputString += str(self.recordValues[idx])

        outputString += "PadTo64 : " + "\n"
        for idx in range(0, len(self.padTo64)):
            outputString += str(self.padTo64[idx])

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
        self.serialize_enum(self.recordID,outputStream)
        outputStream.write_int(int(self.recordSetSerialNumber))
        outputStream.write_int(int(self.padding))
        outputStream.write_short(int(self.recordLength))
        outputStream.write_short(int(self.recordCount))
        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.recordValues[ idx ] );

        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.padTo64[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordID = VariableRecordType.get_enum(self.parse_enum(self.recordID,inputStream))
        self.recordSetSerialNumber = inputStream.read_int()
        self.padding = inputStream.read_int()
        self.recordLength = inputStream.read_short()
        self.recordCount = inputStream.read_short()
        self.recordValues = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.recordValues[  idx  ] = val

        self.padTo64 = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.padTo64[  idx  ] = val


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



