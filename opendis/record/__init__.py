"""Record type classes for OpenDIS7.

This module defines classes for various record types used in DIS PDUs.
"""

from abc import abstractmethod
from typing import TypeVar

from . import base, bitfield
from ..stream import DataInputStream, DataOutputStream
from ..types import (
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

SV = TypeVar('SV', bound=base.StandardVariableRecord)


class Vector3Float(base.Record):
    """6.2.96 Vector record
    
    Vector values for entity coordinates, linear acceleration, and linear
    velocity shall be represented using a Vector record. This record shall
    consist of three fields, each a 32-bit floating point number.
    The unit of measure represented by these fields shall depend on the
    information represented.
    """

    def __init__(self, x: float32 = 0.0, y: float32 = 0.0, z: float32 = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def marshalledSize(self) -> int:
        return 12

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_float(self.x)
        outputStream.write_float(self.y)
        outputStream.write_float(self.z)

    def parse(self, inputStream: DataInputStream) -> None:
        self.x = inputStream.read_float()
        self.y = inputStream.read_float()
        self.z = inputStream.read_float()


class WorldCoordinates(base.Record):
    """6.2.98 World Coordinates record

    Location of the origin of the entity's or object's coordinate system,
    target locations, detonation locations, and other points shall be specified
    by a set of three coordinates: X, Y, and Z, represented by 64-bit floating
    point numbers.
    """

    def __init__(self, x: float64 = 0.0, y: float64 = 0.0, z: float64 = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def marshalledSize(self) -> int:
        return 24

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_float64(self.x)
        outputStream.write_float64(self.y)
        outputStream.write_float64(self.z)

    def parse(self, inputStream: DataInputStream) -> None:
        self.x = inputStream.read_float64()
        self.y = inputStream.read_float64()
        self.z = inputStream.read_float64()


class EntityIdentifier(base.Record):
    """Section 6.2.28

    Entity Identifier. Unique ID for entities in the world. Consists of a
    simulation address and a entity number.
    """

    def __init__(self,
                 simulationAddress: "SimulationAddress | None" = None,
                 entityNumber: uint16 = 0):
        self.simulationAddress = simulationAddress or SimulationAddress()
        self.entityNumber = entityNumber
    
    def marshalledSize(self) -> int:
        return self.simulationAddress.marshalledSize() + 2

    def serialize(self, outputStream: DataOutputStream) -> None:
        self.simulationAddress.serialize(outputStream)
        outputStream.write_uint16(self.entityNumber)

    def parse(self, inputStream: DataInputStream) -> None:
        self.simulationAddress.parse(inputStream)
        self.entityNumber = inputStream.read_uint16()


class EulerAngles(base.Record):
    """6.2.32 Euler Angles record

    Three floating point values representing an orientation, psi, theta,
    and phi, aka the euler angles, in radians.
    These angles shall be specified with respect to the entity's coordinate
    system.
    """

    def __init__(self,
                 psi: float32 = 0.0,
                 theta: float32 = 0.0,
                 phi: float32 = 0.0):  # in radians
        self.psi = psi
        self.theta = theta
        self.phi = phi

    def marshalledSize(self) -> int:
        return 12

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_float32(self.psi)
        outputStream.write_float32(self.theta)
        outputStream.write_float32(self.phi)

    def parse(self, inputStream: DataInputStream) -> None:
        self.psi = inputStream.read_float32()
        self.theta = inputStream.read_float32()
        self.phi = inputStream.read_float32()


class SimulationAddress(base.Record):
    """6.2.80 Simulation Address record
    
    Simulation designation associated with all object identifiers except
    those contained in Live Entity PDUs.
    """

    def __init__(self,
                 site: uint16 = 0,
                 application: uint16 = 0):
        self.site = site
        """A site is defined as a facility, installation, organizational unit or a geographic location that has one or more simulation applications capable of participating in a distributed event."""
        self.application = application
        """An application is defined as a software program that is used to generate and process distributed simulation data including live, virtual and constructive data."""

    def marshalledSize(self) -> int:
        return 4

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_unsigned_short(self.site)
        outputStream.write_unsigned_short(self.application)

    def parse(self, inputStream: DataInputStream) -> None:
        self.site = inputStream.read_unsigned_short()
        self.application = inputStream.read_unsigned_short()


class EventIdentifier(base.Record):
    """6.2.33 Event Identifier record
    
    Identifies an event in the world. Use this format for every PDU EXCEPT
    the LiveEntityPdu.
    """
    # TODO: Distinguish EventIdentifier and LiveEventIdentifier

    def __init__(self,
                 simulationAddress: "SimulationAddress | None" = None,
                 eventNumber: uint16 = 0):
        self.simulationAddress = simulationAddress or SimulationAddress()
        """Site and application IDs"""
        self.eventNumber = eventNumber

    def marshalledSize(self) -> int:
        return self.simulationAddress.marshalledSize() + 2

    def serialize(self, outputStream: DataOutputStream) -> None:
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.eventNumber)

    def parse(self, inputStream: DataInputStream) -> None:
        self.simulationAddress.parse(inputStream)
        self.eventNumber = inputStream.read_unsigned_short()


class ModulationType(base.Record):
    """Section 6.2.59
    
    Information about the type of modulation used for radio transmission.
    """

    def __init__(self,
                 spreadSpectrum: "SpreadSpectrum | None" = None,  # See RPR Enumerations
                 majorModulation: enum16 = 0,  # [UID 155]
                 detail: enum16 = 0,  # [UID 156-162]
                 radioSystem: enum16 = 0):  # [UID 163]
        self.spreadSpectrum = spreadSpectrum or SpreadSpectrum()
        """This field shall indicate the spread spectrum technique or combination of spread spectrum techniques in use. Bit field. 0=freq hopping, 1=psuedo noise, time hopping=2, remaining bits unused"""
        self.majorModulation = majorModulation
        self.detail = detail
        self.radioSystem = radioSystem

    def marshalledSize(self) -> int:
        size = 0
        size += self.spreadSpectrum.marshalledSize()
        size += 2  # majorModulation
        size += 2  # detail
        size += 2  # radioSystem
        return size

    def serialize(self, outputStream: DataOutputStream) -> None:
        self.spreadSpectrum.serialize(outputStream)
        outputStream.write_uint16(self.majorModulation)
        outputStream.write_uint16(self.detail)
        outputStream.write_uint16(self.radioSystem)

    def parse(self, inputStream: DataInputStream) -> None:
        self.spreadSpectrum.parse(inputStream)
        self.majorModulation = inputStream.read_uint16()
        self.detail = inputStream.read_uint16()
        self.radioSystem = inputStream.read_uint16()


class NetId(base.Record):
    """Annex C, Table C.5

    Represents an Operational Net in the format of NXX.XYY, where:
    N = Mode
    XXX = Net Number
    YY = Frequency Table
    """

    _struct = bitfield.bitfield(name="NetId", fields=[
        ("netNumber", bitfield.INTEGER, 10),
        ("frequencyTable", bitfield.INTEGER, 2),
        ("mode", bitfield.INTEGER, 2),
        ("padding", bitfield.INTEGER, 2)
    ])
    
    def __init__(self,
                 netNumber: bf_uint = 0,
                 frequencyTable: bf_enum = 0,  # [UID 299]
                 mode: bf_enum = 0,  # [UID 298]
                 padding: bf_uint = 0):
        # Net number ranging from 0 to 999 decimal
        self.netNumber = netNumber
        self.frequencyTable = frequencyTable
        self.mode = mode
        self.padding = padding

    def marshalledSize(self) -> int:
        return self._struct.marshalledSize()

    def serialize(self, outputStream: DataOutputStream) -> None:
        self._struct(
            self.netNumber,
            self.frequencyTable,
            self.mode,
            self.padding
        ).serialize(outputStream)

    def parse(self, inputStream: DataInputStream) -> None:
        record_bitfield = self._struct.parse(inputStream)
        self.netNumber = record_bitfield.netNumber
        self.frequencyTable = record_bitfield.frequencyTable
        self.mode = record_bitfield.mode
        self.padding = record_bitfield.padding


class SpreadSpectrum(base.Record):
    """6.2.59 Modulation Type Record, Table 90

    Modulation used for radio transmission is characterized in a generic
    fashion by the Spread Spectrum, Major Modulation, and Detail fields.

    Each independent type of spread spectrum technique shall be represented by
    a single element of this array.
    If a particular spread spectrum technique is in use, the corresponding array
    element shall be set to one; otherwise it shall be set to zero.
    All unused array elements shall be set to zero.

    In Python, the presence or absence of each technique is indicated by a bool.
    """

    _struct = bitfield.bitfield(name="SpreadSpectrum", fields=[
        ("frequencyHopping", bitfield.INTEGER, 1),
        ("pseudoNoise", bitfield.INTEGER, 1),
        ("timeHopping", bitfield.INTEGER, 1),
        ("padding", bitfield.INTEGER, 13)
    ])

    def __init__(self,
                 frequencyHopping: bool = False,
                 pseudoNoise: bool = False,
                 timeHopping: bool = False,
                 padding: bf_uint = 0):
        self.frequencyHopping = frequencyHopping
        self.pseudoNoise = pseudoNoise
        self.timeHopping = timeHopping
        self.padding = padding

    def marshalledSize(self) -> int:
        return self._struct.marshalledSize()

    def serialize(self, outputStream: DataOutputStream) -> None:
        # Bitfield expects int input
        self._struct(
            int(self.frequencyHopping),
            int(self.pseudoNoise),
            int(self.timeHopping),
            self.padding
        ).serialize(outputStream)

    def parse(self, inputStream: DataInputStream) -> None:
        record_bitfield = self._struct.parse(inputStream)
        self.frequencyHopping = bool(record_bitfield.frequencyHopping)
        self.pseudoNoise = bool(record_bitfield.pseudoNoise)
        self.timeHopping = bool(record_bitfield.timeHopping)


class ModulationParametersRecord(base.VariableRecord):
    """6.2.58 Modulation Parameters record
    
    Base class for modulation parameters records, as defined in Annex C.
    The total length of each record shall be a multiple of 64 bits.
    """


class UnknownRadio(ModulationParametersRecord):
    """Placeholder for unknown or unimplemented radio types."""

    def __init__(self, data: bytes = b''):
        self.data = data

    def marshalledSize(self) -> int:
        return len(self.data)

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_bytes(self.data)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int | None = None) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.data = inputStream.read_bytes(bytelength)


class GenericRadio(ModulationParametersRecord):
    """Annex C.2 Generic Radio record
    
    There are no other specific Transmitter, Signal, or Receiver PDU
    requirements unique to a generic radio.
    """

    def marshalledSize(self) -> int:
        return 0
    
    def serialize(self, outputStream: DataOutputStream) -> None:
        pass

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int | None = None) -> None:
        pass


