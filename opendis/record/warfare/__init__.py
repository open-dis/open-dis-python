"""Warfare Family PDU record types"""

__all__ = [
    "DEFireFlags",
    "DamageDescriptionRecord",
    "DirectedEnergyDamage",
    "DirectedEnergyAreaAimpoint",
    "DirectedEnergyPrecisionAimpoint",
    "DirectedEnergyTargetEnergyDeposition",
]

from opendis.record import base, bitfield
from opendis.record.common import *
from opendis.stream import DataInputStream, DataOutputStream
from opendis.types import (
    enum8,
    enum16,
    enum32,
    bf_enum,
    bf_int,
    bf_uint,
    float32,
    float64,
    struct8,
    uint8,
    uint16,
    uint32,
)

from .enums import DEFireFlags
from opendis.record.radio import BeamAntennaPattern


class DamageDescriptionRecord(base.StandardVariableRecord):
    """6.2.15 Damage Description record
    
    Damage Description records shall use the Standard Variable record format of
    the Standard Variable Specification record (see 6.2.83). 
    New Damage Description records may be defined at some future date as needed.
    """


class DirectedEnergyDamage(DamageDescriptionRecord):
    """6.2.15.2 Directed Energy Damage Description record
    
    Damage sustained by an entity due to directed energy. Location of the
    damage based on a relative x, y, z location from the center of the entity.
    """
    recordType: enum32 = 4500  # [UID 66] Variable Record Type

    def __init__(
            self,
            damageLocation: Vector3Float | None = None,
            damageDiameter: float32 = 0.0,  # in metres
            temperature: float32 = -273.15,  # in degrees Celsius
            componentIdentification: enum8 = 0,  # [UID 314]
            componentDamageStatus: enum8 = 0,  # [UID 315]
            componentVisualDamageStatus: struct8 = 0,  # [UID 317]
            componentVisualSmokeColor: enum8 = 0,  # [UID 316]
            fireEventID: EventIdentifier | None = None):
        self.padding: uint16 = 0
        self.damageLocation = damageLocation or Vector3Float()
        self.damageDiameter = damageDiameter
        self.temperature = temperature
        self.componentIdentification = componentIdentification
        self.componentDamageStatus = componentDamageStatus
        self.componentVisualDamageStatus = componentVisualDamageStatus
        self.componentVisualSmokeColor = componentVisualSmokeColor
        self.fireEventID = fireEventID or EventIdentifier()
        self.padding2: uint16 = 0
    
    def marshalledSize(self) -> int:
        return 40

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_uint32(self.recordType)
        outputStream.write_uint16(self.recordLength)
        outputStream.write_uint16(self.padding)
        self.damageLocation.serialize(outputStream)
        outputStream.write_float32(self.damageDiameter)
        outputStream.write_float32(self.temperature)
        outputStream.write_uint8(self.componentIdentification)
        outputStream.write_uint8(self.componentDamageStatus)
        outputStream.write_uint8(self.componentVisualDamageStatus)
        outputStream.write_uint8(self.componentVisualSmokeColor)
        self.fireEventID.serialize(outputStream)
        outputStream.write_uint16(self.padding2)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.padding = inputStream.read_unsigned_short()
        self.damageLocation.parse(inputStream)
        self.damageDiameter = inputStream.read_float32()
        self.temperature = inputStream.read_float32()
        self.componentIdentification = inputStream.read_uint8()
        self.componentDamageStatus = inputStream.read_uint8()
        self.componentVisualDamageStatus = inputStream.read_uint8()
        self.componentVisualSmokeColor = inputStream.read_uint8()
        self.fireEventID.parse(inputStream)
        self.padding2 = inputStream.read_uint16()


class DirectedEnergyAreaAimpoint(DamageDescriptionRecord):
    """6.2.20.2 DE Area Aimpoint record

    Targeting information when the target of the directed energy weapon is an
    area. The area may or may not be associated with one or more target
    entities.
    """
    recordType: enum32 = 4001  # [UID 66]

    def __init__(self,
                 beamAntennaPatterns: list["BeamAntennaPattern"] | None = None,
                 directedEnergyTargetEnergyDepositions: list["DirectedEnergyTargetEnergyDeposition"] | None = None):
        self.padding: uint16 = 0
        self.beamAntennaPatterns: list["BeamAntennaPattern"] = beamAntennaPatterns or []
        self.directedEnergyTargetEnergyDepositions: list["DirectedEnergyTargetEnergyDeposition"] = directedEnergyTargetEnergyDepositions or []

    @property
    def beamAntennaPatternCount(self) -> uint16:
        return len(self.beamAntennaPatterns)

    @property
    def directedEnergyTargetEnergyDepositionCount(self) -> uint16:
        return len(self.directedEnergyTargetEnergyDepositions)

    def marshalledSize(self) -> int:
        size = 8  # recordType, recordLength, padding
        for record in self.beamAntennaPatterns:
            size += record.marshalledSize()
        for record in self.directedEnergyTargetEnergyDepositions:
            size += record.marshalledSize()
        return size
    
    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_uint32(self.recordType)
        outputStream.write_uint16(self.recordLength)
        outputStream.write_uint16(self.padding)
        outputStream.write_uint16(self.beamAntennaPatternCount)
        outputStream.write_uint16(
            self.directedEnergyTargetEnergyDepositionCount
        )
        for record in self.beamAntennaPatterns:
            record.serialize(outputStream)

        for record in self.directedEnergyTargetEnergyDepositions:
            record.serialize(outputStream)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.padding = inputStream.read_uint16()
        beamAntennaPatternCount = inputStream.read_uint16()
        directedEnergyTargetEnergyDepositionCount = inputStream.read_uint16()
        for _ in range(0, beamAntennaPatternCount):
            record = BeamAntennaPattern()
            record.parse(inputStream)
            self.beamAntennaPatterns.append(record)
        for _ in range(0, directedEnergyTargetEnergyDepositionCount):
            record = DirectedEnergyTargetEnergyDeposition()
            record.parse(inputStream)
            self.directedEnergyTargetEnergyDepositions.append(record)


