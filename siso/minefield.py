"""minefield.py

15 Minefields
"""
import enum


# [UID 190]
"""15.1 Appearance [UID 190]
Name           | Bits | Description                                | Reference
Minefield Type | 0-1  | Identifies the type of minefield           | [UID 418]
Active Status  | 2    | Describes whether the minefield is active or inactive | [UID 419]
Lane           | 3    | Identifies whether the minefield has an active or inactive lane | [UID 420]
State          | 13   | Describes the state of the minefield       | [UID 421]"""


# [UID 336]
class ProtocolMode(enum.IntEnum):
    """15.2 Protocol Mode [UID 336]"""
    HEARTBEAT_MODE = 0
    QRP_MODE = 1


# [UID 192]
"""15.3 Fusing [UID 192]
Name | Bits | Description | Reference
Primary | 0-6 | Identifies the type of the primary fuse | [UID 422]
Secondary | 7-13 | Identifies the type of the secondary fuse | [UID 422]
Has Anti-Handling Device | 14 | Describes whether the mine has an Anti-Handling device"""


# [UID 202]
"""15.4 Paint Scheme [UID 202]
Name | Bits | Description | Reference
Algae | 0-1 | Identifies the algae build-up on the mine | [UID 424]
Paint Scheme | 2-7 | Identifies the paint scheme of the mine | [UID 425]"""


# [UID 418]
class MinefieldType(enum.IntEnum):
    """15.5 Minefield Type [UID 418]"""
    MIXED_ANTI_PERSONNEL_AND_ANTI_TANK = 0
    PURE_ANTI_PERSONNEL = 1
    PURE_ANTI_TANK = 2


# [UID 419]
class ActiveStatus(enum.IntEnum):
    """15.6 Active [UID 419]"""
    ACTIVE = 0
    INACTIVE = 1


# [UID 420]
class Lane(enum.IntEnum):
    """15.7 Lane [UID 420]"""
    HAS_ACTIVE_LANE = 0
    HAS_INACTIVE_LANE = 1


# [UID 421]
class State(enum.IntEnum):
    """15.8 State [UID 421]"""
    ACTIVE = 0
    DEACTIVATED = 1


# [UID 422]
class FuseType(enum.IntEnum):
    """15.9 Fuse Type [UID 422]"""
    NO_FUSE = 0
    OTHER = 1
    PRESSURE = 2
    MAGNETIC = 3
    TILT_ROD = 4
    COMMAND = 5
    TRIP_WIRE = 6


# [UID 424]
class AlgaePaintScheme(enum.IntEnum):
    """15.10 Algae Paint Scheme [UID 424]"""
    NONE = 0
    LIGHT = 1
    MODERATE = 2
    HEAVY = 3


# [UID 425]
class PaintScheme(enum.IntEnum):
    """15.11 Paint Scheme [UID 425]"""
    NONE = 0
    STANDARD = 1
    CAMO_DESERT = 2
    CAMO_JUNGLE = 3
    CAMO_SNOW = 4
    CAMO_GRAVEL = 5
    CAMO_PAVEMENT = 6
    CAMO_SAND = 7
    NATURAL_WOOD = 8
    CLEAR = 9
    RED = 10
    BLUE = 11
    GREEN = 12
    OLIVE = 13
    WHITE = 14
    TAN = 15
    BLACK = 16
    YELLOW = 17
    BROWN = 18
