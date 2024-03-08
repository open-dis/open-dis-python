"""civilian.air.py"""
import enum


"""5.2.5 Civilian Air Subcategories"""

# [UID 274]
"""5.2.5.1 Ultralight Non-rigid Wing Aircraft [UID 274]46
Value Description
1 Hang Glider, Unpowered
2 Hang Glider, Powered
3 Paraglider, Unpowered
4 Paraglider, Powered
5 Powered Parachute"""
class UltralightNonRigidWingAircraft(enum.IntEnum): ...


# [UID 275]
"""5.2.5.2 Ultralight Rigid Wing Aircraft [UID 275]47
Value Description
1 Weight-shift control
2 Control surface (elevator, rudder, aileron) control"""
class UltralightRigidWingAircraft(enum.IntEnum): ...


# [UID 276]
"""5.2.5.3 Glider [UID 276]48
Value Description
1 Sail Plane
2 Motor Glider"""
class Glider(enum.IntEnum): ...


# [UID 277]
"""5.2.5.4 Fixed Wing Aircraft [UID 277]49
Value Description
11 Single Piston Engine
12 Twin Piston Engine
21 Single Engine Turboprop
22 Twin Engine Turboprop
24 Four Engine Turboprop
32 Twin Jet
33 Tri Jet
34 Four Engine Jet"""
class FixedWingAircraft(enum.IntEnum): ...


# [UID 278]
"""5.2.5.5 Helicopter (Rotary Wing Aircraft) [UID 278]50
Value Description
11 Single Rotor, Piston Engine
12 Single Rotor, Turboshaft Engine, Conventional Tail Rotor
13 Single Rotor, Turboshaft Engine, Shrouded Tail Rotor
14 Single Rotor, Turboshaft Engine, No Tail Rotor
21 Tandem Rotor
22 Coaxial Rotor
23 Intermeshing Rotor"""
class Helicopter(enum.IntEnum): ...


# [UID 279]
"""5.2.5.6 Lighter than Air, Balloon [UID 279]51
Value Description
1 Gas-filled, free
2 Gas-filled, tethered
3 Hot Air
4 Roziere Balloon
5 Helikite"""
class Balloon(enum.IntEnum): ...


# [UID 280]
"""5.2.5.7 Lighter than Air, Airship [UID 280]52
Value Description
1 Non-rigid (blimp)
2 Semi-rigid
3 Rigid
4 Hybrid"""
class Airship(enum.IntEnum): ...


