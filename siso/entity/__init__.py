"""entity.py

5 Entity Type
"""
import enum


class EntityKind(enum.IntEnum):
    OTHER = 0
    PLATFORM = 1
    MUNITION = 2
    LIFE_FORM = 3
    ENVIRONMENTAL = 4
    CULTURAL_FEATURE = 5
    SUPPLY = 6
    RADIO = 7
    EXPENDABLE = 8
    SENSOR_EMITTER = 9


"""17 Entity/Object Attributes and Interactions"""

"""17.1 Dead Reckoning"""

# [UID 44]
class DeadReckoningAlgorithm(enum.IntEnum):
    """17.1.1 Dead Reckoning Algorithm [UID 44]
    Enumerated names for the Dead Reckoning Model (DRM) are formed by a
    combination of letter codes.
    Following is a description of the letter codes:
    F - Fixed orientation; angular velocity not used
    R - Rotating; orientation extrapolated using angular velocity
    P - Position extrapolated using linear velocity; acceleration not used
    V - Velocity and position extrapolated using velocity and acceleration
    W - Linear velocity and acceleration provided in world coordinates
    B - Linear velocity and acceleration provided in body coordinates; angular
        velocity required
    """
    OTHER = 0
    STATIC = 1   # Non-moving Entity
    DRM_FPW = 2  # Constant Velocity / Low Acceleration Linear Motion Entity
    DRM_RPW = 3  # Constant Velocity / Low Acceleration Linear Motion Entity
                 # with Extrapolation of Orientation
    DRM_RVW = 4  # High Speed or Maneuvering Entity with Extrapolation of
                 # Orientation
    DRM_FVW = 5  # High Speed or Maneuvering Entity
    DRM_FPB = 6  # Similar to FPW except in Body Coordinates
    DRM_RPB = 7  # Similar to RPW except in Body Coordinates
    DRM_RVB = 8  # Similar to RVW except in Body Coordinates
    DRM_FVB = 9  # Similar to FVW except in Body Coordinates


# [UID 296]
class DeadReckoningParametersType(enum.IntEnum):
    """17.1.2 Dead Reckoning Parameters Type [UID 296]"""
    NONE = 0
    LOCAL_EULER_ANGLES = 1  # Yaw, Pitch, Roll
    WORLD_ORIENTATION_QUATERNION = 2


# [UID 189]
class CollisionType(enum.IntEnum):
    """17.2 Collision Type [UID 189]"""
    INELASTIC = 0
    ELASTIC = 1
    BOOM_NOZZLE_HAS_CLEARED_THE_RECEIVERS_REFUELING_RECEPTACLE = 55


"""17.3 Entity Marking"""

# [UID 45]
"""17.3.1 Character Set [UID 45]
Value Description
0 Unused
1 ASCII
2 U.S. Army Marking
3 Digit Chevron"""
class CharacterSet(enum.IntEnum):
    """17.3.1 Character Set [UID 45]"""
    UNUSED = 0
    ASCII = 1
    U_S_ARMY_MARKING = 2
    DIGIT_CHEVRON = 3


"""17.4 Entity Capabilities"""
# Within the capabilities record, any individual bit set to one indicates that
# the entity has the corresponding capability.

# [UID 55]
class EntityCapabilities(enum.IntEnum):
    """17.4.1 Entity Capabilities [UID 55]"""
    LAND_PLATFORM_ENTITY_CAPABILITIES = 0  # [UID 450]
    AIR_PLATFORM_ENTITY_CAPABILITIES = 1  # [UID 451]
    SURFACE_PLATFORM_ENTITY_CAPABILITIES = 2  # [UID 452]
    SUBSURFACE_PLATFORM_ENTITY_CAPABILITIES = 3  # [UID 453]
    SPACE_PLATFORM_ENTITY_CAPABILITIES = 4  # [UID 454]
    MUNITION_ENTITY_CAPABILITIES = 5  # [UID 455]
    LIFE_FORMS_ENTITY_CAPABILITIES = 6  # [UID 456]
    ENVIRONMENTAL_ENTITY_CAPABILITIES = 7  # [UID 457]
    CULTURAL_FEATURE_ENTITY_CAPABILITIES = 8  # [UID 458]
    SUPPLY_ENTITY_CAPABILITIES = 9  # [UID 459]
    RADIO_ENTITY_CAPABILITIES = 10  # [UID 460]
    EXPENDABLE_ENTITY_CAPABILITIES = 11  # [UID 461]
    SENSOR_EMITTER_ENTITY_CAPABILITIES = 12  # [UID 462]


# [UID 450]
"""17.4.2 Land Platform Capabilities [UID 450]
Name | Bits | Description
Ammunition Supply | 0 | Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request
Fuel Supply | 1 | Describes whether the entity is able to supply some type of fuel in response to an appropriate service request
Recovery | 2 | Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request
Repair | 3 | Describes whether the entity is able to supply certain repair services in response to an appropriate service request
Reserved | 4 | This entry is reserved for backward compatibility and may not be reused
Sling Loadable | 6 | The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load
details (such as carrier).
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly.
Task Organizable | 8 | The Entity (normally a virtual manned module) can be task organized into an existing mixed mode unit (where mixed mode is intended to comprise a combination of computer-generated forces and virtual or even live forces)."""


# [UID 451]
"""17.4.3 Air Platform Capabilities [UID 451]
Name | Bits | Description | Reference
Ammunition Supply | 0 | Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request
Fuel Supply | 1 | Describes whether the entity is able to supply some type of fuel in response to an appropriate service request
Recovery | 2 | Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request
Repair | 3 | Describes whether the entity is able to supply certain repair services in response to an appropriate service request
ADS-B | 4 | Describes whether the entity is equipped with Automatic Dependent Surveillance - Broadcast (ADS-B)
Sling Load Carrier | 5 | The Entity is able to carry a payload in a sling load. The extended appearance record (if available) will identify the current sling load status and entity association and/or entity offset records (if available) will provide additional sling load details (such as payload).
Sling Loadable | 6 | The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly.
Task Organizable | 8 | The Entity (normally a virtual manned module) can be task organized into an existing mixed mode unit (where mixed mode is intended to comprise a combination of computer-generated forces and virtual or even live forces).
LAIRCM | 9 | Describes whether the entity is equipped with Large Aircraft Infrared Countermeasures (LAIRCM)"""


# [UID 452]
"""17.4.4 Surface Platform Capabilities [UID 452]
Name | Bits | Description | Reference
Ammunition Supply | 0 | Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request
Fuel Supply | 1 | Describes whether the entity is able to supply some type of fuel in response to an appropriate service request
Recovery | 2 | Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request
Repair | 3 | Describes whether the entity is able to supply certain repair services in response to an appropriate service request
Reserved | 4 | This entry is reserved for backward compatibility and may not
be reused
Sling Loadable | 6 | The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly.
Task Organizable | 8 | The Entity (normally a virtual manned module) can be task organized into an existing mixed mode unit (where mixed mode is intended to comprise a combination of computer-generated forces and virtual or even live forces)."""


# [UID 453]
"""17.4.5 Subsurface Platform Capabilities [UID 453]
Name | Bits | Description | Reference
Ammunition Supply | 0 | Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request
Fuel Supply | 1 | Describes whether the entity is able to supply some type of fuel in response to an appropriate service request
Recovery | 2 | Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request
Repair | 3 | Describes whether the entity is able to supply certain repair services in response to an appropriate service request
Reserved | 4 | This entry is reserved for backward compatibility and may not be reused
Sling Loadable | 6 | The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly.
Task Organizable | 8 | The Entity (normally a virtual manned module) can be task organized into an existing mixed mode unit (where mixed mode is intended to comprise a combination of computer-generated forces and virtual or even live forces)."""


# [UID 454]
"""17.4.6 Space Platform Capabilities [UID 454]
Name | Bits | Description | Reference
Ammunition Supply | 0 | Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request
Fuel Supply | 1 | Describes whether the entity is able to supply some type of fuel in response to an appropriate service request
Recovery | 2 | Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request
Repair | 3 | Describes whether the entity is able to supply certain repair services in response to an appropriate service request
Reserved | 4 | This entry is reserved for backward compatibility and may not be reused"""


# [UID 455]
"""17.4.7 Munition Capabilities [UID 455]
Name | Bits | Description | Reference
Reserved | 0-4 | This entry is reserved for backward compatibility and may not be reused
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly."""


# [UID 456]
"""17.4.8 Life Forms Capabilities [UID 456]
Name | Bits | Description | Reference
Ammunition Supply | 0 | Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request
Fuel Supply | 1 | Describes whether the entity is able to supply some type of fuel in response to an appropriate service request
Recovery | 2 | Describes whether the entity is able to provide recovery (e.g., towing) services in response to an appropriate service request
Repair | 3 | Describes whether the entity is able to supply certain repair services in response to an appropriate service request
Reserved | 4 | This entry is reserved for backward compatibility and may not be reused"""


