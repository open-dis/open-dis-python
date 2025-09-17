from enum import Enum

from .vector3double import Vector3Double
from .event_identifier import EventIdentifier
from .entity_id import EntityID

class LaunchedMunitionRecord( object ):
    """Identity of a communications node. Section 6.2.50"""

    def __init__(self):
        """ Initializer for LaunchedMunitionRecord"""
        # fireEventID is an undescribed parameter... 
        self.fireEventID = EventIdentifier()
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        # firingEntityID is an undescribed parameter... 
        self.firingEntityID = EntityID()
        self.padding2 = 0
        # targetEntityID is an undescribed parameter... 
        self.targetEntityID = EntityID()
        self.padding3 = 0
        # targetLocation is an undescribed parameter... 
        self.targetLocation = Vector3Double()

    def to_string(self) ->str:
        outputString = ""
        outputString += "FireEventID :" + "\n" + self.fireEventID.to_string() + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "FiringEntityID :" + "\n" + self.firingEntityID.to_string() + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "TargetEntityID :" + "\n" + self.targetEntityID.to_string() + "\n"
        outputString += "Padding3 : " + str(self.padding3) + "\n"
        outputString += "TargetLocation :" + "\n" + self.targetLocation.to_string() + "\n"
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
        self.fireEventID.serialize(outputStream)
        outputStream.write_short(int(self.padding))
        self.firingEntityID.serialize(outputStream)
        outputStream.write_short(int(self.padding2))
        self.targetEntityID.serialize(outputStream)
        outputStream.write_short(int(self.padding3))
        self.targetLocation.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.fireEventID.parse(inputStream)
        self.padding = inputStream.read_short()
        self.firingEntityID.parse(inputStream)
        self.padding2 = inputStream.read_short()
        self.targetEntityID.parse(inputStream)
        self.padding3 = inputStream.read_short()
        self.targetLocation.parse(inputStream)

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



