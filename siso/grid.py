"""grid.py

13 Gridded Data
"""
import enum


# [UID 243]
class FieldNumber(enum.IntEnum):
    """13.1 Field Number [UID 243]"""
    # There are currently no enumerations defined for [UID 243]


# [UID 244]
class CoordinateSystem(enum.IntEnum):
    """13.2 Coordinate System [UID 244]"""
    RIGHT_HANDED_CARTESIAN = 0  # (local topographic projection: east, north, up)
    LEFT_HANDED_CARTESIAN = 1  # (local topographic projection: east, north, down)
    LATITUDE_LONGITUDE_HEIGHT = 2
    LATITUDE_LONGITUDE_DEPTH = 3


# [UID 245]
class ConstantGrid(enum.IntEnum):
    """13.3 Constant Grid [UID 245]"""
    CONSTANT_GRID = 0
    UPDATED_GRID = 1


# [UID 246]
class SampleType(enum.IntEnum):
    """13.4 Sample Type [UID 246]"""
    NOT_SPECIFIED = 0


# [UID 247]
class DataRepresentation(enum.IntEnum):
    """13.5 Data Representation [UID 247]"""
    TYPE_0 = 0
    TYPE_1 = 1
    TYPE_2 = 2


# [UID 377]
class AxisType(enum.IntEnum):
    """13.6 Axis Type [UID 377]"""
    REGULAR_AXIS = 0
    IRREGULAR_AXIS = 1
