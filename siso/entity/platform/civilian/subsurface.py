"""civilian.subsurface.py"""
import enum


"""5.2.7 Civilian Subsurface Subcategories"""

# [UID 506]
class Submarine(enum.IntEnum):
    """5.2.7.1 Submarine [UID 506]"""
    # There are currently no enumerations defined for [UID 506]


# [UID 507]
class Submersible(enum.IntEnum):
    """5.2.7.2 Submersible [UID 507]"""
    # There are currently no enumerations defined for [UID 507]


# [UID 508]
class SemiSubmersible(enum.IntEnum):
    """5.2.7.3 Semi-Submersibles [UID 508]"""
    NARCO_SUBMARINE = 1
