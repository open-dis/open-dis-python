"""sensor.py

5.10 Sensor/Emitter Kind
"""
import enum


# [UID 28]
class SensorCategory(enum.IntEnum):
    """5.10.3 Category [UID 28]"""
    OTHER = 0
    MULTI_SPECTRAL = 1
    RF_ACTIVE = 2
    RF_PASSIVE = 3
    OPTICAL = 4
    ELECTRO_OPTICAL = 5
    SEISMIC = 6
    CHEMICAL_POINT_DETECTOR = 7
    CHEMICAL_STANDOFF = 8
    THERMAL = 9
    ACOUSTIC_ACTIVE = 10
    ACOUSTIC_PASSIVE = 11
    CONTACT_PRESSURE = 12
    ELECTRO_MAGNETIC_RADIATION = 13
    PARTICLE_RADIATION = 14
    MAGNETIC = 15
    GRAVITATIONAL = 16


"""5.10.4 Subcategory"""
# The Subcategory field for emitter systems for all domains is the Emitter
# System Function as defined in [UID 76].