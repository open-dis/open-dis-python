"""emission.py

9 Emissions
"""
import enum


# [UID 76]
class EmitterSystemFunction(enum.IntEnum):
    """9.1 Emitter System Function [UID 76]"""
    OTHER = 0
    MULTI_FUNCTION = 1
    EARLY_WARNING_SURVEILLANCE = 2
    HEIGHT_FINDER = 3
    FIRE_CONTROL = 4
    ACQUISITION_DETECTION = 5
    TRACKER = 6
    GUIDANCE_ILLUMINATION = 7
    FIRE_POINT_LAUNCH_POINT_LOCATION = 8
    RANGE_ONLY = 9
    RADAR_ALTIMETER = 10
    IMAGING = 11
    MOTION_DETECTION = 12
    NAVIGATION = 13
    WEATHER_METEOLOGICAL = 14
    INSTRUMENTATION = 15
    IDENTIFICATION_CLASSIFICATION_INCLUDING_IFF = 16
    AAA_FIRE_CONTROL = 17
    AIR_SEARCH_BOMB = 18
    AIR_INTERCEPT = 19
    ALTIMETER = 20
    AIR_MAPPING = 21
    AIR_TRAFFIC_CONTROL = 22
    BEACON = 23
    BATTLEFIELD_SURVEILLANCE = 24
    GROUND_CONTROL_APPROACH = 25
    GROUND_CONTROL_INTERCEPT = 26
    COASTAL_SURVEILLANCE = 27
    DECOY_MIMIC = 28
    DATA_TRANSMISSION = 29
    EARTH_SURVEILLANCE = 30
    GUN_LAY_BEACON = 31
    GROUND_MAPPING = 32
    HARBOR_SURVEILLANCE = 33
    IFF = 34  # Deprecated
    ILS = 35  # Deprecated
    IONOSPHERIC_SOUND = 36
    INTERROGATOR = 37
    BARRAGE_JAMMING = 38  # Deprecated
    CLICK_JAMMING = 39  # Deprecated
    DECEPTIVE_JAMMING = 40  # Deprecated
    FREQUENCY_SWEPT_JAMMING = 41  # Deprecated
    JAMMER = 42  # Deprecated
    NOISE_JAMMING = 43  # Deprecated
    PULSED_JAMMING = 44  # Deprecated
    REPEATER_JAMMING = 45  # Deprecated
    SPOT_NOISE_JAMMING = 46  # Deprecated
    MISSILE_ACQUISITION = 47
    MISSILE_DOWNLINK = 48
    METEROLOGICAL = 49  # Deprecated
    SPACE = 50
    SURFACE_SEARCH = 51
    SHELL_TRACKING = 52
    TELEVISION = 56
    UNKNOWN = 57
    VIDEO_REMOTING = 58
    EXPERIMENTAL_OR_TRAINING = 59
    MISSILE_GUIDANCE = 60
    MISSILE_HOMING = 61
    MISSILE_TRACKING = 62
    JAMMING_NOISE = 63  # Deprecated
    JAMMING_DECEPTION = 64  # Deprecated
    DECOY = 66  # Deprecated
    NAVIGATION_DISTANCE_MEASURING_EQUIPMENT = 71
    TERRAIN_FOLLOWING = 72
    WEATHER_AVOIDANCE = 73
    PROXIMITY_FUSE = 74
    INSTRUMENTATION_DEPRECATED = 75  # Deprecated
    RADIOSONDE = 76
    SONOBUOY = 77
    BATHYTHERMAL_SENSOR = 78
    TOWED_COUNTER_MEASURE = 79
    DIPPING_SONAR = 80
    TOWED_ACOUSTIC_SENSOR = 81
    WEAPON_NON_LETHAL = 96
    WEAPON_LETHAL = 97
    TEST_EQUIPMENT = 98
    ACQUISITION_TRACK = 99
    TRACK_GUIDANCE = 100
    GUIDANCE_ILLUMINATION_TRACK_ACQUISITION = 101
    SEARCH_ACQUISITION = 102
    DROPSONDE = 103


