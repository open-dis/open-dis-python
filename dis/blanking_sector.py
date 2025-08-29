from enum import Enum

from .siso_ref_010.enums.eeattribute_state_indicator import EEAttributeStateIndicator

class BlankingSector( object ):
    """The Blanking Sector attribute record may be used to convey persistent areas within a scan volume where emitter power for a specific active emitter beam is reduced to an insignificant value. Section 6.2.21.2"""

    def __init__(self):
        """ Initializer for BlankingSector"""
        """ record type"""
        self.recordType = 3500
        """ The length of the Blanking Sector attribute record in octets."""
        self.recordLength = 40
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ indicates the emitter system for which the blanking sector values are applicable"""
        self.emitterNumber = 0
        """ indicates the beam for which the blanking sector values are applicable."""
        self.beamNumber = 0
        # /** indicate if blanking sector data have changed since issuance of the last Blanking Sector attribute record for this beam, if the Blanking Sector attribute record beam has ceased uid 300 */
        self.stateIndicator = EEAttributeStateIndicator.default

        """ Padding"""
        self.padding2 = 0
        """ This field is provided to indicate the left-most azimuth (clockwise in radians) for which emitted power is reduced. This angle is measured in the X-Y plane of the radar's entity coor- dinate system (see 1.4.3). The range of permissible values is 0 to 2PI, with zero pointing in the X- direction. """
        self.leftAzimuth = 0.0
        """ Indicate the right-most azimuth (clockwise in radians) for which emitted power is reduced. This angle is measured in the X-Y plane of the radar's entity coordinate system (see 1.4.3). The range of permissible values is 0 to 2PI , with zero pointing in the X- direction."""
        self.rightAzimuth = 0.0
        """ This field is provided to indicate the lowest elevation (in radians) for which emit- ted power is reduced. This angle is measured positive upward with respect to the X-Y plane of the radar's entity coordinate system (see 1.4.3). The range of permissible values is -PI/2 to PI/2"""
        self.lowerElevation = 0.0
        """ This field is provided to indicate the highest elevation (in radians) for which emitted power is reduced. This angle is measured positive upward with respect to the X-Y plane of the radar's entitycoordinatesystem(see1.4.3). The range of permissible values is -PI/2 to PI/2"""
        self.upperElevation = 0.0
        """ This field shall specify the residual effective radiated power in the blanking sector in dBm. """
        self.residualPower = 0.0
        """ Padding, 32-bits"""
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
        outputString += "LeftAzimuth : " + str(self.leftAzimuth) + "\n"
        outputString += "RightAzimuth : " + str(self.rightAzimuth) + "\n"
        outputString += "LowerElevation : " + str(self.lowerElevation) + "\n"
        outputString += "UpperElevation : " + str(self.upperElevation) + "\n"
        outputString += "ResidualPower : " + str(self.residualPower) + "\n"
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
        outputStream.write_float(int(self.leftAzimuth))
        outputStream.write_float(int(self.rightAzimuth))
        outputStream.write_float(int(self.lowerElevation))
        outputStream.write_float(int(self.upperElevation))
        outputStream.write_float(int(self.residualPower))
        outputStream.write_long(int(self.padding3))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = inputStream.read_int()
        self.recordLength = inputStream.read_short()
        self.padding = inputStream.read_short()
        self.emitterNumber = inputStream.read_byte()
        self.beamNumber = inputStream.read_byte()
        self.stateIndicator = EEAttributeStateIndicator.get_enum(self.parse_enum(self.stateIndicator,inputStream))
        self.padding2 = inputStream.read_byte()
        self.leftAzimuth = inputStream.read_float()
        self.rightAzimuth = inputStream.read_float()
        self.lowerElevation = inputStream.read_float()
        self.upperElevation = inputStream.read_float()
        self.residualPower = inputStream.read_float()
        self.padding3 = inputStream.read_long()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 13

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



