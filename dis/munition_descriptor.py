from enum import Enum

from .entity_type import EntityType
from .siso_ref_010.enums.munition_descriptor_warhead import MunitionDescriptorWarhead
from .siso_ref_010.enums.munition_descriptor_fuse import MunitionDescriptorFuse

class MunitionDescriptor( object ):
    """Represents the firing or detonation of a munition. Section 6.2.19.2"""

    def __init__(self):
        """ Initializer for MunitionDescriptor"""
        """ What munition was used in the burst"""
        self.munitionType = EntityType()
        # /** type of warhead enumeration uid 60 */
        self.warhead = MunitionDescriptorWarhead.default

        # /** type of fuse used enumeration uid 61 */
        self.fuse = MunitionDescriptorFuse.default

        """ how many of the munition were fired"""
        self.quantity = 0
        """ rate at which the munition was fired"""
        self.rate = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "MunitionType :" + "\n" + self.munitionType.to_string() + "\n"
        outputString += "MunitionDescriptorWarhead : " + self.warhead.get_description + "(" + (str(int(self.warhead))) + ")" + "\n"
        outputString += "MunitionDescriptorFuse : " + self.fuse.get_description + "(" + (str(int(self.fuse))) + ")" + "\n"
        outputString += "Quantity : " + str(self.quantity) + "\n"
        outputString += "Rate : " + str(self.rate) + "\n"
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
        self.munitionType.serialize(outputStream)
        self.serialize_enum(self.warhead,outputStream)
        self.serialize_enum(self.fuse,outputStream)
        outputStream.write_short(int(self.quantity))
        outputStream.write_short(int(self.rate))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.munitionType.parse(inputStream)
        self.warhead = MunitionDescriptorWarhead.get_enum(self.parse_enum(self.warhead,inputStream))
        self.fuse = MunitionDescriptorFuse.get_enum(self.parse_enum(self.fuse,inputStream))
        self.quantity = inputStream.read_short()
        self.rate = inputStream.read_short()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 5

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



