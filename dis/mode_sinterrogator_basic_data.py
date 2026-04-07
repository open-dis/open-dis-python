from enum import Enum


class ModeSInterrogatorBasicData( object ):
    """B.2.37. Mode S interrogator basic data"""

    def __init__(self):
        """ Initializer for ModeSInterrogatorBasicData"""
        """ Mode S interrogator status, part of Mode S interrogator basic data fields. See B.2.39."""
        self.modeSInterrogatorStatus = 0
        """ Padding, part of Mode S interrogator basic data fields"""
        self.padding = 0
        """ Mode S levels present, part of Mode S interrogator basic data fields. See B.2.40"""
        self.modeSLevelsPresent = 0
        """ Padding, part of Mode S interrogator basic data fields"""
        self.padding2 = 0
        """ Padding, part of Mode S interrogator basic data fields"""
        self.padding3 = 0
        """ Padding, part of Mode S interrogator basic data fields"""
        self.padding4 = 0
        """ Padding, part of Mode S interrogator basic data fields"""
        self.padding5 = 0
        """ Padding, part of Mode S interrogator basic data fields"""
        self.padding6 = 0
        """ Padding, part of Mode S interrogator basic data fields"""
        self.padding7 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "ModeSInterrogatorStatus : " + str(self.modeSInterrogatorStatus) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "ModeSLevelsPresent : " + str(self.modeSLevelsPresent) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "Padding3 : " + str(self.padding3) + "\n"
        outputString += "Padding4 : " + str(self.padding4) + "\n"
        outputString += "Padding5 : " + str(self.padding5) + "\n"
        outputString += "Padding6 : " + str(self.padding6) + "\n"
        outputString += "Padding7 : " + str(self.padding7) + "\n"
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
        outputStream.write_byte(int(self.modeSInterrogatorStatus))
        outputStream.write_byte(int(self.padding))
        outputStream.write_byte(int(self.modeSLevelsPresent))
        outputStream.write_byte(int(self.padding2))
        outputStream.write_int(int(self.padding3))
        outputStream.write_int(int(self.padding4))
        outputStream.write_int(int(self.padding5))
        outputStream.write_int(int(self.padding6))
        outputStream.write_int(int(self.padding7))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.modeSInterrogatorStatus = inputStream.read_byte()
        self.padding = inputStream.read_byte()
        self.modeSLevelsPresent = inputStream.read_byte()
        self.padding2 = inputStream.read_byte()
        self.padding3 = inputStream.read_int()
        self.padding4 = inputStream.read_int()
        self.padding5 = inputStream.read_int()
        self.padding6 = inputStream.read_int()
        self.padding7 = inputStream.read_int()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 9

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



