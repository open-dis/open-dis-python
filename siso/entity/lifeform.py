"""lifeform.py

5.4 Life Form Kind
"""
import enum


"""5.4.3 Category"""
#  Categories 0-5 are deprecated (see 5.4.8)



# [UID 472]
class Land(enum.IntEnum):
    """5.4.3.1 Land Categories [UID 472]"""
    CONVENTIONAL_ARMED_FORCES = 10
    ARMY = 11
    MARINES = 12
    AIR_FORCE = 13
    NAVY = 14
    COAST_GUARD = 15
    UNITED_NATIONS = 16
    SPECIAL_OPS_FORCES = 30
    LAW_ENFORCEMENT = 50
    NON_MILITARY_NATIONAL_GOVERNMENT_AGENCIES = 70
    REGIONAL_LOCAL_FORCES = 90
    IRREGULAR_FORCES = 100
    TERRORIST_COMBATANT = 101
    INSURGENT = 102
    PARAMILITARY_FORCES = 110
    HUMANITARIAN_ORGANIZATIONS = 120
    CIVILIAN = 130
    EMERGENCY_MEDICAL_TECHNICIAN = 131
    FIREFIGHTER = 132
    PRESS = 133
    MAMMAL = 200  # [UID 100]
    REPTILE = 201  # [UID 101]
    AMPHIBIAN = 202  # [UID 102]
    INSECT = 203  # [UID 103]
    ARACHNID = 204  # [UID 104]
    MOLLUSK = 205  # [UID 105]
    MARSUPIAL = 206  # [UID 106]


# [UID 478]
class Air(enum.IntEnum):
    """5.4.3.2 Air Categories [UID 478]"""
    BIRD = 200  # [UID 110]
    INSECT = 201  # [UID 111]
    MAMMAL = 202  # [UID 112]


# [UID 479]
class Subsurface(enum.IntEnum):
    """5.4.3.3 Subsurface Categories [UID 479]"""
    FISH = 200  # [UID 120]
    MAMMAL = 201  # [UID 121]
    MOLLUSK = 202  # [UID 122]
    CRUSTACEAN = 203  # [UID 123]
    INSECT = 204  # [UID 124]


"""5.4.3.4 Country Specific Category Overlays"""
# Not Implemented


"""5.4.4 Subcategory"""

# [UID 473]
class Equipment(enum.IntEnum):
    """5.4.4.1 Equipment Class (Humans) [UID 473]"""
    NONE = 0
    WEAPON = 1                            # [UID 514]
    ASSAULT_RIFLES = 5                    # [UID 474]
    HIGH_POWER_RIFLES = 10                # [UID 475]
    SNIPER_RIFLES = 15                    # [UID 481]
    ANTI_MATERIEL_RIFLE = 17              # [UID 510]
    SUB_MACHINE_GUNS = 20                 # [UID 482]
    SHOT_GUNS = 25                        # [UID 511]
    GRENADE_LAUNCHERS = 30                # [UID 515]
    MACHINE_GUNS = 35                     # [UID 516]
    GRENADE_LAUNCHING_MACHINE_GUN = 40    # [UID 517]
    ANTI_TANK_ROCKETS = 45                # [UID 518]
    ANTI_TANK_MISSILES = 50               # [UID 519]
    ANTI_TANK_GUNS = 55
    FLAME_ROCKETS = 60                    # [UID 522]
    FLAME_THROWERS = 65                   # [UID 523]
    ROCKET_LAUNCHERS = 70
    MORTARS = 75                          # [UID 512]
    HAND_GUNS = 80                        # [UID 513]
    MAN_PORTABLE_AIR_DEFENSE_SYSTEM = 85  # [UID 520]
    RECOILLESS_RIFLES = 90                # [UID 521]
    DRONE_GUNS = 95                       # [UID 524]
    EQUIPMENT = 150
    SENSORS = 151
    SIGNAL_SENSOR = 152                   # [UID 505]
    LASERS = 153                          # [UID 527]
    ANIMAL_COMPANION = 160
    PERSONAL_ELECTRONICS = 171            # [UID 526]
    LOGISTICS_EQUIPMENT = 172             # [UID 525]


# [UID 100]
"""5.4.4.2 Land Mammal (Animal) [UID 100]77
Value Description
1 Small Dog78
2 Chihuahua
10 Medium Dog79
11 Australian Cattle Dog
20 Large Dog80
21 German Shepherd
30 Very Large Dog81
31 Giant Turkish Kangal
40 Sheep82
41 Goat
50 Pig83
60 Cow84
61 Ox
70 Ox With Cart85
80 Horse86
81 Donkey
82 Mule
90 Horse With Rider87
91 Horse With Cargo
92 Donkey With Rider
93 Donkey With Cargo
94 Mule With Rider
95 Mule With Cargo
100 Camel88
101 Dromedary Camel (One Hump)
102 Bactrian Camel (Two Humps)
110 Dromedary Camel With Rider89
111 Dromedary Camel With Cargo
200 Rat"""
class LandMammal(enum.IntEnum): ...


# [UID 101]
"""5.4.4.3 Land Reptile (Animal) [UID 101]
Value Description
1 New Zealand Northern Tuatara91
3 Monitor
8 Gecko
13 Iguana
17 Chameleon
30 Non-Venomous Snake92
31 Boa
35 Python
39 Bullsnake
43 Kingsnake
60 Venomous Snake93
61 Rattlesnake
62 Copperhead
63 Cottonmouth
64 Taipan
65 Viper
66 Cobra
67 Australian Brown Snake
90 Tortoise94
100 Turtle
120 American Alligator95
121 Crocodile
122 Australian Freshwater Crocodile"""
class LandReptile(enum.IntEnum): ...


# [UID 102]
"""5.4.4.4 Land Amphibian (Animal) [UID 102]
Value Description
1 Frog96
2 Toad170 Salamander97
230 Caecilian"""
class LandAmphibian(enum.IntEnum): ...


# [UID 103]
"""5.4.4.5 Land Insect (Animal) [UID 103]
Value Description
1 Beetle99
60 Mantis100
70 Cockroach101
80 Army Ant102
81 Fire Ant
90 Grasshopper103
100 Centipede104"""
class LandInsect(enum.IntEnum): ...


