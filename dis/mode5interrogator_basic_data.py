from enum import Enum

from .entity_id import EntityID

class Mode5InterrogatorBasicData( object ):
    """B.2.26. Mode 5 interrogator basic data"""

    def __init__(self):
        """ Initializer for Mode5InterrogatorBasicData"""
        """ Mode 5 interrogator status, part of Mode 5 interrogator basic data fields"""
        self.mode5InterrogatorStatus = 0
        """ Padding, part of Mode 5 interrogator basic data fields"""
        self.padding = 0
        """ Padding, part of Mode 5 interrogator basic data fields"""
        self.padding2 = 0
        """ Mode 5 Message Formats Present, part of Mode 5 interrogator basic data fields"""
        self.mode5MessageFormatsPresent = 0
        """ Interrogated entity ID, part of Mode 5 interrogator basic data fields"""
        self.entityID = EntityID()
        """ Padding, part of Mode 5 interrogator basic data fields"""
        self.padding3 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "Mode5InterrogatorStatus : " + str(self.mode5InterrogatorStatus) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "Mode5MessageFormatsPresent : " + str(self.mode5MessageFormatsPresent) + "\n"
        outputString += "EntityID :" + "\n" + self.entityID.to_string() + "\n"
        outputString += "Padding3 : " + str(self.padding3) + "\n"
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
        outputStream.write_byte(int(self.mode5InterrogatorStatus))
        outputStream.write_byte(int(self.padding))
        outputStream.write_short(int(self.padding2))
        outputStream.write_int(int(self.mode5MessageFormatsPresent))
        self.entityID.serialize(outputStream)
        outputStream.write_short(int(self.padding3))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.mode5InterrogatorStatus = inputStream.read_byte()
        self.padding = inputStream.read_byte()
        self.padding2 = inputStream.read_short()
        self.mode5MessageFormatsPresent = inputStream.read_int()
        self.entityID.parse(inputStream)
        self.padding3 = inputStream.read_short()

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



