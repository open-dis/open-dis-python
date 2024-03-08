"""expendable.py

5.9 Expendable Kind
"""
import enum


"""5.9.3 Category"""

# [UID 25]
class AirCategory(enum.IntEnum):
    """5.9.4 Air Domain Categories [UID 25]"""
    OTHER = 0
    CHAFF = 1
    FLARE = 2
    COMBINED_CHAFF_AND_FLARE = 3
    ACTIVE_EMITTER = 4
    PASSIVE_DECOY = 5
    WINGED_DECOY = 6
    SIGNAL_ILLUMINATION_FLARE = 7
    SMOKE_GENERATOR = 8
    COMBINED_FLARE_AND_SMOKE_GENERATOR = 12
    SAR_NIGHT_LIGHT = 13
    SAR_BUOY = 14


# [UID 26]
class SurfaceCategory(enum.IntEnum):
    """5.9.5 Surface Domain Categories [UID 26]"""
    OTHER = 0
    FLARE = 2
    ACTIVE_EMITTER = 4
    PASSIVE_DECOY = 5
    SMOKE_GENERATOR = 8
    COMBINED_FLARE_AND_SMOKE_GENERATOR = 12
    SAR_BUOY = 14


# [UID 27]
class SubsurfaceCategory(enum.IntEnum):
    """5.9.6 Subsurface Domain Categories [UID 27]"""
    OTHER = 0
    ACTIVE_EMITTER = 4
    PASSIVE_DECOY = 5
    SIGNAL = 7
    NOISE_MAKER_DECOY = 9
    BUBBLE_MAKER_DECOY = 10
    MULTI_MODE_DECOY = 11
