from enum import Enum

from .siso_ref_010.enums.transmitter_modulation_type_system import TransmitterModulationTypeSystem
from .siso_ref_010.enums.transmitter_major_modulation import TransmitterMajorModulation

class ModulationType( object ):
    """Information about the type of modulation used for radio transmission. 6.2.59 """

    def __init__(self):
        """ Initializer for ModulationType"""
        """ This field shall indicate the spread spectrum technique or combination of spread spectrum techniques in use. Bit field. 0=freq hopping, 1=psuedo noise, time hopping=2, reamining bits unused"""
        self.spreadSpectrum = 0
        # /** The major classification of the modulation type.  UID 155 */
        self.majorModulation = TransmitterMajorModulation.default

        """ provide certain detailed information depending upon the major modulation type, uid 156-162"""
        self.detail = 0
        # /** The radio system associated with this Transmitter PDU and shall be used as the basis to interpret other fields whose values depend on a specific radio system. uid =163 */
        self.radioSystem = TransmitterModulationTypeSystem.default


    def to_string(self) ->str:
        outputString = ""
        outputString += "SpreadSpectrum : " + str(self.spreadSpectrum) + "\n"
        outputString += "TransmitterMajorModulation : " + self.majorModulation.get_description + "(" + (str(int(self.majorModulation))) + ")" + "\n"
        outputString += "Detail : " + str(self.detail) + "\n"
        outputString += "TransmitterModulationTypeSystem : " + self.radioSystem.get_description + "(" + (str(int(self.radioSystem))) + ")" + "\n"
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
        outputStream.write_short(int(self.spreadSpectrum))
        self.serialize_enum(self.majorModulation,outputStream)
        outputStream.write_short(int(self.detail))
        self.serialize_enum(self.radioSystem,outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.spreadSpectrum = inputStream.read_short()
        self.majorModulation = TransmitterMajorModulation.get_enum(self.parse_enum(self.majorModulation,inputStream))
        self.detail = inputStream.read_short()
        self.radioSystem = TransmitterModulationTypeSystem.get_enum(self.parse_enum(self.radioSystem,inputStream))

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