# [UID 104]
"""5.4.4.6 Land Arachnid (Animal) [UID 104]
Value Description
1 Spider105
20 Tick106
30 Scorpion107
40 Harvestmen108
50 Mite109"""
class LandArachnid(enum.IntEnum): ...


# [UID 105]
"""5.4.4.7 Land Mollusk (Animal) [UID 105]
Value Description
1 Snail110
50 Slug111"""
class LandMollusk(enum.IntEnum): ...


# [UID 106]
"""5.4.4.8 Land Marsupial (Animal) [UID 106]112
Value Description
1 Brown Four-Eyed Opossum113
2 Bushy-Tailed Opossum
90 Tate's Shrew Opossum114
100 Greater Bilby115
110 Tasmanian Devil116
150 Brush-Tailed Rock-Wallaby117
160 Eastern Wallaroo
170 Red Kangaroo
200 Queensland Koala118
205 Southern Hairy-Nosed Wombat119
210 Brushtail Possum120
211 Sugar Glider"""
class LandMarsupial(enum.IntEnum): ...


# [UID 110]
"""5.4.4.9 Air Bird (Animal) [UID 110]
Value Description
1 Penguin121
2 Seagull
3 Pelican
4 Albatross
5 Swan
6 Cormorant
7 Heron
8 Crane
9 Osprey
10 Loon
11 Stork
12 Flamingo
13 Duck
20 Ostrich122
21 Emu
22 Chicken
30 Black Bird123
31 Starling
32 Budgerigar (Parakeet)
40 Canadian Goose124
41 Crow
50 Eagle125
55 Vulture
60 Falcon
65 Hawk
70 Owl
80 Kite"""
class AirBird(enum.IntEnum): ...


# [UID 111]
"""5.4.4.10 Air Insect (Animal) [UID 111]
Value Description
1 Moth126
2 Butterfly
20 Fly127
30 Mosquito128
40 Wasp129
50 Bee130
60 Beetle131
70 Dragonfly132
80 Locust133"""
class AirInsect(enum.IntEnum): ...


# [UID 112]
"""5.4.4.11 Air Mammal (Animal) [UID 112]
Value Description
1 Bat
10 Flying Squirrel
20 Gliding Possum"""
class AirMammal(enum.IntEnum): ...


# [UID 120]
"""5.4.4.12 Subsurface Fish (Animal) [UID 120]
Value Description
1 Forage Fish, Small Schooling134
2 Herring
3 Sardines
4 Krill
5 Squid
30 Medium Schooling Fish135
31 Hake
32 Cod
33 Haddock
34 Mackerel
60 Large Schooling Fish136
61 Tuna
90 Small Shark137
91 Dogfish Shark
120 Medium Shark138
121 Mako Shark
122 Hammerhead Shark
150 Large Shark139
151 Great White Shark
152 Tiger Shark
153 Blue Shark
154 Whale Shark
180 Skate140
181 Stingray
190 Eel141
200 Marlin142
201 Swordfish"""
class SubsurfaceFish(enum.IntEnum): ...


# [UID 121]
"""5.4.4.13 Subsurface Mammal (Animal) [UID 121]
Value Description
1 Whale143
2 Beaked Whale
3 Beluga Whale
4 Blue Whale
5 Bottlenose Whale
6 Northern Bottlenose Whale
7 Southern Bottlenose Whale
8 Bowhead Whale
9 Bryde's Whale
10 Dwarf Sperm Whale
11 Finback Whale
12 Gray Whale
13 Humpback Whale
14 Long-Finned Pilot Whale
15 Minke Whale
16 Northern Minke Whale
17 Southern Minke Whale
18 Narwhal Whale
19 Orca Whale
20 Pygmy Sperm Whale
21 Right Whale
22 North Atlantic Right Whale
23 North Pacific Right Whale
24 Southern Right Whale
25 Sei Whale
26 Short-Finned Pilot Whale
27 Sperm Whale
50 Dolphin144
51 Bottlenose Dolphin
52 Bottlenose Indo-Pacific Dolphin
53 Bottlenose Burrunan Dolphin
54 Atlantic Spotted Dolphin
55 Australian Snubfin Dolphin
56 Chilean Black Dolphin
57 Chinese White Dolphin
58 Clymene Dolphin
100 Porpoise145
101 Harbour Porpoise
102 Californian Porpoise
103 Dall's Porpoise
104 Burmeister's Porpoise
120 Seal146
121 Bearded Seal
122 Harbor Seal
123 Fur Seal
124 Weddell Seal
125 Elephant Seal
130 Sea Lion147
131 Australian Sea Lion
132 California Sea Lion
140 Walrus148
141 Atlantic Walrus
142 Pacific Walrus
150 Otter149
151 Sea Otter
160 Manatee150
161 Florida Manatee
162 Dugongs
200 Polar Bear151"""
class SubsurfaceMammal(enum.IntEnum): ...


# [UID 122]
"""5.4.4.14 Subsurface Mollusk (Animal) [UID 122]
Value Description
1 Snail
10 Slug
20 Octopus
30 Squid
40 Cuttlefish
50 Clam
60 Muscle
70 Oyster
80 Scallop"""
class SubsurfaceMollusk(enum.IntEnum): ...


# [UID 123]
"""5.4.4.15 Subsurface Crustacean (Animal) [UID 123]
Value Description
1 Shrimp
2 Snapping Shrimp
10 Crayfish
20 Lobster
30 Crab"""
class SubsurfaceCrustacean(enum.IntEnum): ...


# [UID 124]
"""5.4.4.16 Subsurface Insect (Animal) [UID 124]
Value Description
1 Sea Skater
2 Water Beetle"""
class SubsurfaceInsect(enum.IntEnum): ...


"""5.4.5 Specific"""

# [UID 514]
"""5.4.5.1 Weapon Non-specific (Humans) [UID 514]
Value Description
0 Other
10 Knife
50 Machete
100 Explosive Vest
150 M18A1 Claymore"""
class Weapon(enum.IntEnum): ...