# [UID 457]
"""17.4.9 Environmental Capabilities [UID 457]
Name | Bits | Description | Reference
Reserved | 0-4 | This entry is reserved for backward compatibility and may not be reused
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly."""


# [UID 458]
"""17.4.10 Cultural Feature Capabilities [UID 458]
Name | Bits | Description | Reference
Reserved | 0-4 | This entry is reserved for backward compatibility and may not be reused
Sling Loadable | 6 | The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly."""


# [UID 459]
"""17.4.11 Supply Capabilities [UID 459]
Name | Bits | Description | Reference
Ammunition Supply | 0 | Describes whether the entity is able to supply some type of ammunition in response to an appropriate service request
Fuel Supply | 1 | Describes whether the entity is able to supply some type of fuel in response to an appropriate service request
Reserved | 2-4 | This entry is reserved for backward compatibility and may not be reused
Sling Loadable | 6 | The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly."""


# [UID 460]
"""17.4.12 Radio Capabilities [UID 460]
Name | Bits | Description | Reference
Reserved | 0-4 | This entry is reserved for backward compatibility and may not be reused"""


# [UID 461]
"""17.4.13 Expendable Capabilities [UID 461]
Name | Bits | Description | Reference
Reserved | 0-4 | This entry is reserved for backward compatibility and may not be reused"""


# [UID 462]
"""17.4.14 Sensor/Emitter Capabilities [UID 462]
Name | Bits | Description | Reference
Reserved | 0-4 | This entry is reserved for backward compatibility and may not be reused
Sling Loadable | 6 | The Entity is able to be carried as a sling load payload. The extended appearance record (if available) will identify if it is currently sling loaded and entity association and/or entity offset records (if available) will provide additional sling load details (such as carrier).
IED Presence Indicator | 7 | The Entity is an IED or contains an IED. The extended appearance record (if available) will identify how well hidden the IED is on the Entity. An Attached Part (if applicable, for instance a jury-rigged munition does not apply here) will identify the IED explicitly.
Task Organizable | 8 | The Entity (normally a virtual manned module) can be task organized into an existing mixed mode unit (where mixed mode is intended to comprise a combination of computer-generated forces and virtual or even live forces)."""


"""17.5 Attached Parts"""

# [UID 57]
"""17.5.1 Attached Part [UID 57]
These are the enumeration values for attached parts stations.
Value Description
0 Nothing, Empty
1-511 Sequential IDs for model-specific stations
512-639 Fuselage Stations
640-767 Left-wing Stations
768-895 Right-wing Stations
896 M16A42 rifle
897 M249 SAW
898 M60 Machine gun
899 M203 Grenade Launcher
900 M136 AT4
901 M47 Dragon
902 AAWS-M Javelin
903 M18A1 Claymore Mine
904 MK19 Grenade Launcher
905 M2 Machine Gun
906-1023 Other attached parts"""


# [UID 415]
class DetachedIndicator(enum.IntEnum):
    """17.5.2 Detached Indicator [UID 415]"""
    ATTACHED = 0
    DETACHED = 1


"""17.6 Articulated Parts"""

# [UID 58]
class ArticulatedPartTypeMetric(enum.IntEnum):
    """17.6.1 Articulated Part Type Metric [UID 58]"""
    # These are the enumeration values for articulated parts type metrics.
    # These determine the transformation for the articulating part and are
    # added to the type class to obtain the final enumeration value for the
    # part.
    NOT_SPECIFIED = 0
    POSITION = 1
    POSITION_RATE = 2
    EXTENSION = 3
    EXTENSION_RATE = 4
    X = 5
    X_RATE = 6
    Y = 7
    Y_RATE = 8
    Z = 9
    Z_RATE = 10
    AZIMUTH = 11
    AZIMUTH_RATE = 12
    ELEVATION = 13
    ELEVATION_RATE = 14
    ROTATION = 15
    ROTATION_RATE = 16


