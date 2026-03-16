from enum import Enum

from .beam_status import BeamStatus
from .eefundamental_parameter_data import EEFundamentalParameterData
from .track_jam_data import TrackJamData
from .beam_data import BeamData
from .siso_ref_010.enums.electromagnetic_emission_beam_function import ElectromagneticEmissionBeamFunction
from .jamming_technique import JammingTechnique
from .siso_ref_010.enums.high_density_track_jam import HighDensityTrackJam

class EmitterBeam( object ):
    """Emitter beams focused emissions from an electromagnetic or active acoustic transmitter. The beam is defined by the main lobe of the antenna pattern."""

    def __init__(self):
        """ Initializer for EmitterBeam"""
        self.beamDataLength = 0
        self.beamNumber = 0
        self.beamParameterIndex = 0
        # fundamentalParameterData is an undescribed parameter... 
        self.fundamentalParameterData = EEFundamentalParameterData()
        # beamData is an undescribed parameter... 
        self.beamData = BeamData()
        # /**  uid 78 */
        self.beamFunction = ElectromagneticEmissionBeamFunction.default

        self.numberOfTargets = 0
        # /**  uid 79 */
        self.highDensityTrackJam = HighDensityTrackJam.default

        # beamStatus is an undescribed parameter... 
        self.beamStatus = BeamStatus()
        # jammingTechnique is an undescribed parameter... 
        self.jammingTechnique = JammingTechnique()
        self._trackJamData = []


    def get_numberOfTargets(self):
        return len(self._trackJamData)
    def set_numberOfTargets(self, value):
        numberOfTargets = value


    def get_trackJamData(self):
        return self._trackJamData
    def set_trackJamData(self, value):
        self._trackJamData = value
    trackJamData = property(get_trackJamData, set_trackJamData)


    def add_trackJamData(self, value : TrackJamData):
        self._trackJamData.append(value)


    """
    ///            Name : trackJamData
    ///             UID : 
    ///            Type : TrackJamData
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
        outputString += "BeamDataLength : " + str(self.beamDataLength) + "\n"
        outputString += "BeamNumber : " + str(self.beamNumber) + "\n"
        outputString += "BeamParameterIndex : " + str(self.beamParameterIndex) + "\n"
        outputString += "FundamentalParameterData :" + "\n" + self.fundamentalParameterData.to_string() + "\n"
        outputString += "BeamData :" + "\n" + self.beamData.to_string() + "\n"
        outputString += "ElectromagneticEmissionBeamFunction : " + self.beamFunction.get_description + "(" + (str(int(self.beamFunction))) + ")" + "\n"
        outputString += "NumberOfTargets : " + str(len(self._trackJamData)) + "\n"
        outputString += "HighDensityTrackJam : " + self.highDensityTrackJam.get_description + "(" + (str(int(self.highDensityTrackJam))) + ")" + "\n"
        outputString += "BeamStatus :" + "\n" + self.beamStatus.to_string() + "\n"
        outputString += "JammingTechnique :" + "\n" + self.jammingTechnique.to_string() + "\n"
        outputString += "TrackJamData : " + "\n"
        for idx in range(0, len(self._trackJamData)):
            outputString += self._trackJamData[idx].to_string()

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
        outputStream.write_byte(int(self.beamDataLength))
        outputStream.write_byte(int(self.beamNumber))
        outputStream.write_short(int(self.beamParameterIndex))
        self.fundamentalParameterData.serialize(outputStream)
        self.beamData.serialize(outputStream)
        self.serialize_enum(self.beamFunction,outputStream)
        outputStream.write_byte( len(self._trackJamData))
        self.serialize_enum(self.highDensityTrackJam,outputStream)
        self.beamStatus.serialize(outputStream)
        self.jammingTechnique.serialize(outputStream)
        for anObj in self._trackJamData:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.beamDataLength = inputStream.read_byte()
        self.beamNumber = inputStream.read_byte()
        self.beamParameterIndex = inputStream.read_short()
        self.fundamentalParameterData.parse(inputStream)
        self.beamData.parse(inputStream)
        self.beamFunction = ElectromagneticEmissionBeamFunction.get_enum(self.parse_enum(self.beamFunction,inputStream))
        self.numberOfTargets = inputStream.read_byte()
        self.highDensityTrackJam = HighDensityTrackJam.get_enum(self.parse_enum(self.highDensityTrackJam,inputStream))
        self.beamStatus.parse(inputStream)
        self.jammingTechnique.parse(inputStream)
        for idx in range(0, self.numberOfTargets):
            element = TrackJamData()
            element.parse(inputStream)
            self._trackJamData.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 11

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



