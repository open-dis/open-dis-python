"""Warfare Family PDU record types: SISO enumeration classes"""

from opendis.record import base, bitfield
from opendis.stream import DataInputStream, DataOutputStream
from opendis.types import bf_enum, bf_uint


class DEFireFlags(base.Record):
    """SISO-REF-010-2025 18.5.2 DE Fire Flags [UID 313]"""

    _struct = bitfield.bitfield(name="DEFireFlags", fields=[
        ("weaponOn", bitfield.INTEGER, 1),  # state of the DE Weapon
        ("stateUpdateFlag", bitfield.INTEGER, 1),  # DE Weapon State Change
        ("padding", bitfield.INTEGER, 14)  # unused bits
    ])
    
    def __init__(self,
                 weaponOn: bool = False,
                 stateUpdateFlag: bf_enum = 0):  # [UID 299]
        # Net number ranging from 0 to 999 decimal
        self.weaponOn = weaponOn
        self.stateUpdateFlag = stateUpdateFlag
        self.padding: bf_uint = 0

    def marshalledSize(self) -> int:
        return self._struct.marshalledSize()

    def serialize(self, outputStream: DataOutputStream) -> None:
        self._struct(
            self.weaponOn,
            self.stateUpdateFlag,
        ).serialize(outputStream)

    def parse(self, inputStream: DataInputStream) -> None:
        record_bitfield = self._struct.parse(inputStream)
        self.weaponOn = record_bitfield.weaponOn
        self.stateUpdateFlag = record_bitfield.stateUpdateFlag
        self.padding = record_bitfield.padding
