from enum import Enum

from .siso_ref_010.enums.variable_record_type import VariableRecordType

class RecordQuerySpecification( object ):
    """The identification of the records being queried 6.2.72"""

    def __init__(self):
        """ Initializer for RecordQuerySpecification"""
        self.numberOfRecords = 0
        """ variable length list of 32-bit record types uid = 66"""
        self._recordIDs = []


    def get_numberOfRecords(self):
        return len(self._recordIDs)
    def set_numberOfRecords(self, value):
        numberOfRecords = value


    def get_recordIDs(self):
        return self._recordIDs
    def set_recordIDs(self, value):
        self._recordIDs = value
    recordIDs = property(get_recordIDs, set_recordIDs)


    def add_recordIDs(self, value : VariableRecordType):
        self._recordIDs.append(value)


    """
    ///            Name : recordIDs
    ///             UID : =66
    ///            Type : VariableRecordType
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of 32-bit record types uid = 66
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : SISO_ENUM
    /// underlying Type : IsEnum
    """



    def to_string(self) ->str:
        outputString = ""
        outputString += "NumberOfRecords : " + str(len(self._recordIDs)) + "\n"
        outputString += "RecordIDs : " + "\n"
        for idx in range(0, len(self._recordIDs)):
            outputString += self._recordIDs[idx].to_string()

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
        outputStream.write_int( len(self._recordIDs))
        for anObj in self._recordIDs:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.numberOfRecords = inputStream.read_int()
        for idx in range(0, self.numberOfRecords):
            element = VariableRecordType()
            element.parse(inputStream)
            self._recordIDs.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 2

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