# [UID 77]
class StateUpdateIndicator(enum.IntEnum):
    """9.2 State Update Indicator [UID 77]"""
    HEARTBEAT_UPDATE = 0
    CHANGED_DATA_UPDATE = 1


# [UID 78]
class BeamFunction(enum.IntEnum):
    """9.3 Beam Function [UID 78]"""
    OTHER = 0
    SEARCH = 1
    HEIGHT_FINDING = 2
    ACQUISITION = 3
    TRACKING = 4
    ACQUISITION_AND_TRACKING = 5
    COMMAND_GUIDANCE = 6
    ILLUMINATION = 7
    RANGING = 8
    MISSILE_BEACON = 9
    MISSILE_FUSING = 10
    ACTIVE_RADAR_MISSILE_SEEKER = 11
    JAMMING = 12
    IFF = 13
    NAVIGATION_WEATHER = 14
    METEROLOGICAL = 15
    DATA_TRANSMISSION = 16
    NAVIGATION_DIRECTIONAL_BEACON = 17
    TIME_SHARED_SEARCH = 20
    TIME_SHARED_ACQUISITION = 21
    TIME_SHARED_TRACK = 22
    TIME_SHARED_COMMAND_GUIDANCE = 23
    TIME_SHARED_ILLUMINATION = 24
    TIME_SHARED_JAMMING = 25


# [UID 79]
class HighDensityTrackJam(enum.IntEnum):
    """9.4 High Density Track/Jam [UID 79]"""
    NOT_SELECTED = 0
    SELECTED = 1


# [UID 318]
class BeamState(enum.IntEnum):
    """9.5 Beam State [UID 318]"""
    ACTIVE = 0
    DEACTIVATED = 1