# [UID 59]
class ArticulatedPartTypeClass(enum.IntEnum):
    """17.6.2 Articulated Part Type Class [UID 59]"""
    # These are the enumeration values for articulated parts type classes. These
    # determine the articulating part and are added to the type metric to obtain
    # the final enumeration value for the part.
    NOT_SPECIFIED = 0
    RUDDER = 1024
    LEFT_FLAP = 1056
    RIGHT_FLAP = 1088
    LEFT_AILERON = 1120
    RIGHT_AILERON = 1152
    HELICOPTER_MAIN_ROTOR = 1184
    HELICOPTER_TAIL_ROTOR = 1216
    OTHER_AIRCRAFT_CONTROL_SURFACES_DEFINED_AS_NEEDED = 1248
    PROPELLER_NUMBER_1 = 1280
    PROPELLER_NUMBER_2 = 1312
    PROPELLER_NUMBER_3 = 1344
    PROPELLER_NUMBER_4 = 1376
    LEFT_STABILATOR_STABILATOR_NUMBER_1 = 1408
    RIGHT_STABILATOR_STABILATOR_NUMBER_2 = 1440
    LEFT_RUDDERVATOR_RUDDERVATOR_NUMBER_1 = 1472
    RIGHT_RUDDERVATOR_RUDDERVATOR_NUMBER_2 = 1504
    LEFT_LEADING_EDGE_FLAP_SLAT = 1536
    RIGHT_LEADING_EDGE_FLAP_SLAT = 1568
    LEFT_ELEVATOR = 1600
    RIGHT_ELEVATOR = 1632
    CANARD_LEFT = 1664
    CANARD_RIGHT = 1696
    ELEVON_LEFT = 1728
    ELEVON_RIGHT = 1760
    ELEVON_MIDDLE_LEFT = 1792
    ELEVON_MIDDLE_RIGHT = 1824
    ELEVON_OUTER_LEFT = 1856
    ELEVON_OUTER_RIGHT = 1888
    CANOPY_AIRCRAFT = 1920
    SPOILER_LEFT = 1952
    SPOILER_RIGHT = 1984
    PERISCOPE = 2048
    GENERIC_ANTENNA = 2080
    SNORKEL = 2112
    OTHER_EXTENDIBLE_PARTS_DEFINED_AS_NEEDED = 2144
    DIVE_PLANE_SAIL_LEFT = 2176
    DIVE_PLANE_SAIL_RIGHT = 2208
    DIVE_PLANE_BOW_LEFT = 2240
    DIVE_PLANE_BOW_RIGHT = 2272
    DIVE_PLANE_STERN_LEFT = 2304
    DIVE_PLANE_STERN_RIGHT = 2336
    LANDING_GEAR = 3072
    TAIL_HOOK = 3104
    SPEED_BRAKE = 3136
    LEFT_DOOR_OF_PRIMARY_WEAPON_BAY = 3168
    RIGHT_DOOR_OF_PRIMARY_WEAPON_BAY = 3200
    TANK_OR_APC_HATCH = 3232
    WINGSWEEP = 3264
    BRIDGE_LAUNCHER = 3296
    BRIDGE_SECTION_1 = 3328
    BRIDGE_SECTION_2 = 3360
    BRIDGE_SECTION_3 = 3392
    PRIMARY_BLADE_1 = 3424
    PRIMARY_BLADE_2 = 3456
    PRIMARY_BOOM = 3488
    PRIMARY_LAUNCHER_ARM = 3520
    OTHER_FIXED_POSITION_PARTS_DEFINED_AS_NEEDED = 3552
    LANDING_GEAR_NOSE = 3584
    LANDING_GEAR_LEFT_MAIN = 3616
    LANDING_GEAR_RIGHT_MAIN = 3648
    DOORS_OF_LEFT_SIDE_WEAPON_BAY = 3680
    DOORS_OF_RIGHT_SIDE_WEAPON_BAY = 3712
    SPOT_SEARCH_LIGHT_1 = 3744
    SPOT_SEARCH_LIGHT_2 = 3776
    SPOT_SEARCH_LIGHT_3 = 3808
    SPOT_SEARCH_LIGHT_4 = 3840
    LANDING_LIGHT = 3872
    PRIMARY_TURRET_NUMBER_1 = 4096
    PRIMARY_TURRET_NUMBER_2 = 4128
    PRIMARY_TURRET_NUMBER_3 = 4160
    PRIMARY_TURRET_NUMBER_4 = 4192
    PRIMARY_TURRET_NUMBER_5 = 4224
    PRIMARY_TURRET_NUMBER_6 = 4256
    PRIMARY_TURRET_NUMBER_7 = 4288
    PRIMARY_TURRET_NUMBER_8 = 4320
    PRIMARY_TURRET_NUMBER_9 = 4352
    PRIMARY_TURRET_NUMBER_10 = 4384
    PRIMARY_GUN_NUMBER_1 = 4416
    PRIMARY_GUN_NUMBER_2 = 4448
    PRIMARY_GUN_NUMBER_3 = 4480
    PRIMARY_GUN_NUMBER_4 = 4512
    PRIMARY_GUN_NUMBER_5 = 4544
    PRIMARY_GUN_NUMBER_6 = 4576
    PRIMARY_GUN_NUMBER_7 = 4608
    PRIMARY_GUN_NUMBER_8 = 4640
    PRIMARY_GUN_NUMBER_9 = 4672
    PRIMARY_GUN_NUMBER_10 = 4704
    PRIMARY_LAUNCHER_1 = 4736
    PRIMARY_LAUNCHER_2 = 4768
    PRIMARY_LAUNCHER_3 = 4800
    PRIMARY_LAUNCHER_4 = 4832
    PRIMARY_LAUNCHER_5 = 4864
    PRIMARY_LAUNCHER_6 = 4896
    PRIMARY_LAUNCHER_7 = 4928
    PRIMARY_LAUNCHER_8 = 4960
    PRIMARY_LAUNCHER_9 = 4992
    PRIMARY_LAUNCHER_10 = 5024
    PRIMARY_DEFENSE_SYSTEMS_1 = 5056
    PRIMARY_DEFENSE_SYSTEMS_2 = 5088
    PRIMARY_DEFENSE_SYSTEMS_3 = 5120
    PRIMARY_DEFENSE_SYSTEMS_4 = 5152
    PRIMARY_DEFENSE_SYSTEMS_5 = 5184
    PRIMARY_DEFENSE_SYSTEMS_6 = 5216
    PRIMARY_DEFENSE_SYSTEMS_7 = 5248
    PRIMARY_DEFENSE_SYSTEMS_8 = 5280
    PRIMARY_DEFENSE_SYSTEMS_9 = 5312
    PRIMARY_DEFENSE_SYSTEMS_10 = 5344
    PRIMARY_RADAR_1 = 5376
    PRIMARY_RADAR_2 = 5408
    PRIMARY_RADAR_3 = 5440
    PRIMARY_RADAR_4 = 5472
    PRIMARY_RADAR_5 = 5504
    PRIMARY_RADAR_6 = 5536
    PRIMARY_RADAR_7 = 5568
    PRIMARY_RADAR_8 = 5600
    PRIMARY_RADAR_9 = 5632
    PRIMARY_RADAR_10 = 5664
    SECONDARY_TURRET_NUMBER_1 = 5696
    SECONDARY_TURRET_NUMBER_2 = 5728
    SECONDARY_TURRET_NUMBER_3 = 5760
    SECONDARY_TURRET_NUMBER_4 = 5792
    SECONDARY_TURRET_NUMBER_5 = 5824
    SECONDARY_TURRET_NUMBER_6 = 5856
    SECONDARY_TURRET_NUMBER_7 = 5888
    SECONDARY_TURRET_NUMBER_8 = 5920
    SECONDARY_TURRET_NUMBER_9 = 5952
    SECONDARY_TURRET_NUMBER_10 = 5984
    SECONDARY_GUN_NUMBER_1 = 6016
    SECONDARY_GUN_NUMBER_2 = 6048
    SECONDARY_GUN_NUMBER_3 = 6080
    SECONDARY_GUN_NUMBER_4 = 6112
    SECONDARY_GUN_NUMBER_5 = 6144
    SECONDARY_GUN_NUMBER_6 = 6176
    SECONDARY_GUN_NUMBER_7 = 6208
    SECONDARY_GUN_NUMBER_8 = 6240
    SECONDARY_GUN_NUMBER_9 = 6272
    SECONDARY_GUN_NUMBER_10 = 6304
    SECONDARY_LAUNCHER_1 = 6336
    SECONDARY_LAUNCHER_2 = 6368
    SECONDARY_LAUNCHER_3 = 6400
    SECONDARY_LAUNCHER_4 = 6432
    SECONDARY_LAUNCHER_5 = 6464
    SECONDARY_LAUNCHER_6 = 6496
    SECONDARY_LAUNCHER_7 = 6528
    SECONDARY_LAUNCHER_8 = 6560
    SECONDARY_LAUNCHER_9 = 6592
    SECONDARY_LAUNCHER_10 = 6624
    SECONDARY_DEFENSE_SYSTEMS_1 = 6656
    SECONDARY_DEFENSE_SYSTEMS_2 = 6688
    SECONDARY_DEFENSE_SYSTEMS_3 = 6720
    SECONDARY_DEFENSE_SYSTEMS_4 = 6752
    SECONDARY_DEFENSE_SYSTEMS_5 = 6784
    SECONDARY_DEFENSE_SYSTEMS_6 = 6816
    SECONDARY_DEFENSE_SYSTEMS_7 = 6848
    SECONDARY_DEFENSE_SYSTEMS_8 = 6880
    SECONDARY_DEFENSE_SYSTEMS_9 = 6912
    SECONDARY_DEFENSE_SYSTEMS_10 = 6944
    SECONDARY_RADAR_1 = 6976
    SECONDARY_RADAR_2 = 7008
    SECONDARY_RADAR_3 = 7040
    SECONDARY_RADAR_4 = 7072
    SECONDARY_RADAR_5 = 7104
    SECONDARY_RADAR_6 = 7136
    SECONDARY_RADAR_7 = 7168
    SECONDARY_RADAR_8 = 7200
    SECONDARY_RADAR_9 = 7232
    SECONDARY_RADAR_10 = 7264
    DECK_ELEVATOR_1 = 7296
    DECK_ELEVATOR_2 = 7328
    CATAPULT_1 = 7360
    CATAPULT_2 = 7392
    JET_BLAST_DEFLECTOR_1 = 7424
    JET_BLAST_DEFLECTOR_2 = 7456
    ARRESTOR_WIRES_1 = 7488
    ARRESTOR_WIRES_2 = 7520
    ARRESTOR_WIRES_3 = 7552
    WING_OR_ROTOR_FOLD = 7584
    FUSELAGE_FOLD = 7616
    MAIN_CARGO_DOOR = 7648
    CARGO_RAMP = 7680
    AIR_TO_AIR_REFUELING_BOOM = 7712
    PRIMARY_AIR_TO_AIR_REFUELING_RECEPTACLE_DOOR = 7744
    SECONDARY_AIR_TO_AIR_REFUELING_RECEPTACLE_DOOR = 7776
    AIR_TO_AIR_REFUELING_RECEPTACLE_LATCH = 7808
    CARGO_DOOR_1 = 7840
    CARGO_DOOR_2 = 7872
    CARGO_DOOR_3 = 7904
    CARGO_DOOR_4 = 7936
    CARGO_DOOR_5 = 7968
    CARGO_DOOR_6 = 8000
    CARGO_DOOR_7 = 8032
    CARGO_DOOR_8 = 8064
    CARGO_DOOR_9 = 8096
    CARGO_DOOR_10 = 8128
    CENTRE_REFUELLING_DROGUE = 8160
    PORT_REFUELLING_DROGUE = 8192
    STARBOARD_REFUELLING_DROGUE = 8224
    SUBMARINE_ENGINE_EXHAUST_MAST = 8256
    SUBMARINE_MAST_1 = 8288
    SUBMARINE_MAST_2 = 8320
    SUBMARINE_MAST_3 = 8352
    SUBMARINE_MAST_4 = 8384
    SUBMARINE_MAST_5 = 8416
    SUBMARINE_MAST_6 = 8448
    SUBMARINE_MAST_7 = 8480
    SUBMARINE_MAST_8 = 8512
    SUBMARINE_MAST_9 = 8544
    SUBMARINE_MAST_10 = 8576
    VECTORED_THRUST_NOZZLE = 8608
    LEFT_DOOR_OF_LEFT_WEAPON_BAY = 8640
    RIGHT_DOOR_OF_LEFT_WEAPON_BAY = 8672
    LEFT_DOOR_OF_RIGHT_WEAPON_BAY = 8704
    RIGHT_DOOR_OF_RIGHT_WEAPON_BAY = 8736
    GUN_DOOR = 8768
    COUNTERMEASURE_DOOR_LEFT = 8800
    COUNTERMEASURE_DOOR_RIGHT = 8832
    HOOK_DOOR_FORWARD = 8864
    HOOK_DOOR_AFT = 8896
    LIFT_FAN_UPPER_DOOR = 8928
    LIFT_FAN_LOWER_DOOR_LEFT = 8960
    LIFT_FAN_LOWER_DOOR_RIGHT = 8992
    REFUELING_PROBE_DOOR = 9024
    LEFT_ENGINE_NACELLE = 9056
    RIGHT_ENGINE_NACELLE = 9088
    FIRST_LEFT_WHEEL = 9120
    FIRST_RIGHT_WHEEL = 9152
    SECOND_LEFT_WHEEL = 9184
    SECOND_RIGHT_WHEEL = 9216
    THIRD_LEFT_WHEEL = 9248
    THIRD_RIGHT_WHEEL = 9280
    FOURTH_LEFT_WHEEL = 9312
    FOURTH_RIGHT_WHEEL = 9344
    FIFTH_LEFT_WHEEL = 9376
    FIFTH_RIGHT_WHEEL = 9408
    SIXTH_LEFT_WHEEL = 9440
    SIXTH_RIGHT_WHEEL = 9472
    SEVENTH_LEFT_WHEEL = 9504
    SEVENTH_RIGHT_WHEEL = 9536
    EIGHTH_LEFT_WHEEL = 9568
    EIGHTH_RIGHT_WHEEL = 9600
    NINTH_LEFT_WHEEL = 9632
    NINTH_RIGHT_WHEEL = 9664
    TENTH_LEFT_WHEEL = 9696
    TENTH_RIGHT_WHEEL = 9728
    REFUELING_PROBE = 9760
    STEERING_WHEEL = 9792
    CRANE_BODY = 9824
    CRANE_ARM_1 = 9856
    CRANE_ARM_2 = 9888
    CRANE_ARM_3 = 9920
    CRANE_BOOM = 9952
    CRANE_HOOK = 9984


