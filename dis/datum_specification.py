from enum import Enum

from .variable_datum import VariableDatum
from .fixed_datum import FixedDatum

class DatumSpecification( object ):
    """List of fixed and variable datum records. Section 6.2.18 """

    def __init__(self):
        """ Initializer for DatumSpecification"""
        """ Number of fixed datums"""
        self.numberOfFixedDatums = 0
        """ Number of variable datums"""
        self.numberOfVariableDatums = 0
        """ variable length list fixed datums"""
        self._fixedDatumIDList = []
        """ variable length list of variable datums"""
        self._variableDatumIDList = []


    def get_numberOfFixedDatums(self):
        return len(self._fixedDatumIDList)
    def set_numberOfFixedDatums(self, value):
        numberOfFixedDatums = value


    def get_numberOfVariableDatums(self):
        return len(self._variableDatumIDList)
    def set_numberOfVariableDatums(self, value):
        numberOfVariableDatums = value


    def get_fixedDatumIDList(self):
        return self._fixedDatumIDList
    def set_fixedDatumIDList(self, value):
        self._fixedDatumIDList = value
    fixedDatumIDList = property(get_fixedDatumIDList, set_fixedDatumIDList)


    def add_fixedDatumIDList(self, value : FixedDatum):
        self._fixedDatumIDList.append(value)


    """
    ///            Name : fixedDatumIDList
    ///             UID : 
    ///            Type : FixedDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list fixed datums
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_variableDatumIDList(self):
        return self._variableDatumIDList
    def set_variableDatumIDList(self, value):
        self._variableDatumIDList = value
    variableDatumIDList = property(get_variableDatumIDList, set_variableDatumIDList)


    def add_variableDatumIDList(self, value : VariableDatum):
        self._variableDatumIDList.append(value)


    """
    ///            Name : variableDatumIDList
    ///             UID : 
    ///            Type : VariableDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of variable datums
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
        outputString += "NumberOfFixedDatums : " + str(len(self._fixedDatumIDList)) + "\n"
        outputString += "NumberOfVariableDatums : " + str(len(self._variableDatumIDList)) + "\n"
        outputString += "FixedDatumIDList : " + "\n"
        for idx in range(0, len(self._fixedDatumIDList)):
            outputString += self._fixedDatumIDList[idx].to_string()

        outputString += "VariableDatumIDList : " + "\n"
        for idx in range(0, len(self._variableDatumIDList)):
            outputString += self._variableDatumIDList[idx].to_string()

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
        outputStream.write_int( len(self._fixedDatumIDList))
        outputStream.write_int( len(self._variableDatumIDList))
        for anObj in self._fixedDatumIDList:
            anObj.serialize(outputStream)

        for anObj in self._variableDatumIDList:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.numberOfFixedDatums = inputStream.read_int()
        self.numberOfVariableDatums = inputStream.read_int()
        for idx in range(0, self.numberOfFixedDatums):
            element = FixedDatum()
            element.parse(inputStream)
            self._fixedDatumIDList.append(element)

        for idx in range(0, self.numberOfVariableDatums):
            element = VariableDatum()
            element.parse(inputStream)
            self._variableDatumIDList.append(element)


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



