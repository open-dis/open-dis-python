"""record.py

19 Variable Record Types
"""
import enum


"""19.1 Variable Parameter Record Type [UID 56]
Value Description
0 Articulated Part
1 Attached Part
2 Separation
3 Entity Type
4 Entity Association"""
# [UID 56]
class VariableParameterRecordType(enum.IntEnum):
    """19.1 Variable Parameter Record Type [UID 56]"""
    ARTICULATED_PART = 0
    ATTACHED_PART = 1
    SEPARATION = 2
    ENTITY_TYPE = 3
    ENTITY_ASSOCIATION = 4


# [UID 66]
"""19.2 Variable Record Types [UID 66]"""
    """1 Entity ID List
    1001 DDCP Join Transaction Join Request Message
    1002 DDCP Set Playback Window Transaction Set Playback Window Request Message
    1003 DDCP Load Mission Recording Transaction Load Mission Recording Request Message
    1004 DDCP Cue Transaction Cue Request Message
    1005 DDCP Play Transaction Play Request Message
    1006 DDCP Stop Transaction Stop Request Message
    1007 DDCP Pause Transaction Pause Request Message
    1009 DDCP End Transaction End Request Message
    1051 DDCP Join Response Message
    1052 DDCP Request Receipt Message
    1053 DDCP Playback Window Confirmed Message
    1054 DDCP Mission Recording Loaded Message
    1055 DDCP Cue Confirmed Message
    1056 DDCP Time to Complete Message
    1057 DDCP Play Commenced Message
    1058 DDCP Stop Confirmed Message
    1059 DDCP Pause Confirmed Message
    1061 DDCP End Response Message
    1111 DDCP Master Announce Message
    1112 DDCP Device Announce Message
    1114 DDCP Device Exit Message
    1115 DDCP Device Heartbeat Message
    1116 DDCP Master Time Sync Message
    1118 DDCP Error Message
    1119 DDCP Master Stop Sync Message
    1120 DDCP Master Transition Message
    1200 Mission Time
    3000 High Fidelity HAVE QUICK/SATURN Radio324
    3500 Blanking Sector attribute record
    3501 Angle Deception attribute record
    3502 False Targets attribute record
    4000 DE Precision Aimpoint record
    4001 DE Area Aimpoint record
    4500 Directed Energy Damage Description record
    5000 Crypto Control
    5001 Mode 5/S Transponder Location
    5002 Mode 5/S Transponder Location Error
    5003 Squitter Airborne Position Report
    5004 Squitter Airborne Velocity Report
    5005 Squitter Surface Position Report
    5006 Squitter Identification Report
    5007 GICB
    5008 Squitter Event-Driven Report
    5009 Antenna Location
    5010 Basic Interactive
    5011 Interactive Mode 4 Reply
    5012 Interactive Mode 5 Reply
    5013 Interactive Basic Mode 5
    5014 Interactive Basic Mode S
    5500 IO Effect
    5501 IO Communications Node"""