class SimpleIntercomRadio(ModulationParametersRecord):
    """Annex C.3 Simple Intercom Radio
    
    A Simple Intercom shall be identified by both the Transmitter PDU
    Modulation Type record—Radio System field indicating a system type of
    Generic Radio or Simple Intercom (1) and by the Modulation Type
    record—Major Modulation field set to No Statement (0).

    This class has specific field requirements for the TransmitterPdu.
    """

    def marshalledSize(self) -> int:
        return 0
    
    def serialize(self, outputStream: DataOutputStream) -> None:
        pass

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int | None = None) -> None:
        pass


# C.4 HAVE QUICK Radios

class BasicHaveQuickMP(ModulationParametersRecord):
    """Annex C 4.2.2, Table C.3 — Basic HAVE QUICK MP record"""

    def __init__(self,
                 net_id: NetId | None = None,
                 mwod_index: uint16 = 1,
                 reserved16: uint16 = 0,
                 reserved8_1: uint8 = 0,
                 reserved8_2: uint8 = 0,
                 time_of_day: uint32 = 0,
                 padding: uint32 = 0):
        self.net_id = net_id or NetId()
        self.mwod_index = mwod_index
        self.reserved16 = reserved16
        self.reserved8_1 = reserved8_1
        self.reserved8_2 = reserved8_2
        self.time_of_day = time_of_day
        self.padding = padding

    def marshalledSize(self) -> int:
        return 16  # bytes

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        self.net_id.serialize(outputStream)
        outputStream.write_uint16(self.mwod_index)
        outputStream.write_uint16(self.reserved16)
        outputStream.write_uint8(self.reserved8_1)
        outputStream.write_uint8(self.reserved8_2)
        outputStream.write_uint32(self.time_of_day)
        outputStream.write_uint32(self.padding)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int | None = None) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.net_id.parse(inputStream)
        self.mwod_index = inputStream.read_uint16()
        self.reserved16 = inputStream.read_uint16()
        self.reserved8_1 = inputStream.read_uint8()
        self.reserved8_2 = inputStream.read_uint8()
        self.time_of_day = inputStream.read_uint32()
        self.padding = inputStream.read_uint32()


