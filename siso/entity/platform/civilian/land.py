"""civilian.land.py"""
import enum

"""5.2.4 Civilian Land Subcategories"""


# [UID 427]
"""5.2.4.1 Motorcycle [UID 427]16
Value Description
0 Other
1 Scooter (Small)
2 Sport/Street (Mid-Size)
3 Cruiser (Large)
4 Dirt Bike"""
class Motorcycle(enum.IntEnum): ...


# [UID 428]
"""5.2.4.2 Car [UID 428]17
Value Description
0 Other
10 Generic18
11 Generic, Mini/Microcar (Tiny)19
12 Generic, Economy/Compact (Small)20
13 Generic, Intermediate/Standard (Medium)21
14 Generic, Full/Premium/Luxury (Large)22
15 Generic, Oversize23
20 2-Door (Coupe)24
21 2-Door (Coupe), Mini/Microcar (Tiny)
22 2-Door (Coupe), Economy/Compact (Small)
23 2-Door (Coupe), Intermediate/Standard (Medium)
30 3-Door Hatchback25
31 3-Door Hatchback, Mini/Microcar (Tiny)
32 3-Door Hatchback, Economy/Compact (Small)
40 4-Door Sedan
41 4-Door Sedan, Mini/Microcar (Tiny)
42 4-Door Sedan, Economy/Compact (Small)
43 4-Door Sedan, Intermediate/Standard (Medium)
44 4-Door Sedan, Full/Premium/Luxury (Large)
45 4-Door Sedan, Oversize
50 5-Door Hatchback27
51 5-Door Hatchback, Mini/Microcar (Tiny)
52 5-Door Hatchback, Economy/Compact (Small)
53 5-Door Hatchback, Intermediate/Standard (Medium)
54 5-Door Hatchback, Full/Premium/Luxury (Large)
60 Wagon28
62 Wagon, Economy/Compact (Small)
63 Wagon, Intermediate/Standard (Medium)
64 Wagon, Full/Premium/Luxury (Large)
70 Minivan29
80 Limousine30
84 Limousine, Full/Premium/Luxury (Large)
85 Limousine, Oversize
90 Sports (High Performance)
100 Convertible31
101 Convertible, Mini/Microcar (Tiny)
102 Convertible, Economy/Compact (Small)
103 Convertible, Intermediate/Standard (Medium)
104 Convertible, Full/Premium/Luxury (Large)
110 Sports Utility Vehicle (SUV)32
112 Sports Utility Vehicle (SUV), Economy/Compact (Small)
113 Sports Utility Vehicle (SUV), Intermediate/Standard (Medium)
114 Sports Utility Vehicle (SUV), Full/Premium/Luxury (Large)
115 Sports Utility Vehicle (SUV), Oversize"""
class Car(enum.IntEnum): ...


# [UID 429]
"""5.2.4.3 Bus [UID 429]33
Value Description
0 Other
1 Commuter (Flat Nose)
2 Commuter (Snout Nose)
3 Shuttle
4 Double Decker
5 Guided
6 Kneeling
7 Midibus
8 Minibus
9 Mini Wheelchair
10 Motorcoach
11 Prison Bus
12 Schoolbus
13 School Wheelchair
14 Tour
15 Tram Parking Lot
16 Trolley
17 Airport Transport
18 Articulated (Multi-Unit)"""
class Bus(enum.IntEnum): ...


# [UID 430]
"""5.2.4.4 Single Unit Cargo Truck [UID 430]34
Value Description
0 Other
1 Pickup Truck, Mini
2 Pickup Truck, Mid-Size
3 Pickup Truck, Full-Size
4 Pickup Truck, Crew Cab
5 Pickup Truck, Extended Cab
6 Pickup Truck, Long Bed
7 Pickup Truck, Cab Forward
10 Cargo Truck
11 Cargo Truck, up to 2.5 Ton
12 Cargo Truck, up to 5 Ton
13 Cargo Truck, up to 7.5 Ton
14 Cargo Truck, up to 10 Ton
15 Cargo Truck, over 10 Ton
20 Tanker
30 Semi-Trailer Cab (w/o Trailer)
70 Van
71 Van, Extended
72 Van, Compact
73 Van, Wheelchair
74 Van, Delivery
100 Delivery Truck
101 Delivery Truck, Box
102 Delivery Truck, Flatbed
103 Delivery Truck, Stake Bed
104 Mess Truck
105 Truck, Palletised Load System (PLS)35
106 Truck, Petroleum, Oil, and Lubricants (POL) Palletised Load System (PLS)
107 Truck, Petroleum, Oil, and Lubricants (POL), Surveillance
108 Refrigerated Truck, Small
109 Refrigerated Truck, Medium
110 Refrigerated Truck, Large
"""
class SingleUnitCargoTruck(enum.IntEnum): ...


