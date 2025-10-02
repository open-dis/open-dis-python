"""Bitfield type factory and related utilities.

This module provides a factory function to create ctypes.Structure subclasses
representing bitfields as defined in the DIS standard. These bitfields are used
in various DIS records to pack multiple non-octet-aligned fields into a compact
binary representation.
"""

from ctypes import (
    _SimpleCData,
    BigEndianStructure,
    c_uint8,
    c_uint16,
    c_uint32,
    sizeof,
)
from typing import Literal, Sequence

from opendis.stream import DataInputStream, DataOutputStream

# Type definitions for bitfield field descriptors
CTypeFieldDescription = tuple[str, type[_SimpleCData], int]
DisFieldDescription = tuple[str, "DisFieldType", int]

# Field type constants simplify the construction of bitfields
# which would otherwise require manually specifying ctypes types.
# The currently implemented bitfields only use integers, but DIS7
# mentions CHAR types which may be needed in future.
DisFieldType = Literal["INTEGER"]
INTEGER = "INTEGER"


def _field(name: str,
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


def bitfield(name: str,
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
        struct_fields.append(_field(name, ftype, bits))

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
