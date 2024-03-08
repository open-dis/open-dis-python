"""sensortype.py

16 Sensor Types
"""
import enum


# [UID 193]
class SensorType(enum.IntEnum):
    """16.1 Sensor Type Category [UID 193]"""
    OTHER = 0
    OPTICAL = 1  # [UID 194]
    FLIR = 2  # [UID 195]
    RADAR = 3  # [UID 196]
    MAGNETIC = 4  # [UID 197]
    LASER = 5  # [UID 198]
    SONAR = 6  # [UID 199]
    PHYSICAL = 7  # [UID 200]
    MULTISPECTRAL = 8  # [UID 201]


# [UID 194]
class OpticalSensorType(enum.IntEnum):
    """16.1.1 Sensor Type Subcategories for Optical [UID 194]"""
    UNAIDED_EYE_ACTIVELY_SEARCHING = 0
    UNAIDED_EYE_NOT_ACTIVELY_SEARCHING = 1
    BINOCULARS = 2
    IMAGE_INTENSIFIER = 3
    HMMWV_OCCUPANT_ACTIVELY_SEARCHING = 4
    HMMWV_OCCUPANT_NOT_ACTIVELY_SEARCHING = 5
    TRUCK_OCCUPANT_ACTIVELY_SEARCHING = 6
    TRUCK_OCCUPANT_NOT_ACTIVELY_SEARCHING = 7
    TRACKED_VEHICLE_OCCUPANT_CLOSED_HATCH_ACTIVELY_SEARCHING = 8
    TRACKED_VEHICLE_OCCUPANT_CLOSED_HATCH_NOT_ACTIVELY_SEARCHING = 9
    TRACKED_VEHICLE_OCCUPANT_OPEN_HATCH_ACTIVELY_SEARCHING = 10
    TRACKED_VEHICLE_OCCUPANT_OPEN_HATCH_NOT_ACTIVELY_SEARCHING = 11


# [UID 195]
class FlirSensorType(enum.IntEnum):
    """16.1.2 Sensor Type Subcategories for FLIR [UID 195]"""
    GENERIC_3_5 = 0
    GENERIC_8_12 = 1
    ASTAMIDS_I = 2
    ASTAMIDS_II = 3
    GSTAMIDS_3_5 = 4
    GSTAMIDS_8_12 = 5
    HSTAMIDS_3_5 = 6
    HSTAMIDS_8_12 = 7
    COBRA_3_5 = 8
    COBRA_8_12 = 9


# [UID 196]
class RadarSensorType(enum.IntEnum):
    """16.1.3 Sensor Type Subcategories for RADAR [UID 196]"""
    GENERIC = 0
    GENERIC_GPR = 1
    GSTAMIDS_I = 2
    GSTAMIDS_II = 3
    HSTAMIDS_I = 4
    HSTAMIDS_II = 5


# [UID 197]
class MagneticSensorType(enum.IntEnum):
    """16.1.4 Sensor Type Subcategories for Magnetic [UID 197]"""
    GENERIC = 0
    AN_PSS_11 = 1
    AN_PSS_12 = 2
    GSTAMIDS = 3


# [UID 198]
class LaserSensorType(enum.IntEnum):
    """16.1.5 Sensor Type Subcategories for Laser [UID 198]"""
    GENERIC = 0
    ASTAMIDS = 1


# [UID 199]
class SonarSensorType(enum.IntEnum):
    """16.1.6 Sensor Type Subcategories for SONAR [UID 199]"""
    GENERIC = 0


# [UID 200]
class PhysicalSensorType(enum.IntEnum):
    """16.1.7 Sensor Type Subcategories for Physical [UID 200]"""
    GENERIC = 0
    PROBE_METAL_CONTENT = 1
    PROBE_NO_METAL_CONTENT = 2


# [UID 201]
class MultispectralSensorType(enum.IntEnum):
    """16.1.8 Sensor Type Subcategories for Multispectral [UID 201]"""
    GENERIC = 0


# [UID 414]
class SensorTypeSource(enum.IntEnum):
    """16.2 Sensor Type Source [UID 414]"""
    OTHER_ACTIVE_SENSORS = 0
    ELECTROMAGNETIC = 1
    PASSIVE_SENSORS = 2
    MINEFIELD_SENSORS = 3
    UNDERWATER_ACOUSTICS = 4
    LASERS = 5