# [UID 431]
"""5.2.4.5 Single Unit Utility Emergency Truck [UID 431]
Value Description
0 Other
1 Ambulance Truck
2 Fire/Paramedic Truck
3 Ambulance, Advanced Life Support
4 Ambulance Pickup Truck
10 Fire Engine
11 Aerial Ladder Fire Engine
12 Airport Fire Engine
13 Wildland Fire Engine
14 Fire Chief
20 Police Paddy Wagon
21 Police, SWAT
22 Police, Bomb Squad
23 Police, Pickup Truck
30 Hazmat
40 Wrecker, Normal Hook and Chain
41 Wrecker, Normal Boom
42 Wrecker, Normal Wheel Lift
43 Wrecker, Normal Flatbed
44 Wrecker, Normal Integrated
45 Wrecker, Heavy Hook and Chain
46 Wrecker, Heavy Boom
47 Wrecker, Heavy Wheel Lift
48 Wrecker, Heavy Flatbed
49 Wrecker, Heavy Integrated
60 Postal Truck
70 Street Sweeper
71 Street Sweeper, Three Wheeled
80 Waste Collection, Other
81 Waste Collection, Front Loader
82 Waste Collection, Rear Loader
83 Waste Collection, Automated Side Loader
84 Waste Collection, Pneumatic Collection
85 Waste Collection, Grapple
90 Utility Truck
91 Utility Truck w/ Boom
100 Aerial Work Platform, Other
101 Aerial Work Platform, Scissor Lift
102 Aerial Work Platform, Telescoping
120 Maintenance Truck
121 Decontamination Truck
122 Water Cannon Truck
123 Water Purification Truck
124 Smoke Generator Truck
150 Auto Rickshaw"""
class SingleUnitUtilityEmergencyTruck(enum.IntEnum): ...


# [UID 432]
"""5.2.4.6 Multiple Unit Cargo Truck [UID 432]37
Value Description
0 Other
1 Tractor Trailer
2 Tanker"""
class MultipleUnitCargoTruck(enum.IntEnum): ...


# [UID 433]
"""5.2.4.7 Multiple Unit Utility Emergency Truck [UID 433]38
Value Description
0 Other
1 Fire Engine, Hook And Ladder"""
class MultipleUnitUtilityEmergencyTruck(enum.IntEnum): ...


# [UID 434]
"""5.2.4.8 Construction Specialty Vehicle [UID 434]39
Value Description
0 Other
1 Tug
2 Forklift
3 Loader
4 Loader, Backhoe
5 Crane, Tractor Mounted
6 Crane, Wheeled
7 Grader
8 Road Roller, Other
9 Road Roller, Double Drum, Smooth
10 Road Roller, Single Drum, Smooth
11 Road Roller, Double Drum, Sheeps
12 Road Roller, Single Drum, Sheeps
13 Road Roller, Pneumatic Tired
14 Excavator, Other
15 Excavator, Dragline
16 Excavator, Long Reach
17 Excavator, Mobile Tire
18 Mini Excavator
19 Excavator Giant
20 Bulldozer, Tractor Mounted
21 Bulldozer, Tracked
22 Scraper
23 Skid Steer
24 Dump Truck, Other
25 Dump Truck, Articulated
26 Dump Truck, Transfer
27 Dump Truck, Super
28 Dump Truck, Off Road
29 Paver
30 Drilling Machine
31 Concrete Mixer, Other
32 Concrete Mixer, Rear Discharge
33 Concrete Mixer, Front Discharge
34 Concrete Mixer, Six Axle
35 Concrete Mixer, Long Reach Boom
36 Concrete Mixer, Volumetric
37 Trencher, Chain
38 Trencher, Rockwheel
39 Snowcat
40 Crane, Tracked
41 Crane, Shovel
42 Sweeper, Rotary
43 Roller, Vibratory Compactor
44 Fork Lift, Truck
45 Fork Lift, Rought Terrain
46 Transloader
47 Truck, Water, Construction
48 Truck, Fuel Delivery
49 Truck, Sawmill
50 Truck, Line Marking, Construction
51 Tractor, Industrial
52 Compactor, High Speed
53 Truck, Drilling
54 Truck, Drilling Support
55 Crane, Construction"""
class ConstructionSpecialtyVehicle(enum.IntEnum): ...