class CCTTSincgarsMP(ModulationParametersRecord):
    """Annex C 6.2.3, Table C.7 — CCTT SINCGARS MP record"""

    def __init__(self,
                 fh_net_id: uint16 = 0,
                 hop_set_id: uint16 = 0,
                 lockout_set_id: uint16 = 0,
                 start_of_message: enum8 = 0,
                 clear_channel: enum8 = 0,
                 fh_sync_time_offset: uint32 = 0,
                 transmission_security_key: uint16 = 0):
        self.fh_net_id = fh_net_id
        self.hop_set_id = hop_set_id
        self.lockout_set_id = lockout_set_id
        self.start_of_message = start_of_message
        self.clear_channel = clear_channel
        self.fh_sync_time_offset = fh_sync_time_offset
        self.transmission_security_key = transmission_security_key
        self.padding: uint16 = 0

    def marshalledSize(self) -> int:
        return 16  # bytes

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_uint16(self.fh_net_id)
        outputStream.write_uint16(self.hop_set_id)
        outputStream.write_uint16(self.lockout_set_id)
        outputStream.write_uint8(self.start_of_message)
        outputStream.write_uint8(self.clear_channel)
        outputStream.write_uint32(self.fh_sync_time_offset)
        outputStream.write_uint16(self.transmission_security_key)
        outputStream.write_uint16(self.padding)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int | None = None) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.fh_net_id = inputStream.read_uint16()
        self.hop_set_id = inputStream.read_uint16()
        self.lockout_set_id = inputStream.read_uint16()
        self.start_of_message = inputStream.read_uint8()
        self.clear_channel = inputStream.read_uint8()
        self.fh_sync_time_offset = inputStream.read_uint32()
        self.transmission_security_key = inputStream.read_uint16()
        self.padding = inputStream.read_uint16()


