from enum import Enum

from .siso_ref_010.enums.transmitter_antenna_pattern_reference_system import TransmitterAntennaPatternReferenceSystem
from .euler_angles import EulerAngles

class BeamAntennaPattern( object ):
    """Used when the antenna pattern type field has a value of 1. Specifies the direction, pattern, and polarization of radiation from an antenna. Section 6.2.9.2"""

    def __init__(self):
        """ Initializer for BeamAntennaPattern"""
        """ The rotation that transforms the reference coordinate sytem into the beam coordinate system. Either world coordinates or entity coordinates may be used as the reference coordinate system, as specified by the reference system field of the antenna pattern record."""
        self.beamDirection = EulerAngles()
        """ Full width of the beam to the -3dB power density points in the x-y plane of the beam coordinnate system.  Elevation beamwidth is represented by a 32-bit floating point number in units of radians."""
        self.azimuthBeamwidth = 0
        """ This field shall specify the full width of the beam to the –3 dB power density points in the x-z plane of the beam coordinate system. Elevation beamwidth shall be represented by a 32-bit floating point number in units of radians."""
        self.elevationBeamwidth = 0
        # /** The reference coordinate system wrt which beam direction  is specified. This field should not change over the duration of an exercise. World coordindate systemis prefered for exercises. The entity coordinate system should be used only when highly directional antennas must be precisely modeled. uid 168 */
        self.referenceSystem = TransmitterAntennaPatternReferenceSystem.default

        """ Padding"""
        self.padding1 = 0
        """ Padding"""
        self.padding2 = 0
        """ This field shall specify the magnitude of the Z-component (in beam coordinates) of the Electrical field at some arbitrary single point in the main beam and in the far field of the antenna. """
        self.ez = 0.0
        """ This field shall specify the magnitude of the X-component (in beam coordinates) of the Electri- cal field at some arbitrary single point in the main beam and in the far field of the antenna."""
        self.ex = 0.0
        """ This field shall specify the phase angle between EZ and EX in radians. If fully omni-direc- tional antenna is modeled using beam pattern type one, the omni-directional antenna shall be repre- sented by beam direction Euler angles psi, theta, and phi of zero, an azimuth beamwidth of 2PI, and an elevation beamwidth of PI"""
        self.phase = 0.0
        """ padding"""
        self.padding3 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "BeamDirection :" + "\n" + self.beamDirection.to_string() + "\n"
        outputString += "AzimuthBeamwidth : " + str(self.azimuthBeamwidth) + "\n"
        outputString += "ElevationBeamwidth : " + str(self.elevationBeamwidth) + "\n"
        outputString += "TransmitterAntennaPatternReferenceSystem : " + self.referenceSystem.get_description + "(" + (str(int(self.referenceSystem))) + ")" + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "Ez : " + str(self.ez) + "\n"
        outputString += "Ex : " + str(self.ex) + "\n"
        outputString += "Phase : " + str(self.phase) + "\n"
        outputString += "Padding3 : " + str(self.padding3) + "\n"
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
        self.beamDirection.serialize(outputStream)
        outputStream.write_float(int(self.azimuthBeamwidth))
        outputStream.write_float(int(self.elevationBeamwidth))
        self.serialize_enum(self.referenceSystem,outputStream)
        outputStream.write_byte(int(self.padding1))
        outputStream.write_short(int(self.padding2))
        outputStream.write_float(int(self.ez))
        outputStream.write_float(int(self.ex))
        outputStream.write_float(int(self.phase))
        outputStream.write_int(int(self.padding3))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.beamDirection.parse(inputStream)
        self.azimuthBeamwidth = inputStream.read_float()
        self.elevationBeamwidth = inputStream.read_float()
        self.referenceSystem = TransmitterAntennaPatternReferenceSystem.get_enum(self.parse_enum(self.referenceSystem,inputStream))
        self.padding1 = inputStream.read_byte()
        self.padding2 = inputStream.read_short()
        self.ez = inputStream.read_float()
        self.ex = inputStream.read_float()
        self.phase = inputStream.read_float()
        self.padding3 = inputStream.read_int()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 10

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



