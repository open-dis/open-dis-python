from enum import Enum

from .entity_type import EntityType

class ExpendableReload( object ):
    """An entity's expendable (chaff, flares, etc.) information. Section 6.2.37"""

    def __init__(self):
        """ Initializer for ExpendableReload"""
        """ Type of expendable"""
        self.expendable = EntityType()
        self.station = 0
        self.standardQuantity = 0
        self.maximumQuantity = 0
        self.standardQuantityReloadTime = 0
        self.maximumQuantityReloadTime = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "Expendable :" + "\n" + self.expendable.to_string() + "\n"
        outputString += "Station : " + str(self.station) + "\n"
        outputString += "StandardQuantity : " + str(self.standardQuantity) + "\n"
        outputString += "MaximumQuantity : " + str(self.maximumQuantity) + "\n"
        outputString += "StandardQuantityReloadTime : " + str(self.standardQuantityReloadTime) + "\n"
        outputString += "MaximumQuantityReloadTime : " + str(self.maximumQuantityReloadTime) + "\n"
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
        self.expendable.serialize(outputStream)
        outputStream.write_int(int(self.station))
        outputStream.write_short(int(self.standardQuantity))
        outputStream.write_short(int(self.maximumQuantity))
        outputStream.write_int(int(self.standardQuantityReloadTime))
        outputStream.write_int(int(self.maximumQuantityReloadTime))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.expendable.parse(inputStream)
        self.station = inputStream.read_int()
        self.standardQuantity = inputStream.read_short()
        self.maximumQuantity = inputStream.read_short()
        self.standardQuantityReloadTime = inputStream.read_int()
        self.maximumQuantityReloadTime = inputStream.read_int()

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