class AntennaPatternRecord(base.VariableRecord):
    """6.2.8 Antenna Pattern record
    
    The total length of each record shall be a multiple of 64 bits.
    """


class UnknownAntennaPattern(AntennaPatternRecord):
    """Placeholder for unknown or unimplemented antenna pattern types."""

    def __init__(self, data: bytes = b''):
        self.data = data

    def marshalledSize(self) -> int:
        return len(self.data)

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_bytes(self.data)

    def parse(self,  # pyright: ignore[reportIncompatibleMethodOverride]
              inputStream: DataInputStream,
              bytelength: int) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        # Read the remaining bytes in the record
        self.data = inputStream.read_bytes(bytelength - 6)


class BeamAntennaPattern(AntennaPatternRecord):
    """6.2.8.2 Beam Antenna Pattern record
    
    Used when the antenna pattern type field has a value of 1. Specifies the
    direction, pattern, and polarization of radiation from an antenna.
    """

    def __init__(self,
                 beamDirection: "EulerAngles | None" = None,
                 azimuthBeamwidth: float32 = 0.0,  # in radians
                 elevationBeamwidth: float32 = 0.0,  # in radians
                 referenceSystem: enum8 = 0,  # [UID 168]
                 ez: float32 = 0.0,
                 ex: float32 = 0.0,
                 phase: float32 = 0.0):  # in radians
        self.beamDirection = beamDirection or EulerAngles()
        """The rotation that transforms the reference coordinate sytem into the beam coordinate system. Either world coordinates or entity coordinates may be used as the reference coordinate system, as specified by the reference system field of the antenna pattern record."""
        self.azimuthBeamwidth = azimuthBeamwidth
        self.elevationBeamwidth = elevationBeamwidth
        self.referenceSystem = referenceSystem
        self.padding1: uint8 = 0
        self.padding2: uint16 = 0
        self.ez = ez
        """This field shall specify the magnitude of the Z-component (in beam coordinates) of the Electrical field at some arbitrary single point in the main beam and in the far field of the antenna."""
        self.ex = ex
        """This field shall specify the magnitude of the X-component (in beam coordinates) of the Electrical field at some arbitrary single point in the main beam and in the far field of the antenna."""
        self.phase = phase
        """This field shall specify the phase angle between EZ and EX in radians. If fully omni-directional antenna is modeled using beam pattern type one, the omni-directional antenna shall be represented by beam direction Euler angles psi, theta, and phi of zero, an azimuth beamwidth of 2PI, and an elevation beamwidth of PI"""
        self.padding3: uint32 = 0

    def marshalledSize(self) -> int:
        return 40

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        self.beamDirection.serialize(outputStream)
        outputStream.write_float32(self.azimuthBeamwidth)
        outputStream.write_float32(self.elevationBeamwidth)
        outputStream.write_uint8(self.referenceSystem)
        outputStream.write_uint8(self.padding1)
        outputStream.write_uint16(self.padding2)
        outputStream.write_float32(self.ez)
        outputStream.write_float32(self.ex)
        outputStream.write_float32(self.phase)
        outputStream.write_uint32(self.padding3)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int | None = 40) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.beamDirection.parse(inputStream)
        self.azimuthBeamwidth = inputStream.read_float32()
        self.elevationBeamwidth = inputStream.read_float32()
        self.referenceSystem = inputStream.read_uint8()
        self.padding1 = inputStream.read_uint8()
        self.padding2 = inputStream.read_uint16()
        self.ez = inputStream.read_float32()
        self.ex = inputStream.read_float32()
        self.phase = inputStream.read_float32()
        self.padding3 = inputStream.read_uint32()


