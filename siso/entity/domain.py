"""domain.py

5.11 Domain
"""
import enum


# [UID 14]
class MunitionKind(enum.IntEnum):
    """5.11.1 Munition Kind [UID 14]"""
    OTHER = 0
    ANTI_AIR = 1
    ANTI_ARMOR = 2
    ANTI_GUIDED_WEAPON = 3
    ANTI_RADAR = 4
    ANTI_SATELLITE = 5
    ANTI_SHIP = 6
    ANTI_SUBMARINE = 7
    ANTI_PERSONNEL = 8
    BATTLEFIELD_SUPPORT = 9
    STRATEGIC = 10
    TACTICAL = 11
    DIRECTED_ENERGY = 12


# [UID 8]
class OtherKind(enum.IntEnum):
    """5.11.2 Other Kinds [UID 8]"""
    # This enumeration is applicable to the Platform, Lifeform, Environmental,
    # Cultural Feature, Radio, Expendable, and Sensor/Emitter Kinds.
    OTHER = 0
    LAND = 1
    AIR = 2
    SURFACE = 3
    SUBSURFACE = 4
    SPACE = 5


# [UID 600]
class SupplyKind(enum.IntEnum):
    """5.11.3 Supply Kind [UID 600]"""
    NOT_USED_DEPRECATED = 0
    SUBSISTENCE = 1
    CLOTHING_INDIVEQUIPMENT_TOOLS_ADMIN_SUPPLIES = 2
    PETROLEUM_OILS_LUBRICANTS = 3
    CONSTRUCTION_MATERIALS = 4
    AMMUNITION_DEPRECATED = 5
    PERSONNEL_DEMAND_ITEMS = 6
    MAJOR_ITEMS = 7
    MEDICAL_MATERIAL = 8
    REPAIR_PARTS_COMPONENTS = 9
    MATERIAL_SUPPORT_NONMILITARY_PROGRAMS = 10
    SUPPLIES = 11
    SLING_LOADS = 12
