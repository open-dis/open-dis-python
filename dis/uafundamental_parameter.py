from enum import Enum

from .siso_ref_010.enums.uascan_pattern import UAScanPattern
from .siso_ref_010.enums.uaactive_emission_parameter_index import UAActiveEmissionParameterIndex

class UAFundamentalParameter( object ):
    """Regeneration parameters for active emission systems that are variable throughout a scenario. Section 6.2.91"""

    def __init__(self):
        """ Initializer for UAFundamentalParameter"""
        # /** Which database record shall be used uid 146 */
        self.activeEmissionParameterIndex = UAActiveEmissionParameterIndex.default

        # /** The type of scan pattern, If not used, zero uid 147 */
        self.scanPattern = UAScanPattern.default

        """ center azimuth bearing of th emain beam. In radians."""
        self.beamCenterAzimuthHorizontal = 0.0
        """ Horizontal beamwidth of th emain beam Meastued at the 3dB down point of peak radiated power. In radians."""
        self.azimuthalBeamwidthHorizontal = 0.0
        """ center of the d/e angle of th emain beam relative to the stablised de angle of the target. In radians."""
        self.beamCenterDepressionElevation = 0.0
        """ vertical beamwidth of the main beam. Meastured at the 3dB down point of peak radiated power. In radians."""
        self.depressionElevationBeamWidth = 0.0

    def to_string(self) ->str:
        outputString = ""
        outputString += "UAActiveEmissionParameterIndex : " + self.activeEmissionParameterIndex.get_description + "(" + (str(int(self.activeEmissionParameterIndex))) + ")" + "\n"
        outputString += "UAScanPattern : " + self.scanPattern.get_description + "(" + (str(int(self.scanPattern))) + ")" + "\n"
        outputString += "BeamCenterAzimuthHorizontal : " + str(self.beamCenterAzimuthHorizontal) + "\n"
        outputString += "AzimuthalBeamwidthHorizontal : " + str(self.azimuthalBeamwidthHorizontal) + "\n"
        outputString += "BeamCenterDepressionElevation : " + str(self.beamCenterDepressionElevation) + "\n"
        outputString += "DepressionElevationBeamWidth : " + str(self.depressionElevationBeamWidth) + "\n"
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
        self.serialize_enum(self.activeEmissionParameterIndex,outputStream)
        self.serialize_enum(self.scanPattern,outputStream)
        outputStream.write_float(int(self.beamCenterAzimuthHorizontal))
        outputStream.write_float(int(self.azimuthalBeamwidthHorizontal))
        outputStream.write_float(int(self.beamCenterDepressionElevation))
        outputStream.write_float(int(self.depressionElevationBeamWidth))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.activeEmissionParameterIndex = UAActiveEmissionParameterIndex.get_enum(self.parse_enum(self.activeEmissionParameterIndex,inputStream))
        self.scanPattern = UAScanPattern.get_enum(self.parse_enum(self.scanPattern,inputStream))
        self.beamCenterAzimuthHorizontal = inputStream.read_float()
        self.azimuthalBeamwidthHorizontal = inputStream.read_float()
        self.beamCenterDepressionElevation = inputStream.read_float()
        self.depressionElevationBeamWidth = inputStream.read_float()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 6

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



