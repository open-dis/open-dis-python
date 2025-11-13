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
from opendis.types import bf_enum, bf_int, bf_uint

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
          bits: int,
          base_ctype: type[_SimpleCData]) -> CTypeFieldDescription:
    """Helper function to create the field description tuple used by ctypes.

    Args:
        name: Field name
        ftype: Field type (currently only INTEGER supported)
        bits: Number of bits for this field
        base_ctype: The base C type to use for all fields (ensures proper packing)
    """
    if ftype != INTEGER:
        raise ValueError(f"Unrecognized ftype: {ftype}")
    if bits <= 0 or bits > 32:
        raise ValueError(f"Field size must be between 1 and 32: got {bits}")
    return (name, base_ctype, bits)


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
    # First pass: calculate total bitsize and validate
    bitsize = 0
    for field_name, ftype, bits in fields:
        if ftype not in (INTEGER,):
            raise ValueError(f"Unsupported field type: {ftype}")
        if not isinstance(bits, int):
            raise ValueError(f"Field size must be int: {bits!r}")
        if bits <= 0 or bits > 32:
            raise ValueError(f"Field size must be between 1 and 32: got {bits}")
        bitsize += bits

    if bitsize == 0:
        raise ValueError(f"Bitfield size cannot be zero")
    elif bitsize % 8 != 0:
        raise ValueError(f"Bitfield size must be multiple of 8, got {bitsize}")
    bytesize = bitsize // 8

    # Determine base ctype based on TOTAL size (critical for Python 3.12+ compatibility)
    # All fields must use the same underlying type to avoid padding issues
    if bitsize <= 8:
        base_ctype = c_uint8
    elif bitsize <= 16:
        base_ctype = c_uint16
    elif bitsize <= 32:
        base_ctype = c_uint32
    else:
        raise ValueError(f"Bitfield size {bitsize} exceeds maximum of 32 bits")

    # Second pass: create fields with consistent base type
    struct_fields = []
    for field_name, ftype, bits in fields:
        struct_fields.append(_field(field_name, ftype, bits, base_ctype))

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