class VariableRecordType(enum.IntEnum):
    """19.2 Variable Record Types [UID 66]"""
    ENTITY_ID_LIST = 1
    DDCP_JOIN_TRANSACTION_JOIN_REQUEST_MESSAGE = 1001
    DDCP_SET_PLAYBACK_WINDOW_TRANSACTION_SET_PLAYBACK_WINDOW_REQUEST_MESSAGE = 1002
    DDCP_LOAD_MISSION_RECORDING_TRANSACTION_LOAD_MISSION_RECORDING_REQUEST_MESSAGE = 1003
    DDCP_CUE_TRANSACTION_CUE_REQUEST_MESSAGE = 1004
    DDCP_PLAY_TRANSACTION_PLAY_REQUEST_MESSAGE = 1005
    DDCP_STOP_TRANSACTION_STOP_REQUEST_MESSAGE = 1006
    DDCP_PAUSE_TRANSACTION_PAUSE_REQUEST_MESSAGE = 1007
    DDCP_END_TRANSACTION_END_REQUEST_MESSAGE = 1009
    DDCP_JOIN_RESPONSE_MESSAGE = 1051
    DDCP_REQUEST_RECEIPT_MESSAGE = 1052
    DDCP_PLAYBACK_WINDOW_CONFIRMED_MESSAGE = 1053
    DDCP_MISSION_RECORDING_LOADED_MESSAGE = 1054
    DDCP_CUE_CONFIRMED_MESSAGE = 1055
    DDCP_TIME_TO_COMPLETE_MESSAGE = 1056
    DDCP_PLAY_COMMENCED_MESSAGE = 1057
    DDCP_STOP_CONFIRMED_MESSAGE = 1058
    DDCP_PAUSE_CONFIRMED_MESSAGE = 1059
    DDCP_END_RESPONSE_MESSAGE = 1061
    DDCP_MASTER_ANNOUNCE_MESSAGE = 1111
    DDCP_DEVICE_ANNOUNCE_MESSAGE = 1112
    DDCP_DEVICE_EXIT_MESSAGE = 1114
    DDCP_DEVICE_HEARTBEAT_MESSAGE = 1115
    DDCP_MASTER_TIME_SYNC_MESSAGE = 1116
    DDCP_ERROR_MESSAGE = 1118
    DDCP_MASTER_STOP_SYNC_MESSAGE = 1119
    DDCP_MASTER_TRANSITION_MESSAGE = 1120
    MISSION_TIME = 1200
    HIGH_FIDELITY_HAVE_QUICK_SATURN_RADIO = 3000
    BLANKING_SECTOR_ATTRIBUTE_RECORD = 3500
    ANGLE_DECEPTION_ATTRIBUTE_RECORD = 3501
    FALSE_TARGETS_ATTRIBUTE_RECORD = 3502
    DE_PRECISION_AIMPOINT_RECORD = 4000
    DE_AREA_AIMPOINT_RECORD = 4001
    DE_DAMAGE_DESCRIPTION_RECORD = 4500
    CRYPTO_CONTROL = 5000
    MODE_5_S_TRANSPONDER_LOCATION = 5001
    MODE_5_S_TRANSPONDER_LOCATION_ERROR = 5002
    SQUITTER_AIRBORNE_POSITION_REPORT = 5003
    SQUITTER_AIRBORNE_VELOCITY_REPORT = 5004
    SQUITTER_SURFACE_POSITION_REPORT = 5005
    SQUITTER_IDENTIFICATION_REPORT = 5006
    GICB = 5007
    SQUITTER_EVENT_DRIVEN_REPORT = 5008
    ANTENNA_LOCATION = 5009
    BASIC_INTERACTIVE = 5010
    INTERACTIVE_MODE_4_REPLY = 5011
    INTERACTIVE_MODE_5_REPLY = 5012
    INTERACTIVE_BASIC_MODE_5 = 5013
    INTERACTIVE_BASIC_MODE_S = 5014
    IO_EFFECT = 5500
    IO_COMMUNICATIONS_NODE = 5501
    """10000 Identification
    10010 Trainer Initial Conditions Filename
    10020 Increment 3.1 Mission Data Load Name
    10030 Increment 2 Mission Data Load Name
    10110 Set Markpoint Command
    10115 Markpoint ID
    10140 Reaction Level
    10150 Weapon Reload
    10157 CES Entity Set / Clear Status
    10160 Activate Entity
    10170 Disengage / Reengage
    10190 Fuel Freeze
    10250 Fire Launch Dispense
    10254 Target Assignment
    10256 CIC Enable
    10258 Shoot Inhibit
    10259 Posture
    10262 Jammer State
    10263 Jammer Type
    10264 Dynamic Targeting
    10267 Manual Jamming On Override
    10268 SOJ Axis
    10280 Emitter Override
    10290 Shields
    10300 Crash Override
    10306 Stop Buzzer
    10307 Target Lasing - On / Off
    10308 Target Lasing - Laser Code
    10310 Power Plant
    10311 Tactical Lighting On / Off Control - Light Control
    10312 Tactical Lighting Blinker Control - Blinker Value
    10313 Tactical Lighting On / Off Control - Light Control Type
    10314 Park Vehicle
    10315 Signaling On / Off
    10316 Signaling Device
    10400 Ownship ID
    10600 State Change
    11000 Entity Type
    11100 Concatenated
    11110 Kind
    11120 Domain
    11130 Country
    11140 Category
    11150 Subcategory
    11160 Specific
    11170 Extra
    11180 Force ID
    11200 Force ID
    11300 Description
    11500 Tanker Boom Control
    11501 Airport Lights
    11502 Weather Post
    11503 Localizer and GlideSlope
    11504 TACAN NavAids
    12000 Alternative Entity Type
    12110 Kind
    12120 Domain
    12130 Country
    12140 Category
    12150 Subcategory
    12160 Specific
    12170 Extra
    12300 Description
    13000 Entity Marking
    13100 Entity Marking Characters
    13200 Crew ID
    14000 Task Organization
    14200 Regiment Name
    14300 Battalion Name
    14400 Company Name
    14500 Platoon Name
    14520 Squad Name
    14540 Team Name
    14600 Bumper Number
    14700 Vehicle Number
    14800 Unit Number
    15000 DIS Identity
    15100 DIS Site ID
    15200 DIS Host ID
    15300 DIS Entity ID
    15400 Mount Intent
    15500 Tether-Unthether Command ID
    15510 Teleport Entity Data Record
    15600 DIS Aggregate ID (Set if communication to aggregate)
    15800 Ownership Status
    19177 Reconstitute"""
    IDENTIFICATION = 10000
    TRAINER_INITIAL_CONDITIONS_FILENAME = 10010
    INCREMENT_3_1_MISSION_DATA_LOAD_NAME = 10020
    INCREMENT_2_MISSION_DATA_LOAD_NAME = 10030
    SET_MARKPOINT_COMMAND = 10110
    MARKPOINT_ID = 10115
