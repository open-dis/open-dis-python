"""supply.py

5.7 Supply Kind
"""
import enum


"""5.7.3 Category"""

# [UID 601]
class Subsistence(enum.IntEnum):
    """5.7.3.1 Class 1 Supply Category - Subsistence [UID 601]"""
    OTHER = 1
    NON_PERISHABLE = 2
    COMBAT_RATIONS = 3
    REFRIGERATED = 4
    OTHER_NON_REFRIGERATED = 5
    WATER = 6


# [UID 602]
class Clothing(enum.IntEnum):
    """5.7.3.2 Class 2 Supply Category - Clothing [UID 602]"""
    OTHER = 1
    AIR = 2
    GROUND_SUPPORT_MATERIEL = 3
    GENERAL_SUPPLIES = 4
    CLOTHING = 5
    ELECTRONICS = 6
    WEAPONS = 7
    INDUSTRIAL_SUPPLIES = 8


# [UID 603]
class POLProduct(enum.IntEnum):
    """5.7.3.3 Class 3 Supply Category - POL Products [UID 603]"""
    OTHER = 1
    POL_FOR_AIR_VEHICLES = 2
    POL_FOR_LAND_VEHICLES = 3
    PACKAGED_POL = 4


# [UID 604]
class ConstructionMaterial(enum.IntEnum):
    """5.7.3.4 Class 4 Supply Category - Construction Materials [UID 604]"""
    OTHER = 1
    CONSTRUCTION = 2
    BARRIER = 3


# [UID 605]
class Ammunition(enum.IntEnum):
    """5.7.3.5 Class 5 - Ammunition"""
    # Not used, see Munitions


# [UID 606]
class PersonnelDemandItems(enum.IntEnum):
    """5.7.3.6 Class 6 Supply Category - Personnel Demand Items [UID 606]"""
    OTHER = 1


# [UID 607]
class MajorItems(enum.IntEnum):
    """5.7.3.7 Class 7 Supply Category - Major Items [UID 607]"""
    OTHER = 1
    AIR = 2  # Not used, as described in Air Domain
    GROUND_SUPPORT_MATERIEL = 3
    ADMIN_VEHICLES = 4  # Not used, as described in Land Domain
    ELECTRONICS = 5
    RACKS_ADAPTORS_PYLONS = 6
    TACTICAL_VEHICLES = 7  # Not used, as described in Land Domain
    MISSILES = 8  # Not used, as described in Munition Domain
    WEAPONS = 9
    SPECIAL_WEAPONS = 10
    AIRCRAFT_ENGINES = 11
    DROP_TANK = 20
    CONFORMAL_FUEL_TANK = 21
    LUGGAGE_POD = 22
    ECM_POD = 23
    PARA_DROGUE = 24
    TARGETING_POD = 25
    FAIRING = 26
    AIR_REFUELLING_POD = 27
    HEAVY_AIRDROP = 28
    CONTAINER_DELIVERY_SYSTEM_AIRDROP = 29
    ROCKET_POD_LAUNCHER = 30
    TACTICAL_POD = 31


# [UID 608]
class MedicalMaterial(enum.IntEnum):
    """5.7.3.8 Class 8 Supply Category - Medical Material [UID 608]"""
    OTHER = 1
    MEDICAL_MATERIEL = 1
    BLOOD_FLUIDS = 2


# [UID 609]
class RepairPartsAndComponents(enum.IntEnum):
    """5.7.3.9 Class 9 Supply Category - Repair Parts and Components [UID 609]"""
    OTHER = 1
    AIR = 2
    GROUND_SUPPORT_MATERIEL = 3
    ADMIN_VEHICLES = 4
    ELECTRONICS = 5
    TACTICAL_VEHICLES = 6
    MISSILES = 7
    WEAPONS = 8
    SPECIAL_WEAPONS = 9
    AIRCRAFT_ENGINES = 10


# [UID 610]
class MaterialToSupportNonMilitaryPrograms(enum.IntEnum):
    """5.7.3.10 Class 10 Supply Category - Material to Support Non-Military Programs [UID 610]"""
    OTHER = 1


# [UID 611]
class NonDoctrinalSupplies(enum.IntEnum):
    """5.7.3.11 Class 11 Supply Category - Non Doctrinal Supplies [UID 611]"""
    OTHER = 1
    PALLETS = 2
    FUEL_TANKS_DRUMS_AND_BLADDERS = 3
    CHESTS = 4
    BOXES = 5


# [UID 612]
class SlingLoads(enum.IntEnum):
    """5.7.3.12 Class 12 Supply Category - Sling Loads (Not Doctrinal) [UID 612]"""
    OTHER = 1
    SLING_LOAD_BLIVET = 2
    SLING_LOAD_CRATE = 3
    SLING_LOAD_WATER_BUCKET = 4
    SLING_LOAD_VEHICLES = 5
    SLING_LOAD_HOWITZER = 6
    SLING_LOAD_COLLAPSIBLE = 7
    SLING_LOAD_BLADDER = 8
    SLING_LOAD_PALLET_OF_CRATES = 9
    SLING_LOAD_HELICOPTERS = 10
    SLING_LOAD_HOIST = 11
    SLING_LOAD_CONCRETE_BLOCK = 12
