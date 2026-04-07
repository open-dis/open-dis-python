from enum import Enum

from .standard_variable_record import StandardVariableRecord

class StandardVariableSpecification( object ):
    """Does not work, and causes failure in anything it is embedded in. Section 6.2.83"""

    def __init__(self):
        """ Initializer for StandardVariableSpecification"""
        """ Number of static variable records"""
        self.numberOfStandardVariableRecords = 0
        """ variable length list of standard variables, The class type and length here are WRONG and will cause the incorrect serialization of any class in whihc it is embedded."""
        self._standardVariables = []


    def get_numberOfStandardVariableRecords(self):
        return len(self._standardVariables)
    def set_numberOfStandardVariableRecords(self, value):
        numberOfStandardVariableRecords = value


    def get_standardVariables(self):
        return self._standardVariables
    def set_standardVariables(self, value):
        self._standardVariables = value
    standardVariables = property(get_standardVariables, set_standardVariables)


    def add_standardVariables(self, value : StandardVariableRecord):
        self._standardVariables.append(value)


    """
    ///            Name : standardVariables
    ///             UID : 
    ///            Type : StandardVariableRecord
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of standard variables, The class type and length here are WRONG and will cause the incorrect serialization of any class in whihc it is embedded.
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
        outputString += "NumberOfStandardVariableRecords : " + str(len(self._standardVariables)) + "\n"
        outputString += "StandardVariables : " + "\n"
        for idx in range(0, len(self._standardVariables)):
            outputString += self._standardVariables[idx].to_string()

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
        outputStream.write_short( len(self._standardVariables))
        for anObj in self._standardVariables:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.numberOfStandardVariableRecords = inputStream.read_short()
        for idx in range(0, self.numberOfStandardVariableRecords):
            element = StandardVariableRecord()
            element.parse(inputStream)
            self._standardVariables.append(element)


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



