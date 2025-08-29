from enum import Enum

from .attribute import Attribute
from .entity_id import EntityID

class AttributeRecordSet( object ):
    """Each Attribute Record Set shall contain the following information: the Entity or Object ID to which all Attribute records in the set apply, plus one or more Attribute records"""

    def __init__(self):
        """ Initializer for AttributeRecordSet"""
        # entityId is an undescribed parameter... 
        self.entityId = EntityID()
        self.numberOfAttributeRecords = 0
        self._attributeRecords = []


    def get_numberOfAttributeRecords(self):
        return len(self._attributeRecords)
    def set_numberOfAttributeRecords(self, value):
        numberOfAttributeRecords = value


    def get_attributeRecords(self):
        return self._attributeRecords
    def set_attributeRecords(self, value):
        self._attributeRecords = value
    attributeRecords = property(get_attributeRecords, set_attributeRecords)


    def add_attributeRecords(self, value : Attribute):
        self._attributeRecords.append(value)


    """
    ///            Name : attributeRecords
    ///             UID : 
    ///            Type : Attribute
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : null
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
        outputString += "EntityId :" + "\n" + self.entityId.to_string() + "\n"
        outputString += "NumberOfAttributeRecords : " + str(len(self._attributeRecords)) + "\n"
        outputString += "AttributeRecords : " + "\n"
        for idx in range(0, len(self._attributeRecords)):
            outputString += self._attributeRecords[idx].to_string()

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
        self.entityId.serialize(outputStream)
        outputStream.write_short( len(self._attributeRecords))
        for anObj in self._attributeRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.entityId.parse(inputStream)
        self.numberOfAttributeRecords = inputStream.read_short()
        for idx in range(0, self.numberOfAttributeRecords):
            element = Attribute()
            element.parse(inputStream)
            self._attributeRecords.append(element)


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