# [UID 474]
"""5.4.5.2 Assault Rifles (Humans) [UID 474]
Value Description
0 Other
1 4.5mm Interdynamics MKR
10 5.45mm AK-74
11 5.45mm AKS-74
12 5.45mm AK-74M
13 5.45mm Kbk wz. 1988 Tantal
30 5.56mm AK-101
31 5.56mm Diemaco C7152
32 5.56mm Colt Canada C8 Carbine
33 5.56mm GIAT FAMAS G2
34 5.56mm FN FNC
35 5.56mm HK G36
36 5.56mm IMI Galil
37 5.56mm INSAS
38 5.56mm Daewoo K1
39 5.56mm Daewoo K2
40 5.56mm M16A1
41 5.56mm M16A2/A3/A4
42 5.56mm Colt M4
43 5.56mm Colt M4 Special Operations Peculiar Modification (SOPMOD)
44 5.56mm Ruger Mini-14
45 5.56mm Enfield SA-80A2
46 5.56mm Pindad SS1 V1
47 5.56mm Pindad SS1 V2
48 5.56mm Pindad SS1 V3
49 5.56mm Steyr AUG A1
50 5.56mm T65
51 5.56mm T91
52 5.56mm Tavor TAR-21
53 5.56mm Type CQ / M311
54 5.56mm Daewoo K11
55 5.56mm Austeyr F88
56 5.56mm Austeyr F88-GLA
57 5.56mm Austeyr F88-S-A1
58 5.56mm Austeyr F88-S-A2
59 5.56mm Austeyr F88-C
60 5.56mm Austeyr F88-S-A1C
61 5.56mm Austeyr F88-S-A1 LTR
62 5.56mm Austeyr EF88
63 5.56mm Bushmaster XM15
64 5.56mm HK416
65 5.56mm F90
66 5.56mm F90(G)
67 5.56mm F90M
68 5.56mm F90M(G)
69 5.56mm F90CQB
100 5.8mm QBZ-95 (Type 95)
110 7.62mm AK-103
111 7.62mm AK-104
112 7.62mm AK-47
113 7.62mm AKM
114 7.62mm AKS-47
115 7.62mm HK G3A3
116 7.62mm IMI Galil
117 7.62mm KLS
118 7.62mm SKS
119 7.62mm Type 56
120 7.62mm Type 63/68
121 7.62mm Type 81
240 8mm Lebel M16"""
class AssaultRifle(enum.IntEnum): ...


# [UID 475]
"""5.4.5.3 High Power Rifles (Humans) [UID 475]
Value Description
0 Other
10 7.62mm M14
11 7.62mm Remington 700
12 7.62mm SIG-Sauer SSG-2000
13 7.62mm Stoner SR-25
14 7.62mm Mosin-Nagant Model 1891/30
15 7.62mm HK417
16 7.62mm HK417 16" Recce
50 7.65mm BAR M1918
51 7.65mm M1 Garand"""
class HighPowerRifle(enum.IntEnum): ...


# [UID 481]
"""5.4.5.4 Sniper (Humans) [UID 481]
Value Description
0 Other
1 5.8mm QBU-88 (Type 88)
30 7.62mm C3
31 7.62mm FR F2
32 7.62mm AWM-F (G22)
33 7.62mm G3 SG/1
34 7.62mm Galil Sniper
35 7.62mm L96A1
36 7.62mm M14 DMR
37 7.62mm M24 Sniper Weapon System (SWS)
38 7.62mm M40A1/A3
39 7.62mm Steyr SSG 69
40 7.62mm SVD (Dragunov)
41 7.62mm TYPE 79
42 7.62mm SR-25 MK11
43 7.62mm AW SR-98
44 7.62mm Blaser R93
100 7.7mm TYPE 99
105 8.58mm Blaser R93 Tactical 2
110 9mm VSS Vintorez
170 12.7mm Steyr HS .50
171 12.7mm M82A1A Special Applications Scoped Rifle (SASR)
172 12.7mm NSV
173 12.7mm OSV-96
174 12.7mm Rangemaster 50
175 12.7mm V94
200 20mm Denel NTW-20"""
class SniperRifle(enum.IntEnum): ...


# [UID 510]
"""5.4.5.5 Anti-Materiel Rifles (Humans) [UID 510]
Value Description
0 Other
10 12.7mm AW50
11 12.7mm AW50F"""
class AntiMaterielRifle(enum.IntEnum): ...


# [UID 482]
"""5.4.5.6 Sub Machine Gun (Humans) [UID 482]
Value Description
0 Other
10 5.45mm AKS-74U (AKSU-74)
20 5.56mm Daewoo K1A
60 9mm Daewoo K7
61 9mm MAC-10
62 9mm Madsen MK II
63 9mm Mini-Uzi
64 9mm Model 83 Skorpion SMG
65 9mm MP5A2
66 9mm MP5-N
67 9mm Sterling SMG
68 9mm Type CF-05
69 9mm Uzi"""
class SubMachineGun(enum.IntEnum): ...


