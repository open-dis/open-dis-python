from enum import Enum

from .record_specification_element import RecordSpecificationElement

class RecordSpecification( object ):
    """This record shall specify the number of record sets contained in the Record Specification record and the record details. Section 6.2.73."""

    def __init__(self):
        """ Initializer for RecordSpecification"""
        """ The number of record sets"""
        self.numberOfRecordSets = 0
        """ variable length list record specifications."""
        self._recordSets = []


    def get_numberOfRecordSets(self):
        return len(self._recordSets)
    def set_numberOfRecordSets(self, value):
        numberOfRecordSets = value


    def get_recordSets(self):
        return self._recordSets
    def set_recordSets(self, value):
        self._recordSets = value
    recordSets = property(get_recordSets, set_recordSets)


    def add_recordSets(self, value : RecordSpecificationElement):
        self._recordSets.append(value)


    """
    ///            Name : recordSets
    ///             UID : 
    ///            Type : RecordSpecificationElement
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list record specifications.
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
        outputString += "NumberOfRecordSets : " + str(len(self._recordSets)) + "\n"
        outputString += "RecordSets : " + "\n"
        for idx in range(0, len(self._recordSets)):
            outputString += self._recordSets[idx].to_string()

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
        outputStream.write_int( len(self._recordSets))
        for anObj in self._recordSets:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.numberOfRecordSets = inputStream.read_int()
        for idx in range(0, self.numberOfRecordSets):
            element = RecordSpecificationElement()
            element.parse(inputStream)
            self._recordSets.append(element)


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



