from enum import Enum


class EntityID( object ):
    """Unique identifier triplet for this entity.  Also referred to as EntityIdentifier"""

    def __init__(self):
        """ Initializer for EntityID"""
        """ Site ID values are unique identification number for originating site, often corresponding to an internet address.  Site ID values are agreed upon by individual simulations."""
        self.siteID = 0
        """ Application ID values are unique identification number for originating application at a given site.  Application ID values are sssigned by individual sites."""
        self.applicationID = 0
        """ Entity ID values are unique identification number for s givent entity in the originating application at a given site.  Entity ID values are sssigned by individual simulation programs."""
        self.entityID = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "SiteID : " + str(self.siteID) + "\n"
        outputString += "ApplicationID : " + str(self.applicationID) + "\n"
        outputString += "EntityID : " + str(self.entityID) + "\n"
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
        outputStream.write_short(int(self.siteID))
        outputStream.write_short(int(self.applicationID))
        outputStream.write_short(int(self.entityID))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.siteID = inputStream.read_short()
        self.applicationID = inputStream.read_short()
        self.entityID = inputStream.read_short()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 3

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