# [UID 511]
"""5.4.5.7 Shot Guns (Humans) [UID 511]
Value Description
0 Other
20 Browning Superposed O/U
21 Browning Cynergy
22 Browning Auto-5
23 18.5mm Browning Citori O/U 12 Gauge
24 16.8mm Browning Citori O/U 16 Gauge
25 15.6mm Browning Citori O/U 20 Gauge
26 14mm Browning Citori O/U 28 Gauge
27 10.4mm Browning Citori O/U .410 Bore
28 18.5mm Browning Double Automatic 12 Gauge
29 18.5mm Ithaca 37 12 Gauge
30 16.8mm Ithaca 37 16 Gauge
31 15.6mm Ithaca 37 20 Gauge
32 14mm Ithaca 37 28 Gauge
33 19.7mm Ithaca Mag-10 SA 10 Gauge
34 19.7mm Marlin Model 55 10 Gauge
35 18.5mm Marlin Model 55 12 Gauge
36 16.8mm Marlin Model 55 16 Gauge
37 15.6mm Marlin Model 55 20 Gauge
38 18.5mm Mossberg 500 12 Gauge
39 15.6mm Mossberg 500 20 Gauge
40 10.4mm Mossberg 500 .410 Bore
41 18.5mm Mossberg 590 12 Gauge
42 15.6mm Mossberg 590 20 Gauge
43 10.4mm Mossberg 590 .410 Bore
44 18.5mm Mossberg 930 SA 12 Gauge
45 Remington Model 11 SA
46 Remington Model 10 12 Gauge
47 15.6mm Remington Model 17 20 Gauge
48 Remington Model 31
49 Remington Model 11-48 SA
50 18.5mm Remington 870 12 Gauge
51 16.8mm Remington 870 16 Gauge
52 15.6mm Remington 870 20 Gauge
53 14mm Remington 870 28 Gauge
54 10.4mm Remington 870 .410 Bore
55 Remington Model 58 SA
56 18.5mm Remington 878 SA 12 Gauge
57 18.5mm Remington Model 1100 SA 12 Gauge
58 16.8mm Remington Model 1100 SA 16 Gauge
59 15.6mm Remington Model 1100 SA 20 Gauge
60 14mm Remington Model 1100 SA 28 Gauge
61 10.4mm Remington Model 1100 SA .410 Bore
62 18.5mm Remington 11-87 SA 12 Gauge
63 15.6mm Remington 11-87 SA 20 Gauge
64 19.7mm Remington Model SP-10 SA 10 Gauge
65 18.5mm Remington 887 12 Gauge
70 18.5mm Remington Sparta 100 SxS 12 Gauge
71 15.6mm Remington Sparta 100 SxS 20 Gauge
72 10.4mm Remington Sparta 100 SxS .410 Bore
73 18.5mm Remington Spartan 310 O/U 12 Gauge
74 15.6mm Remington Spartan 310 O/U 20 Gauge
75 14mm Remington Spartan 310 O/U 28 Gauge
76 10.4mm Remington Spartan 310 O/U .410 Bore
77 18.5mm Remington Spartan 453 SA 12 Gauge
80 18.5mm Winchester Model 1200 12 Gauge
81 16.8mm Winchester Model 1200 16 Gauge
82 15.6mm Winchester Model 1200 20 Gauge
83 Winchester Model 1887/1901
84 Winchester Model 1897
85 Winchester Model 1912
86 Winchester Model 21 SxS
87 Winchester Model 37 SxS
88 18.5mm HR Ultraslug SxS 12 Gauge
89 15.6mm HR Ultraslug SxS 20 Gauge
90 18.5mm Ciener Ultimate O/U 12 Gauge
91 18.5mm Coach Gun SxS Double Barrel 12 Gauge
92 18.5mm Ruger Gold Label SxS 12 Gauge
93 18.5mm High Standard Model 10 SA 12 Gauge
94 18.5mm Kel-Tex KSG 12 Gauge
95 18.5 KAC Masterkey 12 Gauge
96 18.5mm M26 M.A.S.S. 12 Gauge
97 18.5mm SRM Arms M1216 SA 12 Gauge
98 18.5mm AA-12 FA Atchisson Assault
99 18.5mm Pancor Jackhammer FA 12 Gauge
110 18.5mm USAS-12 FA 12 Gauge
111 18.5mm MAUL SA 12 Gauge
112 18.5mm FN SLP SA 12 Gauge
113 18.5mm FN TPS 12 Gauge
115 18.5mm ENARM Pentagun SA 12 Gauge
116 Stevens Model 520/620
117 Stoeger Coach Gun SxS
118 Stoeger Condor O/U
120 18.5mm Armscor Model 30 SA 12 Gauge
121 Weatherby SA-08 SA
122 18.5mm Fabarm SDASS Tactical 12 Gauge
123 18.5mm MAG-7 12 Gauge
124 18.5mm Neostead 12 Gauge
125 18.5mm Armsel Striker SA 12 Gauge
127 18.5mm Parker Hale Rogun SA 12 Gauge
130 26mm RGA-86 Revolver
131 18.5mm Sjorgren SA 12 Gauge
132 18.5mm Akdal MKA 1919 SA 12 Gauge
133 18.5mm Retay Masai Mara SA 12 Gauge
134 18.5mm Safir T-14 SA 12 Gauge
150 18.5mm Benelli M1 Super 90 SA 12 Gauge
151 15.6mm Benelli M1 Super 90 SA 20 Gauge
152 18.5mm Benelli M3 Super 90 SA 12 Gauge
153 15.6mm Benelli M3 Super 90 SA 20 Gauge
154 18.5mm Benelli M4 Super 90 SA 12 Gauge
155 18.5mm Benelli Nova 12 Gauge
156 15.6mm Benelli Nove 20 Gauge
157 18.5mm Benelli Raffaello SA 12 Gauge
158 18.5mm Benelli Supernova 12 Gauge
159 18.5mm Benelli Vinci SA 12 Gauge
160 18.5mm Beretta 1201FP SA 12 Gauge
161 18.5mm Beretta 682 O/U 12 Gauge
162 15.6mm Beretta 682 O/U 20 Gauge
163 14mm Beretta 682 O/U 28 Gauge
164 10.4mm Beretta 682 O/U .410 Bore
165 18.5mm Beretta A303 SA 12 Gauge
166 18.5mm Beretta AL391 SA 12 Gauge
167 15.6mm Beretta AL391 SA 20 Gauge
168 18.5mm Beretta DT-10 O/U 12 Gauge
169 Beretta Silver Pigeon O/U
170 18.5mm Beretta Xtrema 2 SA 12 Gauge
171 15.6mm Franchi AL-48 SA 20 Gauge
172 14mm Franchi AL-48 SA 28 Gauge
173 10.4mm Franchi mod .410 FA .410 Bore
174 18.5mm Franchi SPAS-12 SA 12 Gauge
175 18.5mm Franchi SPAS-15 SA 12 Gauge
176 18.5mm Valtro PM-5/PM-5-350 12 Gauge
180 Blazer F3 O/U
181 18.5mm HK FABARM FP6 12 Gauge
182 18.5mm HK CAWS FA 12 Gauge
200 18.5mm Baikal MP-153 SA 12 Gauge
201 18.5mm Bandayevsky RB-12 12 Gauge
202 18.5mm Molot Bekas-M 12 Gauge
203 16.8mm Molot Bekas-M 16 Gauge
204 18.5mm TOZ-194 12 Gauge
205 23mm KS-23
206 MTs-255 Revoler 12 Gauge
207 18.5mm RMB-93 12 Gauge
208 18.5mm Saiga-12 SA 12 Gauge
209 15.6mm Saiga-12 SA 20 Gauge
210 10.4mm Saiga-12 SA .410 Bore
211 18.5mm Vepr-12 SA 12 Gauge
212 18.5mm Fort 500 12 Gauge
220 18.5mm Norinco HP9-1 12 Gauge"""
class ShotGun(enum.IntEnum): ...


