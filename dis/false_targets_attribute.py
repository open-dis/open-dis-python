from enum import Enum

from .siso_ref_010.enums.eeattribute_state_indicator import EEAttributeStateIndicator

class FalseTargetsAttribute( object ):
    """The False Targets attribute record shall be used to communicate discrete values that are associated with false targets jamming that cannot be referenced to an emitter mode. The values provided in the False Targets attri- bute record shall be considered valid only for the victim radar beams listed in the jamming beam's Track/Jam Data records (provided in the associated Electromagnetic Emission PDU). Section 6.2.21.3"""

    def __init__(self):
        """ Initializer for FalseTargetsAttribute"""
        """ record type"""
        self.recordType = 3502
        """ The length of the record in octets."""
        self.recordLength = 40
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ This field indicates the emitter system generating the false targets."""
        self.emitterNumber = 0
        """ This field indicates the jamming beam generating the false targets. """
        self.beamNumber = 0
        # /** This field shall be used to indicate if false target data have changed since issuance of the last False Targets attribute record for this beam, if the False Targets attribute record is part of a heartbeat update to meet periodic update requirements or if false target data for the beam has ceased. uid 300 */
        self.stateIndicator = EEAttributeStateIndicator.default

        """ padding"""
        self.padding2 = 0
        self.padding3 = 0
        """ This field indicates the jamming beam generating the false targets. """
        self.falseTargetCount = 0
        """ This field shall specify the speed (in meters per second) at which false targets move toward the victim radar. Negative values shall indicate a velocity away from the victim radar. """
        self.walkSpeed = 0.0
        """ This field shall specify the rate (in meters per second squared) at which false tar- gets accelerate toward the victim radar. Negative values shall indicate an acceleration direction away from the victim radar. """
        self.walkAcceleration = 0.0
        """ This field shall specify the distance (in meters) that a false target is to walk before it pauses in range. """
        self.maximumWalkDistance = 0.0
        """ This field shall specify the time (in seconds) that a false target is to be held at the Maxi- mum Walk Distance before it resets to its initial position. """
        self.keepTime = 0.0
        """ This field shall specify the distance between false targets in meters. Positive values for this field shall indicate that second and subsequent false targets are initially placed at increasing ranges from the victim radar. """
        self.echoSpacing = 0.0
        """ Sets the position of the first false target relative to the jamming entity in meters."""
        self.firstTargetOffset = 0.0

    def to_string(self) ->str:
        outputString = ""
        outputString += "RecordType : " + str(self.recordType) + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "EmitterNumber : " + str(self.emitterNumber) + "\n"
        outputString += "BeamNumber : " + str(self.beamNumber) + "\n"
        outputString += "EEAttributeStateIndicator : " + self.stateIndicator.get_description + "(" + (str(int(self.stateIndicator))) + ")" + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "Padding3 : " + str(self.padding3) + "\n"
        outputString += "FalseTargetCount : " + str(self.falseTargetCount) + "\n"
        outputString += "WalkSpeed : " + str(self.walkSpeed) + "\n"
        outputString += "WalkAcceleration : " + str(self.walkAcceleration) + "\n"
        outputString += "MaximumWalkDistance : " + str(self.maximumWalkDistance) + "\n"
        outputString += "KeepTime : " + str(self.keepTime) + "\n"
        outputString += "EchoSpacing : " + str(self.echoSpacing) + "\n"
        outputString += "FirstTargetOffset : " + str(self.firstTargetOffset) + "\n"
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
        outputStream.write_short(int(self.padding3))
        outputStream.write_short(int(self.falseTargetCount))
        outputStream.write_float(int(self.walkSpeed))
        outputStream.write_float(int(self.walkAcceleration))
        outputStream.write_float(int(self.maximumWalkDistance))
        outputStream.write_float(int(self.keepTime))
        outputStream.write_float(int(self.echoSpacing))
        outputStream.write_float(int(self.firstTargetOffset))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = inputStream.read_int()
        self.recordLength = inputStream.read_short()
        self.padding = inputStream.read_short()
        self.emitterNumber = inputStream.read_byte()
        self.beamNumber = inputStream.read_byte()
        self.stateIndicator = EEAttributeStateIndicator.get_enum(self.parse_enum(self.stateIndicator,inputStream))
        self.padding2 = inputStream.read_byte()
        self.padding3 = inputStream.read_short()
        self.falseTargetCount = inputStream.read_short()
        self.walkSpeed = inputStream.read_float()
        self.walkAcceleration = inputStream.read_float()
        self.maximumWalkDistance = inputStream.read_float()
        self.keepTime = inputStream.read_float()
        self.echoSpacing = inputStream.read_float()
        self.firstTargetOffset = inputStream.read_float()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 15

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