class DirectedEnergyPrecisionAimpoint(DamageDescriptionRecord):
    """6.2.20.3 DE Precision Aimpoint record

    Targeting information when the target of the directed energy weapon is not
    an area but a specific target entity. Use of this record assumes that the DE
    weapon would not fire unless a target is known and is currently tracked.
    """
    recordType: enum32 = 4000

    def __init__(self,
                 targetSpotLocation: WorldCoordinates | None = None,
                 targetSpotEntityLocation: Vector3Float | None = None,
                 targetSpotVelocity: Vector3Float | None = None,  # in m/s
                 targetSpotAcceleration: Vector3Float | None = None,  # in m/s^2
                 targetEntityID: EntityIdentifier | None = None,
                 targetComponentID: enum8 = 0,  # [UID 314]
                 beamSpotType: enum8 = 0,  # [UID 311]
                 beamSpotCrossSectionSemiMajorAxis: float32 = 0.0,  # in meters
                 beamSpotCrossSectionSemiMinorAxis: float32 = 0.0,  # in meters
                 beamSpotCrossSectionOrientationAngle: float32 = 0.0,  # in radians
                 peakIrradiance: float32 = 0.0):  # in W/m^2
        self.padding: uint16 = 0
        self.targetSpotLocation = targetSpotLocation or WorldCoordinates()
        self.targetSpotEntityLocation = targetSpotEntityLocation or Vector3Float()
        self.targetSpotVelocity = targetSpotVelocity or Vector3Float()
        self.targetSpotAcceleration = targetSpotAcceleration or Vector3Float()
        self.targetEntityID = targetEntityID or EntityIdentifier()
        self.targetComponentID = targetComponentID
        self.beamSpotType = beamSpotType
        self.beamSpotCrossSectionSemiMajorAxis = beamSpotCrossSectionSemiMajorAxis
        self.beamSpotCrossSectionSemiMinorAxis = beamSpotCrossSectionSemiMinorAxis
        self.beamSpotCrossSectionOrientationAngle = beamSpotCrossSectionOrientationAngle
        self.peakIrradiance = peakIrradiance
        self.padding2: uint32 = 0

    def marshalledSize(self) -> int:
        return 96

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_uint32(self.recordType)
        outputStream.write_uint16(self.recordLength)
        outputStream.write_uint16(self.padding)
        self.targetSpotLocation.serialize(outputStream)
        self.targetSpotEntityLocation.serialize(outputStream)
        self.targetSpotVelocity.serialize(outputStream)
        self.targetSpotAcceleration.serialize(outputStream)
        self.targetEntityID.serialize(outputStream)
        outputStream.write_uint8(self.targetComponentID)
        outputStream.write_uint8(self.beamSpotType)
        outputStream.write_float32(self.beamSpotCrossSectionSemiMajorAxis)
        outputStream.write_float32(self.beamSpotCrossSectionSemiMinorAxis)
        outputStream.write_float32(self.beamSpotCrossSectionOrientationAngle)
        outputStream.write_float32(self.peakIrradiance)
        outputStream.write_uint32(self.padding2)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int) -> None:
        """recordType and recordLength are assumed to have been read before
        this method is called.
        """
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.padding = inputStream.read_uint16()
        self.targetSpotLocation.parse(inputStream)
        self.targetSpotEntityLocation.parse(inputStream)
        self.targetSpotVelocity.parse(inputStream)
        self.targetSpotAcceleration.parse(inputStream)
        self.targetEntityID.parse(inputStream)
        self.targetComponentID = inputStream.read_uint8()
        self.beamSpotType = inputStream.read_uint8()
        self.beamSpotCrossSectionSemiMajorAxis = inputStream.read_float32()
        self.beamSpotCrossSectionSemiMinorAxis = inputStream.read_float32()
        self.beamSpotCrossSectionOrientationAngle = inputStream.read_float32()
        self.peakIrradiance = inputStream.read_float32()
        self.padding2 = inputStream.read_uint32()


class DirectedEnergyTargetEnergyDeposition(base.Record):
    """6.2.20.4 DE Target Energy Deposition record

    Directed energy deposition properties for a target entity shall be
    communicated using the DE Target Energy Deposition record. This record is
    required to be included inside another DE record as it does not have a
    record type.
    """

    def __init__(self,
                 targetEntityID: EntityIdentifier | None = None,
                 peakIrradiance: float32 = 0.0):  # in W/m^2
        self.targetEntityID = targetEntityID or EntityIdentifier()
        self.padding: uint16 = 0
        self.peakIrradiance = peakIrradiance

    def marshalledSize(self) -> int:
        return self.targetEntityID.marshalledSize() + 6

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        self.targetEntityID.serialize(outputStream)
        outputStream.write_uint16(self.padding)
        outputStream.write_float32(self.peakIrradiance)

    def parse(self, inputStream: DataInputStream) -> None:
        super().parse(inputStream)
        self.targetEntityID.parse(inputStream)
        self.padding = inputStream.read_uint16()
        self.peakIrradiance = inputStream.read_float32()
