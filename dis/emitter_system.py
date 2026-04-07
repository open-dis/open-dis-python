from enum import Enum

from .siso_ref_010.enums.emitter_name import EmitterName
from .siso_ref_010.enums.emitter_system_function import EmitterSystemFunction

class EmitterSystem( object ):
    """This field shall specify information about a particular emitter system. Section 6.2.23."""

    def __init__(self):
        """ Initializer for EmitterSystem"""
        # /** Name of the emitter, 16-bit enumeration uid 75 */
        self.emitterName = EmitterName.default

        # /** function of the emitter, 8-bit enumeration uid 76 */
        self.emitterFunction = EmitterSystemFunction.default

        """ emitter ID, 8-bit enumeration"""
        self.emitterIDNumber = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "EmitterName : " + self.emitterName.get_description + "(" + (str(int(self.emitterName))) + ")" + "\n"
        outputString += "EmitterSystemFunction : " + self.emitterFunction.get_description + "(" + (str(int(self.emitterFunction))) + ")" + "\n"
        outputString += "EmitterIDNumber : " + str(self.emitterIDNumber) + "\n"
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
        self.serialize_enum(self.emitterName,outputStream)
        self.serialize_enum(self.emitterFunction,outputStream)
        outputStream.write_byte(int(self.emitterIDNumber))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.emitterName = EmitterName.get_enum(self.parse_enum(self.emitterName,inputStream))
        self.emitterFunction = EmitterSystemFunction.get_enum(self.parse_enum(self.emitterFunction,inputStream))
        self.emitterIDNumber = inputStream.read_byte()

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



