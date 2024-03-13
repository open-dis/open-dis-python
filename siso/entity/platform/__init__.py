"""platform.py

5.2 Platform Kind
"""
import enum


"""5.2.3 Category"""

# [UID 9]
class Land(enum.IntEnum):
    """5.2.3.1 Land Domain Categories [UID 9]"""
    OTHER = 0
    TANK = 1
    ARMORED_FIGHTING_VEHICLE = 2
    ARMORED_UTILITY_VEHICLE = 3
    SELF_PROPELLED_ARTILLERY = 4
    TOWED_ARTILLERY = 5
    SMALL_WHEELED_UTILITY_VEHICLE = 6
    LARGE_WHEELED_UTILITY_VEHICLE = 7
    SMALL_TRACKED_UTILITY_VEHICLE = 8
    LARGE_TRACKED_UTILITY_VEHICLE = 9
    MORTAR = 10
    MINE_PLOW = 11
    MINE_RAKE = 12
    MINE_ROLLER = 13
    CARGO_TRAILER = 14
    FUEL_TRAILER = 15
    GENERATOR_TRAILER = 16
    WATER_TRAILER = 17
    ENGINEER_EQUIPMENT = 18
    HEAVY_EQUIPMENT_TRANSPORT_TRAILER = 19
    MAINTENANCE_EQUIPMENT_TRAILER = 20
    LIMBER = 21
    CHEMICAL_DECONTAMINATION_TRAILER = 22
    WARNING_SYSTEM = 23
    TRAIN_ENGINE = 24
    TRAIN_CAR = 25
    TRAIN_CABOOSE = 26
    CIVILIAN_VEHICLE_DEPRECATED = 27
    AIR_DEFENSE___MISSILE_DEFENSE_UNIT_EQUIPMENT = 28
    C3I_SYSTEM = 29
    OPERATIONS_FACILITY = 30
    INTELLIGENCE_FACILITY = 31
    SURVEILLANCE_FACILITY = 32
    COMMUNICATIONS_FACILITY = 33
    COMMAND_FACILITY = 34
    C4I_FACILITY = 35
    CONTROL_FACILITY = 36
    FIRE_CONTROL_FACILITY = 37
    MISSILE_DEFENSE_FACILITY = 38
    FIELD_COMMAND_POST = 39
    OBSERVATION_POST = 40
    MINE_FLAIL = 41
    UNMANNED = 50
    MOTORCYCLE = 80
    CAR = 81
    BUS = 82
    SINGLE_UNIT_CARGO_TRUCK = 83
    SINGLE_UNIT_UTILITY_EMERGENCY_TRUCK = 84
    MULTIPLE_UNIT_CARGO_TRUCK = 85
    MULTIPLE_UNIT_UTILITY_EMERGENCY_TRUCK = 86
    CONSTRUCTION_SPECIALTY_VEHICLE = 87
    FARM_SPECIALTY_VEHICLE = 88
    TRAILER = 89
    RECREATIONAL = 90
    NON_MOTORIZED = 91
    TRAINS = 92
    UTILITY_EMERGENCY_CAR = 93


# [UID 10]
class Air(enum.IntEnum):
    """5.2.3.2 Air Domain Categories [UID 10]"""
    OTHER = 0
    FIGHTER_AIR_DEFENSE = 1
    ATTACK_STRIKE = 2
    BOMBER = 3
    CARGO_TANKER = 4
    ASW_PATROL_OBSERVATION = 5
    EW = 6
    RECONNAISSANCE = 7
    SURVEILLANCE_C2_AIRBORNE_EARLY_WARNING = 8
    AIR_SEA_RESCUE = 9
    ATTACK_HELICOPTER = 20
    UTILITY_HELICOPTER = 21
    ANTI_SUBMARINE_WARFARE_PATROL_HELICOPTER = 22
    CARGO_HELICOPTER = 23
    OBSERVATION_HELICOPTER = 24


