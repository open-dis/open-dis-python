"""Record type classes for OpenDIS7.

This module defines classes for various record types used in DIS PDUs.
"""

from collections.abc import Sequence
from ctypes import (
    _SimpleCData,
    BigEndianStructure,
    c_uint8,
    c_uint16,
    c_uint32,
    sizeof,
)
from typing import Literal

from .stream import DataInputStream, DataOutputStream
from .types import (
    enum16,
    bf_enum,
    bf_int,
    bf_uint,
    uint8,
    uint16,
    uint32,
)

# Type definitions for bitfield field descriptors
CTypeFieldDescription = tuple[str, type[_SimpleCData], int]
DisFieldDescription = tuple[str, "DisFieldType", int]

# Field type constants simplify the construction of bitfields
# which would otherwise require manually specifying ctypes types.
# The currently implemented bitfields only use integers, but DIS7
# mentions CHAR types which may be needed in future.
DisFieldType = Literal["INTEGER"]
INTEGER = "INTEGER"


def field(name: str,
          ftype: DisFieldType,
          bits: int) -> CTypeFieldDescription:
    """Helper function to create the field description tuple used by ctypes."""
    match (ftype, bits):
        case (INTEGER, b) if 0 < b <= 8:
            return (name, c_uint8, bits)
        case (INTEGER, b) if 8 < b <= 16:
            return (name, c_uint16, bits)
        case (INTEGER, b) if 16 < b <= 32:
            return (name, c_uint32, bits)
        case _:
            raise ValueError(f"Unrecognized (ftype, bits): {ftype}, {bits}")


def _bitfield(name: str,
              fields: Sequence[DisFieldDescription]):
    """Factory function for bitfield structs, which are subclasses of
    ctypes.Structure.
    These are used in records that require them to unpack non-octet-sized fields.

    Args:
        name: Name of the bitfield struct.
        bytesize: Size of the bitfield in bytes.
        fields: Sequence of tuples defining fields of the bitfield, in the form
            (field_name, "INTEGER", field_size_in_bits).
    """
    # Argument validation
    struct_fields = []
    bitsize = 0
    for name, ftype, bits in fields:
        if ftype not in (INTEGER,):
            raise ValueError(f"Unsupported field type: {ftype}")
        if not isinstance(bits, int):
            raise ValueError(f"Field size must be int: {bits!r}")
        if bits <= 0 or bits > 32:
            raise ValueError(f"Field size must be between 1 and 32: got {bits}")
        bitsize += bits
        struct_fields.append(field(name, ftype, bits))

    if bitsize == 0:
        raise ValueError(f"Bitfield size cannot be zero")
    elif bitsize % 8 != 0:
        raise ValueError(f"Bitfield size must be multiple of 8, got {bitsize}")
    bytesize = bitsize // 8

    # Create the struct class
    class Bitfield(BigEndianStructure):
        _fields_ = struct_fields

        @staticmethod
        def marshalledSize() -> int:
            return bytesize
    
        def serialize(self, outputStream: DataOutputStream) -> None:
            outputStream.write_bytes(bytes(self))
    
        @classmethod
        def parse(cls, inputStream: DataInputStream) -> "Bitfield":
            return cls.from_buffer_copy(inputStream.read_bytes(bytesize))

    # Sanity check: ensure the struct size matches expected size
    assert sizeof(Bitfield) == bytesize, \
        f"Bitfield size mismatch: expected {bytesize}, got {sizeof(Bitfield)}"

    # Assign the class name
    Bitfield.__name__ = name
    return Bitfield


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

    _struct = _bitfield(name="NetId", fields=[
        ("netNumber", INTEGER, 10),
        ("frequencyTable", INTEGER, 2),
        ("mode", INTEGER, 2),
        ("padding", INTEGER, 2)
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

    _struct = _bitfield(name="SpreadSpectrum", fields=[
        ("frequencyHopping", INTEGER, 1),
        ("pseudoNoise", INTEGER, 1),
        ("timeHopping", INTEGER, 1),
        ("padding", INTEGER, 13)
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


class GenericRadio:
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


class SimpleIntercomRadio:
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

class BasicHaveQuickMP:
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
