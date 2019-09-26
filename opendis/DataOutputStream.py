"""
Writing to Java DataInputStream format.
From https://github.com/arngarden/python_java_datastream/blob/master/data_output_stream.py
This uses big endian (network) format
"""

import struct

class DataOutputStream:
    def __init__(self, stream):
        self.stream = stream

    def write_boolean(self, bool):
        self.stream.write(struct.pack('?', bool))

    def write_byte(self, val):
        self.stream.write(struct.pack('b', val))

    def write_unsigned_byte(self, val):
        self.stream.write(struct.pack('B', val))
    
    def write_char(self, val):
        self.stream.write(struct.pack('>H', ord(val)))

    def write_double(self, val):
        self.stream.write(struct.pack('>d', val))

    def write_float(self, val):
        self.stream.write(struct.pack('>f', val))

    def write_short(self, val):
        self.stream.write(struct.pack('>h', val))

    def write_unsigned_short(self, val):
        self.stream.write(struct.pack('>H', val))

    def write_long(self, val):
        self.stream.write(struct.pack('>q', val))

    def write_utf(self, string):
        self.stream.write(struct.pack('>H', len(string)))
        self.stream.write(string)

    def write_int(self, val):
        self.stream.write(struct.pack('>i', val))

    def write_unsigned_int(self, val):
        self.stream.write(struct.pack('>I', val))

