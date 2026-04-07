from enum import Enum

from .iffdata import IFFData

class IFFDataSpecification( object ):
    """Requires hand coding to be useful. Section 6.2.43"""

    def __init__(self):
        """ Initializer for IFFDataSpecification"""
        """ Number of IFF records"""
        self.numberOfIFFDataRecords = 0
        """ IFF data records"""
        self._iffDataRecords = []


    def get_numberOfIFFDataRecords(self):
        return len(self._iffDataRecords)
    def set_numberOfIFFDataRecords(self, value):
        numberOfIFFDataRecords = value


    def get_iffDataRecords(self):
        return self._iffDataRecords
    def set_iffDataRecords(self, value):
        self._iffDataRecords = value
    iffDataRecords = property(get_iffDataRecords, set_iffDataRecords)


    def add_iffDataRecords(self, value : IFFData):
        self._iffDataRecords.append(value)


    """
    ///            Name : iffDataRecords
    ///             UID : 
    ///            Type : IFFData
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : IFF data records
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """



    def to_string(self) ->str:
        outputString = ""
        outputString += "NumberOfIFFDataRecords : " + str(len(self._iffDataRecords)) + "\n"
        outputString += "IffDataRecords : " + "\n"
        for idx in range(0, len(self._iffDataRecords)):
            outputString += self._iffDataRecords[idx].to_string()

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
        outputStream.write_short( len(self._iffDataRecords))
        for anObj in self._iffDataRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.numberOfIFFDataRecords = inputStream.read_short()
        for idx in range(0, self.numberOfIFFDataRecords):
            element = IFFData()
            element.parse(inputStream)
            self._iffDataRecords.append(element)


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



