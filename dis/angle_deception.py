from enum import Enum

from .siso_ref_010.enums.eeattribute_state_indicator import EEAttributeStateIndicator

class AngleDeception( object ):
    """The Angle Deception attribute record may be used to communicate discrete values that are associated with angle deception jamming that cannot be referenced to an emitter mode. The values provided in the record records (provided in the associated Electromagnetic Emission PDU). (The victim radar beams are those that are targeted by the jammer.) Section 6.2.21.2.2"""

    def __init__(self):
        """ Initializer for AngleDeception"""
        """ record type"""
        self.recordType = 3501
        """ The length of the record in octets."""
        self.recordLength = 48
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ indicates the emitter system for which the angle deception values are applicable. """
        self.emitterNumber = 0
        """ indicates the jamming beam for which the angle deception values are applicable."""
        self.beamNumber = 0
        # /** This field shall be used to indicate if angle deception data have changed since issuance of the last Angle Deception attribute record for this beam, if the Angle Deception attribute record is part of a heartbeat update to meet periodic update requirements or if the angle deception data for the beam has ceased. uid 300 */
        self.stateIndicator = EEAttributeStateIndicator.default

        """ padding"""
        self.padding2 = 0
        """ This field indicates the relative azimuth angle at which the deceptive radar returns are centered. This angle is measured in the X-Y plane of the victim radar's entity coordinate system (see 1.4.3). This angle is measured in radians from the victim radar entity's azimuth for the true jam- mer position to the center of the range of azimuths in which deceptive radar returns are perceived as shown in Figure 43. Positive and negative values indicate that the perceived positions of the jammer are right and left of the true position of the jammer, respectively. The range of permissible values is -PI to PI"""
        self.azimuthOffset = 0.0
        """ indicates the range of azimuths (in radians) through which the deceptive radar returns are perceived, centered on the azimuth offset as shown in Figure 43. The range of permissible values is 0 to 2PI radians"""
        self.azimuthWidth = 0.0
        """ This field indicates the rate (in radians per second) at which the Azimuth Offset value is changing. Positive and negative values indicate that the Azimuth Offset is moving to the right or left, respectively."""
        self.azimuthPullRate = 0.0
        """ This field indicates the rate (in radians per second squared) at which the Azimuth Pull Rate value is changing. Azimuth Pull Acceleration is defined as positive to the right and negative to the left."""
        self.azimuthPullAcceleration = 0.0
        """ This field indicates the relative elevation angle at which the deceptive radar returns begin. This angle is measured as an angle with respect to the X-Y plane of the victim radar's entity coordinate system (see 1.4.3). This angle is measured in radians from the victim radar entity's eleva- tion for the true jammer position to the center of the range of elevations in which deceptive radar returns are perceived as shown in Figure 44. Positive and negative values indicate that the perceived positions of the jammer are above and below the true position of the jammer, respectively. The range of permissible values is -PI/2 to PI/2"""
        self.elevationOffset = 0.0
        """ This field indicates the range of elevations (in radians) through which the decep- tive radar returns are perceived, centered on the elevation offset as shown in Figure 44. The range of permissible values is 0 to PI radians"""
        self.elevationWidth = 0.0
        """ This field indicates the rate (in radians per second) at which the Elevation Off- set value is changing. Positive and negative values indicate that the Elevation Offset is moving up or down, respectively. """
        self.elevationPullRate = 0.0
        """ This field indicates the rate (in radians per second squared) at which the Elevation Pull Rate value is changing. Elevation Pull Acceleration is defined as positive to upward and negative downward. """
        self.elevationPullAcceleration = 0.0
        """ """
        self.padding3 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "RecordType : " + str(self.recordType) + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "EmitterNumber : " + str(self.emitterNumber) + "\n"
        outputString += "BeamNumber : " + str(self.beamNumber) + "\n"
        outputString += "EEAttributeStateIndicator : " + self.stateIndicator.get_description + "(" + (str(int(self.stateIndicator))) + ")" + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "AzimuthOffset : " + str(self.azimuthOffset) + "\n"
        outputString += "AzimuthWidth : " + str(self.azimuthWidth) + "\n"
        outputString += "AzimuthPullRate : " + str(self.azimuthPullRate) + "\n"
        outputString += "AzimuthPullAcceleration : " + str(self.azimuthPullAcceleration) + "\n"
        outputString += "ElevationOffset : " + str(self.elevationOffset) + "\n"
        outputString += "ElevationWidth : " + str(self.elevationWidth) + "\n"
        outputString += "ElevationPullRate : " + str(self.elevationPullRate) + "\n"
        outputString += "ElevationPullAcceleration : " + str(self.elevationPullAcceleration) + "\n"
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
        outputStream.write_int(int(self.recordType))
        outputStream.write_short(int(self.recordLength))
        outputStream.write_short(int(self.padding))
        outputStream.write_byte(int(self.emitterNumber))
        outputStream.write_byte(int(self.beamNumber))
        self.serialize_enum(self.stateIndicator,outputStream)
        outputStream.write_byte(int(self.padding2))
        outputStream.write_float(int(self.azimuthOffset))
        outputStream.write_float(int(self.azimuthWidth))
        outputStream.write_float(int(self.azimuthPullRate))
        outputStream.write_float(int(self.azimuthPullAcceleration))
        outputStream.write_float(int(self.elevationOffset))
        outputStream.write_float(int(self.elevationWidth))
        outputStream.write_float(int(self.elevationPullRate))
        outputStream.write_float(int(self.elevationPullAcceleration))
        outputStream.write_int(int(self.padding3))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = inputStream.read_int()
        self.recordLength = inputStream.read_short()
        self.padding = inputStream.read_short()
        self.emitterNumber = inputStream.read_byte()
        self.beamNumber = inputStream.read_byte()
        self.stateIndicator = EEAttributeStateIndicator.get_enum(self.parse_enum(self.stateIndicator,inputStream))
        self.padding2 = inputStream.read_byte()
        self.azimuthOffset = inputStream.read_float()
        self.azimuthWidth = inputStream.read_float()
        self.azimuthPullRate = inputStream.read_float()
        self.azimuthPullAcceleration = inputStream.read_float()
        self.elevationOffset = inputStream.read_float()
        self.elevationWidth = inputStream.read_float()
        self.elevationPullRate = inputStream.read_float()
        self.elevationPullAcceleration = inputStream.read_float()
        self.padding3 = inputStream.read_int()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 16

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



