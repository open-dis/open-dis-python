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
)
from typing import Literal

from .types import (
    bf_enum,
    bf_int,
    bf_uint,
)

from .DataInputStream import DataInputStream
from .DataOutputStream import DataOutputStream

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


def _bitfield(
        name: str,
        bytesize: int,
        fields: Sequence[
            tuple[str, type[_SimpleCData]] | tuple[str, type[_SimpleCData], int]
        ],
    ):
    """Factory function for bitfield structs, which are subclasses of
    ctypes.Structure.
    These are used in records that require them to unpack non-octet-sized fields.

    Args:
        name: Name of the bitfield struct.
        bytesize: Size of the bitfield in bytes.
        fields: Sequence of tuples defining the fields of the bitfield.
                See https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_
    """
    if bytesize <= 0:
        raise ValueError("Cannot create bitfield with less than one byte")

    class Bitfield(BigEndianStructure):
        _fields_ = fields
    
        @staticmethod
        def marshalledSize() -> int:
            return bytesize
    
        def serialize(self, outputStream: DataOutputStream) -> None:
            outputStream.write_bytes(bytes(self))
    
        @classmethod
        def parse(cls, inputStream: DataInputStream) -> "Bitfield":
            return cls.from_buffer_copy(inputStream.read_bytes(bytesize))
    Bitfield.__name__ = name
    return Bitfield


class NetId:
    """Annex C, Table C.5

    Represents an Operational Net in the format of NXX.XYY, where:
    N = Mode
    XXX = Net Number
    YY = Frequency Table
    """

    _struct = _bitfield(name="NetId", bytesize=2, fields=[
        ("netNumber", c_uint, 10),
        ("frequencyTable", c_uint, 2),
        ("mode", c_uint, 2),
        ("padding", c_uint, 2)
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

    _struct = _bitfield("SpreadSpectrum", 2, [
        ("frequencyHopping", c_uint, 1),
        ("pseudoNoise", c_uint, 1),
        ("timeHopping", c_uint, 1),
        ("padding", c_uint, 13)
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
