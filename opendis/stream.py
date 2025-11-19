"""Stream utilities

This module provides utilities for handling streams in the OpenDIS library.
"""

__all__ = ['DataInputStream', 'DataOutputStream']

from io import BufferedIOBase
import struct

from .types import (
    int8,
    int16,
    int32,
    int64,
    uint8,
    uint16,
    uint32,
    uint64,
    float32,
    float64,
    char8,
    char16,
)


class DataInputStream:
    def __init__(self, stream: BufferedIOBase):
        self.stream = stream

    def read_boolean(self) -> bool:
        return struct.unpack('?', self.stream.read(1))[0]

    def read_byte(self) -> int8:
        return struct.unpack('b', self.stream.read(1))[0]

    def read_unsigned_byte(self) -> uint8:
        return struct.unpack('B', self.stream.read(1))[0]

    def read_char(self) -> char16:
        return chr(struct.unpack('>H', self.stream.read(2))[0])

    def read_double(self) -> float64:
        return struct.unpack('>d', self.stream.read(8))[0]

    def read_float(self) -> float32:
        return struct.unpack('>f', self.stream.read(4))[0]

    def read_short(self) -> int16:
        return struct.unpack('>h', self.stream.read(2))[0]

    def read_unsigned_short(self) -> uint16:
        return struct.unpack('>H', self.stream.read(2))[0]

    def read_long(self) -> int64:
        return struct.unpack('>q', self.stream.read(8))[0]

    def read_utf(self) -> bytes:
        utf_length = struct.unpack('>H', self.stream.read(2))[0]
        return self.stream.read(utf_length)

    def read_int(self) -> int32:
        return struct.unpack('>i', self.stream.read(4))[0]

    def read_unsigned_int(self) -> uint32:
        return struct.unpack('>I', self.stream.read(4))[0]

    def read_bytes(self, n: int) -> bytes:
        """Read n bytes from the stream."""
        return self.stream.read(n)

    # Aliases for convenience
    def read_char8(self) -> char8:
        return char8(self.read_char())

    def read_float32(self) -> float32:
        return float32(self.read_float())

    def read_float64(self) -> float64:
        return float64(self.read_double())

    def read_int8(self) -> int8:
        return int8(self.read_byte())

    def read_int16(self) -> int16:
        return int16(self.read_short())

    def read_int32(self) -> int32:
        return int32(self.read_int())

    def read_int64(self) -> int64:
        return int64(self.read_long())

    def read_uint8(self) -> uint8:
        return uint8(self.read_unsigned_byte())

    def read_uint16(self) -> uint16:
        return uint16(self.read_unsigned_short())

    def read_uint32(self) -> uint32:
        return uint32(self.read_unsigned_int())

    def read_uint64(self) -> uint64:
        return uint64(self.read_long())


class DataOutputStream:
    def __init__(self, stream: BufferedIOBase):
        self.stream = stream

    def write_boolean(self, boolean: bool) -> None:
        self.stream.write(struct.pack('?', boolean))

    def write_byte(self, val: int) -> None:
        self.stream.write(struct.pack('b', val))

    def write_unsigned_byte(self, val: int) -> None:
        self.stream.write(struct.pack('B', val))
    
    def write_char(self, val: str) -> None:
        self.stream.write(struct.pack('>H', ord(val)))

    def write_double(self, val: float) -> None:
        self.stream.write(struct.pack('>d', val))

    def write_float(self, val: float) -> None:
        self.stream.write(struct.pack('>f', val))

    def write_short(self, val: int) -> None:
        self.stream.write(struct.pack('>h', val))

    def write_unsigned_short(self, val: int) -> None:
        self.stream.write(struct.pack('>H', val))

    def write_long(self, val: int) -> None:
        self.stream.write(struct.pack('>q', val))

    def write_utf(self, string: bytes) -> None:
        self.stream.write(struct.pack('>H', len(string)))
        self.stream.write(string)

    def write_int(self, val: int) -> None:
        self.stream.write(struct.pack('>i', val))

    def write_unsigned_int(self, val: int) -> None:
        self.stream.write(struct.pack('>I', val))

    def write_bytes(self, val: bytes) -> None:
        """Write bytes to the stream."""
        self.stream.write(val)

    # Aliases for convenience
    def write_char8(self, val: char8) -> None:
        self.write_byte(ord(val))

    def write_float32(self, val: float32) -> None:
        self.write_float(val)

    def write_float64(self, val: float64) -> None:
        self.write_double(val)

    def write_int8(self, val: int8) -> None:
        self.write_byte(val)

    def write_int16(self, val: int16) -> None:
        self.write_short(val)

    def write_int32(self, val: int32) -> None:
        self.write_int(val)

    def write_int64(self, val: int64) -> None:
        self.write_long(val)

    def write_uint8(self, val: uint8) -> None:
        self.write_unsigned_byte(val)

    def write_uint16(self, val: uint16) -> None:
        self.write_unsigned_short(val)

    def write_uint32(self, val: uint32) -> None:
        self.write_unsigned_int(val)

    def write_uint64(self, val: uint64) -> None:
        self.stream.write(struct.pack('>Q', val))
