from enum import Enum

from .siso_ref_010.enums.aggregate_state_specific import AggregateStateSpecific
from .siso_ref_010.enums.country import Country
from .siso_ref_010.enums.aggregate_state_aggregate_kind import AggregateStateAggregateKind
from .siso_ref_010.enums.platform_domain import PlatformDomain
from .siso_ref_010.enums.aggregate_state_subcategory import AggregateStateSubcategory

class AggregateType( object ):
    """Identifies the type and organization of an aggregate. Section 6.2.5"""

    def __init__(self):
        """ Initializer for AggregateType"""
        # /** Grouping criterion used to group the aggregate. Enumeration from EBV document uid 206 */
        self.aggregateKind = AggregateStateAggregateKind.default

        # /** Domain of entity (air, surface, subsurface, space, etc.) where zero means domain does not apply. uid 8 */
        self.domain = PlatformDomain.default

        # /** country to which the design of the entity is attributed uid 29 */
        self.country = Country.default

        """ category of entity"""
        self.category = 0
        # /** subcategory of entity uid 208 */
        self.subcategory = AggregateStateSubcategory.default

        # /** specific info based on subcategory field. specific is a reserved word in sql. uid 209 */
        self.specificInfo = AggregateStateSpecific.default

        self.extra = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "AggregateStateAggregateKind : " + self.aggregateKind.get_description + "(" + (str(int(self.aggregateKind))) + ")" + "\n"
        outputString += "PlatformDomain : " + self.domain.get_description + "(" + (str(int(self.domain))) + ")" + "\n"
        outputString += "Country : " + self.country.get_description + "(" + (str(int(self.country))) + ")" + "\n"
        outputString += "Category : " + str(self.category) + "\n"
        outputString += "AggregateStateSubcategory : " + self.subcategory.get_description + "(" + (str(int(self.subcategory))) + ")" + "\n"
        outputString += "AggregateStateSpecific : " + self.specificInfo.get_description + "(" + (str(int(self.specificInfo))) + ")" + "\n"
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
        self.serialize_enum(self.aggregateKind,outputStream)
        self.serialize_enum(self.domain,outputStream)
        self.serialize_enum(self.country,outputStream)
        outputStream.write_byte(int(self.category))
        self.serialize_enum(self.subcategory,outputStream)
        self.serialize_enum(self.specificInfo,outputStream)
        outputStream.write_byte(int(self.extra))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.aggregateKind = AggregateStateAggregateKind.get_enum(self.parse_enum(self.aggregateKind,inputStream))
        self.domain = PlatformDomain.get_enum(self.parse_enum(self.domain,inputStream))
        self.country = Country.get_enum(self.parse_enum(self.country,inputStream))
        self.category = inputStream.read_byte()
        self.subcategory = AggregateStateSubcategory.get_enum(self.parse_enum(self.subcategory,inputStream))
        self.specificInfo = AggregateStateSpecific.get_enum(self.parse_enum(self.specificInfo,inputStream))
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



