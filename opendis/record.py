"""Record type classes for OpenDIS7.

This module defines classes for various record types used in DIS PDUs.
"""

from abc import ABC, abstractmethod

import bitfield
from .stream import DataInputStream, DataOutputStream
from .types import (
    enum8,
    enum16,
    enum32,
    bf_enum,
    bf_int,
    bf_uint,
    float32,
    uint8,
    uint16,
    uint32,
)


class EulerAngles:
    """Section 6.2.32 Euler Angles record

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

    def serialize(self, outputStream):
        """serialize the class"""
        outputStream.write_float32(self.psi)
        outputStream.write_float32(self.theta)
        outputStream.write_float32(self.phi)

    def parse(self, inputStream):
        """Parse a message. This may recursively call embedded objects."""
        self.psi = inputStream.read_float32()
        self.theta = inputStream.read_float32()
        self.phi = inputStream.read_float32()


class ModulationType:
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


class NetId:
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


class SpreadSpectrum:
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


class ModulationParametersRecord(ABC):
    """6.2.58 Modulation Parameters record
    
    Base class for modulation parameters records, as defined in Annex C.
    The total length of each record shall be a multiple of 64 bits.
    """

    @abstractmethod
    def marshalledSize(self) -> int:
        """Return the size of the record when serialized."""
        raise NotImplementedError()
    
    @abstractmethod
    def serialize(self, outputStream: DataOutputStream) -> None:
        """Serialize the record to the output stream."""
        raise NotImplementedError()
    
    @abstractmethod
    def parse(self, inputStream: DataInputStream) -> None:
        """Parse the record from the input stream."""
        raise NotImplementedError()


class UnknownRadio(ModulationParametersRecord):
    """Placeholder for unknown or unimplemented radio types."""

    def __init__(self, data: bytes = b''):
        self.data = data

    def marshalledSize(self) -> int:
        return len(self.data)

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_bytes(self.data)

    def parse(self, inputStream: DataInputStream, bytelength: int = 0) -> None:
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

    def parse(self, inputStream: DataInputStream) -> None:
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

    def parse(self, inputStream: DataInputStream) -> None:
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
        self.net_id.serialize(outputStream)
        outputStream.write_uint16(self.mwod_index)
        outputStream.write_uint16(self.reserved16)
        outputStream.write_uint8(self.reserved8_1)
        outputStream.write_uint8(self.reserved8_2)
        outputStream.write_uint32(self.time_of_day)
        outputStream.write_uint32(self.padding)

    def parse(self, inputStream: DataInputStream) -> None:
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
        outputStream.write_uint16(self.fh_net_id)
        outputStream.write_uint16(self.hop_set_id)
        outputStream.write_uint16(self.lockout_set_id)
        outputStream.write_uint8(self.start_of_message)
        outputStream.write_uint8(self.clear_channel)
        outputStream.write_uint32(self.fh_sync_time_offset)
        outputStream.write_uint16(self.transmission_security_key)
        outputStream.write_uint16(self.padding)

    def parse(self, inputStream: DataInputStream) -> None:
        self.fh_net_id = inputStream.read_uint16()
        self.hop_set_id = inputStream.read_uint16()
        self.lockout_set_id = inputStream.read_uint16()
        self.start_of_message = inputStream.read_uint8()
        self.clear_channel = inputStream.read_uint8()
        self.fh_sync_time_offset = inputStream.read_uint32()
        self.transmission_security_key = inputStream.read_uint16()
        self.padding = inputStream.read_uint16()


class AntennaPatternRecord(ABC):
    """6.2.8 Antenna Pattern record
    
    The total length of each record shall be a multiple of 64 bits.
    """

    @abstractmethod
    def marshalledSize(self) -> int:
        """Return the size of the record when serialized."""
        raise NotImplementedError()
    
    @abstractmethod
    def serialize(self, outputStream: DataOutputStream) -> None:
        """Serialize the record to the output stream."""
        raise NotImplementedError()
    
    @abstractmethod
    def parse(self, inputStream: DataInputStream) -> None:
        """Parse the record from the input stream."""
        raise NotImplementedError()


class UnknownAntennaPattern(AntennaPatternRecord):
    """Placeholder for unknown or unimplemented antenna pattern types."""

    def __init__(self, data: bytes = b''):
        self.data = data

    def marshalledSize(self) -> int:
        return len(self.data)

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_bytes(self.data)

    def parse(self, inputStream: DataInputStream, bytelength: int = 0) -> None:
        """Parse a message. This may recursively call embedded objects."""
        self.data = inputStream.read_bytes(bytelength)


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

    def parse(self, inputStream: DataInputStream) -> None:
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


class VariableTransmitterParametersRecord(ABC):
    """6.2.95 Variable Transmitter Parameters record
    
    One or more VTP records may be associated with a radio system, and the same
    VTP record may be associated with multiple radio systems.
    Specific VTP records applicable to a radio system are identified in the
    subclause that defines the radio system’s unique requirements in Annex C.
    The total length of each record shall be a multiple of 64 bits.
    """
    recordType: enum32

    @abstractmethod
    def marshalledSize(self) -> int:
        """Return the size of the record when serialized."""

    @abstractmethod
    def serialize(self, outputStream: DataOutputStream) -> None:
        """Serialize the record to the output stream."""
    
    @abstractmethod
    def parse(self, inputStream: DataInputStream) -> None:
        """Parse the record from the input stream.
        
        The recordType field is assumed to have been read, so as to identify
        the type of VTP record to be parsed, before this method is called.
        """


class UnknownVariableTransmitterParameters(VariableTransmitterParametersRecord):
    """Placeholder for unknown or unimplemented variable transmitter parameter
    types.
    """
    recordType: enum32 = 0

    def __init__(self, recordType: enum32 = 0, data: bytes = b""):
        self.recordType = recordType  # [UID 66]  Variable Parameter Record Type
        self.data = data
    
    def marshalledSize(self) -> int:
        return 6 + len(self.data)
    
    @property
    def recordLength(self) -> uint16:
        return self.marshalledSize()

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_uint32(self.recordType)
        outputStream.write_uint16(self.recordLength)
        outputStream.write_bytes(self.data)

    def parse(self, inputStream: DataInputStream) -> None:
        self.recordType = inputStream.read_uint32()
        recordLength = inputStream.read_uint16()
        self.data = inputStream.read_bytes(recordLength)


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
    
    @property
    def recordLength(self) -> uint16:
        return self.marshalledSize()
    
    def marshalledSize(self) -> int:
        return 40
    
    def serialize(self, outputStream: DataOutputStream) -> None:
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
    
    def parse(self, inputStream: DataInputStream) -> None:
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
