"""civilian.surface.py"""
import enum


"""5.2.6 Civilian Surface Subcategories"""

# [UID 441]
"""5.2.6.1 Passenger Vessel [UID 441]53
Value Description
1 Cruise Ship
2 Cruise Ferry
3 High Speed Ferry
4 Ferry
5 Ocean Liner"""
class PassengerVessel(enum.IntEnum): ...


# [UID 442]
"""5.2.6.2 Dry Cargo Ship [UID 442]54
Value Description
1 Common Dry Cargo Ship
2 Dry Bulk Cargo Ship
3 Container Ship
4 Reefer Ship (Refrigerator Ship)
5 Ro-Ro Ship (Roll-on/Roll-off Ship)
6 Barge
7 Heavy Lift Ship"""
class DryCargoShip(enum.IntEnum): ...


# [UID 443]
"""5.2.6.3 Tanker [UID 443]55
Value Description
1 Liquid Petroleum Gas (LPG)Tanker
2 Chemical Tanker
3 Liquid Natural Gas (LNG) Tanker
4 Coastal Trading Vessel (Coaster)
5 Crude Oil Tanker (up to 159,999 DWT)
6 Liquid Bulk Tanker
7 Very Large Crude Carrier (160,000–319,999 DWT)
8 Ultra Large Crude Carrier (320,000–549,999 DWT)
9 Condensate Storage Tanker"""
class Tanker(enum.IntEnum): ...


# [UID 444]
"""5.2.6.4 Support Vessel [UID 444]56
Value Description
1 Platform Supply Vessel
2 Tender Vessel
3 Tugboat
4 Dive Support Vessel
5 Fireboat
6 Well Stimulation Vessel (WSV)
7 Anchor Handling Tug Supply Vessel (AHTS)
8 Offshore Construction Vessel (OCV)
9 Emergency Response and Rescue Vessel (ERRV)"""
class SupportVessel(enum.IntEnum): ...


# [UID 445]
"""5.2.6.5 Private Motorboat [UID 445]57
Value Description
1 Small Motorboat (up to 26ft/7.9m)
2 Medium Motorboat (up to 39ft/11.9m)
3 Large Motorboat (up to 65ft/19.8m)
4 Very Large Motorboat (greater than 65ft/19.8m)"""
class PrivateMotorboat(enum.IntEnum): ...


# [UID 446]
"""5.2.6.6 Private Sailboat [UID 446]58
Value Description
1 Small Sailboat (up to 26ft/7.9m)
2 Medium Sailboat (up to 39ft/11.9m)
3 Large Sailboat (up to 65ft/19.8m)
4 Very Large Sailboat (greater than 65ft/19.8m)"""
class PrivateSailboat(enum.IntEnum): ...


# [UID 447]
"""5.2.6.7 Fishing Vessel [UID 447]59
Value Description
1 Small Fishing Vessel (up to 26ft/7.9m)
2 Medium Fishing Vessel (up to 65ft/19.8m)
3 Large Fishing Vessel (greater than 65ft/19.8m)
4 Fish Processing Vessel
5 Masted Fishing Vessel"""
class FishingVessel(enum.IntEnum): ...


# [UID 448]
"""5.2.6.8 Other Vessels [UID 448]60
Value Description
1 Go-Fast Boat
2 Research Vessel
3 Hydrofoil Vessel
4 Cable Layer Vessel
5 Dredger Vessel
6 Junk/Dhow Vessel
7 Catamaran
8 Pontoon
9 Personal Water Craft
10 Refugee Raft"""
class OtherVessel(enum.IntEnum): ...


# [UID 633]
"""5.2.6.9 Life-Saving Equipment [UID 633]61
Value Description
1 Lifeboat
2 Liferaft
3 MOB Boat
4 Lifebuoy"""
class LifeSavingEquipment(enum.IntEnum): ...