class VariableTransmitterParametersRecord(base.StandardVariableRecord):
    """6.2.95 Variable Transmitter Parameters record
    
    One or more VTP records may be associated with a radio system, and the same
    VTP record may be associated with multiple radio systems.
    Specific VTP records applicable to a radio system are identified in the
    subclause that defines the radio system's unique requirements in Annex C.
    The total length of each record shall be a multiple of 64 bits.
    """


class UnknownVariableTransmitterParameters(VariableTransmitterParametersRecord):
    """Placeholder for unknown or unimplemented variable transmitter parameter
    types.
    """

    def __init__(self, recordType: enum32 = 0, data: bytes = b""):
        self.recordType = recordType  # [UID 66]  Variable Parameter Record Type
        self.data = data
    
    def marshalledSize(self) -> int:
        return 6 + len(self.data)
    
    @property
    def recordLength(self) -> uint16:
        return self.marshalledSize()

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_uint32(self.recordType)
        outputStream.write_uint16(self.recordLength)
        outputStream.write_bytes(self.data)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.recordType = inputStream.read_uint32()
        recordLength = inputStream.read_uint16()
        # Read the remaining bytes in the record
        self.data = inputStream.read_bytes(recordLength - 6)


class HighFidelityHAVEQUICKRadio(VariableTransmitterParametersRecord):
    """Annex C C4.2.3, Table C.4 — High Fidelity HAVE QUICK Radio record"""
    recordType: enum32 = 3000

    def __init__(self,
                 netId: NetId | None = None,
                 todTransmitIndicator: enum8 = 0,
                 todDelta: uint32 = 0,
                 wod1: uint32 = 0,
                 wod2: uint32 = 0,
                 wod3: uint32 = 0,
                 wod4: uint32 = 0,
                 wod5: uint32 = 0,
                 wod6: uint32 = 0):
        self.padding1: uint16 = 0
        self.netId = netId or NetId()
        self.todTransmitIndicator = todTransmitIndicator
        self.padding2: uint8 = 0
        self.todDelta = todDelta
        self.wod1 = wod1
        self.wod2 = wod2
        self.wod3 = wod3
        self.wod4 = wod4
        self.wod5 = wod5
        self.wod6 = wod6
    
    def marshalledSize(self) -> int:
        return 40
    
    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_uint16(self.padding1)
        self.netId.serialize(outputStream)
        outputStream.write_uint8(self.todTransmitIndicator)
        outputStream.write_uint8(self.padding2)
        outputStream.write_uint32(self.todDelta)
        outputStream.write_uint32(self.wod1)
        outputStream.write_uint32(self.wod2)
        outputStream.write_uint32(self.wod3)
        outputStream.write_uint32(self.wod4)
        outputStream.write_uint32(self.wod5)
        outputStream.write_uint32(self.wod6)
    
    def parse(self,
              inputStream: DataInputStream,
              bytelength: int) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.padding1 = inputStream.read_uint16()
        self.netId.parse(inputStream)
        self.todTransmitIndicator = inputStream.read_uint8()
        self.padding2 = inputStream.read_uint8()
        self.todDelta = inputStream.read_uint32()
        self.wod1 = inputStream.read_uint32()
        self.wod2 = inputStream.read_uint32()
        self.wod3 = inputStream.read_uint32()
        self.wod4 = inputStream.read_uint32()
        self.wod5 = inputStream.read_uint32()
        self.wod6 = inputStream.read_uint32()