"""17.7 Object Modification"""

# [UID 240]
"""17.7.1 Point Object State Modification [UID 240]
Name | Bits | Description | Reference
Is Location Modified | 0 | Describes whether the point object location has been modified since the last update number
Is Orientation Modified | 1 | Describes whether the point object orientation has been modified since the last update number"""


# [UID 241]
"""17.7.2 Linear Object State Modification [UID 241]
Name | Bits | Description | Reference
Is Location Modified | 0 | Describes whether the location of the linear segment has been modified since the last update number
Is Orientation Modified | 1 | Describes whether the orientation of the linear segment has been modified since the last update number"""


# [UID 242]
"""17.7.3 Areal Object State Modification [UID 242]
Name | Bits | Description | Reference
Is Location Modified | 0 | Describes whether the location of the areal object has been modified since the last update number"""


"""17.8 Entity Association"""

# [UID 319]
class AssociationStatus(enum.IntEnum):
    """17.8.1 Association Status [UID 319]"""
    NOT_SPECIFIED = 0
    PHYSICAL_ASSOCIATION_GENERAL_OBJECT_1 = 1
    FUNCTIONAL_ASSOCIATION_GENERAL = 2
    ASSOCIATION_BROKEN = 3
    PHYSICAL_ASSOCIATION_OBJECT_2 = 4
    FUNCTIONAL_ASSOCIATION_OBJECT_1 = 5
    FUNCTIONAL_ASSOCIATION_OBJECT_2 = 6


# [UID 321]
class GroupMemberType(enum.IntEnum):
    """17.8.2 Group Member Type [UID 321]"""
    NOT_PART_OF_A_GROUP = 0
    GROUP_LEADER = 1
    GROUP_MEMBER = 2
    FORMATION_LEADER = 3
    FORMATION_MEMBER = 4
    CONVOY_LEADER = 5
    CONVOY_MEMBER = 6


# [UID 322]
class PhysicalAssociationTypeGroups(enum.IntEnum):
    """17.8.3 Physical Association Type Groups [UID 322]"""
    NOT_SPECIFIED = 0
    TOWED_MOUNT_SLING_LOAD = 1
    RESTRAINED = 2
    MISSION = 3
    OTHER_CONNECTIONS = 4


# [UID 323]
class PhysicalAssociationType(enum.IntEnum):
    """17.8.4 Physical Association Type [UID 323]"""
    NOT_SPECIFIED = 0
    TOWED_IN_AIR_SINGLE_HOOK_NOT_SPECIFIED = 1
    TOWED_ON_LAND = 2
    TOWED_ON_WATER_SURFACE = 3
    TOWED_UNDERWATER = 4
    MOUNTED_ATTACHED = 5
    MOUNTED_UNATTACHED_AND_UNSUPPORTED = 6
    MOUNTED_UNATTACHED_AND_SUPPORTED = 7
    TOWED_IN_AIR_CENTER_HOOK = 8
    TOWED_IN_AIR_FORWARD_HOOK = 9
    TOWED_IN_AIR_AFT_HOOK = 10
    TOWED_IN_AIR_TANDEM_HOOK_FORE_AND_AFT = 11
    TOWED_IN_AIR_MISMANAGED_TANDEM_FORE_AND_CENTER = 12
    TOWED_IN_AIR_MISMANAGED_TANDEM_CENTER_AND_AFT = 13
    TOWED_IN_AIR_ALL_HOOKS = 14
    HOISTED = 15
    RESTRAINED_TO_A_LIFEFORM = 30
    RESTRAINED_TO_A_PLATFORM = 31
    RESTRAINED_TO_AN_OBJECT = 32
    REFUELING_OPERATION = 61
    SEARCH_AND_RESCUE_BASKET = 62
    SEARCH_AND_RESCUE_RESCUE_COLLAR = 63
    ENGAGEMENT_OBJECT_2_IS_BEING_ENGAGED = 64
    RETURN_TO_BASE_OBJECT_2_IS_THE_DESTINATION_OBJECT = 65
    LINE_BETWEEN_COMMUNICATION_TOWERS = 90
    LINE_BETWEEN_POWER_TOWERS = 91
    INDOORS = 92
    TOP_SURFACE = 93


# [UID 324]
class PhysicalConnectionType(enum.IntEnum):
    """17.8.5 Physical Connection Type [UID 324]"""
    NOT_SPECIFIED = 0
    ATTACHED_DIRECTLY_TO_SURFACE = 1
    CABLE_WIRE = 2
    ROPE = 3
    CHAIN = 4
    POWER_LINE = 5
    TELEPHONE_LINE = 6
    CABLE_LINE = 7
    REFUELING_DOGUE = 8
    REFUELING_BOOM = 9
    HANDCUFFS = 10
    IN_CONTACT_WITH = 11
    FAST_ROPE = 12


"""17.9 Separation"""

# [UID 282]
class ReasonForSeparation(enum.IntEnum):
    """17.9.1 Reason For Separation [UID 282]"""
    NO_STATEMENT = 0
    ATTACHED_PART_SEPARATION = 1
    SUBMUNITION_SEPARATION = 2


# [UID 283]
class PreEntityIndicator(enum.IntEnum):
    """17.9.2 Pre-Entity Indicator [UID 283]"""
    NO_STATEMENT = 0
    ENTITY_ID_EXISTED_PRIOR_TO_SEPARATION_WITHOUT_ENTITY_STATE_PDU = 1
    ENTITY_ID_EXISTED_PRIOR_TO_SEPARATION_WITH_ENTITY_STATE_PDU_ISSUED = 2
    ENTITY_INITIALLY_CREATED_AT_SEPARATION_EVENT = 3


# [UID 320]
"""17.10 Entity Type Change Indicator [UID 320]
Value Description
0 Initial Report or No Change Since Last Issuance
1 Change Since Last Issuance"""
class EntityTypeChangeIndicator(enum.IntEnum):
    """17.10 Entity Type Change Indicator [UID 320]"""
    INITIAL_REPORT_OR_NO_CHANGE_SINCE_LAST_ISSUANCE = 0
    CHANGE_SINCE_LAST_ISSUANCE = 1


"""17.11 Appearance"""

"""17.11.1 Entity Appearance"""
# This section specifies the Appearance records. These records are specific to Kind (see [UID 7]) and with respect to the Platform Kind, they are specific to Domain (see [UID 8]).

"""17.11.1.1 Platform Appearance"""

# [UID 31]
"""17.11.1.1.1 Platforms of the Land Domain [UID 31]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Mobility Killed | 1 | Describes whether it is capable of moving on its own power
Fire Power Killed | 2 | Describes whether it can fire weapons
Damage 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke Emanating | 5 | Describes whether or not smoke is emanating from the entity
Is Engine Emitting Smoke | 6 | Describes whether or not the engine is emitting smoke
Trailing Dust Cloud | 7-8 | Describes the size of the dust cloud trailing effect | [UID 381]
Primary Hatch | 9-11 | Describes whether the primary hatch is open or closed and whether someone is visible | [UID 382]
Head Lights On | 12 | Describes whether head lights are on or off
Tail Lights On | 13 | Describes whether tail lights are on or off
Brake Lights On | 14 | Describes whether brake lights are on or off
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Launcher/Operational | 16 | Describes the status of the mechanism required for the platform to be operational, such as the elevated status of the primary launcher | [UID 383]
Camouflage Type | 17-18 | Describes the camouflage color | [UID 384]
Concealed Position | 19 | Describes the type of concealment | [UID 385]
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Tent Extended | 24 | Describes whether or not the tent is extended
Ramp Extended | 25 | Describes whether or not the ramp is extended
Blackout Lights On | 26 | Describes whether blackout lights are on or off
Blackout Brake Lights On | 27 | Describes whether blackout brake lights are on or off
Spot/Search Light #1 On | 28 | Describes whether spot/search light #1 is on or off | If a record containing additional detail is not present, then this field pertains to all spot/search lights
Interior Lights (Forward) On | 29 | Describes whether interior lights (forward) are on or off | If a record containing additional detail is not present, then this field pertains to all interior lights
Occupants Surrendered | 30 | Describes whether or not the vehicle occupants have surrendered
Masked / Cloaked | 31 | Describes whether or not the entity is masked or cloaked"""