"""9.6 Jamming Technique [UID 284]
1 ...................................... Noise
1.5 Amplitude Modulation (AM) Noise
1.10 Barrage Noise
1.10.5 Click
1.10.10 Source Noise
1.15 Bistatic Clutter
1.20 Comb
1.25 Cooperative Blinked Noise (CBN)
1.30 Doppler Noise
1.35 Frequency Modulation (FM) by Noise
1.40 Impulse Noise
1.45 Partial Band
1.50 Pseudorandom AM
1.55 Pulse Noise
1.60 Quasi-Noise (aka Pseudorandom)
1.65 Range Bin Masking (RBM) (aka Cover Pulse)
1.65.5 Range Bin Masking with Velocity Bin Masking
1.70 Repeater Noise
1.70.5 Narrowband Repeater Noise
1.70.10 Wide Band Repeater Noise
1.75 Spot Noise
1.75.5 Automatic Spot Noise (ASJ)
1.75.10 Blinking Spot Noise
1.75.15 Burst Spot Noise
1.75.20 Doppler Spot Noise
1.75.25 Skirt Frequency
1.80 Swept Noise (aka Swept Spot Noise, Sweep)
1.80.5 Frequency Swept
1.80.10 Swept AM
1.85 Velocity Bin Masking (VBM)
2 ...................................... Deception
2.5 Analyzer
2.10 Angle
2.10.5 Angle Gate Walk-Off
2.10.10 Cooperative Angle (CAJ)
2.10.15 Cross-Eye
2.10.20 Cross-Polarization
2.10.25 Delta
2.10.30 Inverse Gain (aka Inverse Amplitude)
2.10.35 Sea-Bounced
2.10.40 Swept Square Wave (SSW)
2.10.45 Terrain Bounce
2.15 Angle and Gate Stealer
2.15.5 Cross-Polarization and Range Gate Pull-Off (RGPO)
2.15.10 Cross-Polarization and Velocity Gate Pull-Off (VGPO)
2.15.15 Cross-Polarization, RGPO and VGPO
2.15.20 Inverse Gain and RGPO
2.15.25 Inverse Gain and RGPO and VGPO
2.15.30 Inverse Gain and VGPO
2.15.35 RGPO and SSW
2.15.40 SSW and VGPO
2.20 Angle and False Target
2.20.5 Angle and Velocity False Targets (VFT)
2.20.5.5 Inverse Gain and VFT
2.20.5.10 SSW and VFT
2.20.10 Range False Targets (RFT) and Inverse Gain
2.20.15 RFT and SSW
2.25 Angle and Random Range Programs (RANRAP)
2.25.5 RANRAP and SSW
2.30 Angle and Velocity
2.30.5 Inverse Gain and VBM
2.30.10 SSW and VBM
2.35 Automatic Gain Control (AGC)
2.40 AGC and Gate Stealer
2.40.5 AGC and RGPO
2.40.10 AGC and VGPO
2.40.15 AGC and RGPO and VGPO
2.45 Colinear
2.50 Constant False Alarm Rate
2.55 Double Cross
2.60 Down Link
2.65 False Target
2.65.5 Coherent False Targets
2.65.10 False Doppler Target (FDT)
2.65.15 Multiple False Targets
2.65.20 Range False Targets (RFT)
2.65.25 Transponder
2.65.30 Velocity False Targets (VFT)
2.70 Figure Eight
2.75 Gate Stealer
2.75.5 Chirp Gate Stealer (CGS)
2.75.10 Range Gate Pull-Off (RGPO)
2.75.15 RGPO and VGPO
2.75.20 VGPO (aka Velocity Gate Stealer, VGS)
2.80 Gate Stealer and Repeater
2.80.5 Repeater Swept Amplitude Modulation (RSAM) and VGPO
2.85 Glint Enhance
2.90 Image Frequency
2.95 Jittered Pulse Repetition Frequency
2.100 Jittered Pulse Width
2.105 Pseudorandom Noise (PRN)
2.110 Pulse
2.115 Pulse Compression Deception
2.120 Random Range Programs (RANRAP)
2.125 Refraction
2.130 Repeater
2.130.5 Continuous Wave Repeater
2.130.10 Repeater Noise
2.130.15 Multiple Frequency Repeater (MFR)
2.130.20 Narrow Band Repeater Noise (NBRN)
2.130.25 Random Doppler (RD)
2.130.30 Repeater Digital Radio Frequency Memory (DRFM)
2.130.30.1 DRFM Level A
2.130.30.2 DRFM Level B
2.130.30.3 DRFM Level C
2.130.30.4 DRFM Level D
2.130.30.5 DRFM Level E
2.130.35 Repeater Swept Amplitude Modulation (RSAM)
2.135 Scintillation
2.140 Serrodyne
2.145 Velocity
3 ...................................... Deception and Noise
3.5 Angle and Noise
3.5.5 Angle and Barrage
3.5.5.5 Barrage and Inverse Gain
3.5.5.10 Barrage and SSW
3.10 Angle and FM by Noise
3.10.5 FM by Noise and Inverse Gain
3.10.10 FM by Noise and SSW
3.15 Angle and Pseudorandom AM
3.15.5 Inverse Gain and Pseudorandom AM
3.15.10 Pseudorandom AM and SSW
3.20 Angle and Spot
3.20.5 Inverse Gain and Low Level Noise
3.20.10 Inverse Gain and Spot Noise
3.20.15 Spot and SSW
3.25 Gate Stealer and Noise
3.25.5 Noise and RGPO
3.25.5.5 Low Level Noise and RGPO
3.25.10 Noise and VGPO
3.25.10.5 Low Level Noise and VGPO
3.30 False Target Deception and Swept Noise
4 ...................................... Special
4.1 Super Jam"""
# TODO


# [UID 300]
class EEAttributeStateIndicator(enum.IntEnum):
    """9.7 EE Attribute State Indicator [UID 300]"""
    HEARTBEAT_UPDATE = 0
    CHANGED_DATA_UPDATE = 1
    HAS_CEASED = 2
