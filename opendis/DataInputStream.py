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
    float32,
    float64,
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