# [UID 515]
"""5.4.5.8 Grenade Launchers (Humans) [UID 515]
Value Description
0 Other
1 40x46mm Arsenal UGGL-M1
2 40x46mm Arsenal MSGL
3 40mm VOG Arsenal MSGL
4 40x46mm Arsenal UBGL-M16
5 40x46mm Arsenal UBGL-M8
6 40x46mm Arsenal UBGL-M7
10 30mm BS-1 Tishina
11 40mm BTS-203
12 40mm Indumil IMC-40
20 40mm VOG BG-15
21 40mm VOG GP-25 Kostoyor
22 40mm VOG GP-30 Obuvka
23 40mm VOG GP-34
24 40mm VOG RGM-40 Kastet
25 40mm VOG RG-6
30 40x46mm M79
31 40x46mm M203
32 40x36mm M320
35 40x46mm CIS 40 GL
36 40x46mm EAGLE GL
37 40x46mm HK AG36
38 40x46mm HK AG-C/GLM
39 40x46mm HK69A1
40 40x46mm Beretta GLX 160
41 40x46mm ARDE UBGL
42 40x46mm XML148
43 40x46mm China Lake GL
44 40x46mm Hawk MM-1
50 25x40mm XM25 CDTE
60 37mm Milkor37/38 LL Stopper
61 40mm Milkor40 GL
62 40mm Milkor MGL
65 40x47mm Pallad wz1974
66 40x47mm Pallad wz1983
70 UGL 200 Canister RWGL-3
80 20x30mm ST Daewoo K11
90 35mm Type-91 BreechLoad GL
95 40x53mm CZW-40
100 45mm DP-64
105 20x42mm Neopup PAW-20"""
class GrenadeLauncher(enum.IntEnum): ...


# [UID 516]
"""5.4.5.9 Machine Guns (Humans) [UID 516]
Value Description
0 Other
10 5.56x45mm XM214 Microgun Six-Pak
11 7.62x51mm M134/XM196 Minigun
20 5.56x45mm M249/FN Minimi SAW/LMG
21 5.56x45mm FN Minimi Mk3 LMG
22 7.62x51mm FN Minimi 7.62 Mk3 GPMG
25 7.62x63mm M1941 Johnson
26 7.62x63mm M1918 BAR
27 7.62x51mm M1919A4/Mk 21 Mod 0 Browning MMG
28 7.62x63mm M1919A6 Browning MMG
29 7.62x51mm M37 Browning MMG
30 5.56x45mm Ares Shrike 5.56 LMG
31 5.56x45mm LSAT LMG
32 5.56x45mm CMG-1 LMG
33 5.56x45mm CMG-2 LMG
34 5.56x45mm Stoner 63A LMG
35 5.56x45mm Ultimax 100 LMG
36 5.56x54mm Beretta AS70/90 LMG
37 5.56x45mm CETME Ameli LMG
38 5.56x45mm IMI Negev LMG
39 5.56x45mm INSAS LMG
40 5.56x45mm AUG LMG
41 5.56x45mm AUG HBAR LMG
43 5.56x45mm HK MG4 LMG
44 5.56x45mm HK23/GR-9 LMG
46 5.56x45mm M27 IAR SAW
47 5.56x45mm L86 LSW
48 5.56x45mm Daewoo K3 LMG
49 5.56x45mm Vector Mini SS GPMG
50 7.62x51mm M60 GPMG
51 7.62x51mm M60E3 GPMG
52 7.62x51mm M60E4 GPMG
53 7.62x51mm M60E6 GPMG
55 7.62x51mm Mark 48 GMPG
58 7.62x51mm M240/FN MAG 58 GPMG
59 7.62x51mm M240E4/M240B GPMG
60 7.62x51mm M240E1/M240D GPMG
61 7.62x51mm M240G GPMG
62 7.62x51mm M240E5/M240H GPMG
63 7.62x51mm M240L GPMG
65 7.62x39mm Kk 62 LMG
70 7.62x51mm Vector SS-77 GPMG
71 7.62x51mm SIG MG 710-3 GPMG
72 7.62x51mm Sterling 7.62 GMPG
73 7.62x51mm Sumitomo Type-62 GPMG
74 7.62x51mm Daewoo K12 GPMG
75 7.62x51mm MG 51 GPMG
76 7.62x51mm Rheinmetall MG 3
77 7.62x51mm Rheinmetall MG 3KWS
80 7.62x51mm MG5/HK121 GPMG
81 7.62x51mm HK21 GPMG
85 7.62x51mm AA-52 GPMP
86 7.62x51mm UKM-2000 GPMG
88 7.62x54mm Uk vz. 59 GPMG
89 7.92x57mm MG 42 GPMG
100 12.7x99mm M2A1 Browning HMG
101 12.7x99mm M2HB Browning HMG
102 12.7x99mm M2HB-QCB Browning HMG
105 12.7x99mm M85C HMG
108 12.7x99mm Rheinmetall RMG.50 HMG
110 12.7x99mm HK25 HMG
112 12.7x99mm CIS 50MG
120 5.45x39mm IP-2 LMG
121 5.45x39mm Nikonov LMG
122 5.45x39mm M74 RPK
125 7.62x39mm M43 RPK
126 7.62x39mm RPD SAW
127 7.62x39mm Zastava M72
128 7.62x39mm Type-81 LMG
135 7.62x51mm Zastava M77
140 7.62x54mm PK GPMG
141 7.62x54mm AEK-999 GPMP
142 7.62x54mm Pecheneg GPMG
143 7.62x54mm Zastava M84
144 7.62x54mm Type-67 GPMG
145 7.62x54mm Type-80 GPMG
150 12.7x108mm NSV HMG
151 12.7x108mm Kord HMG
152 12.7x108mm KPD-12.7 HMG
153 12.7x108mm Zastava M02 Coyotoe HMG
154 12.7x108mm Zastava M87
155 12.7x108mm Type-77 HMG
156 12.7x108mm W85 HMG
157 12.7x108mm Type-90 HMG
164 5.8x42mm QJY-88 LMG
165 5.8x42mm QBB-95 DBP87 LMG
166 5.56x45mm QBB-95-1 LMG"""
class MachineGun(enum.IntEnum): ...


