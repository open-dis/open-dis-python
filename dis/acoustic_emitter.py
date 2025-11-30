from enum import Enum

from .siso_ref_010.enums.uaacoustic_emitter_system_function import UAAcousticEmitterSystemFunction
from .siso_ref_010.enums.uaacoustic_system_name import UAAcousticSystemName

class AcousticEmitter( object ):
    """Information about a specific UA emitter. Section 6.2.2."""

    def __init__(self):
        """ Initializer for AcousticEmitter"""
        # /** The system for a particular UA emitter, and an enumeration uid 144 */
        self.acousticSystemName = UAAcousticSystemName.default

        # /** The function of the acoustic system uid 145 */
        self.acousticFunction = UAAcousticEmitterSystemFunction.default

        """ The UA emitter identification number relative to a specific system"""
        self.acousticIDNumber = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "UAAcousticSystemName : " + self.acousticSystemName.get_description + "(" + (str(int(self.acousticSystemName))) + ")" + "\n"
        outputString += "UAAcousticEmitterSystemFunction : " + self.acousticFunction.get_description + "(" + (str(int(self.acousticFunction))) + ")" + "\n"
        outputString += "AcousticIDNumber : " + str(self.acousticIDNumber) + "\n"
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
        self.serialize_enum(self.acousticSystemName,outputStream)
        self.serialize_enum(self.acousticFunction,outputStream)
        outputStream.write_byte(int(self.acousticIDNumber))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.acousticSystemName = UAAcousticSystemName.get_enum(self.parse_enum(self.acousticSystemName,inputStream))
        self.acousticFunction = UAAcousticEmitterSystemFunction.get_enum(self.parse_enum(self.acousticFunction,inputStream))
        self.acousticIDNumber = inputStream.read_byte()

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



