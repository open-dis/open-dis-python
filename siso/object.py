"""object.py

6 Object Type
"""
import enum


# [UID 225]
class StateKind(enum.IntEnum):
    """6.2 Object State Kind [UID 225]"""
    OTHER = 0
    OBSTACLE = 1
    PREPARED_POSITION = 2
    CULTURAL_FEATURE = 3
    PASSAGEWAY = 4
    TACTICAL_SMOKE = 5
    OBSTACLE_MARKER = 6
    OBSTACLE_BREACH = 7
    ENVIRONMENTAL_OBJECT = 8


# [UID 226]
"""
6.3 Point Object State Types [UID 226]
6.3.1 Other domain
0.5 ................................... Tactical smoke
0.5.0 Other
0.5.1 Ground Burst
0.5.1.0 Other
0.5.1.1 Artillery
0.5.2 Air Burst
0.5.2.0 Other
0.5.2.1 Grenade
0.5.3 Tactical Smoke, Canister
0.5.3.1 M83, White
0.5.3.2 M18, Green
0.5.3.3 M18, Violet
0.5.3.4 M18, Yellow
0.5.3.5 M18, Red
6.3.2 Land domain
1.1 ................................... Obstacle
1.1.0 Other
1.1.1 Abatis
1.1.1.0 Other
1.1.1.1 8 Tree
1.1.1.2 14 Tree
1.1.2 Log Crib
1.1.2.0 Other
1.1.2.1 Rectangular
1.1.2.2 Triangular
1.1.3 Crater
1.1.3.0 Other
1.1.3.1 Small
1.1.3.2 Medium
1.1.3.3 Large
1.1.4 Barrier
1.1.4.1 Dragon’s Teeth
1.1.4.2 Barrier, HESCO Basket, Small
1.1.4.3 Barrier, HESCO Basket, Medium
1.1.4.4 Barrier, HESCO Basket, Large
1.1.4.5 Barrier, HESCO Basket, Double-Stacked
1.1.4.6 Barrier, Construction
1.1.4.7 Barrier, Jersey, Plastic
1.1.4.8 Barrier, Fence, Chain, 6-foot
1.1.4.9 Barrier, Fence, Wood, 6-foot
1.1.4.10 Barrier, Texas
1.1.5 Rock Drop
1.1.5.1 Rock Drop, Covered
1.1.5.2 Rock Drop, Uncovered
1.1.9 Pot Hole
1.2 ................................... Prepared position
1.2.0 Other
1.2.1 Vehicle Defilade
1.2.1.0 Other
1.2.1.1 Armored Vehicle
1.2.1.2 Fighting Vehicle
1.2.1.3 Mortar Carrier
1.2.1.4 Tank
1.2.2 Infantry Fighting Position
1.2.2.0 Other
1.2.2.1 Covered Machine Gun Bunker
1.2.2.2 Overhead Covered Infantry Position
1.2.2.3 Non-Covered Infantry Position
1.2.2.4 Non-Covered Machine Gun Bunker
1.2.2.5 Hasty Fighting Position
1.3 ................................... Cultural feature
1.3.0 Other
1.3.1 Building / Structure
1.3.1.0 Other
1.3.1.1 Church
1.3.1.2 Apartment Building
1.3.1.3 Government Building
1.3.1.4 Industrial Building
1.3.1.5 Hanger
1.3.1.6 Microwave Tower
1.3.1.7 Power Pylon
1.3.1.8 Radio / TV Tower
1.3.1.9 School
1.3.1.10 Transformer Yard
1.3.1.12 Radio Tower, 100ft
1.3.1.13 Radio Tower, 500ft
1.3.1.14 Radio Tower, 1000ft
1.3.1.15 Porta Potty
1.3.1.16 FOB, Trailer Office
1.3.1.17 FOB, Guard Tower
1.3.1.18 Guard House
1.3.1.19 Windmill
1.3.2 Building Rubble
1.3.2.0 Other
1.3.3 Disturbed Earth
1.3.4 Disturbed Road
1.3.4.1 Disturbed Road, Gravel
1.3.4.2 Disturbed Road, Asphalt
1.3.4.3 Disturbed Road, Concrete
1.3.5 Tent
1.3.5.1 Tent, Small
1.3.5.2 Tent, Medium
1.3.5.3 Tent, Large
1.3.5.4 Tent, Modular General Purpose Tent System (MGPTS)
1.3.5.5 Tent, Arctic
1.3.5.6 Tent, TEMPER
1.3.5.7 Tent, Expandable Frame
1.3.5.8 Tent, Fritsche
1.3.5.9 Tent, Bedouin
1.3.5.10 Tent, Chemically and Biological Protected Shelter (CBPS)
1.3.5.11 Tent, Kuchi
1.3.6 Maintenance Structure
1.3.6.1 Lightweight Maintenance Enclosure (LME), Bradley
1.3.6.2 Lightweight Maintenance Enclosure (LME), M1
1.3.6.3 Large Area Maintenance Shelter (LAMS) Vehicle Maintenance (VM)
1.3.6.4 Large Area Maintenance Shelter (LAMS) Aviation Maintenance (AM)
1.3.7 MOUT Building
1.3.7.1 MOUT Building, House
1.3.7.2 MOUT Building, Hospital
1.3.7.3 MOUT Building, Gas Station
1.3.7.4 MOUT Building, Store
1.3.7.5 MOUT Building, Office Building
1.3.7.6 MOUT Building, Warehouse
1.3.7.7 MOUT Building, Control Tower
1.3.7.8 MOUT Building, Water Tower
1.3.7.9 MOUT Building, Police Station
1.3.7.10 MOUT Building, Fire Station
1.3.7.11 MOUT Building, Power Station
1.3.7.12 MOUT Building, Apartment
1.3.7.13 MOUT Building, School
1.3.7.14 MOUT Building, Church
1.3.7.15 MOUT Building, Farm House
1.3.7.16 MOUT Building, Mudbrick House
1.3.7.17 MOUT Building, Mudbrick Store
1.3.8 Container-Based Building
1.3.8.1 Container-Based Building, Store, Single
1.3.8.2 Container-Based Building, House, Single
1.3.8.3 Container-Based Building, House, Single, Railing
1.3.8.4 Container-Based Building, House, Double
1.3.8.5 Container-Based Building, Mosque, Single
1.3.8.6 Container-Based Building, Bridge, Single
1.3.8.7 Container-Based Building, FOB
1.3.10 Tree, Deciduous
1.3.10.1 Tree, Deciduous, Small
1.3.10.2 Tree, Deciduous, Medium
1.3.10.3 Tree, Deciduous, Large
1.3.11 Tree, Evergreen
1.3.11.1 Tree, Evergreen, Small
1.3.11.2 Tree, Evergreen, Medium
1.3.11.3 Tree, Evergreen, Large
1.3.12 Pump
1.3.12.1 Pump, Gas
1.3.13 Industrial Processing Plant
1.3.13.1 Oil Refinery
1.3.14 Utility Pole
1.4 ................................... Passageway
1.4.0 Other
1.4.1 Stationary Bridge
1.4.1.0 Other
1.4.1.1 2-Lane
1.4.1.2 4-Lane
1.4.2 AVLB
1.4.2.0 Other
1.4.2.1 M60A1
1.4.2.2 MTU20
1.4.2.3 Joint Assault Bridge (JAB)
1.4.3 Ribbon Bridge
1.4.3.0 Other
1.4.3.1 2-Lane
1.4.3.2 4-Lane
1.4.4 Pier
1.6 ................................... Obstacle marker
1.6.2 NBC Hazard Marker
1.8 ................................... Environmental Object
1.8.1 Flood
1.8.1.1 Flood, Small
1.8.1.2 Flood, Medium
1.8.1.3 Flood, Large

6.4 Linear Object State Types [UID 227]
6.4.1 Other domain
0.5 ................................... Tactical smoke
0.5.0 Other
0.5.1 Exhaust Smoke
0.5.1.0 Other
6.4.2 Land domain
1.1 ................................... Obstacle
1.1.0 Other
1.1.1 Tank Ditch
1.1.1.0 Other
1.1.2 Concertina Wire
1.1.2.0 Other
1.1.2.1 2-Roll
1.1.2.2 3-Roll
1.1.3 Concrete Barrier
1.1.4 Speed Bump
1.1.5 Rut
1.1.9 Chain Link Fence
1.3 ................................... Cultural feature
1.3.1 Wire
1.3.1.1 Wire, Crush
1.3.2 Tracks, Tire
1.6 ................................... Obstacle marker
1.6.0 Other
1.6.1 Minefield Lane Marker
1.6.1.0 Other
1.7 ................................... Obstacle breach
1.7.0 Other
1.7.1 Breach
1.7.1.0 Other

6.5 Areal Object State Types [UID 228]
6.5.1 Other domain
0.1 ................................... Obstacle
0.1.0 Other
0.1.1 Minefield
0.1.1.0 Other
0.1.1.1 Hasty
0.1.1.2 Prepared
0.1.1.3 Scattered
0.1.1.4 Solitary
"""


# [UID 226]
class PointObjectState(enum.IntEnum): ...


# [UID 227]
class LinearObjectState(enum.IntEnum): ...
    