# [UID 517]
"""5.4.5.10 Grenade Launching Machine Gun (Humans) [UID 517]
Value Description
0 Other
20 40x53mm HK GMG
25 40x53mm Mk47 Striker
26 40mm M75
27 40mm M129
28 40x46mm XM 174
29 40x46mm Mk18 Mod 0
30 40x53mm Mk19
31 40x46mm Mk20 Mod 0
40 30x29mm RAG-30/SAG-30
41 30x29mm AGS-17 Plamya
42 30x29mm AGS-30 Atlant
43 40mm VOG AGS-40 Balkan
44 40x53mm SB LAG 40
50 40x53mm Vektor Y3
55 40x53mm CIS 40
60 40x56mm Howa Type-96
65 40x53mm Daewoo Precision Industries K4
70 25x59mm XM307 Advanced Crew Served Weapon
80 35x32mm QLZ87"""
class GrenadeLaunchingMachineGun(enum.IntEnum): ...


# [UID 518]
"""5.4.5.11 Anti-Tank Rockets (Humans) [UID 518]
Value Description
0 Other
10 82mm B-300
11 82mm Shipon
12 83mm MK153 Mod 0 SMAW
20 66mm M72 LAW
21 66mm M72A1 LAW
22 66mm M72A2 LAW
23 66mm M72A3 LAW
24 66mm M72A4 LAW
25 66mm M72A5 LAW
26 66mm M72A6 LAW
27 66mm M72A7 LAW
28 66mm M72E8 LAW
29 66mm M72E9 LAW
30 66mm M72E10 LAW
31 66mm M72AS LAW
35 94mm LAW 80
40 60mm M1 Bazooka
41 60mm M1A1 Bazooka
42 60mm M9 Bazooka
43 60mm M9A1 Bazooka
44 89mm M20 Super Bazooka
45 89mm M20A1 Super Bazooka
46 89mm M20B1 Super Bazooka
47 89mm M20A1B1 Super Bazooka
48 89mm M25 Three Shot Bazooka
49 89mm Instalaza M65
50 90mm Instalaza C90
51 90mm C90-CR (M3)
52 90mm C90-CR-AM (M3)
53 90mm C90-CR-BK (M3)
54 90mm C90-CR-IN (M3)
60 60mm PzF 3
61 60mm PzF 3-IT
62 60mm PzF 3 Bunkerfaust
65 44mm PzF 44
70 30mm Panzerfaust 30
71 50mm Panzerfaust 60
72 60mm Panzerfaust 100
73 60mm Panzerfaust 150
75 88mm Panzerschreck RPzB
80 83mm RL-83 Blindicide
81 100mm RL-100 Blindicide
85 90mm M79 Osa (Wasp)
86 64mm M80 Zolja (Wasp)
90 67mm Armburst Crossbow
93 40mm Type-69 RPG
95 89mm PIAT
100 40mm RPG-2
101 64mm RPG-18 Mukha
102 72.5mm RPG-22 Netto
103 72.5mm RPG-26 Aglen
104 105mm RPG-29 Vampir
105 105mm RPG-30 Kryuk
106 105mm RPG-32 Nashshab
110 40mm RPG-7
111 40mm PSRL-1 (RPG-7USA)
112 40mm GS-777/PSRL-2
120 68mm RPG-76 Komar (Mosquito)
125 120mm SEP Dard 120
128 58mm WASP 58
130 73mm LRAC 73-50
131 89mm LRAC 89-F1 STRIM
135 90mm MATADOR (Man-Portable Anti-Tank, Anti-DOoR)
136 90mm MATADOR-MP
137 90mm MATADOR-WB
138 90mm MATADOR-AS
140 78mm MARA Anti-Tank Rocket Launcher
145 120mm Type-98 PF98"""
class AntiTankRocket(enum.IntEnum): ...


# [UID 519]
"""5.4.5.12 Anti-Tank Missiles (Humans) [UID 519]
Value Description
0 Other
30 120mm Type 64 MAT KAM-3
31 153mm Type 79 Jyu-MAT KAM-9
32 120mm Type 87 Chu-MAT
33 140mm Type 01 LMAT
58 140mm M47 Dragon
59 140mm Saeghe 1-2
60 127mm FGM-148 Javelin
63 139mm FGM-172 SRAW
64 139mm FGM-172B SRAW-MPV
68 152mm BGM-71 TOW
69 152mm Orev TOW II
75 120mm Vickers Vigilant / Clevite
80 110mm Bantam (Rb 53)
81 150mm RBS-56 BILL 1
82 150mm RBS-56-2 BILL 2
85 130mm Spike SR
86 130mm Spike MR (CLU)
87 130mm Spike LR (CLU)
95 60mm Mosquito
98 160mm SS.10
100 103mm MILAN
101 115mm MILAN 2
102 115mm MILAN 2T
103 115mm MILAN 3
104 115mm MILAN ER
105 136mm ERYX
107 152mm Entac
110 125mm RAAD
111 125mm I-RAAD-T
112 152mm Toophan
113 152mm Toophan 2
114 152mm Toophan 5
120 136mm Bumbar
125 130mm Shershen PK-2
126 152mm Shershen-Q P-2B
130 130mm Mectron MSS-1.2
140 120mm HJ-8
141 120mm HJ-8A
142 120mm HJ-8B
143 120mm HJ-8C
144 120mm HJ-8D
145 120mm HJ-8E
146 120mm HJ-8F
147 120mm HJ-8FAE
148 120mm HJ-8L
149 120mm HJ-8H
150 120mm HJ-8S
151 120mm Baktar-Shikan
152 120mm HJ-11 (AFT-11)
153 152mm HJ-9A
154 135mm HJ-12 Red Arrow
155 125mm HJ-73 MCLOS
156 125mm HJ-73B SACLOS
157 125mm HJ-73C SACLOS ERA
170 125mm AT-3 Sagger A/9M14 Malyutka
171 125mm AT-3B Sagger B/9M14M Malyutka-M
172 125mm AT-3C Sagger C/9M14P Malyutka-P
173 125mm AT-3D Sagger D/9M14-2 Malyutka-2
174 125mm Susong-Po
175 125mm AT-3C POLK
176 125mm Kun Wu 1
177 125mm Maliutka M2T
178 120mm AT-4A Spigot A/9M111 Fagot
179 120mm AT-4B Spigot B/9M111-2 Fagot
180 120mm AT-4C Spigot C/9M111M Faktoriya
181 135mm AT-5A Spandrel/9M113 Kronkurs
182 135mm AT-5B Spandrel/9M113M Kronkurs-M
183 135mm Tosan
184 94mm AT-7 Saxhorn/9K115 Metis
185 130mm AT-13 Saxhorn-2/9K115-2 Metis-M
186 152mm AT-14 Spriggan/9M133 Kornet
187 152mm Dehlavie
200 102mm Mathogo"""
class AntiTankMissile(enum.IntEnum): ...


