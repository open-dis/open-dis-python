"""
Writing to Java DataInputStream format.
From https://github.com/arngarden/python_java_datastream/blob/master/data_output_stream.py
This uses big endian (network) format
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