class DamageDescriptionRecord(base.StandardVariableRecord):
    """6.2.15 Damage Description record
    
    Damage Description records shall use the Standard Variable record format of
    the Standard Variable Specification record (see 6.2.83). 
    New Damage Description records may be defined at some future date as needed.
    """


class UnknownDamage(DamageDescriptionRecord):
    """Placeholder for unknown or unimplemented damage description types."""

    def __init__(self, recordType: enum32 = 0, data: bytes = b''):
        self.recordType = recordType  # [UID 66]  Variable Parameter Record Type
        self.data = data

    def marshalledSize(self) -> int:
        return 6 + len(self.data)

    def serialize(self, outputStream: DataOutputStream) -> None:
        super().serialize(outputStream)
        outputStream.write_uint32(self.recordType)
        outputStream.write_uint16(self.recordLength)
        outputStream.write_bytes(self.data)

    def parse(self,
              inputStream: DataInputStream,
              bytelength: int) -> None:
        # Validate bytelength argument by calling base method
        super().parse(inputStream, bytelength)
        self.recordType = inputStream.read_uint32()
        recordLength = inputStream.read_uint16()
        # Read the remaining bytes in the record
        self.data = inputStream.read_bytes(recordLength - 6)


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


__variableRecordClasses: dict[int, type[base.StandardVariableRecord]] = {
    3000: HighFidelityHAVEQUICKRadio,
    4000: DirectedEnergyPrecisionAimpoint,
    4001: DirectedEnergyAreaAimpoint,
    4500: DirectedEnergyDamage,
}

def getSVClass(
        recordType: int,
        expectedType: type[SV] = base.StandardVariableRecord
) -> type[SV] | None:
    if not isinstance(recordType, int) or recordType < 0:
        raise ValueError(
            f"recordType must be a non-negative integer, got {recordType!r}"
        )
    vrClass = __variableRecordClasses.get(recordType, None)
    if vrClass is None:
        return None
    if not issubclass(vrClass, expectedType):
        raise TypeError(
            f"Record Type {recordType}: Record class {vrClass.__name__} is not "
            f"a subclass of {expectedType.__name__}"
        )
    return vrClass  # type: ignore[return-value]
