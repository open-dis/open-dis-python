from enum import Enum

from .siso_ref_010.enums.entity_kind import EntityKind
from .siso_ref_010.enums.country import Country
from .domain import Domain

class EntityType( object ):
    """Identifies the type of Entity"""

    def __init__(self):
        """ Initializer for EntityType"""
        # /** Kind of entity uid 7 */
        self.entityKind = EntityKind.default

        # TODO - Process the default value for a CLASSREF type
        """ Domain of entity (air, surface, subsurface, space, etc.)"""
        self.domain = Domain()
        # /** country to which the design of the entity is attributed uid 29 */
        self.country = Country.default

        """ category of entity"""
        self.category = 0
        """ subcategory based on category"""
        self.subCategory = 0
        """ specific info based on subcategory"""
        self.specific = 0
        self.extra = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "EntityKind : " + self.entityKind.get_description + "(" + (str(int(self.entityKind))) + ")" + "\n"
        outputString += "Domain :" + "\n" + self.domain.to_string() + "\n"
        outputString += "Country : " + self.country.get_description + "(" + (str(int(self.country))) + ")" + "\n"
        outputString += "Category : " + str(self.category) + "\n"
        outputString += "SubCategory : " + str(self.subCategory) + "\n"
        outputString += "Specific : " + str(self.specific) + "\n"
        outputString += "Extra : " + str(self.extra) + "\n"
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
        self.serialize_enum(self.entityKind,outputStream)
        self.domain.serialize(outputStream)
        self.serialize_enum(self.country,outputStream)
        outputStream.write_byte(int(self.category))
        outputStream.write_byte(int(self.subCategory))
        outputStream.write_byte(int(self.specific))
        outputStream.write_byte(int(self.extra))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.entityKind = EntityKind.get_enum(self.parse_enum(self.entityKind,inputStream))
        self.domain.parse(inputStream)
        self.country = Country.get_enum(self.parse_enum(self.country,inputStream))
        self.category = inputStream.read_byte()
        self.subCategory = inputStream.read_byte()
        self.specific = inputStream.read_byte()
        self.extra = inputStream.read_byte()

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



