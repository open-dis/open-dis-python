"""ua.py

12 Underwater Acoustics
"""

import enum


# [UID 143]
class StateChangeUpdateIndicator(enum.IntEnum):
    """12.1 State/Change Update Indicator [UID 143]"""
    STATE_UPDATE = 0
    CHANGED_DATA_UPDATE = 1


# [UID 145]
class AcousticEmitterSystemFunction(enum.IntEnum):
    """12.2 Acoustic Emitter System Function [UID 145]"""
    OTHER = 0
    PLATFORM_SEARCH_DETECT_TRACK = 1
    NAVIGATION = 2
    MINE_HUNTING = 3
    WEAPON_SEARCH_DETECT_TRACK_DETECT = 4


# [UID 146]
class ActiveEmissionParameterIndex(enum.IntEnum):
    """12.3 Active Emission Parameter Index [UID 146]"""
    OTHER = 0


# [UID 147]
class ScanPattern(enum.IntEnum):
    """12.4 Scan Pattern [UID 147]"""
    OTHER = 0
    CONICAL = 1
    HELICAL = 2
    RASTER = 3
    SECTOR_SEARCH = 4
    CONTINUOUS_SEARCH = 5


# [UID 148]
class PassiveParameterIndex(enum.IntEnum):
    """12.5 Passive Parameter Index [UID 148]"""
    OTHER = 0


"""12.6 Propulsion Plant Configuration"""

# [UID 149]
class PropulsionPlantHullMountedMasker(enum.IntEnum):
    """12.6.1 Propulsion Plant Configuration [UID 149]
    Name                   | Bits | Description
    Hull Mounted Masker On |  7   | Describes whether the hull-mounted masker is on or off
    """
    OTHER = 0


# [UID 335]
class PropulsionPlantConfiguration(enum.IntEnum):
    """12.6.2 Configuration [UID 335]
    Name          | Bits | Description                                    | Reference
    Configuration | 0-6  | Describes the configuration of the power plant | [UID 335]
    """
    OTHER = 0
    DIESEL_ELECTRIC = 1
    DIESEL = 2
    BATTERY = 3
    TURBINE_REDUCTION = 4
    STEAM = 5
    GAS_TURBINE = 6


"""12.7 Additional Passive Activity (APA) Parameter Index"""

# [UID 150]
class APAParameter(enum.IntEnum):
    """12.7.1 APA Parameter [UID 150]"""
    OTHER = 0


# [UID 281]
class APAStatus(enum.IntEnum):
    """12.7.2 APA Status [UID 281]"""
    DESELECTED_OFF = 0
    APA_VALUE_CHANGE_ONLY = 1
    STATE_CHANGE = 2
    RECORD_ACTIVATION = 3