"""20000 Loads
21000 Crew Members
21100 Crew Member ID
21200 Health
21300 Job Assignment
23000 Fuel
23100 Quantity
23105 Quantity
24000 Ammunition
24001 120-mm HEAT, quantity
24002 120-mm SABOT, quantity
24003 12.7-mm M8, quantity
24004 12.7-mm M20, quantity
24005 7.62-mm M62, quantity
24006 M250 UKL8A1, quantity
24007 M250 UKL8A3, quantity
24008 7.62-mm M80, quantity
24009 12.7-mm, quantity
24010 7.62-mm, quantity
24060 Mines, quantity
24100 Type
24110 Kind
24120 Domain
24130 Country
24140 Category
24150 Subcategory
24160 Extra
24300 Description
25000 Cargo
26000 Vehicle Mass
27000 Supply Quantity
28000 Armament"""
"""30000 Status
30010 Activate entity
30100 Subscription State
30300 Round trip time delay
30400 TADIL J message count (label 0)
30401 TADIL J message count (label 1)
30402 TADIL J message count (label 2)
30403 TADIL J message count (label 3)
30404 TADIL J message count (label 4)
30405 TADIL J message count (label 5)
30406 TADIL J message count (label 6)
30407 TADIL J message count (label 7)
30408 TADIL J message count (label 8)
30409 TADIL J message count (label 9)
30410 TADIL J message count (label 10)
30411 TADIL J message count (label 11)
30412 TADIL J message count (label 12)
30413 TADIL J message count (label 13)
30414 TADIL J message count (label 14)
30415 TADIL J message count (label 15)
30416 TADIL J message count (label 16)
30417 TADIL J message count (label 17)
30418 TADIL J message count (label 18)
30419 TADIL J message count (label 19)
30420 TADIL J message count (label 20)
30421 TADIL J message count (label 21)
30422 TADIL J message count (label 22)
30423 TADIL J message count (label 23)
30424 TADIL J message count (label 24)
30425 TADIL J message count (label 25)
30426 TADIL J message count (label 26)
30427 TADIL J message count (label 27)
30428 TADIL J message count (label 28)
30429 TADIL J message count (label 29)
30430 TADIL J message count (label 30)
30431 TADIL J message count (label 31)
31000 Position
31010 Route (Waypoint) type
31100 MilGrid10
31200 Geocentric Coordinates
31210 X
31220 Y
31230 Z
31300 Latitude
31400 Longitude
31500 Line of Sight
31510 X
31520 Y
31530 Z
31600 Altitude
31700 Destination Latitude
31800 Destination Longitude
31900 Destination Altitude
32000 Orientation
32100 Hull Heading Angle
32200 Hull Pitch Angle
32300 Roll Angle
32500 X
32600 Y
32700 Z
33000 Appearance
33100 Ambient Lighting
33101 Lights
33200 Paint Scheme
33300 Smoke
33400 Trailing Effects
33500 Flaming
33600 Marking
33710 Mine Plows Attached
33720 Mine Rollers Attached
33730 Tank Turret Azimuth
34000 Failures and Malfunctions
34100 Age
34110 Kilometers
35000 Damage
35050 Cause
35100 Mobility Kill
35200 Fire-Power Kill
35300 Personnel Casualties
36000 Velocity
36100 X-velocity
36200 Y-velocity
36300 Z-velocity
36400 Speed
37000 Acceleration
37100 X-acceleration
37200 Y-acceleration
37300 Z-acceleration
38100 Engine Status
39000 Primary Target Line (PTL)"""
"""40000 Exercise
40010 Exercise State
40015 Restart/Refresh
40020 AFATDS File Name
41000 Terrain Database
42000 Missions
42100 Mission ID
42200 Mission Type
42300 Mission Request Time Stamp
43000 Exercise Description
43100 Name
43200 Entities
43300 Version
43410 Guise Mode
43420 Simulation Application Active Status
43430 Simulation Application Role Record
43440 Simulation Application State
44000 Visual Output Mode
44100 Simulation Manager Role
44110 Simulation Manager Site ID
44120 Simulation Manager Applic. ID
44130 Simulation Manager Entity ID
44140 Simulation Manager Active Status
44200 After Active Review Role
44210 After Active Review Site ID
44220 After Active Applic. ID
44230 After Active Review Entity ID
44240 After Active Review Active Status
44300 Exercise Logger Role
44310 Exercise Logger Site ID
44320 Exercise Logger Applic. ID
44330 Exercise Entity ID
44340 Exercise Logger Active Status
44400 Synthetic Environment Manager Role
44410 Synthetic Environment Manager Site ID
44420 Synthetic Environment Manager Applic. ID
44430 Synthetic Environment Manager Entity ID
44440 Synthetic Environment Manager Active Status
44500 SIMNET-DIS Translator Role
44510 SIMNET-DIS Translator Site ID
44520 SIMNET-DIS Translator Applic. ID
44530 SIMNET-DIS Translator Entity ID
44540 SIMNET-DIS Translator Active Status
45000 Application Rate
45005 Application Time
45010 Application Timestep
45020 Feedback Time
45030 Simulation Rate
45040 Simulation Time
45050 Simulation Timestep
45060 Time Interval
45070 Time Latency
45080 Time Scheme
46000 Exercise Elapsed Time
46010 Elapsed Time"""
"""50000 Environment
50103 Scenario Date
50106 Time & Date Valid
50118 Scenario Time
50120 Snow Enable/Disable
50124 Weather Attributes Request
50126 MET Heartbeat Message
50600 Contrails Enable
50700 Contrail Altitudes
51000 Weather
51010 Weather Condition
51100 Thermal Condition
51110 Thermal Visibility
51111 Thermal Visibility
52000 Time
52001 Time
52100 Time of Day, Discrete
52200 Time of Day, Continuous
52300 Time Mode
52305 Time Scene
52310 Current Hour
52320 Current Minute
52330 Current Second
52340 Azimuth
52350 Maximum Elevation
52360 Time Zone
52370 Time Rate
52380 The number of simulation seconds since the start of the exercise (simulation
time)
52400 Time Sunrise Enabled
52410 Sunrise Hour
52420 Sunrise Minute
52430 Sunrise Second
52440 Sunrise Azimuth
52500 Time Sunset Enabled
52510 Sunset Hour
52511 Sunset Hour
52520 Sunset Minute
52530 Sunset Second
52600 Date
52601 Date (European)
52602 Date (US)
52610 Month
52620 Day
52630 Year
53000 Clouds
53050 Cloud Layer Enable
53060 Cloud Layer Selection
53100 Visibility
53200 Base Altitude
53250 Base Altitude
53300 Ceiling
53350 Ceiling
53400 Characteristics
53410 Concentration Length
53420 Transmittance
53430 Radiance
54000 Precipitation
54100 Rain
55000 Fog
55100 Visibility
55101 Visibility
55105 Visibility
55200 Density
55300 Base
55401 View Layer from above.
55410 Transition Range
55420 Bottom
55425 Bottom
55430 Ceiling
55435 Ceiling
56000 Heavenly Bodies
56100 Sun
56105 Sun Visible
56110 Position
56111 Sun Position Elevation, Degrees
56120 Position Azimuth
56121 Sun Position Azimuth, Degrees
56130 Position Elevation
56140 Position Intensity
56200 Moon
56205 Moon Visible
56210 Position
56220 Position Azimuth
56221 Moon Position Azimuth, Degrees
56230 Position Elevation
56231 Moon Position Elevation, Degrees
56240 Position Intensity
56310 Horizon
56320 Horizon Azimuth
56330 Horizon Elevation
56340 Horizon Heading
56350 Horizon Intensity
57200 Humidity
57300 Visibility
57400 Winds
57410 Speed
57411 Wind Speed, Knots
57420 Wind Direction
57421 Wind Direction, Degrees
57500 Rainsoak
57610 Tide Speed
57611 Tide Speed, Knots
57620 Tide Direction
57621 Tide Direction, Degrees
58000 Haze
58100 Visibility
58105 Visibility
58200 Density
58430 Ceiling
58435 Ceiling
59000 Contaminants and Obscurants
59100 Contaminant/Obscurant Type
59110 Persistence
59115 Chemical Dosage
59120 Chemical Air Concentration
59125 Chemical Ground Deposition
59130 Chemical Maximum Ground Deposition
59135 Chemical Dosage Threshold
59140 Biological Dosage
59145 Biological Air Concentration
59150 Biological Dosage Threshold
59155 Biological Binned Particle Count
59160 Radiological Dosage"""
"""60000 Communications
61005 Fire Bottle Reload
61100 Channel Type
61101 Channel Type
61200 Channel Identification
61300 Alpha Identification
61400 Radio Identification
61500 Land Line Identification
61600 Intercom Identification
61700 Group Network Channel Number
62100 Radio Communications Status
62101 Boom Interphone
62200 Stationary Radio Transmitters Default Time
62300 Moving Radio Transmitters Default Time
62400 Stationary Radio Signals Default Time
62500 Moving Radio Signal Default Time
63101 Radio Initialization Transec Security Key
63102 Radio Initialization Internal Noise Level
63103 Radio Initialization Squelch Threshold
63104 Radio Initialization Antenna Location
63105 Radio Initialization Antenna Pattern Type
63106 Radio Initialization Antenna Pattern Length
63107 Radio Initialization Beam Definition
63108 Radio Initialization Transmit Heartbeat Time
63109 Radio Initialization Transmit Distance Threshold Variable Record
63110 Radio Channel Initialization Lockout ID
63111 Radio Channel Initialization Hopset ID
63112 Radio Channel Initialization Preset Frequency
63113 Radio Channel Initialization Frequency Sync Time
63114 Radio Channel Initialization Comsec Key
63115 Radio Channel Initialization Alpha"""
"""70000 Algorithm Parameters
71000 Dead Reckoning Algorithm (DRA)
71100 DRA Location Threshold
71200 DRA Orientation Threshold
71300 DRA Time Threshold
72000 Simulation Management Parameters
72100 Checkpoint Interval
72600 Transmitter Time Threshold
72700 Receiver Time Threshold
73000 Interoperability Mode
74000 SIMNET Data Collection325
75000 Event ID
75100 Source Site ID
75200 Source Host ID"""
"""90000 Articulated Parts
90050 Part ID
90070 Index [UID 55]
90100 Position
90200 Position Rate
90300 Extension
90400 Extension Rate
90500 X
90600 X-rate
90700 Y
90800 Y-rate
90900 Z
91000 Z-rate
91100 Azimuth
91200 Azimuth Rate
91300 Elevation
91400 Elevation Rate
91500 Rotation
91600 Rotation Rate"""
"""100001 DRA Angular X-Velocity
100002 DRA Angular Y-Velocity
100003 DRA Angular Z-Velocity
100004 Appearance, Trailing Effects
100005 Appearance, Hatch
100008 Appearance, Character Set
100010 Capability, Ammunition Supplier
100011 Capability, Miscellaneous Supplier
100012 Capability, Repair Provider
100014 Articulation Parameter
100047 Articulation Parameter Type
100048 Articulation Parameter Value
100058 Time of Day-Scene
100061 Latitude-North (Location of weather cell)
100063 Longitude-East (Location of weather cell)
100068 Tactical Driver Status
100100 Sonar System Status
100160 Accomplished accept
100161 Upper latitude
100162 Latitude-South (Location of weather cell)
100163 Western longitude
100164 Longitude-West (location of weather cell)
100165 CD ROM Number (Disk ID for terrain)
100166 DTED disk ID
100167 Altitude
100169 Tactical System Status
100170 JTIDS Status
100171 TADIL-J Status
100172 DSDD Status
100200 Weapon System Status
100205 Subsystem status
100206 Number of interceptors fired
100207 Number of interceptor detonations
100208 Number of message buffers dropped
100213 Satellite sensor background (year, day)
100214 Satellite sensor background (hour, minute)
100218 Script Number
100300 Entity/Track/Update Data
100400 Local/Force Training
100500 Entity/Track Identity Data
100510 Entity for Track Event
100520 IFF (Friend-Foe) status
100600 Engagement Data
100610 Target Latitude
100620 Target Longitude
100631 Area of Interest (Ground Impact Circle) Center Latitude
100632 Area of Interest (Ground Impact Circle) Center Longitude
100633 Area of Interest (Ground Impact Circle) Radius
100634 Area of Interest Type
100640 Target Aggregate ID
100650 GIC Identification Number
100660 Estimated Time of Flight to TBM Impact
100661 Estimated Intercept Time
100662 Estimated Time of Flight to Next Waypoint
100700 Entity/Track Equipment Data
100800 Emission/EW Data
100900 Appearance Data"""
"""101000 Command/Order Data
101100 Environmental Data
101200 Significant Event Data
101300 Operator Action Data
101310 ADA Engagement Mode
101320 ADA Shooting Status
101321 ADA Mode
101330 ADA Radar Status
101340 Shoot Command
101350 ADA Weapon Status
101360 ADA Firing Disciple
101370 Order Status
101400 Time Synchronization
101500 Tomahawk Data
102100 Number of Detonations
102200 Number of Intercepts"""
"""200201 OBT Control MT-201
200202 Sensor Data MT-202
200203 Environmental Data MT-203
200204 Ownship Data MT-204
200205 Acoustic Contact Data MT-205
200207 Sonobuoy Data MT-207
200210 Sonobuoy Contact Data MT-210
200211 Helo Control MT-211
200213 ESM Control Data
200214 ESM Contact Data MT-214
200215 ESM Emitter Data MT-215
200216 Weapon Definition Data MT-217
200217 Weapon Preset Data MT-217
200301 OBT Control MT-301
200302 Sensor Data MT-302
200303 Environmental Data MT-303m
200304 Ownship Data MT-304
200305 Acoustic Contact Data MT-305
200307 Sonobuoy Data MT-307
200310 Sonobuoy Contact Data MT-310
200311 Helo Scenario / Equipment Status
200313 ESM Control Data MT-313
200314 ESM Contact Data MT-314
200315 ESM Emitter Data MT-315
200316 Weapon Definition Data MT-316
200317 Weapon Preset Data MT-317
200400 Pairing/Association (eMT-56)
200401 Pointer (eMT-57)
200402 Reporting Responsibility (eMT-58)
200403 Track Number (eMT-59)
200404 ID for Link-11 Reporting (eMT-60)
200405 Remote Track (eMT-62)
200406 Link-11 Error Rate (eMT-63)
200407 Track Quality (eMT-64)
200408 Gridlock (eMT-65)
200409 Kill (eMT-66)
200410 Track ID Change / Resolution (eMT-68)
200411 Weapons Status (eMT-69)
200412 Link-11 Operator (eMT-70)
200413 Force Training Transmit (eMT-71)
200414 Force Training Receive (eMT-72)
200415 Interceptor Amplification (eMT-75)
200416 Consumables (eMT-78)
200417 Link-11 Local Track Quality (eMT-95)
200418 DLRP (eMT-19)
200419 Force Order (eMT-52)
200420 Wilco / Cantco (eMT-53)
200421 EMC Bearing (eMT-54)
200422 Change Track Eligibility (eMT-55)
200423 Land Mass Reference Point
200424 System Reference Point
200425 PU Amplification
200426 Set/Drift
200427 Begin Initialization (MT-1)
200428 Status and Control (MT-3)
200429 Scintillation Change (MT-39)
200430 Link 11 ID Control (MT-61)
200431 PU Guard List
200432 Winds Aloft (MT-14)
200433 Surface Winds (MT-15)
200434 Sea State (MT-17)
200435 Magnetic Variation (MT-37)
200436 Track Eligibility (MT-29)
200437 Training Track Notification
200501 Tacan Data (MT-32)
200502 Interceptor Amplification (MT-75)
200503 Tacan Assignment (MT-76)
200504 Autopilot Status (MT-77)
200505 Consumables (MT-78)
200506 Downlink (MT-79)
200507 TIN Report (MT-80)
200508 Special Point Control (MT-81)
200509 Control Discretes (MT-82)
200510 Request Target Discretes(MT-83)
200511 Target Discretes (MT-84)
200512 Reply Discretes (MT-85)
200513 Command Maneuvers (MT-86)
200514 Target Data (MT-87)
200515 Target Pointer (MT-88)
200516 Intercept Data (MT-89)
200517 Decrement Missile Inventory (MT-90)
200518 Link-4A Alert (MT-91)
200519 Strike Control (MT-92)
200521 Speed Change (MT-25)
200522 Course Change (MT-26)
200523 Altitude Change (MT-27)
200524 ACLS AN/SPN-46 Status
200525 ACLS Aircraft Report
200600 SPS-67 Radar Operator Functions
200601 SPS-55 Radar Operator Functions
200602 SPQ-9A Radar Operator Functions
200603 SPS-49 Radar Operator Functions
200604 MK-23 Radar Operator Functions
200605 SPS-48 Radar Operator Functions
200606 SPS-40 Radar Operator Functions
200607 MK-95 Radar Operator Functions
200608 Kill/No Kill
200609 CMT pc
200610 CMC4AirGlobalData
200611 CMC4GlobalData
200612 LINKSIM_COMMENT_PDU
200613 NSST Ownship Control"""
"""240000 Other
240001 Mass Of The Vehicle
240002 Force ID
240003 Entity Type Kind
240004 Entity Type Domain
240005 Entity Type Country
240006 Entity Type Category
240007 Entity Type Sub Category
240008 Entity Type Specific
240009 Entity Type Extra
240010 Alternative Entity Type Kind
240011 Alternative Entity Type Domain
240012 Alternative Entity Type Country
240013 Alternative Entity Type Category
240014 Alternative Entity Type Sub Category
240015 Alternative Entity Type Specific
240016 Alternative Entity Type Extra
240017 Entity Location X
240018 Entity Location Y
240019 Entity Location Z
240020 Entity Linear Velocity X
240021 Entity Linear Velocity Y
240022 Entity Linear Velocity Z
240023 Entity Orientation Psi
240024 Entity Orientation Theta
240025 Entity Orientation Phi
240026 Dead Reckoning Algorithm
240027 Dead Reckoning Linear Acceleration X
240028 Dead Reckoning Linear Acceleration Y
240029 Dead Reckoning Linear Acceleration Z
240030 Dead Reckoning Angular Velocity X
240031 Dead Reckoning Angular Velocity Y
240032 Dead Reckoning Angular Velocity Z
240033 Entity Appearance
240034 Entity Marking Character Set
240035 Entity Marking 11 Bytes
240036 Capability
240037 Number Articulation Parameters
240038 Articulation Parameter ID
240039 Articulation Parameter Type
240040 Articulation Parameter Value
240041 Type Of Stores
240042 Quantity Of Stores
240043 Fuel Quantity
240044 Radar System Status
240045 Radio Communication System Status
240046 Default Time For Radio Transmission For Stationary Transmitters
240047 Default Time For Radio Transmission For Moving Transmitters
240048 Body Part Damaged Ratio
240049 Name Of The Terrain Database File
240050 Name Of Local File
240051 Aimpoint Bearing
240052 Aimpoint Elevation
240053 Aimpoint Range
240054 Air Speed
240055 Altitude
240056 Application Status
240057 Auto Iff
240058 Beacon Delay
240059 Bingo Fuel Setting
240060 Cloud Bottom
240061 Cloud Top
240062 Direction
240063 End Action
240064 Frequency
240065 Freeze
240066 Heading
240067 Identification
240068 Initial Point Data
240069 Latitude
240070 Lights
240071 Linear
240072 Longitude
240073 Low Altitude
240074 Mfd Formats
240075 Nctr
240076 Number Projectiles
240077 Operation Code
240078 Pitch
240079 Profiles
240080 Quantity
240081 Radar Modes
240082 Radar Search Volume
240083 Roll
240084 Rotation
240085 Scale Factor X
240086 Scale Factor Y
240087 Shields
240088 Steerpoint
240089 Spare1
240090 Spare2
240091 Team
240092 Text
240093 Time Of Day
240094 Trail Flag
240095 Trail Size
240096 Type Of Projectile
240097 Type Of Target
240098 Type Of Threat
240099 Uhf Frequency
240100 Utm Altitude
240101 Utm Latitude
240102 Utm Longitude
240103 Vhf Frequency
240104 Visibility Range
240105 Void Aaa Hit
240106 Void Collision
240107 Void Earth Hit
240108 Void Friendly
240109 Void Gun Hit
240110 Void Rocket Hit
240111 Void Sam Hit
240112 Weapon Data
240113 Weapon Type
240114 Weather
240115 Wind Direction
240116 Wind Speed
240117 Wing Station
240118 Yaw
240119 Memory Offset
240120 Memory Data
240121 VASI
240122 Beacon
240123 Strobe
240124 Culture
240125 Approach
240126 Runway End
240127 Obstruction
240128 Runway Edge
240129 Ramp Taxiway
240130 Laser Bomb Code
240131 Rack Type
240132 HUD
240133 RoleFileName
240134 PilotName
240135 PilotDesignation
240136 Model Type
240137 DIS Type
240138 Class
240139 Channel
240140 Entity Type
240141 Alternative Entity Type
240142 Entity Location
240143 Entity Linear Velocity
240144 Entity Orientation
240145 Dead Reckoning
240146 Failure Symptom
240147 Max Fuel
240148 Refueling Boom Connect
240149 Altitude AGL
240150 Calibrated Airspeed
240151 TACAN Channel
240152 TACAN Band
240153 TACAN Mode"""
"""270115 Fuel Flow Rate (kg/min)
270116 Fuel Temperature (degC)
270117 Fuel Pressure (Pa)
270150 SKE Slot
270151 SKE Lead
270152 SKE Frequency
270153 FCI Cmd
270154 FCI Num
270155 SKE Bit Field
270156 Formation Position
270157 Formation Number
270158 FFS Mode Active
270159 FFS Role
270160 FFS VCAS
270161 FFS Bit Field
270162 FFS Call Sign
270163 FFS Guidance Data
270164 FFS Text Data
270165 FFS Airdrop Request Data
270166 FFS Airdrop Data"""
"""300000 Horizontal Circular Error Probable (m)
300001 Horizontal Position Error (m)
300002 Vertical Position Error (m)
300003 Horizontal Velocity Error (m/s)
300004 Vertical Velocity Error (m/s)
300005 4th Lowest Jammer to Signal Ratio for P(Y)-L1 (dB)
300006 4th Lowest Jammer to Signal Ratio for P(Y)-L2 (dB)
300007 GPS Figure of Merit
300008 Weapon Transfer GPS State
300009 Weapon Transfer Horizontal Position Error (m)
300010 Weapon Transfer Vertical Position Error (m)
300011 Weapon Transfer Vertical Position Error (m)
300012 Weapon Transfer Horizontal Velocity Error (m/s)
300013 Time Transfer Error (sec)
300014 Age of Ephemeris (sec)
300016 Non-Flyout Munition Entity Request DIS Type Enumeration
300017 Non-Flyout Munition Entity Request Launch Point X (m)
300018 Non-Flyout Munition Entity Request Launch Point Y (m)
300019 Non-Flyout Munition Entity Request Launch Point Z (m)
300020 Non-Flyout Munition Entity Request Maximum Altitude (m MSL)
300021 Non-Flyout Munition Entity Request Flight Path
300022 Non-Flyout Munition Entity Request Impact Point X (m)
300023 Non-Flyout Munition Entity Request Impact Point Y (m)
300024 Non-Flyout Munition Entity Request Impact Point Z (m)
300025 Non-Flyout Munition Entity Request Elapsed Flight Time (sec)
300026 Non-Flyout Munition Entity Request Launch Time (sec)
300027 Time Error (sec)
301100 Link 16 Command Variety 1
301130 Push
301140 Rolex
301150 Terminate Intercept
301151 Heal Damage
301152 Destroy
301160 Transfer Control Management
301170 Link 16 Controls - PPLI Enable
301171 Link 16 Controls - Command & Control Enable
301174 Link 16 Reference Point Message Initiation
301175 Assign External Entity Link 16 Track Number
301176 Link 16 Intelligence Info
301177 Link 16 Track Management
301178 Link 16 Controls - CES Global PPLI Publish
301179 Link 16 Controls - CES Global Surveillance Publish
301180 Request Global Link 16 Configuration
301181 Link 16 Controls - Surveillance Enable
301182 Link 16 Pointer
301183 Link 16 Vector
301184 Link 16 Control Unit Change
301185 Link 16 Text
301186 Request Link 16 Objects
301187 Link 16 Ref Object Name List
301189 Total Number of PDUs in Link 16 Ref Objects Response
301190 PDU Number in Link 16 Ref Objects Response
301191 Total Number of Link 16 Ref Objects
301197 Link 16 Controls - F2F A Enable
301198 Link 16 Controls - F2F B Enable
301199 STN of Formation Leader
301200 Formation Name
301201 Formation Role
301202 Surveillance Contributor Sensor Based Detection
301220 F2F A NPG
301221 Link 16 Controls - F2F A Net
301222 F2F B NPG
301223 Link 16 Controls - F2F B Net
301224 Surveillance Enabled NPB
301225 Surveillance Enabled Net
301226 Control Unit Enabled
301227 Control Unit Enabled NPG
301228 Control Unit Enabled Net
301229 Voice Frequency
301234 Link 16 JTIDS Voice Callsign
301237 Entity ID of Control Unit
301238 STN of Control Unit
301239 NTR Participation Level
301240 Link 16 Controls - CES Global PPLI Subscribe
301241 Link 16 Controls - CES Global Surveillance Subscribe
301242 NTR in Mission
301243 NTR Marking
301244 NTR Receipt/Compliance
301255 Formation F2F NPG
301256 Formation F2F Channel"""
"""400008 JLVC (JSPA) LogReport
400009 JLVC (JSPA) SupplyAdjust
400010 JLVC (JSPA) EntityControl
400011 JLVC (JSPA) HealthUpdate
400012 JLVC (JSPA) RepairComplete
400013 JLVC (JSPA) UnitActivation
400014 JLVC (JSPA) BattleDamageRepair
400015 JLVC (JSPA) Minefield
400016 JLVC (JSPA) Wire
400017 JLVC (JSPA) Abatis
400018 JLVC (JSPA) Crater
400019 JLVC (JSPA) Ditch
400020 JLVC (JSPA) Lanes
400021 JLVC (JSPA) IED
400022 JLVC (JSPA) Rubble
400023 JLVC (JSPA) SubmergedBarrier
400024 JLVC (JSPA) FloatingBarrier
400025 JLVC (JSPA) Foxhole
400026 JLVC (JSPA) VehicleHole
400027 JLVC (JSPA) VehicleFortification
400028 JLVC (JSPA) Sandbag
400029 JLVC (JSPA) Checkpoint
400030 JLVC (JSPA) ContamCloud2D
400031 JLVC (JSPA) PopulationEffect
400032 JLVC (JSPA) Mine
400033 JLVC (JSPA) SeaMinefield"""
"""500001 Munition
500002 Engine Fuel
500003 Storage Fuel
500004 Not Used
500005 Expendable
500006 Total Record Sets
500007 Launched Munition
500008 Association
500009 Sensor
500010 Munition Reload
500011 Engine Fuel Reload
500012 Storage Fuel Reload
500013 Expendable Reload
500014 IFF Change Control - Mode 1 Code
500015 IFF Change Control - Mode 2 Code
500016 IFF Change Control - Mode 3 Code
500017 IFF Change Control - Mode 4 Code
500018 IFF Change Control - Mode 5 Code
500019 IFF Change Control - Mode 6 Code
500021 Link 16 Data
500022 ARM Alert
500023 IFF Change Control - Mode On/Off
500024 Weapon Status Data
500025 Expendable Status Data
500026 Tactic Status Data
500027 Emitter/Sensor Data
500028 IOS Control Data
500029 Static Status Data
500200 Request Inactive Entities
500201 Inactive Entity Quantity
500202 Inactive Entity ID
500203 Inactive Entity Type
500204 Activation Trigger Type
500205 Activation Trigger Value"""
"""551001 Air-to-Air Missile Qty
551002 AIM-7 Missile Qty
551003 AIM-9 Missile Qty
551004 AIM-120 Missile Qty
551005 Air-to-Ground Missile Qty
551006 Surface-to-Air Missile Qty
551007 Bullet Qty
552001 Chaff Qty
552002 Flare Qty
553001 Fuel Level
553002 Route Type
553003 Threat Mode
553004 Target Occluded
553005 Terrain Height
553006 Entity Status
553007 Marshal Status
553008 Power Plant Status
553009 Nav Light Status
553010 Interior Light Status
553011 Landing Light Status
553012 Formation Light Status
553013 Anti-Collision Light Status
553014 Nav/Formation Flash Rate
553015 Anti-Col. 'On' Duration
553016 Anti-Col. 'Off' Duration
553017 Intercept Status
553018 LifeForm Signaling Device Type
553019 LifeForm Movement Type
553020 LifeForm In Vehicle
553021 Mobility Kill
553022 Firepower Kill
553028 Tanker Enabled/Disabled
553029 Threat Status Tactic OK to Shoot Down Weapons
554001 TACAN Channel
554002 TACAN Band
554003 TACAN Mode
554004 RWR Status
554005 UHF Radio Frequency
554006 Emit Jamming Status
554007 Emit Jamming Type
554008 Receive Jamming Status
554009 RADAR Mode
554010 Available RADAR Modes
554100 Jammer Pod Enumeration
554101 Jammer Pod Behavior
554102 Jammer Pod Programs
554103 Jammer Pod Receiver Sensitivity
554104 Jammer Pod Receiver Frequency Minimum
554105 Jammer Pod Receiver Frequency Maximum
554106 Jammer Pod Power
554107 Jammer Pod Variability
554108 Jammer Pod Number of False Targets
554109 Jammer Pod Jammer Knob
554110 Jammer Pod Missile Jamming
555001 Emitter Override
555002 Jammer Override
555003 Disengage / Reengage
555004 Heading Override
555005 Altitude Override
555006 Speed Override
555007 Verbose Override
555008 Occlusion Override
556001 Commit Range
556007 Current Scenario IFF Mode 4A Code for This Threat's Affiliation
556008 Current Scenario IFF Mode 4B Code for This Threat's Affiliation
556016 Ok to Engage Waypoint Number
556017 Max Speed at Sea Level
556018 Max Speed
556019 Current Waypoint Number
556020 Route Information
556029 Threat Status Static Multi Target Track
557001 Air-Air IR Missile Qty
557002 Air-Air Radar Missile Qty
557003 Air-Ground IR Missile Qty
557004 Air-Ground Radar Missile Qty
557005 Air-Ground Anti-Radiation Missile Qty
557006 Air-Ground Bomb Qty
557007 Air-Ground Rocket Qty
557008 Surface-Air IR Missile Qty
557009 Surface-Air Radar Missile Qty
557010 Bullet Qty
559001 PPLI Publish Enabled
559002 Surveillance PublishEnabled
559003 NPG
559004 NPG Channel
559005 JTIDS Track Number
559006 Link 16 Controls - Surveillance Reportable
559007 Link 16 Controls - Surveillance Track Quality
559008 Link 16 Controls - Target Position Quality
559009 Link 16 Controls - Quality Error Type
559010 Link 16 Controls - Affiliation Determination Rule
559011 Link 16 Controls - Reset Entity Affiliation
559012 Link 16 Controls - Reset All Affiliation
559999 End of Messages"""
"""600001 Malfunction Activate/Deactivate Set
600002 Malfunction Status
600210 Request JTIDS Track Numbers
600212 Track Numbers vs EID
600214 Total Number of JTIDS Track Numbers
600215 PDU Number in JTIDS Track Number Response
600216 Total Number of PDUs in JTIDS Track Number Response
600218 Air to Air Refueler Entities Request
600219 Air to Air Refueling Count
600220 Air To Air Refueler Entity
600300 Formation Library Request
600301 Total Number Formation Library PDUs
600302 PDU Number in Formation Library Response
600303 Total Number Formation Library Items in PDU
600304 Formation Library Variable
600305 Create Runtime Formation
600306 Formation Request Header
600307 Formation Position Absolute
600308 Formation Position Relative
610006 Expendables Reload
610007 Position Freeze
610008 Activate Ownship
610009 Chocks
610010 Warm-up Cool-down Override
610011 Ground Power
610012 Scramble Start
610013 Ownship as a Threat
610015 Fuel External
610016 Fuel Internal
610017 Fuel Tank Temp
610025 Gross Weight
610026 Angle Of Attack
610027 G Load
610029 Weight On Wheels
610032 Stored Energy System Reload
610035 Kill Override
610036 Expendables Freeze
610037 GPS Satellites Enable/Disable
610040 Ownship Message Display
610042 Weapon Quantity Freeze
610043 Global Control - Freeze Weapons Quantity On All Ownships
610044 Global Control - Freeze Fuel Quantity On All Ownships
610045 Global Control - Freeze Kill Override On All Ownships
610046 Global Control - Freeze Crash Override On All Ownships
610047 Ownship OFP Block Number
610048 Waypoint Information Query
610049 Waypoint Information
610050 Ownship Subsystem Status Data"""
"""613002 Cockpit Switch Status
613003 Integrated Control Panel Messages
613004 Throttle Positions
613005 Current Critical Switch Position
613006 Correct Critical Switch Position
613007 Current Critical Switch Data
613008 Correct Critical Switch Data
613013 Mission Initial Conditions Set
613016 Global Control - Malfunction Active on All Ownships
613017 Global Control - Malfunction Clear On All Ownships
613020 Validated Critical Switch Report
613021 SAR Map Pathname
613022 Validated Critical Switch Ownship ID
613027 Lower Boom Event Report
613028 Raise Boom Event Report
613029 Breakaway Event Report
613030 Complete Event Report
613031 Aux Comm Panel Frequency Display
615000 Network Station Information
615001 Global Control Select Network Station
615002 Network Station Under Global Control
615003 Global Control Still Controlling
615004 Global Control Release Control of Network Station
615005 Global Control Freeze Weapon Quantity
615006 Global Control Freeze Fuel Quantity
615007 Global Control Freeze Kill Override
615008 Global Control Freeze Crash Override
615009 Global Control Malfunction Active
615010 Global Control Malfunction Clear
615011 Global Control Start Devices
615012 Global Control Freeze Devices
615013 Global Control JTIDS Command
615015 Network Station IC Set Information
615017 Global Control Reset IC Set
615018 Number of Controlling Units
615019 Network Station JTIDS Controlling Units
615020 Network Station JTIDS Objective Tracks
615021 Number of Reference Objects
615022 Network Station JTIDS Reference Objects
615023 Networked Station Still Under Control
615024 Global Control Delete Threat Entities
615025 Network Station Ownship Callsigns
615026 Global Control Request Formation Library Data
615027 Total Number Formation Library PDUs
615028 PDU Number in Formation Library Response
615029 Total Number Formation Library Items in PDUs
615030 Network Station Formation Library Item
615031 Global Control Add Relative Formation
615032 Network Station TIC Filename
615033 Global Control Freeze Warm-up Override
615034 Global Control Reload SES
615035 Global Control Reload Weapons
615036 Global Control Reload Expendables
615037 Global Control Reload Fuel
615038 Global Control Reload Firebottle
700000 Test Pattern (DORT)
700001 Audio Test (DORT)
700002 Audio Tone (DORT)
700003 Calibrate Throttles (DORT)
700004 Operational Limits Event Report
700005 Operational Limits"""
"""1000620 Event Marker Message
2000000 Receiver Aircraft Aero Model Data
2000010 Tanker Aircraft Aero Model Data
2000020 Boom Aircraft Aero Model Data
2000030 Access to Image Generator Data
2000040 Host Load Numbers
5005001 Extended Fire Event Reports
5005002 Battle Damage Assessment (BDA) Event Report
5005003 Extended Fire Event Launcher
5005006 Extended Fire Event Missile
5005008 Extended Fire Event MRM Weapon
5005009 Extended Fire Event Gun Fire Control
5005010 Extended Fire Event Bomb
5005011 Extended Fire Event Expendable
5005012 Battle Damage Assessment
5005014 Extended Fire Pickle Event
5005055 Radar Track Report
5005060 Jammer Report
5005061 Jammer False Targets Report
5005063 Detect Event Report
5005070 MALD Beam Report
5005080 Transmitter Radiation Volume (deprecated)
5005081 Transmitter Radiation Volume v2
5007010 Physical Network Definition
5007020 Network Channel Definition
5007030 Logical Network Definition
5007040 Logical Network - Entity Definition
5007050 Physical Network - Entity Definition
5008010 C2 Message
5008020 Candidate Object
5008030 Set of Candidate Objects
5008040 Bounded Region
5008050 Angular Region
5008060 RoE Object
5008070 Track Object
5008080 Set of Track Objects
5009010 Logical Entity Definition
5009020 Logical Entity Relationship Definition
5507010 Intent-Based EW Message"""
