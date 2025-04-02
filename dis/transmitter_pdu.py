from enum import Enum

from .modulation_type import ModulationType
from .siso_ref_010.enums.transmitter_transmit_state import TransmitterTransmitState
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .vector3float import Vector3Float
from .radio_comms_header import RadioCommsHeader
from .siso_ref_010.enums.transmitter_input_source import TransmitterInputSource
from .variable_transmitter_parameters import VariableTransmitterParameters
from .siso_ref_010.enums.transmitter_antenna_pattern_type import TransmitterAntennaPatternType
from .radio_communications_family_pdu import RadioCommunicationsFamilyPdu
from .modulation_parameters import ModulationParameters
from .vector3double import Vector3Double
from .siso_ref_010.enums.transmitter_crypto_system import TransmitterCryptoSystem
from .radio_type import RadioType

class TransmitterPdu( RadioCommunicationsFamilyPdu ):
    """5.8.3 Communicates the state of a particular radio transmitter or simple intercom."""

    def __init__(self):
        """ Initializer for TransmitterPdu"""
        super().__init__()
        # header is an undescribed parameter... 
        self.header = RadioCommsHeader()
        """ Type of radio"""
        self.radioEntityType = RadioType()
        # /** transmit state uid 164 */
        self.transmitState = TransmitterTransmitState.default

        # /** input source uid 165 */
        self.inputSource = TransmitterInputSource.default

        """ count field"""
        self.variableTransmitterParameterCount = 0
        """ Location of antenna"""
        self.antennaLocation = Vector3Double()
        """ relative location of antenna"""
        self.relativeAntennaLocation = Vector3Float()
        # /** antenna pattern type uid 167 */
        self.antennaPatternType = TransmitterAntennaPatternType.default

        """ atenna pattern length"""
        self.antennaPatternCount = 0
        """ frequency"""
        self.frequency = 0
        """ transmit frequency Bandwidth"""
        self.transmitFrequencyBandwidth = 0.0
        """ transmission power"""
        self.power = 0.0
        """ modulation"""
        self.modulationType = ModulationType()
        # /** crypto system enumeration uid 166 */
        self.cryptoSystem = TransmitterCryptoSystem.default

        """ crypto system key identifer"""
        self.cryptoKeyId = 0
        """ how many modulation parameters we have"""
        self.modulationParameterCount = 0
        self.padding1 = 0
        self.padding2 = 0
        """ variable length list of modulation parameters"""
        self._modulationParametersList = []
        """ variable length list of antenna pattern records"""
        self._antennaPatternList = []
        self.pduType = DisPduType.transmitter


    def get_antennaPatternCount(self):
        return len(self._antennaPatternList)
    def set_antennaPatternCount(self, value):
        antennaPatternCount = value


    def get_modulationParameterCount(self):
        return len(self._modulationParametersList)
    def set_modulationParameterCount(self, value):
        modulationParameterCount = value


    def get_modulationParametersList(self):
        return self._modulationParametersList
    def set_modulationParametersList(self, value):
        self._modulationParametersList = value
    modulationParametersList = property(get_modulationParametersList, set_modulationParametersList)


    def add_modulationParametersList(self, value : ModulationParameters):
        self._modulationParametersList.append(value)


    """
    ///            Name : modulationParametersList
    ///             UID : 
    ///            Type : ModulationParameters
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of modulation parameters
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_antennaPatternList(self):
        return self._antennaPatternList
    def set_antennaPatternList(self, value):
        self._antennaPatternList = value
    antennaPatternList = property(get_antennaPatternList, set_antennaPatternList)


    def add_antennaPatternList(self, value : VariableTransmitterParameters):
        self._antennaPatternList.append(value)


    """
    ///            Name : antennaPatternList
    ///             UID : 
    ///            Type : VariableTransmitterParameters
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of antenna pattern records
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
        outputString += super().to_string()
        outputString += "Header :" + "\n" + self.header.to_string() + "\n"
        outputString += "RadioEntityType :" + "\n" + self.radioEntityType.to_string() + "\n"
        outputString += "TransmitterTransmitState : " + self.transmitState.get_description + "(" + (str(int(self.transmitState))) + ")" + "\n"
        outputString += "TransmitterInputSource : " + self.inputSource.get_description + "(" + (str(int(self.inputSource))) + ")" + "\n"
        outputString += "VariableTransmitterParameterCount : " + str(self.variableTransmitterParameterCount) + "\n"
        outputString += "AntennaLocation :" + "\n" + self.antennaLocation.to_string() + "\n"
        outputString += "RelativeAntennaLocation :" + "\n" + self.relativeAntennaLocation.to_string() + "\n"
        outputString += "TransmitterAntennaPatternType : " + self.antennaPatternType.get_description + "(" + (str(int(self.antennaPatternType))) + ")" + "\n"
        outputString += "AntennaPatternCount : " + str(len(self._antennaPatternList)) + "\n"
        outputString += "Frequency : " + str(self.frequency) + "\n"
        outputString += "TransmitFrequencyBandwidth : " + str(self.transmitFrequencyBandwidth) + "\n"
        outputString += "Power : " + str(self.power) + "\n"
        outputString += "ModulationType :" + "\n" + self.modulationType.to_string() + "\n"
        outputString += "TransmitterCryptoSystem : " + self.cryptoSystem.get_description + "(" + (str(int(self.cryptoSystem))) + ")" + "\n"
        outputString += "CryptoKeyId : " + str(self.cryptoKeyId) + "\n"
        outputString += "ModulationParameterCount : " + str(len(self._modulationParametersList)) + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "ModulationParametersList : " + "\n"
        for idx in range(0, len(self._modulationParametersList)):
            outputString += self._modulationParametersList[idx].to_string()

        outputString += "AntennaPatternList : " + "\n"
        for idx in range(0, len(self._antennaPatternList)):
            outputString += self._antennaPatternList[idx].to_string()

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
        super( TransmitterPdu, self ).serialize(outputStream)
        self.header.serialize(outputStream)
        self.radioEntityType.serialize(outputStream)
        self.serialize_enum(self.transmitState,outputStream)
        self.serialize_enum(self.inputSource,outputStream)
        outputStream.write_short(int(self.variableTransmitterParameterCount))
        self.antennaLocation.serialize(outputStream)
        self.relativeAntennaLocation.serialize(outputStream)
        self.serialize_enum(self.antennaPatternType,outputStream)
        outputStream.write_short( len(self._antennaPatternList))
        outputStream.write_long(int(self.frequency))
        outputStream.write_float(int(self.transmitFrequencyBandwidth))
        outputStream.write_float(int(self.power))
        self.modulationType.serialize(outputStream)
        self.serialize_enum(self.cryptoSystem,outputStream)
        outputStream.write_short(int(self.cryptoKeyId))
        outputStream.write_byte( len(self._modulationParametersList))
        outputStream.write_byte(int(self.padding1))
        outputStream.write_short(int(self.padding2))
        for anObj in self._modulationParametersList:
            anObj.serialize(outputStream)

        for anObj in self._antennaPatternList:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( TransmitterPdu, self).parse(inputStream)
        self.header.parse(inputStream)
        self.radioEntityType.parse(inputStream)
        self.transmitState = TransmitterTransmitState.get_enum(self.parse_enum(self.transmitState,inputStream))
        self.inputSource = TransmitterInputSource.get_enum(self.parse_enum(self.inputSource,inputStream))
        self.variableTransmitterParameterCount = inputStream.read_short()
        self.antennaLocation.parse(inputStream)
        self.relativeAntennaLocation.parse(inputStream)
        self.antennaPatternType = TransmitterAntennaPatternType.get_enum(self.parse_enum(self.antennaPatternType,inputStream))
        self.antennaPatternCount = inputStream.read_short()
        self.frequency = inputStream.read_long()
        self.transmitFrequencyBandwidth = inputStream.read_float()
        self.power = inputStream.read_float()
        self.modulationType.parse(inputStream)
        self.cryptoSystem = TransmitterCryptoSystem.get_enum(self.parse_enum(self.cryptoSystem,inputStream))
        self.cryptoKeyId = inputStream.read_short()
        self.modulationParameterCount = inputStream.read_byte()
        self.padding1 = inputStream.read_byte()
        self.padding2 = inputStream.read_short()
        for idx in range(0, self.modulationParameterCount):
            element = ModulationParameters()
            element.parse(inputStream)
            self._modulationParametersList.append(element)

        for idx in range(0, self.antennaPatternCount):
            element = VariableTransmitterParameters()
            element.parse(inputStream)
            self._antennaPatternList.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 20

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



