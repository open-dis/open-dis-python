from enum import Enum

from .vector3float import Vector3Float
from .vector3double import Vector3Double
from .siso_ref_010.enums.deprecision_aimpoint_beam_spot_type import DEPrecisionAimpointBeamSpotType
from .entity_id import EntityID

class DirectedEnergyPrecisionAimpoint( object ):
    """DE Precision Aimpoint Record. Section 6.2.20.3"""

    def __init__(self):
        """ Initializer for DirectedEnergyPrecisionAimpoint"""
        """ Type of Record"""
        self.recordType = 4000
        """ Length of Record"""
        self.recordLength = 88
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ Position of Target Spot in World Coordinates."""
        self.targetSpotLocation = Vector3Double()
        """ Position (meters) of Target Spot relative to Entity Position."""
        self.targetSpotEntityLocation = Vector3Float()
        """ Velocity (meters/sec) of Target Spot."""
        self.targetSpotVelocity = Vector3Float()
        """ Acceleration (meters/sec/sec) of Target Spot."""
        self.targetSpotAcceleration = Vector3Float()
        """ Unique ID of the target entity."""
        self.targetEntityID = EntityID()
        """ Target Component ID ENUM, same as in DamageDescriptionRecord."""
        self.targetComponentID = 0
        # /** Spot Shape ENUM. uid 311 */
        self.beamSpotType = DEPrecisionAimpointBeamSpotType.default

        """ Beam Spot Cross Section Semi-Major Axis."""
        self.beamSpotCrossSectionSemiMajorAxis = 0
        """ Beam Spot Cross Section Semi-Major Axis."""
        self.beamSpotCrossSectionSemiMinorAxis = 0
        """ Beam Spot Cross Section Orientation Angle."""
        self.beamSpotCrossSectionOrientationAngle = 0
        """ Peak irradiance"""
        self.peakIrradiance = 0
        """ padding"""
        self.padding2 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "RecordType : " + str(self.recordType) + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "TargetSpotLocation :" + "\n" + self.targetSpotLocation.to_string() + "\n"
        outputString += "TargetSpotEntityLocation :" + "\n" + self.targetSpotEntityLocation.to_string() + "\n"
        outputString += "TargetSpotVelocity :" + "\n" + self.targetSpotVelocity.to_string() + "\n"
        outputString += "TargetSpotAcceleration :" + "\n" + self.targetSpotAcceleration.to_string() + "\n"
        outputString += "TargetEntityID :" + "\n" + self.targetEntityID.to_string() + "\n"
        outputString += "TargetComponentID : " + str(self.targetComponentID) + "\n"
        outputString += "DEPrecisionAimpointBeamSpotType : " + self.beamSpotType.get_description + "(" + (str(int(self.beamSpotType))) + ")" + "\n"
        outputString += "BeamSpotCrossSectionSemiMajorAxis : " + str(self.beamSpotCrossSectionSemiMajorAxis) + "\n"
        outputString += "BeamSpotCrossSectionSemiMinorAxis : " + str(self.beamSpotCrossSectionSemiMinorAxis) + "\n"
        outputString += "BeamSpotCrossSectionOrientationAngle : " + str(self.beamSpotCrossSectionOrientationAngle) + "\n"
        outputString += "PeakIrradiance : " + str(self.peakIrradiance) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
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
        self.targetSpotLocation.serialize(outputStream)
        self.targetSpotEntityLocation.serialize(outputStream)
        self.targetSpotVelocity.serialize(outputStream)
        self.targetSpotAcceleration.serialize(outputStream)
        self.targetEntityID.serialize(outputStream)
        outputStream.write_byte(int(self.targetComponentID))
        self.serialize_enum(self.beamSpotType,outputStream)
        outputStream.write_float(int(self.beamSpotCrossSectionSemiMajorAxis))
        outputStream.write_float(int(self.beamSpotCrossSectionSemiMinorAxis))
        outputStream.write_float(int(self.beamSpotCrossSectionOrientationAngle))
        outputStream.write_float(int(self.peakIrradiance))
        outputStream.write_int(int(self.padding2))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = inputStream.read_int()
        self.recordLength = inputStream.read_short()
        self.padding = inputStream.read_short()
        self.targetSpotLocation.parse(inputStream)
        self.targetSpotEntityLocation.parse(inputStream)
        self.targetSpotVelocity.parse(inputStream)
        self.targetSpotAcceleration.parse(inputStream)
        self.targetEntityID.parse(inputStream)
        self.targetComponentID = inputStream.read_byte()
        self.beamSpotType = DEPrecisionAimpointBeamSpotType.get_enum(self.parse_enum(self.beamSpotType,inputStream))
        self.beamSpotCrossSectionSemiMajorAxis = inputStream.read_float()
        self.beamSpotCrossSectionSemiMinorAxis = inputStream.read_float()
        self.beamSpotCrossSectionOrientationAngle = inputStream.read_float()
        self.peakIrradiance = inputStream.read_float()
        self.padding2 = inputStream.read_int()

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