# [UID 520]
class AntiTankGun(enum.IntEnum):
    """5.4.5.13 Anti-Tank Guns"""
    # No values are currently defined for this field


# [UID 522]
"""5.4.5.14 Flame Rockets [UID 522]
Value Description
0 Other
20 66mm M202 Flash
30 62mm FHJ-84
40 90mm C90-CR-FIM (M3)
50 93mm RPO-A Shmel
51 93mm RPO-Z Shmel
52 93mm RPO-D Shmel"""
class FlameRocket(enum.IntEnum): ...


# [UID 523]
"""5.4.5.15 Flame Throwers [UID 523]
Value Description
0 Other
10 Handflammpatrone
11 FmW 41
20 M1A1
21 M2A1-7
22 M9A1-7
30 LPO-50
35 K Pattern
36 Portable, No 2 Ack Pack
37 Marsden
38 Harvey
45 ROKS-2
46 ROKS-3
50 Type-93
51 Type-100"""
class FlameThrower(enum.IntEnum): ...


class RocketLauncher(enum.IntEnum):
    """5.4.5.16 Rocket Launchers"""
    # No values are currently defined for this field


# [UID 512]
"""5.4.5.17 Mortars (Humans) [UID 512]
Value Description
0 Others
30 60mm M224
50 81mm F2
51 81mm L16
52 81mm M252"""
class Mortar(enum.IntEnum): ...


# [UID 513]
"""5.4.5.18 Hand Guns (Humans) [UID 513]
Value Description
0 Other
1 5.45mm PSM
30 9mm MK3 SLP
31 9mm Beretta 92S/92FS (M9)
32 9mm H&K USP
33 9mm Stechkin APS
34 9mm Makarov PM
35 9mm Smith and Wesson SD (Sigma)
36 9mm Glock 17
37 9mm SIG Sauer M17
38 9mm SIG Pro
39 9mm Smith and Wesson SW1911
40 9mm Smith and Wesson 5900-series
41 .45 Cal M1911
50 9.07mm Ruger GP 100
60 10mm Glock 20"""
class HandGun(enum.IntEnum): ...


# [UID 520]
"""5.4.5.19 Man-Portable Air Defense System (Humans) [UID 520]
Value Description
0 Other
1 70mm FIM-43 Redeye
2 70mm FIM-92 Stinger
10 76mm Blowpipe
11 76mm Starburst (Javelin S-15)
12 130mm Starstreak HVM
15 90mm Mistral
20 72mm 9K32M Strela-2 (SA-7)
21 72mm 9K36 Strela-3 (SA-14)
22 72mm 9K38 Igla (SA-18)
23 72mm 9K310 Igla-M (SA-16)
24 72mm 9K333 Verba (SA-25)
25 72mm 9K338 Igla-S (SA-24 Grinch)
26 72mm 9K32M Strela-2M (SA-7B)
30 72mm HN-5 Hong-Ying-5
31 72mm QW-1 Vanguard
32 72mm QW-2 Vanguard 2
33 90mm QW-3
34 72mm FN-6
45 71mm Misagh-1
46 71mm Misagh-2
50 80mm Type-91 Kin-SAM
55 80mm KP-SAM Shun-Gung (Chiron)
60 106mm RBS-70"""
class ManPortableAirDefenseSystem(enum.IntEnum): ...


# [UID 521]
"""5.4.5.20 Recoilless Rifles (Humans) [UID 521]
Value Description
0 Other
15 84mm M136 AT-4 CS
20 57mm M18 RR
21 75mm M20 RR
22 120mm M-28 Davy Crockett
23 155mm M-29 Davy Crockett
24 106mm M40 Recoilless Rifle
25 82mm M60 RR
26 90mm M67 RR
30 84mm M1 Carl Gustav
31 84mm M2 Carl Gustav
32 84mm M3 Carl Gustav
33 84mm M4 Carl Gustav
35 74mm Pansarskott m/68 Miniman
40 84mm ALAC
45 82mm B-10 RR
46 107mm B-11 RR
50 80mm Breda Folgore
55 120mm BAT RR
60 73mm SPG-9 Kopye
65 88mm RCL 3.45in
70 90mm Pvpj 110
75 50mm Jagdfaust
80 30mm Rheinmetall RMK30
90 88mm 55 S 55 Raikka
91 95mm 95 S 58-61
95 73mm LG40
96 105mm LG40
97 105mm LG42"""
class RecoillessRifle(enum.IntEnum): ...


# [UID 505]
class SignalSensor(enum.IntEnum):
    """5.4.5.21 Signal Sensor (Humans) [UID 505]"""
    SIGNAL_SMOKE = 1
    FLASH_LIGHT = 2
    SIGNAL_MIRROR = 3
    IR_STROBE = 4
    IR_ILLUMINATOR = 5
    SPOTLIGHT = 6


# [UID 524]
class DroneGun(enum.IntEnum):
    """5.4.5.22 Drone Guns (Humans) [UID 524]"""
    OTHER = 0
    DRONEGUN_TACTICAL = 15
    DRONEGUN_MKII = 16


# [UID 525]
class LogisticsEquipment(enum.IntEnum):
    """5.4.5.23 Logistics EQ Class [UID 525]"""
    SLING_LOAD_PENDANT = 1


# [UID 526]
class PersonalElectronics(enum.IntEnum):
    """5.4.5.24 Personal Electronics Class [UID 526]"""
    CELL_PHONE = 1