# [UID 32]
"""17.11.1.1.2 Platforms of the Air Domain [UID 32]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Propulsion Killed | 1 | Describes whether it is capable of moving on its own power
NVG Mode | 2 | Describes whether air platform lighting is in covert or overt mode | [UID 400]
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke Emanating | 5 | Describes whether or not smoke is emanating from the entity
Is Engine Emitting Smoke | 6 | Describes whether or not the engine is emitting smoke
Trailing Effects | 7-8 | Describes the size of the contrails or ionization trailing effects | [UID 381]
Canopy/Troop Door | 9-11 | Describes the state of the canopy/troop door | [UID 387]
Landing Lights On | 12 | Describes whether landing lights are on or off
Navigation Lights On | 13 | Describes whether navigation lights are on or off
Anti-Collision Lights On | 14 | Describes whether Anti-Collision lights are on or off
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Afterburner On | 16 | Describes if the air platform is in afterburner
Lower Anti-Collision Light On | 17 | Describes whether the lower Anti-Collision light is on or off
Upper Anti-Collision Light On | 18 | Describes whether the upper Anti-Collision light is on or off
Anti-Collision Light Day/Night | 19 | Describes the day/night status of the Anti-Collision lights | [UID 397], This field is set to Day (0) if both the upper and lower Anti-Collision lights are Off (0)
Is Blinking | 20 | Indicates whether any air platform lights are blinking or not
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Formation Lights On | 24 | Describes whether formation lights are on or off
Landing Gear Extended | 25 | Describes whether the landing gear is wholly retracted or
extended
Cargo Doors Opened | 26 | Describes whether the cargo doors (main door) are closed or
open
Navigation/Position Brightness | 27 | Describes the brightness of the navigation/position lights | [UID 398]
Spot/Search Light #1 On | 28 | Describes whether spot/search light #1 is on or off | If a record containing additional detail is not present, then this field pertains to all spot/search lights
Interior Lights On | 29 | Describes whether interior lights are on or off
Reverse Thrust Engaged | 30 | Describes whether the air platform has engaged reverse thrust
Weight-on-Wheels | 31 | Describes whether the air platform has weight on its main landing gear"""


# [UID 33]
"""17.11.1.1.3 Platforms of the Surface Domain [UID 33]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Mobility Killed | 1 | Describes whether it is capable of moving on its own power
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke Emanating | 5 | Describes whether or not smoke is emanating from the entity
Is Engine Emitting Smoke | 6 | Describes whether or not the engine is emitting smoke
Wake Size | 7-8 | Describes the size of the wake trailing effect | [UID 381]
Running Lights On | 12 | Describes whether running lights are on or off
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Is Accomodation Ladder Lowered | 16 | Describes if the accomodation ladder is lowered or not
Is Fence Raised | 17 | Describes whether the safety fence around a helicopter landing deck is raised
Is Flag Raised | 18 | Describes whether the national identification flag is raised
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Spot Lights On | 28 | Describes whether spot lights are on or off
Interior Lights On | 29 | Describes whether interior lights are on or off"""


# [UID 34]
"""17.11.1.1.4 Platforms of the Subsurface Domain [UID 34]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Mobility Killed | 1 | Describes whether it is capable of moving on its own power
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke Emanating | 5 | Describes whether or not smoke is emanating from the entity
Is Engine Emitting Smoke | 6 | Describes whether or not the engine is emitting smoke
Hatch | 9-11 | Describes whether the hatch is open or closed [UID 388]
Running Lights On | 12 | Describes whether running lights are on or off
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]"""


# [UID 35]
"""17.11.1.1.5 Platforms of the Space Domain [UID 35]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Mobility Killed | 1 | Describes whether it is capable of moving on its own power
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke/Vapor Emanating | 5 | Describes whether or not smoke or vapor is emanating from the entity
Is Engine Emitting Smoke | 6 | Describes whether or not the engine is emitting smoke
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]"""


# [UID 36]
"""17.11.1.2 Munition Appearance [UID 36]
Name | Bits | Description | Reference
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke/Vapor Emanating | 5 | Describes whether or not smoke or vapor is emanating from the entity
Is Engine Emitting Smoke | 6 | Describes whether or not the engine is emitting smoke
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Launch Flash Present | 16 | Describes whether or not the guided munition's launch flash is present
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Cover/Shroud Status | 24-25 | Describes the status of the cover or shroud | [UID 426]
Masked / Cloaked | 31 | Describes whether or not the entity is masked or cloaked"""


"""17.11.1.3 Life Form Appearance"""

"""17.11.1.3.1 Human Life Form Appearance [UID 37]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Health | 3-4 | Describes the visual appearance of the severity of any injury | [UID 390]
Compliance Status | 5-8 | Describes the manner and degree to which the life form is complying | [UID 391]
Clothing IR Signature | 9-10 | Describes the general nature of the IR Signature due to clothing or covering | [UID 802]
Signal Smoke in Use | 11 | Describes whether signal smoke is being used or not
Flash Lights On | 12 | Describes whether flash lights are on or off
Signal Mirror in Use | 13 | Describes whether a signal mirror is being used or not
IR Strobe On | 14 | Describes whether an IR strobe is on or off
IR Illuminator On | 15 | Describes whether an IR illuminator (flare) is on or off
Life Form Posture | 16-19 | Describes the posture (position) of the life form | [UID 392]
Is Smoking Cigarette | 20 | Describes whether the life form has a lit cigarette or not. The primary purpose is for IR signature generation, so it could be a cigar or other item.
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Mounted/Hoisted Status | 22 | Describes whether or not the life form is mounted/hoisted on another platform, such as a troop transport or helicopter hoist
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Weapon/Implement 1 | 24-25 | Describes the position of the life form's primary weapon/implement | [UID 393]
Weapon/Implement 2 | 26-27 | Describes the position of the life form's secondary weapon/implement | [UID 393]
Camouflage Type | 28-29 | Describes the camouflage color | [UID 384]
Concealed Stationary | 30 | Describes whether or not the life form is in a prepared concealed position | [UID 385]
Concealed Movement | 31 | Describes whether or not the life form uses concealment during movement | [UID 394]"""


# [UID 480]
"""17.11.1.3.2 Non-Human Life Form Appearance [UID 480]
Name | Bits | Description | Reference
Health | 3-4 | Describes the visual appearance of the severity of any injury | [UID 390]
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Mounted/Hoisted Status | 22 | Describes whether or not the life form is mounted/hoisted on another platform, such as a troop transport or helicopter hoist
State | 23 | Describes whether the entity is active or deactivated | [UID 386]"""


# [UID 38]
"""17.11.1.4 Environmental Appearance [UID 38]
Name | Bits | Description | Reference
Density | 16-19 | Describes the density | [UID 395]
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Masked / Cloaked | 31 | Describes whether or not the entity is masked or cloaked"""


# [UID 39]
"""17.11.1.5 Cultural Feature Appearance [UID 39]
Name | Bits | Description | Reference
Damage Area | 0-2 | Describes the damaged area | [UID 889], Identifies the damaged area when Damage is Slight Damage (1) or Moderate Damage (2).
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke Emanating | 5 | Describes whether or not smoke is emanating from the entity
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Internal Heat On | 22 | Describes whether the internal heat is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Exterior Lights On | 28 | Describes whether the exterior lights are on or off
Interior Lights On | 29 | Describes whether the interior lights are on or off
Masked / Cloaked | 31 | Describes whether or not the entity is masked or cloaked"""


# [UID 40]
"""17.11.1.6 Supply Appearance [UID 40]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Parachute Status | 7-8 | Describes the status of a supply's parachute | [UID 401]
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Deployed Status | 24-25 | Describes the deployed status | [UID 399]
Masked/Cloaked | 31 | Describes whether or not the entity is masked or cloaked"""


# [UID 41]
"""17.11.1.7 Radio Appearance [UID 41]
Name | Bits | Description | Reference
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
State | 23 | Describes whether the entity is active or deactivated | [UID 386]"""