# [UID 435]
"""5.2.4.9 Farm Specialty Vehicle [UID 435]40
Value Description
0 Other
1 Tractor
2 Harvester/Reaper
3 Skidder
4 Forwarder
5 Lawn Mower, Other
6 Lawn Mower, Riding
7 Lawn Mower, Standing
8 Lawn Mower, Push"""
class FarmSpecialtyVehicle(enum.IntEnum): ...


# [UID 436]
"""5.2.4.10 Trailer [UID 436]41
Value Description
0 Other
1 Trailer, Flatbed
2 Trailer, Container
3 Trailer, Container, Refrigerated
4 Trailer, Double
5 Trailer, Auto Transport
6 Trailer, Articulated
7 Trailer, Tanker
8 Trailer, Tanker, Small
9 Trailer, Tanker, Large
10 Trailer, Tanker, Gasoline
11 Trailer, Tanker, Milk
12 Trailer, Tanker, Water
13 Trailer, Tanker, Septic
14 Trailer, Boat
15 Trailer, Boat, Small
16 Trailer, Boat, Large
17 Trailer, Recreational
18 Trailer, Recreational, Conventional
19 Trailer, Recreational, Travel Expandable
20 Trailer, Recreational, Fifth Wheel Travel
21 Trailer, Recreational, Folding Camping
22 Trailer, Recreational, Truck Camper
23 Trailer, Aerostat Mooring Platform
24 Trailer, Household
25 Trailer, Kitchen
26 Trailer, UltraLight Aircraft
27 Trailer, Heavy Equipment"""
class Trailer(enum.IntEnum): ...


# [UID 437]
"""5.2.4.11 Recreational [UID 437]42
Value Description
0 Other
1 ATV, 2X4
2 ATV, 4X4
3 ATV, 6X6
4 ATV, 3-wheeled
5 Toy, Other
6 Toy, Car
7 Toy, ATV
8 Golf Cart
9 Snowmobile
10 Recreational Vehicle
11 Recreational Vehicle, Type A Motorhome
12 Recreational Vehicle, Type B Motorhome
13 Recreational Vehicle, Type C Motorhome
14 Conversion Van"""
class Recreational(enum.IntEnum): ...


# [UID 438]
"""5.2.4.12 Non-motorized [UID 438]43
Value Description
0 Other
1 Unicycle
2 Bicycle
3 Bicycle, Mountain
4 Bicycle, Racing
5 Tricycle
6 Quadricycle
7 Rickshaw, Two Person
8 Rickshaw, One Person
9 Tandem Bicycle
10 Cycle Trailer
11 Cycle Sidecar
12 Sled
13 Skis
14 Snowboard
15 Skateboard
16 Skates
17 Skates, In-Line
18 Wagon Cart
19 Dolly
20 Handtruck
21 Push Cart
22 Wheelbarrow
23 Kick Scooter
24 Wheelchair"""
class NonMotorized(enum.IntEnum): ...


# [UID 439]
"""5.2.4.13 Trains [UID 439]44
Value Description
0 Other
1 Engine (Locomotive)
2 Box Car
3 Tanker
4 Flatcar
5 Caboose
6 Passenger Car
7 Hopper"""
class Trains(enum.IntEnum): ...


# [UID 440]
"""5.2.4.14 Utility Emergency Car [UID 440]45
Value Description
0 Other
1 Ambulance Car
2 Police Car
3 Police Chief
4 Hearse
5 Taxi"""
class UtilityEmergencyCar(enum.IntEnum): ...


