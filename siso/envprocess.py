"""envprocess.py

14 Environmental Process
"""
import enum


"""14.1 Model Type [UID 248]
Value Description
0 No Statement"""
# [UID 248]
class ModelType(enum.IntEnum):
    """14.1 Model Type [UID 248]"""
    NO_STATEMENT = 0


"""14.2 Environment Status [UID 249]
Any individual bit set to one indicates that the Environmental Process has the corresponding status.
Name | Bits | Description | Reference
Is Last | 0 | Indicates that the current update shall be the last update for
the specified process
Is Active | 1 | Describes whether the environmental process is active or not"""


"""14.3 Environment Record Type"""

"""14.3.1 Environment Record Type Groups [UID 273]
Value Description
0 State
1 Geometry"""
# [UID 273]
class EnvironmentRecordType(enum.IntEnum):
    """14.3.1 Environment Record Type Groups [UID 273]"""
    STATE = 0
    GEOMETRY = 1


# [UID 250]
class StateRecord(enum.IntEnum):
    """14.3.3 State Records [UID 250] (Group 0)"""
    COMBIC_STATE = 0x100
    FLARE_STATE = 0x103


# [UID 250]
class GeometryRecord(enum.IntEnum):
    """14.3.2 Geometry Records [UID 250] (Group 1)"""
    BOUNDING_SPHERE = 0x10000
    UNIFORM_GEOMETRY = 0x50000
    POINT_1 = 0xA0000
    LINE_1 = 0xC0000
    SPHERE_1 = 0xD0000
    ELLIPSOID_1 = 0x100000
    CONE_1 = 0x300000
    RECT_VOLUME_1 = 0x500000
    RECT_VOLUME_3 = 0x5000000
    POINT_2 = 0xA000000
    LINE_2 = 0xC000000
    SPHERE_2 = 0xD000000
    ELLIPSOID_2 = 0x10000000
    CONE_2 = 0x30000000
    RECT_VOLUME_2 = 0x50000000
    GAUSSIAN_PLUME = 0x60000000
    GAUSSIAN_PUFF = 0x70000000


"""14.4 Geometry Records [UID 251-267]
The geometry records for [UID 251-267] have been moved. The current definitions can be found in DIS PCR 240."""


"""14.5 State Records [UID 268-269]
The state records for [UID 268-269] have been moved. The current definitions can be found in DIS PCR 240.
"""