# [UID 42]
"""17.11.1.8 Expendable Appearance [UID 42]
Name | Bits | Description | Reference
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke Emanating | 5 | Describes whether or not smoke is emanating from the entity
Parachute Status | 7-8 | Describes the status of a flare's parachute | [UID 401]
Flare/Smoke Color | 9-11 | Describes the color of a flare's light output or the color of smoke emanating from a smoke expendable | [UID 402]
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Launch Flash Present | 16 | Describes whether or launch flash is present
Flare/Smoke Status | 17-18 | Describes the status of a flare or smoke expendable | [UID 403]
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Spot Chaff Status | 24-25 | Describes the status of spot chaff | [UID 404]
Masked/Cloaked | 31 | Describes whether or not the entity is masked or cloaked"""


# [UID 43]
"""17.11.1.9 Sensor/Emitter Appearance [UID 43]
Name | Bits | Description | Reference
Paint Scheme | 0 | Describes the visual paint design | [UID 378]
Mobility Killed | 1 | Describes whether it is capable of moving on its own power
Mission Killed | 2 | Describes whether it is capable of carrying out its mission (e.g., damaged antenna)
Damage | 3-4 | Describes the damaged appearance | [UID 379]
Is Smoke Emanating | 5 | Describes whether or not smoke is emanating from the entity
Is Engine Emitting Smoke | 6 | Describes whether or not the engine is emitting smoke
Trailing Effects | 7-8 | Describes the size of the trailing effects | [UID 381]
Lights On | 12 | Describes whether the lights are on or off
Is Flaming | 15 | Describes whether the entity is burning and flames are visible
Antenna Raised | 16 | Describes whether the antenna is raised or not
Camouflage Type | 17-18 | Describes the camouflage color | [UID 384]
Concealed Position | 19 | Describes the type of concealment | [UID 385]
Is Frozen | 21 | Describes whether the entity is frozen and should not be dead reckoned
Power Plant On | 22 | Describes whether the power plant is on or off
State | 23 | Describes whether the entity is active or deactivated | [UID 386]
Tent Extended | 24 | Describes whether or not the tent is extended
Blackout Lights On | 26 | Describes whether blackout lights are on or off
Interior Lights On | 29 | Describes whether interior lights are on or off"""


"""17.11.2 Object Appearance"""
# This section specifies the Appearance records. All object states have the
# same General Appearance (see [UID 229]). All object states have a Specific
# Appearance that are specific to the Object State Type (point, linear, or
# areal), Object Kind (see [UID 225]), Domain and Category, and sometimes into
# the Subcategory.

# [UID 229]
"""17.11.2.1 General [UID 229]
Name | Bits | Description | Reference
Percent Complete | 0-7 | 8-bit unsigned integer indicating the percent completion of
the object (0..100)
Damage | 8-9 | Describes the damaged appearance | [UID 405]
Predistributed | 10 | Describes whether the object was predistributed | [UID 406]
State | 11 | Describes the state of the object | [UID 386]
Is Smoking | 12 | Describes whether or not there is a smoke plume
Is Flaming | 13 | Describes whether the object is burning and flames are visible
IED Present | 14-15 | Describes whether the object has or contains an IED | [UID 411]"""


"""17.11.2.2 Point Object State Appearance"""

# [UID 230]
"""17.11.2.2.1 Building / Structure [UID 230]
Name | Bits | Description | Reference
Color | 0-7 | Describes the color of the building or structure | [UID 463]
Paint Scheme | 8-15 | Describes the visual paint design | [UID 464]
Is Aperture Open | 16 | Describes whether the aperture (e.g., tent) is open or closed"""


"""17.11.2.2.2 Log crib, Abatis, Vehicle defilade, and Infantry fighting position [UID 231]
Name Bits Description Reference
Breach State 0-1 Describes the breached appearance of the object [UID 407]"""
# [UID 231]
"""17.11.2.2.2 Log crib, Abatis, Vehicle defilade, and Infantry fighting position [UID 231]
Name | Bits | Description | Reference
Breach State | 0-1 | Describes the breached appearance of the object | [UID 407]"""

# [UID 232]
"""17.11.2.2.3 Air burst, Ground burst [UID 232]
Name | Bits | Description | Reference
Opacity Percent | 0-7 | 8-bit unsigned integer indicating the percent opacity of the
smoke (0..100)
Size | 8-15 | 8-bit unsigned integer indicating the radius in meters of the cylinder which approximates an individual burst
Height | 16-23 | 8-bit unsigned integer indicating the height in meters of the cylinder which approximates an individual burst
Number of Bursts | 24-29 | 6-bit unsigned integer indicating the number of bursts in the
instance of tactical smoke
Chemical Type | 30-31 | Describes the chemical content of the smoke | [UID 408]"""

# [UID 233]
"""17.11.2.2.4 Crater [UID 233]
Name | Bits | Description | Reference
Diameter | 0-7 | 8-bit unsigned integer indicating the diameter of the crater in meters
Depth | 8-15 | 8-bit unsigned integer indicating the depth of the crater in centimeters
Height | 16-23 | 8-bit unsigned integer indicating the height of the crater in centimeters
Breach State | 30-31 | Describes the breached appearance of the object | [UID 409]"""

# [UID 234]
"""17.11.2.2.5 Ribbon Bridge [UID 234]
Name | Bits | Description | Reference
Number of Segments | 0-7 | 8-bit unsigned integer indicating the number of segments composing the ribbon bridge"""

# [UID 483]
"""17.11.2.2.6 Building Rubble [UID 483]
There are currently no enumerations defined for [UID 483]"""

# [UID 484]
"""17.11.2.2.7 Stationary Bridge and AVLB [UID 484]
There are currently no enumerations defined for [UID 484]"""

# [UID 485]
"""17.11.2.2.8 Disturbed Earth / Road [UID 485]
Name | Bits | Description | Reference
Diameter | 0-7 | 8-bit unsigned integer indicating the diameter in decimeters
Height | 8-15 | 8-bit unsigned integer indicating the height in centimeters
Contrast | 16-19 | 4-bit unsigned integer indicating 16 levels of contrast (low to high) distinguishing variation of object from surrounding surface"""

# [UID 486]
"""17.11.2.2.9 Pothole [UID 486]
Name | Bits | Description | Reference
Diameter | 0-7 | 8-bit unsigned integer indicating the diameter in decimeters
Depth | 8-15 | 8-bit unsigned integer indicating the depth in centimeters"""

# [UID 487]
"""17.11.2.2.10 Tree [UID 487]
Name | Bits | Description | Reference
Season | 0-1 | Indicates the visually represented season | [UID 465]
Leaf Coverage | 2-3 | Indicates the leaf coverage | [UID 509]"""

"""17.11.2.3 Linear Object State Appearance"""

# [UID 235]
"""17.11.2.3.1 Tank ditch, and Concertina Wire [UID 235]
Name | Bits | Description | Reference
Breach State | 0-1 | Describes the breached appearance of the object | [UID 409]
Breach Length | 16-23 | 8-bit unsigned integer indicating the fixed length in meters of a breached segment
Breach Location | 24-31 | 8-bit record where each bit indicates whether its associated
segment is breached or not, such that bit 0 of the record is the first segment"""

# [UID 236]
"""17.11.2.3.2 Exhaust smoke [UID 236]
Name | Bits | Description | Reference
Opacity Percent | 0-7 | 8-bit unsigned integer indicating the percent opacity of the smoke (0..100)
Smoke Is Attached | 8 | Describes whether or not the smoke is attached to the vehicle
Chemical Type | 9-10 | Describes the chemical content of the smoke | [UID 408]"""

# [UID 237]
"""17.11.2.3.3 Minefield Lane Marker [UID 237]
Name | Bits | Description | Reference
Visible Side | 0-1 | Describes the visible side of the lane marker | [UID 410]"""

# [UID 238]
"""17.11.2.3.4 Breach [UID 238]
There are currently no enumerations defined for [UID 238]"""

# [UID 488]
"""17.11.2.3.5 Wire [UID 488]
Name | Bits | Description | Reference
Color | 0-7 | 8-bit enumeration indicating the color | [UID 463]
Contrast | 16-19 | 4-bit unsigned integer indicating 16 levels of contrast (low to high) distinguishing variation of object from surrounding surface
Is Buried | 20 | Describes whether the wire is buried or not"""

# [UID 489]
"""17.11.2.3.6 Speed Bump [UID 489]
Name | Bits | Description | Reference
Color | 0-7 | 8-bit enumeration indicating the color | [UID 463]
Contrast | 16-19 | 4-bit unsigned integer indicating 16 levels of contrast (low to high) distinguishing variation of object from surrounding surface
Material | 20-23 | 4-bit enumeration indicating the type of material | [UID 466]"""

# [UID 239]
"""17.11.2.4 Areal Object State Minefield Appearance [UID 239]
Name | Bits | Description | Reference
Breach State | 0-1 | Describes the breached appearance of the object | [UID 407]
Mine Count | 16-31 | 16-bit unsigned integer indicating the number of mines in the minefield"""


"""17.11.2.5 General Object Enumerations"""

