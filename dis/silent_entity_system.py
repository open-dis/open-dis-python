from enum import Enum

from .entity_type import EntityType

class SilentEntitySystem( object ):
    """information abou an enitity not producing espdus. Section 6.2.79"""

    def __init__(self):
        """ Initializer for SilentEntitySystem"""
        """ number of the type specified by the entity type field"""
        self.numberOfEntities = 0
        """ number of entity appearance records that follow"""
        self.numberOfAppearanceRecords = 0
        """ Entity type"""
        self.entityType = EntityType()
        """ Variable length list of appearance records"""
        self.appearanceRecordList =  []

    def to_string(self) ->str:
        outputString = ""
        outputString += "NumberOfEntities : " + str(self.numberOfEntities) + "\n"
        outputString += "NumberOfAppearanceRecords : " + str(self.numberOfAppearanceRecords) + "\n"
        outputString += "EntityType :" + "\n" + self.entityType.to_string() + "\n"
        outputString += "AppearanceRecordList : " + "\n"
        for idx in range(0, len(self.appearanceRecordList)):
            outputString += str(self.appearanceRecordList[idx])

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
        outputStream.write_short(int(self.numberOfEntities))
        outputStream.write_short(int(self.numberOfAppearanceRecords))
        self.entityType.serialize(outputStream)
        for idx in range(0, 0):
            outputStream.write_int( self.appearanceRecordList[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.numberOfEntities = inputStream.read_short()
        self.numberOfAppearanceRecords = inputStream.read_short()
        self.entityType.parse(inputStream)
        self.appearanceRecordList = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_int()
            self.appearanceRecordList[  idx  ] = val


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



