"""
Reading from Java DataInputStream format.
From https://github.com/arngarden/python_java_datastream
This uses big endian (network) format.
"""

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