### Before ###
"""17.11.2.5.1 Object Damage [UID 405]
Value Description
0 No Damage
1 Damaged
2 Destroyed"""

### After ###
# [UID 405]
class ObjectDamage(enum.IntEnum):
    """17.11.2.5.1 Object Damage [UID 405]"""
    NO_DAMAGE = 0
    DAMAGED = 1
    DESTROYED = 2


# [UID 406]
class Predistributed(enum.IntEnum):
    """17.11.2.5.2 Predistributed [UID 406]
    Value Description
    0 Object Created During the Exercise
    1 Object Predistributed Prior to Exercise Start
    """
    CREATED_DURING_EXERCISE = 0
    PREDISTRIBUTED_PRIOR = 1


# [UID 407]
class BreachState(enum.IntEnum):
    """17.11.2.5.3 Breach State [UID 407]
    Value Description
    0 No Breaching
    1 Breached
    2 Cleared
    """
    NO_BREACHING = 0
    BREACHED = 1
    CLEARED = 2


# [UID 408]
class ChemicalType(enum.IntEnum):
    """17.11.2.5.4 Chemical Type [UID 408]
    Value Description
    0 Other
    1 Hydrochloric
    2 White Phosphorous
    3 Red Phosphorous
    """
    OTHER = 0
    HYDROCHLORIC = 1
    WHITE_PHOSPHOROUS = 2
    RED_PHOSPHOROUS = 3


# [UID 409]
class TankDitchBreach(enum.IntEnum):
    """17.11.2.5.5 Tank Ditch Breach [UID 409]"""
    NO_BREACHING = 0
    SLIGHT_BREACHING = 1
    MODERATE_BREACHED = 2
    CLEARED = 3

# [UID 410]
class LaneMarkerVisible(enum.IntEnum):
    """17.11.2.5.6 Lane Marker Visible [UID 410]"""
    LEFT_SIDE_VISIBLE = 0
    RIGHT_SIDE_VISIBLE = 1
    BOTH_SIDES_VISIBLE = 2


"""17.11.3 General Appearance Enumerations"""

# [UID 378]
class PaintScheme(enum.IntEnum):
    """17.11.3.1 Paint Scheme [UID 378]"""
    UNIFORM_COLOR = 0
    CAMOUFLAGE = 1


# [UID 379]
class Damage(enum.IntEnum):
    """17.11.3.2 Damage [UID 379]"""
    NO_DAMAGE = 0
    SLIGHT_DAMAGE = 1
    MODERATE_DAMAGE = 2
    DESTROYED = 3


# [UID 889]
class DamageArea(enum.IntEnum):
    """17.11.3.3 Damage Area [UID 889]"""
    DAMAGE_AREA_1 = 0  # (default is Side 1 = Front Side)
    # or Not Applicable if Damage Areas are not defined.
    DAMAGE_AREA_2 = 1  # (default is Side 2 = Right Side)
    DAMAGE_AREA_3 = 2  # (default is Side 3 = Back Side)
    DAMAGE_AREA_4 = 3  # (default is Side 4 = Left Side)
    DAMAGE_AREA_5 = 4  # (default is Corner 1 = Front Right Corner)
    DAMAGE_AREA_6 = 5  # (default is Corner 2 = Back Right Corner)
    DAMAGE_AREA_7 = 6  # (default is Corner 3 = Back Left Corner)
    DAMAGE_AREA_8 = 7  # (default is Corner 4 = Front Left Corner)


# [UID 381]
class TrailingEffects(enum.IntEnum):
    """17.11.3.4 Trailing Effects [UID 381]"""
    NONE = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


# [UID 382]
class Hatch(enum.IntEnum):
    """17.11.3.5 Hatch [UID 382]"""
    NOT_APPLICABLE = 0
    CLOSED = 1
    POPPED = 2
    POPPED_AND_PERSON_IS_VISIBLE = 3
    OPEN = 4
    OPEN_AND_PERSON_IS_VISIBLE = 5


# [UID 383]
class LauncherOperational(enum.IntEnum):
    """17.11.3.6 Launcher/Operational [UID 383]"""
    NOT_RAISED_NOT_OPERATIONAL = 0
    RAISED_OPERATIONAL = 1


# [UID 384]
class CamouflageType(enum.IntEnum):
    """17.11.3.7 Camouflage Type [UID 384]"""
    DESERT_CAMOUFLAGE = 0
    WINTER_CAMOUFLAGE = 1
    FOREST_CAMOUFLAGE = 2
    OTHER = 3


# [UID 385]
class ConcealedPosition(enum.IntEnum):
    """17.11.3.8 Concealed Position [UID 385]"""
    NOT_CONCEALED = 0
    PREPARED_CONCEALED_POSITION = 1


# [UID 386]
class EntityState(enum.IntEnum):
    """17.11.3.9 Entity or Object State [UID 386]"""
    ACTIVE = 0
    DEACTIVATED = 1


# [UID 387]
class Canopy(enum.IntEnum):
    """17.11.3.10 Canopy [UID 387]"""
    NOT_APPLICABLE = 0
    SINGLE_CANOPY_SINGLE_TROOP_DOOR_CLOSED = 1
    FRONT_AND_REAR_CANOPY_LEFT_AND_RIGHT_TROOP_DOOR_CLOSED = 2
    FRONT_CANOPY_LEFT_TROOP_DOOR_OPEN = 3
    SINGLE_CANOPY_SINGLE_TROOP_DOOR_OPEN = 4
    REAR_CANOPY_RIGHT_TROOP_DOOR_OPEN = 5
    FRONT_AND_REAR_CANOPY_LEFT_AND_RIGHT_TROOP_DOOR_OPEN = 6


# [UID 388]
class SubsurfaceHatch(enum.IntEnum):
    """17.11.3.11 Subsurface Hatch [UID 388]"""
    NOT_APPLICABLE = 0
    HATCH_IS_CLOSED = 1
    HATCH_IS_OPEN = 4


# [UID 390]
class LifeFormHealth(enum.IntEnum):
    """17.11.3.12 Life Form Health [UID 390]"""
    NO_INJURY = 0
    SLIGHT_INJURY = 1
    MODERATE_INJURY = 2
    FATAL_INJURY = 3


# [UID 391]
class LifeFormCompliance(enum.IntEnum):
    """17.11.3.13 Life Form Compliance [UID 391]"""
    NOT_SPECIFIED = 0
    DETAINED = 1
    SURRENDER = 2
    USING_FISTS = 3
    VERBAL_ABUSE_LEVEL_1 = 4
    VERBAL_ABUSE_LEVEL_2 = 5
    VERBAL_ABUSE_LEVEL_3 = 6
    PASSIVE_RESISTANCE_LEVEL_1 = 7
    PASSIVE_RESISTANCE_LEVEL_2 = 8
    PASSIVE_RESISTANCE_LEVEL_3 = 9
    USING_NON_LETHAL_WEAPON_1 = 10
    USING_NON_LETHAL_WEAPON_2 = 11
    USING_NON_LETHAL_WEAPON_3 = 12
    USING_NON_LETHAL_WEAPON_4 = 13
    USING_NON_LETHAL_WEAPON_5 = 14
    USING_NON_LETHAL_WEAPON_6 = 15


# [UID 392]
class LifeFormPosture(enum.IntEnum):
    """17.11.3.14 Life Form Posture [UID 392]"""
    NOT_SPECIFIED = 0
    UPRIGHT_STANDING_STILL = 1
    UPRIGHT_WALKING = 2
    UPRIGHT_RUNNING = 3
    KNEELING = 4
    PRONE = 5
    CRAWLING = 6
    SWIMMING = 7
    PARACHUTING = 8
    JUMPING = 9
    SITTING = 10
    SQUATTING = 11
    CROUCHING = 12
    WADING = 13
    SURRENDER = 14
    DETAINED = 15


# [UID 393]
class LifeFormWeaponImplement(enum.IntEnum):
    """17.11.3.15 Life Form Weapon/Implement [UID 393]"""
    NOT_PRESENT = 0
    STOWED = 1
    DEPLOYED_ACTIVE = 2
    FIRING_POSITION_IN_USE = 3


# [UID 394]
class ConcealedMovement(enum.IntEnum):
    """17.11.3.16 Concealed Movement [UID 394]"""
    OPEN_MOVEMENT = 0
    RUSHES_BETWEEN_COVERED_POSITIONS = 1


# [UID 395]
class EnvironmentalDensity(enum.IntEnum):
    """17.11.3.17 Environmental Density [UID 395]"""
    CLEAR = 0
    HAZY = 1
    DENSE = 2
    VERY_DENSE = 3
    OPAQUE = 4


# [UID 397]
class AntiCollisionDayNight(enum.IntEnum):
    """17.11.3.18 Anti-Collision Day/Night [UID 397]"""
    DAY = 0
    NIGHT = 1