# [UID 11]
class Surface(enum.IntEnum):
    """5.2.3.3 Surface Domain Categories [UID 11]"""
    OTHER = 0
    CARRIER = 1
    COMMAND_SHIP = 2
    GUIDED_MISSILE_CRUISER = 3
    GUIDED_MISSILE_DESTROYER = 4
    DESTROYER = 5
    GUIDED_MISSILE_FRIGATE = 6
    LIGHT_PATROL_CRAFT = 7
    MINE_COUNTERMEASURE_SHIP = 8
    DOCK_LANDING_SHIP = 9
    TANK_LANDING_SHIP = 10
    LANDING_CRAFT = 11
    LIGHT_CARRIER = 12
    CRUISER_HELICOPTER_CARRIER = 13
    HYDROFOIL = 14
    AIR_CUSHION_SURFACE_EFFECT = 15
    AUXILIARY = 16
    AUXILIARY_MERCHANT_MARINE = 17
    UTILITY = 18
    UNMANNED_SURFACE_VEHICLE = 19
    LITTORAL_COMBAT_SHIPS = 20
    SURVEILLANCE_SHIP = 21
    FRIGATE_INCLUDING_CORVETTE = 50
    BATTLESHIP = 51
    HEAVY_CRUISER = 52
    DESTROYER_TENDER = 53
    AMPHIBIOUS_ASSAULT_SHIP = 54
    AMPHIBIOUS_CARGO_SHIP = 55
    AMPHIBIOUS_TRANSPORT_DOCK = 56
    AMMUNITION_SHIP = 57
    COMBAT_STORES_SHIP = 58
    SURVEILLANCE_TOWED_ARRAY_SONAR_SYSTEM = 59  # (SURTASS)
    FAST_COMBAT_SUPPORT_SHIP = 60
    NON_COMBATANT_SHIP_DEPRECATED = 61
    COAST_GUARD_CUTTERS = 62
    COAST_GUARD_BOATS = 63
    FAST_ATTACK_CRAFT = 64
    PASSENGER_VESSEL = 80  # (Group 1 Merchant) [UID 441]
    DRY_CARGO_SHIP = 81  # (Group 2 Merchant) [UID 442]]
    TANKER = 82  # (Group 3 Merchant) [UID 443]
    SUPPORT_VESSEL = 83  # [UID 444]
    PRIVATE_MOTORBOAT = 84  # [UID 445]
    PRIVATE_SAILBOAT = 85  # [UID 446]
    FISHING_VESSEL = 86  # [UID 447]
    OTHER_VESSELS = 87  # [UID 448]
    SEARCH_AND_RESCUE_VESSELS = 100
    LIFE_SAVING_EQUIPMENT = 101  # [UID 633]


# [UID 12]
class Subsurface(enum.IntEnum):
    """5.2.3.4 Subsurface Domain Categories [UID 12]"""
    OTHER = 0
    SSBN = 1  # (Nuclear Ballistic Missile)
    SSGN = 2  # (Nuclear Guided Missile)
    SSN = 3  # (Nuclear Attack - Torpedo)
    SSG = 4  # (Conventional Guided Missile)
    SS = 5  # (Conventional Attack - Torpedo, Patrol)
    SSAN = 6  # (Nuclear Auxiliary)
    SSA = 7  # (Conventional Auxiliary)
    UUV = 8  # (Unmanned Underwater Vehicle)
    SSB = 9  # (Submarine Ballistic, Ballistic Missile Submarine)
    SSC = 10  # (Coastal Submarine, over 150 tons)
    SSP = 11  # (Attack Submarine - Diesel Air-Independent Propulsion)
    SSM = 12  # (Midget Submarine, under 150 tons)
    SSNR = 13  # (Special Attack Submarine)
    SST = 14  # (Training Submarine)
    AGSS = 15  # (Auxiliary Submarine)
    SEMI_SUBMERSIBLE_BOATS = 16
    CIVILIAN_SUBMARINES = 80
    CIVILIAN_SUBMERSIBLES = 81
    CIVILIAN_SEMI_SUBMERSIBLE_BOATS = 82


# [UID 13]
class Space(enum.IntEnum):
    """5.2.3.5 Space Domain Categories [UID 13]"""
    OTHER = 0
    MANNED_SPACECRAFT = 1
    UNMANNED_DEPRECATED = 2
    BOOSTER = 3
    DEBRIS = 10
    SATELLITE_UNKNOWN_UNSPECIFIED_MISSION = 11
    SATELLITE_COMMUNICATION = 12
    SATELLITE_NAVIGATION = 13
    SATELLITE_SCIENCE_EXPERIMENTAL_DEMONSTRATION = 14
    SATELLITE_INERT = 15  # (Target/Reflector/Calibration)
    SATELLITE_EARTH_OBSERVATION = 16
    SATELLITE_SPACE_SURVEILLANCE = 17
    SATELLITE_ASTRONOMY = 18