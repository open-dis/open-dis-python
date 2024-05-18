from collections.abc import Sequence
from ctypes import _CData, BigEndianStructure, c_uint
from .types import (
    bf_enum,
    bf_int,
    bf_uint,
)

from DataInputStream import DataInputStream
from DataOutputStream import DataOutputStream


def bitfield(
        name: str,
        bytesize: int,
        fields: Sequence[
            tuple[str, type[_CData]] | tuple[str, type[_CData], int]
        ],
    ):
    """Factory function for bitfield structs, which are subclasses of
    ctypes.Structure.
    These are used in records that require them to unpack non-octet-sized fields.
    """
    assert bytesize > 0, "Cannot create bitfield with zero bytes"

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
    _struct = bitfield("NetId", 2, [
        ("netNumber", c_uint, 10),
        ("frequencyTable", c_uint, 2),
        ("mode", c_uint, 2),
        ("padding", c_uint, 2)
    ])
    
    def __init__(self,
                 netNumber: bf_uint,
                 frequencyTable: bf_enum,  # [UID 299]
                 mode: bf_enum,  # [UID 298]
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
    _struct = bitfield("SpreadSpectrum", 2, [
        ("frequencyHopping", c_uint, 1),
        ("pseudoNoise", c_uint, 1),
        ("timeHopping", c_uint, 1),
        ("padding", c_uint, 13)
    ])
    
    def __init__(self,
                 frequencyHopping: bool,
                 pseudoNoise: bool,
                 timeHopping: bool,
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
        # Pass bool to __init__ instead of int
        record_bitfield = self._struct.parse(inputStream)
        self.frequencyHopping = bool(record_bitfield.frequencyHopping)
        self.pseudoNoise = bool(record_bitfield.pseudoNoise)
        self.timeHopping = bool(record_bitfield.timeHopping)