# [UID 398]
class NavigationPositionBrightness(enum.IntEnum):
    """17.11.3.19 Navigation/Position Brightness [UID 398]"""
    DIM = 0
    BRIGHT = 1


# [UID 399]
class SupplyDeployed(enum.IntEnum):
    """17.11.3.20 Supply Deployed [UID 399]"""
    NOT_APPLICABLE = 0
    STOWED = 1
    DEPLOYED = 2
    DEPLOYED_AND_ACTIVE = 3


# [UID 400]
class NVGMode(enum.IntEnum):
    """17.11.3.21 NVG Mode [UID 400]"""
    OVERT_LIGHTING = 0
    COVERT_LIGHTING = 1  # (Night Vision Goggles)


# [UID 401]
class Parachute(enum.IntEnum):
    """17.11.3.22 Parachute [UID 401]"""
    NONE = 0
    DEPLOYED = 1
    COLLAPSED = 2
    MALFUNCTION_STREAMER = 3


# [UID 402]
class FlareSmokeColor(enum.IntEnum):
    """17.11.3.23 Flare/Smoke Color [UID 402]"""
    WHITE = 0
    RED = 1
    GREEN = 2
    IR = 3


# [UID 403]
class FlareSmoke(enum.IntEnum):
    """17.11.3.24 Flare/Smoke [UID 403]"""
    NOT_IGNITED = 0
    BURNING = 1
    BURNED_OUT = 2


# [UID 404]
class SpotChaff(enum.IntEnum):
    """17.11.3.25 Spot Chaff [UID 404]"""
    NONE = 0
    DEPLOYED = 1
    MALFUNCTION = 2


# [UID 411]
class IEDPresent(enum.IntEnum):
    """17.11.3.26 IED Present [UID 411]"""
    NONE = 0
    VISIBLE = 1
    PARTIALLY_HIDDEN = 2
    COMPLETELY_HIDDEN = 3


# [UID 426]
class CoverShroudStatus(enum.IntEnum):
    """17.11.3.27 Cover/Shroud Status [UID 426]"""
    CLOSED = 0
    OPENING = 1
    COVER_SHROUD_BLOWN_DETACHED = 2
    OPEN_ATTACHED = 3


# [UID 463]
class Color(enum.IntEnum):
    """17.11.3.28 Color [UID 463]"""
    # The color values 1 to 15 are defined in the HTML 3.0 specification;
    # color values 20 to 159 are defined in the SVG 1.0 specification
    NOT_SPECIFIED = 0
    WHITE_VGA = 1
    RED_VGA = 2
    YELLOW_VGA = 3
    LIME_VGA = 4
    CYAN_VGA = 5
    BLUE_VGA = 6
    MAGENTA_VGA = 7
    GREY_VGA = 8
    SILVER_VGA = 9
    MAROON_VGA = 10
    OLIVE_VGA = 11
    GREEN_VGA = 12
    TEAL_VGA = 13
    NAVY_VGA = 14
    PURPLE_VGA = 15
    RESERVED1 = 16
    RESERVED2 = 17
    RESERVED3 = 18
    RESERVED4 = 19
    BLACK = 20
    NAVY = 21
    DARK_BLUE = 22
    MEDIUM_BLUE = 23
    BLUE = 24
    DARK_GREEN = 25
    GREEN = 26
    TEAL = 27
    DARK_CYAN = 28
    DEEP_SKY_BLUE = 29
    DARK_TURQUOISE = 30
    MEDIUM_SPRING_GREEN = 31
    LIME = 32
    SPRING_GREEN = 33
    CYAN = 34
    MIDNIGHT_BLUE = 35
    DODGER_BLUE = 36
    LIGHT_SEA_GREEN = 37
    FOREST_GREEN = 38
    SEA_GREEN = 39
    DARK_SLATE_GRAY = 40
    LIME_GREEN = 41
    MEDIUM_SEA_GREEN = 42
    TURQUOISE = 43
    ROYAL_BLUE = 44
    STEEL_BLUE = 45
    DARK_SLATE_BLUE = 46
    MEDIUM_TURQUOISE = 47
    INDIGO = 48
    DARK_OLIVE_GREEN = 49
    CADET_BLUE = 50
    CORNFLOWER_BLUE = 51
    MEDIUM_AQUAMARINE = 52
    DIM_GRAY = 53
    SLATE_BLUE = 54
    OLIVE_DRAB = 55
    SLATE_GRAY = 56
    LIGHT_SLATE_GRAY = 57
    MEDIUM_SLATE_BLUE = 58
    LAWN_GREEN = 59
    CHARTREUSE = 60
    AQUAMARINE = 61
    MAROON = 62
    PURPLE = 63
    OLIVE = 64
    GRAY = 65
    GREY = 66
    SKY_BLUE = 67
    LIGHT_SKY_BLUE = 68
    BLUE_VIOLET = 69
    DARK_RED = 70
    DARK_MAGENTA = 71
    SADDLE_BROWN = 72
    DARK_SEA_GREEN = 73
    LIGHT_GREEN = 74
    MEDIUM_PURPLE = 75
    DARK_VIOLET = 76
    PALE_GREEN = 77
    DARK_ORCHID = 78
    YELLOW_GREEN = 79
    SIENNA = 80
    BROWN = 81
    DARK_GRAY = 82
    LIGHT_BLUE = 83
    GREEN_YELLOW = 84
    PALE_TURQUOISE = 85
    LIGHT_STEEL_BLUE = 86
    POWDER_BLUE = 87
    FIRE_BRICK = 88
    DARK_GOLDEN_ROD = 89
    MEDIUM_ORCHID = 90
    ROSY_BROWN = 91
    DARK_KHAKI = 92
    SILVER = 93
    MEDIUM_VIOLET_RED = 94
    INDIAN_RED = 95
    PERU = 96
    CHOCOLATE = 97
    TAN = 98
    LIGHT_GRAY = 99
    PALE_VIOLET_RED = 100
    THISTLE = 101
    ORCHID = 102
    GOLDEN_ROD = 103
    CRIMSON = 104
    GAINSBORO = 105
    PLUM = 106
    BURLY_WOOD = 107
    LIGHT_CYAN = 108
    LAVENDER = 109
    DARK_SALMON = 110
    VIOLET = 111
    PALE_GOLDEN_ROD = 112
    LIGHT_CORAL = 113
    KHAKI = 114
    ALICE_BLUE = 115
    HONEY_DEW = 116
    AZURE = 117
    SANDY_BROWN = 118
    WHEAT = 119
    BEIGE = 120
    WHITE_SMOKE = 121
    MINT_CREAM = 122
    GHOST_WHITE = 123
    SALMON = 124
    ANTIQUE_WHITE = 125
    LINEN = 126
    LIGHT_GOLDEN_ROD_YELLOW = 127
    OLD_LACE = 128
    RED = 129
    FUCHSIA = 130
    MAGENTA = 131
    DEEP_PINK = 132
    ORANGE_RED = 133
    TOMATO = 134
    HOT_PINK = 135
    CORAL = 136
    DARK_ORANGE = 137
    LIGHT_SALMON = 138
    ORANGE = 139
    LIGHT_PINK = 140
    PINK = 141
    GOLD = 142
    PEACH_PUFF = 143
    NAVAJO_WHITE = 144
    MOCCASIN = 145
    BISQUE = 146
    MISTY_ROSE = 147
    BLANCHED_ALMOND = 148
    PAPAYA_WHIP = 149
    LAVENDER_BLUSH = 150
    SEA_SHELL = 151
    CORNSILK = 152
    LEMON_CHIFFON = 153
    FLORAL_WHITE = 154
    SNOW = 155
    YELLOW = 156
    LIGHT_YELLOW = 157
    IVORY = 158
    WHITE = 159


# [UID 464]
class ExtendedPaintScheme(enum.IntEnum):
    """17.11.3.29 Extended Paint Scheme [UID 464]"""
    DEFAULT = 0


# [UID 465]
class Season(enum.IntEnum):
    """17.11.3.30 Season [UID 465]"""
    SUMMER = 0
    WINTER = 1
    SPRING = 2
    AUTUMN = 3


# [UID 466]
class Material(enum.IntEnum):
    """17.11.3.31 Material [UID 466]"""
    NOT_SPECIFIED = 0
    PLASTIC = 1
    RUBBER = 2
    ROAD = 3


# [UID 509]
class LeafCoverage(enum.IntEnum):
    """17.11.3.32 Leaf Coverage [UID 509]"""
    NORMAL = 0
    BARE = 1


# [UID 802]
class ClothingIRSignature(enum.IntEnum):
    """17.11.3.33 Clothing IR Signature [UID 802]"""
    STANDARD_CLOTHING = 0
    CAMOUFLAGE = 1  # (not just Paint Scheme)
    THERMAL_BLANKET = 2
    OTHER = 3