# [UID 527]
class Laser(enum.IntEnum):
    """5.4.5.25 Lasers Class [UID 527]"""
    GENERIC_LASER_DESIGNATOR = 1
    GENERC_LASER_POINTER = 2


"""5.4.6 Extra"""

# [UID 477]
"""5.4.6.1 Human Personal Data [UID 477]153
Value Description
0 Not Specified (Male)
1 Asian (Male)
2 Pacific Islander (Male)
3 Black (Male)
4 East Asian (Male)
5 Hispanic (Male)
6 White (Male)
7 Arab (Male)
8 Homogenous Country Code (Male)
9 Indigenous Country Code (Male)
10 Infant (0 months-1 year) (Male)
20 Toddler (1-3 years) (Male)
30 Child (3-10 years) (Male)
40 Adolescent (10-12 years) (Male)
50 Teenager (13-16 years) (Male)
60 Young Adult (17-25 years) (Male)
70 Adult (25-55 years) (Male)
80 Senior Adult (55-70 years) (Male)
90 Elderly (71+ years) (Male)
100 Female
101 Asian (Female)
102 Pacific Islander (Female)
103 Black (Female)
104 East Asian (Female)
105 Hispanic (Female)
106 White (Female)
107 Arab (Female)
108 Homogenous Country Code (Female)
109 Indigenous Country Code (Female)
110 Infant (0 months-1 year) (Female)
120 Toddler (1-3 years) (Female)
130 Child (3-10 years) (Female)
140 Adolescent (10-12 years) (Female)
150 Teenager (13-16 years) (Female)
160 Young Adult (17-25 years) (Female)
170 Adult (25-55 years) (Female)
180 Senior Adult (55-70 years) (Female)
190 Elderly (71+ years) (Female)"""


# [UID 134]
"""5.4.6.2 Land Mammal Variant (Animal) [UID 134]
Value Description
1 Animal with a Male Child Rider
2 Animal with a Female Child Rider
3 Animal with an Adult Male Rider
4 Animal with an Adult Female Rider
5 Animal Harnessed to a Plow
6 Animal Harnessed to a Cart"""


# [UID 135]
"""5.4.6.3 Land Reptiles, Amphibians, Insects, and Arachnids Variant (Animal) [UID 135]
Value Description
1 Black
2 Green
3 Spotted
4 Red
5 Brown"""


# [UID 136]
"""5.4.6.4 Air Bird Variant (Animal) [UID 136]
Value Description
1 Bird with Fish
2 V-Pattern Flock Shape
3 Circular Flock Shape
4 Irregular Flock Shape"""


# [UID 137]
"""5.4.6.5 Air Insect Variant (Animal) [UID 137]
Value Description
1 Vertical Shaped Insect Swarm
2 Circular Shaped Insect Swarm
3 Irregular Shaped Insect Swarm"""


# [UID 138]
"""5.4.6.6 Subsurface Fish, Mollusk, Crustacean, and Insect Variant (Animal) [UID 138]
Value Description
1 Black
2 Green
3 Spotted
4 Red
5 Brown
6 Blue
7 Silver
8 Grey"""


# [UID 139]
"""5.4.6.7 Subsurface Mammal Variant (Animal) [UID 139]
Value Description
1 Singing
2 Spouting"""


"""5.4.7 Animal Lifeform Size Ranges"""

# [UID 130]
"""5.4.7.1 Animal Lifeform Group Size Range Enumeration for all Domains [UID 130]154
Value Description
201 Number of animals range from 201 to 249
202 Number of animals range from 250 to 299
203 Number of animals range from 300 to 399
204 Number of animals range from 400 to 499
205 Number of animals range from 500 to 999
206 Number of animals range from 1,000 to 1,499
207 Number of animals range from 1,500 to 1,999
208 Number of animals range from 2,000 to 2,999
210 Number of animals range from 3,000 to 4,999
212 Number of animals range from 5,000 to 6,999
214 Number of animals range from 7,000 to 9,999
216 Number of animals range from 10,000 to 19,999
218 Number of animals range from 20,000 to 50,000
220 Number of animals range greater than 50,000"""


# [UID 131]
"""5.4.7.2 Specific Dimension Enumerations for Land Area Size [UID 131]155
Value Description
222 Small Area (2,000m2 - 4,000m2 / .5 to 1 sq. acre )
223 Small Area, Dense (2,000m2 - 4,000m2 / .5 to1 sq. acre)
224 Medium Area (20,000m2 - 41,000m2 / 10 to 20 sq. acres)
225 Medium Area, Dense (20,000m2 - 41,000m2 / 10 to 20 sq. acres)
226 Large Area (40,000m2 - 81,000m2 / 20 to 40 sq. acres)
227 Large Area, Dense (40,000m2 - 81,000m2 / 20 to 40 sq. acres)"""


# [UID 132]
"""5.4.7.3 Specific Dimension Enumerations for Air Area Size [UID 132]156
Value Description
222 Small Flock/Swarm (.5km long x 5m wide - 1km x 5m)
223 Small Flock/Swarm, Dense (.5km long x 5m wide - 1km x 5m)
224 Medium Flock/Swarm (1km long x 10m wide - 2km x 10m)
225 Medium Flock/Swarm, Dense (1km long x 10m wide - 2km x 10m)
226 Large Flock/Swarm (10km long x 100m wide - 20km x 100m)
227 Large Flock/Swarm, Dense (10km long x 100m wide - 20km x 100m)"""


# [UID 133]
"""5.4.7.4 Specific Dimension Enumerations for Subsurface Area Size [UID 133]157
Value Description
222 Small School (.5km long x 250m wide x 83m deep - 1km x .5km x 166m)
223 Small School, Dense (.5km long x 250m wide x 83m deep - 1km x .5km x
166m)
224 Medium School (.5km x 1km x 125m - 1km x 2km x 500m)
225 Medium School, Dense (.5km x 1km x 125m - 1km x 2km x 500m)
226 Large School (5km x 2km x 500m - 10km x 4km x 1km)
227 Large School, Dense (5km x 2km x 500m - 10km x 4km x 1km)"""


"""5.4.8 Legacy Weapon Subcategories (deprecated)"""
