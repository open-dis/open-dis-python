"""radiocomm.py

8 Radio Communications"""
import enum


"""8.1 Transmitter and Receiver"""

"""8.1.1 Modulation Type"""

# [UID 155]
class MajorModulation(enum.IntEnum):
    """8.1.1.1 Major Modulation [UID 155]"""
    NO_STATEMENT = 0
    AMPLITUDE = 1  # [UID 156]
    AMPLITUDE_AND_ANGLE = 2  # [UID 157]
    ANGLE = 3  # [UID 158]
    COMBINATION = 4  # [UID 159]
    PULSE = 5  # [UID 160]
    UNMODULATED = 6  # [UID 161]
    CARRIER_PHASE_SHIFT_MODULATION = 7  # [UID 162]
    SATCOM = 8  # [UID 589]


"""8.1.1.2 Detail
The enumerations for this field depend upon the value of the Major Modulation field [UID 155].
"""

# [UID 156]
class AmplitudeModulation(enum.IntEnum):
    """8.1.1.2.1 Amplitude Modulation [UID 156]"""
    OTHER = 0
    AFSK = 1  # (Audio Frequency Shift Keying)
    AM = 2  # (Amplitude Modulation)
    CW = 3  # (Continuous Wave Modulation)
    DSB = 4  # (Double Sideband)
    ISB = 5  # (Independent Sideband)
    LSB = 6  # (Single Band Suppressed Carrier, Lower Sideband Mode)
    SSB_FULL = 7  # (Single Sideband Full Carrier)
    SSB_REDUC = 8  # (Single Band Reduced Carrier)
    USB = 9  # (Single Band Suppressed Carrier, Upper Sideband Mode)
    VSB = 10  # (Vestigial Sideband)


# [UID 157]
class AmplitudeAndAngleModulation(enum.IntEnum):
    """8.1.1.2.2 Amplitude and Angle Modulation [UID 157]"""
    OTHER = 0
    AMPLITUDE_AND_ANGLE = 1


# [UID 158]
class AngleModulation(enum.IntEnum):
    """8.1.1.2.3 Angle Modulation [UID 158]"""
    OTHER = 0
    FM = 1  # (Frequency Modulation)
    FSK = 2  # (Frequency Shift Keying)
    PM = 3  # (Phase Modulation)
    MSK = 4  # (Minimum Shift Keying)


class CombinationModulation(enum.IntEnum):
    """8.1.1.2.4 Combination Modulation [UID 159]"""
    OTHER = 0
    AMPLITUDE_ANGLE_PULSE = 1


# [UID 160]
class PulseModulation(enum.IntEnum):
    """8.1.1.2.5 Pulse Modulation [UID 160]"""
    OTHER = 0
    PULSE = 1
    X_BAND_TACAN_PULSE = 2
    Y_BAND_TACAN_PULSE = 3


# [UID 161]
class UnmodulatedModulation(enum.IntEnum):
    """8.1.1.2.6 Unmodulated Modulation [UID 161]"""
    OTHER = 0
    CONTINUOUS_WAVE_EMISSION_OF_AN_UNMODULATED_CARRIER = 1


# [UID 162]
class CarrierPhaseShiftModulation(enum.IntEnum):
    """8.1.1.2.7 Carrier Phase Shift Modulation [UID 162]"""
    OTHER = 0


# [UID 589]
class SATCOMModulation(enum.IntEnum):
    """8.1.1.2.8 SATCOM Modulation [UID 589]"""
    OTHER = 0
    NO_DELAY = 1


# [UID 163]
class RadioSystem(enum.IntEnum):
    """8.1.1.3 Radio System [UID 163]"""
    OTHER = 0
    GENERIC_RADIO_OR_SIMPLE_INTERCOM = 1
    HAVE_QUICK_I = 2
    HAVE_QUICK_II = 3
    SATURN295 = 4
    SINCGARS = 5
    CCTT_SINCGARS = 6
    EPLRS = 7  # (Enhanced Position Location Reporting System)
    JTIDS_MIDS296 = 8
    LINK_11297 = 9
    LINK_11B298 = 10
    L_BAND_SATCOM = 11
    ENHANCED_SINCGARS_7_3 = 12
    NAVIGATION_AID = 13


# [UID 164]
class TransmitState(enum.IntEnum):
    """8.1.2 Transmit State [UID 164]"""
    OFF = 0
    ON_NOT_TRANSMITTING = 1
    ON_TRANSMITTING = 2


# [UID 165]
class InputSource(enum.IntEnum):
    """8.1.3 Input Source [UID 165]"""
    OTHER = 0
    PILOT = 1
    COPPILOT = 2
    FIRST_OFFICER = 3
    DRIVER = 4
    LOADER = 5
    GUNNER = 6
    COMMANDER = 7
    DIGITAL_DATA_DEVICE = 8
    INTERCOM = 9
    AUDIO_JAMMER = 10
    DATA_JAMMER = 11
    GPS_JAMMER = 12
    GPS_MEACONER = 13
    SATCOM_UPLINK_JAMMER = 14


# [UID 166]
class CryptoSystem(enum.IntEnum):
    """8.1.4 Crypto System [UID 166]"""
    NO_ENCRYPTION = 0
    KY_28 = 1
    KY_58 = 2
    NARROW_SPECTRUM_SECURE_VOICE = 3
    WIDE_SPECTRUM_SECURE_VOICE = 4
    SINCGARS_ICOM = 5
    KY_75 = 6
    KY_100 = 7
    KY_57 = 8
    KYV_5 = 9
    LINK_11_KG_40A_P = 10
    LINK_11B_KG_40A_S = 11
    LINK_11_KG_40AR = 12
    KGV_135A = 13


# [UID 449]
class CryptoMode(enum.IntEnum):
    """8.1.5 Crypto Mode [UID 449]"""
    BASEBAND = 0
    DIPHASE = 1


# [UID 167]
class AntennaPatternType(enum.IntEnum):
    """8.1.6 Antenna Pattern Type [UID 167]"""
    ISOTROPIC = 0  # (Spherical Radiation Pattern)
    BEAM = 1
    SPHERICAL_HARMONIC = 2  # Deprecated
    TRANSMITTER_RADIATION_VOLUME = 4
    BEAM_AND_TRANSMITTER_RADIATION_VOLUME = 5
    OMNIDIRECTIONAL = 6  # (Toroidal Radiation Pattern)


# [UID 168]
class BeamAntennaPatternReferenceSystem(enum.IntEnum):
    """8.1.7 Beam Antenna Pattern Reference System [UID 168]"""
    WORLD_COORDINATES = 1
    ENTITY_COORDINATES = 2


"""8.1.8 CCTT SINCGARS Modulation Parameters"""

# [UID 170]
class CCTTStartOfMessage(enum.IntEnum):
    """8.1.8.1 Start of Message [UID 170]"""
    NOT_START_OF_MESSAGE = 0
    START_OF_MESSAGE = 1


# [UID 171]
class ClearChannel(enum.IntEnum):
    """8.1.8.2 Clear Channel [UID 171]"""
    NOT_CLEAR_CHANNEL = 0
    CLEAR_CHANNEL = 1


"""8.1.9 High Fidelity HAVE QUICK/SATURN Transmitter Parameters"""
# NOTE: SATURN was formerly HAVE QUICK IIA (HQIIA)

# [UID 297]
class TODTransmitIndicator(enum.IntEnum):
    """8.1.9.1 TOD Transmit Indicator [UID 297]"""
    NOT_TOD_TRANSMITTED = 0
    TOD_TRANSMITTED = 1


# [UID 298]
class NETIDMode(enum.IntEnum):
    """8.1.9.2 NET ID Mode [UID 298]"""
    HAVE_QUICK_I_HAVE_QUICK_II_COMBAT = 1  # A
    SATURN_COMBAT300 = 2                   # B
    TRAINING = 3                           # T


# [UID 299]
class NETIDFrequencyTable(enum.IntEnum):
    """8.1.9.3 NET ID Frequency Table [UID 299]"""
    HQ_I_OPERATIONS = 0
    HQII_NATO_EUROPE_AREA_OPERATIONS = 1
    HQII_NON_NATO_EUROPE_AREA_OPERATIONS = 2
    SATURN_OPERATIONS = 3


# [UID 179]
class ReceiverState(enum.IntEnum):
    """8.1.10 Receiver State [UID 179]"""
    OFF = 0
    ON_NOT_RECEIVING = 1
    ON_RECEIVING = 2


# [UID 306]
class RadioAttachedIndicator(enum.IntEnum):
    """8.1.11 Radio Attached Indicator (RAI) [UID 306]"""
    NO_STATEMENT = 0
    UNATTACHED = 1
    ATTACHED = 2


"""8.2 Signal"""

"""8.2.1 Encoding Scheme"""

# [UID 270]
class EncodingClass(enum.IntEnum):
    """8.2.1.1 Encoding Class [UID 270]"""
    ENCODED_AUDIO = 0
    RAW_BINARY_DATA = 1
    APPLICATION_SPECIFIC_DATA = 2
    DATABASE_INDEX = 3


# [UID 271]
class EncodingType(enum.IntEnum):
    """8.2.1.2 Encoding Type [UID 271]"""
    _8_BIT_MU_LAW = 1  # (ITU-T G.711)
    CVSD = 2  # (MIL-STD-188-113)
    ADPCM = 3  # (ITU-T G.726)
    _16_BIT_LINEAR_PCM_2S_COMPLEMENT_BIG_ENDIAN = 4
    _8_BIT_LINEAR_PCM_UNSIGNED = 5
    VQ = 6  # Deprecated
    _UNAVAILABLE_FOR_USE_1 = 7
    GSM_FULL_RATE = 8  # (ETSI 06.10)
    GSM_HALF_RATE = 9  # (ETSI 06.20)
    SPEEX_NARROW_BAND = 10
    OPUS = 11
    LPC_10 = 12  # (FIPS PUB 137)
    _16_BIT_LINEAR_PCM_2S_COMPLEMENT_LITTLE_ENDIAN = 100
    _UNAVAILABLE_FOR_USE_2 = 255


# [UID 178]
class TDLType(enum.IntEnum):
    """8.2.1.3 TDL Type [UID 178]"""
    OTHER = 0
    PADIL = 1
    NATO_LINK_1 = 2
    ATDL_1 = 3
    LINK_11B = 4  # (TADIL B)
    SITUATIONAL_AWARENESS_DATA_LINK = 5
    JTIDS_TADIL_J = 6  # Link 16 Legacy Format
    JTIDS_FDL_TADIL_J = 7  # Link 16 Legacy Format
    LINK_11 = 8  # (TADIL A)
    IJMS = 9
    LINK_4A = 10  # (TADIL C)
    LINK_4C = 11
    TIBS = 12
    ATL = 13
    CONSTANT_SOURCE = 14
    ABBREVIATED_COMMAND_AND_CONTROL = 15
    MILSTAR = 16
    ATHS = 17
    OTHGOLD = 18
    TACELINT = 19
    WEAPONS_DATA_LINK = 20  # (AWW-13)
    ABBREVIATED_COMMAND_AND_CONTROL_DEPRECATED = 21
    ENHANCED_POSITION_LOCATION_REPORTING_SYSTEM = 22
    POSITION_LOCATION_REPORTING_SYSTEM = 23
    SINCGARS = 24
    HAVE_QUICK_I = 25
    HAVE_QUICK_II = 26
    SATURN305 = 27
    INTRA_FLIGHT_DATA_LINK_1 = 28
    INTRA_FLIGHT_DATA_LINK_2 = 29
    IMPROVED_DATA_MODEM = 30
    AIR_FORCE_APPLICATION_PROGRAM_DEVELOPMENT = 31
    COOPERATIVE_ENGAGEMENT_CAPABILITY = 32
    FORWARD_AREA_AIR_DEFENSE_DATA_LINK = 33
    GROUND_BASED_DATA_LINK = 34
    INTRA_VEHICULAR_INFO_SYSTEM = 35
    MARINE_TACTICAL_SYSTEM = 36
    TACTICAL_FIRE_DIRECTION_SYSTEM = 37
    INTEGRATED_BROADCAST_SERVICE = 38
    AIRBORNE_INFORMATION_TRANSFER = 39
    ADVANCED_TACTICAL_AIRBORNE_RECONNAISSANCE_SYSTEM_DATA_LINK = 40
    BATTLE_GROUP_PASSIVE_HORIZON_EXTENSION_SYSTEM_DATA_LINK = 41
    COMMON_HIGH_BANDWIDTH_DATA_LINK = 42
    GUARDRAIL_INTEROPERABLE_DATA_LINK = 43
    GUARDRAIL_COMMON_SENSOR_SYSTEM_ONE_DATA_LINK = 44
    GUARDRAIL_COMMON_SENSOR_SYSTEM_TWO_DATA_LINK = 45
    GUARDRAIL_CSS2_MULTI_ROLE_DATA_LINK = 46
    GUARDRAIL_CSS2_DIRECT_AIR_TO_SAT_RELAY_DATA_LINK = 47
    LINE_OF_SIGHT_DATA_LINK_IMPLEMENTATION = 48
    LIGHTWEIGHT_CDL = 49
    L_52M = 50  # (SR-71)
    RIVET_REACH_RIVET_OWL_DATA_LINK = 51
    SENIOR_SPAN = 52
    SENIOR_SPUR = 53
    SENIOR_STRETCH = 54
    SENIOR_YEAR_INTEROPERABLE_DATA_LINK = 55
    SPACE_CDL = 56
    TR_1_MODE_MIST_AIRBORNE_DATA_LINK = 57
    KU_BAND_SATCOM_DATA_LINK_IMPLEMENTATION = 58
    MISSION_EQUIPMENT_CONTROL_DATA_LINK = 59
    RADAR_DATA_TRANSMITTING_SET_DATA_LINK = 60
    SURVEILLANCE_AND_CONTROL_DATA_LINK = 61
    TACTICAL_UAV_VIDEO = 62
    UHF_SATCOM_DATA_LINK_IMPLEMENTATION = 63
    TACTICAL_COMMON_DATA_LINK = 64
    LOW_LEVEL_AIR_PICTURE_INTERFACE = 65
    WEAPONS_DATA_LINK_AGM_130 = 66
    AUTOMATIC_IDENTIFICATION_SYSTEM = 67
    WEAPONS_DATA_LINK_AIM_120 = 68
    WEAPONS_DATA_LINK_AIM_9 = 69
    WEAPONS_DATA_LINK_CAMM = 70
    GC3 = 99
    JTIDS_MIDS_TADIL_J = 100  # Link 16 Standardized Format
    EDR_JTIDS_MIDS_TADIL_J = 101  # Link 16 Enhanced Data Rate
    JTIDS_MIDS_NET_DATA_LOAD = 102  # (TIMS/TOMS)
    LINK_22 = 103
    AFIWC_IADS_COMMUNICATIONS_LINKS = 104
    F_22_INTRA_FLIGHT_DATA_LINK = 105
    L_BAND_SATCOM = 106
    TSAF_COMMUNICATIONS_LINK = 107
    ENHANCED_SINCGARS_7_3 = 108
    F_35_MULTIFUNCTION_ADVANCED_DATA_LINK = 109
    CURSOR_ON_TARGET = 110
    ALL_PURPOSE_STRUCTURED_EUROCONTROL_SURVEILLANCE_INFORMATION_EXCHANGE = 111
    VARIABLE_MESSAGE_FORMAT_OVER_COMBAT_NET_RADIO = 112
    LINK_16_SURROGATE_FOR_NON_NATO_TDL306 = 113
    MQ_1_9_C_BAND_LOS_UPLINK = 114
    MQ_1_9_C_BAND_LOS_DOWNLINK = 115
    MQ_1_9_KU_BAND_SATCOM_UPLINK = 116
    MQ_1_9_KU_BAND_SATCOM_DOWNLINK = 117
    WEAPONS_DATALINK_SDB_II = 118
    JTAC_SA_UPLINK = 119
    CIB = 120
    JREAP_A = 121  # Joint Range Extension Application Protocol A
    JPALS_DATA_LINK = 125
    ONESAF_IADS_COMMUNICATIONS_LINK = 126
    TACTICAL_TARGETING_NETWORK_TECHNOLOGY_APPLICATION = 127



# [UID 177]
class UPin(enum.IntEnum):
    """8.2.2 User Protocol Identification Number (UPIN) [UID 177]"""
    # Not Implemented


"""8.3 Intercom"""

# [UID 180]
class IntercomControlType(enum.IntEnum):
    """8.3.1 Control Type [UID 180]"""
    RESERVED = 0
    STATUS = 1
    REQUEST_ACKNOWLEDGE_REQUIRED = 2
    REQUEST_NO_ACKNOWLEDGE = 3
    ACK_REQUEST_GRANTED = 4
    NACK_REQUEST_DENIED = 5


# [UID 181]
class CommunicationsChannelType(enum.IntEnum):
    """8.3.2 Communications Channel Type [UID 181]"""
    RESERVED = 0
    CONNECTION_FDX = 1
    CONNECTION_HDX_DESTINATION_IS_RECEIVE_ONLY = 2
    CONNECTION_HDX_DESTINATION_IS_TRANSMIT_ONLY = 3
    CONNECTION_HDX = 4


# [UID 416]
class CommunicationsChannelClass(enum.IntEnum):
    """8.3.3 Communications Channel Class [UID 416]"""
    SIMULATED_COMMUNICATIONS_CHANNEL = 0
    SIMULATION_SUPPORT_COMMUNICATIONS_CHANNEL = 1


# [UID 182]
class Command(enum.IntEnum):
    """8.3.4 Command [UID 182]"""
    NO_COMMAND = 0
    STATUS = 1
    CONNECT = 2
    DISCONNECT = 3
    RESET = 4
    ON = 5
    OFF = 6


# [UID 183]
class TransmitLineState(enum.IntEnum):
    """8.3.5 Transmit Line State [UID 183]"""
    NOT_APPLICABLE = 0
    NOT_TRANSMITTING = 1
    TRANSMITTING = 2


"""8.3.6 Intercom Communications Parameters"""

# [UID 185]
class IntercomRecordType(enum.IntEnum):
    """8.3.6.1 Record Type [UID 185]"""
    SPECIFIC_DESTINATION = 1
    GROUP_DESTINATION = 2
    GROUP_ASSIGNMENT = 3


# [UID 184]
class IntercomDestinationLineStateCommand(enum.IntEnum):
    """8.3.6.2 Destination Line State Command [UID 184]"""
    NONE = 0
    SET_LINE_STATE_TRANSMITTING = 1
    SET_LINE_STATE_NOT_TRANSMITTING = 2
    RETURN_TO_LOCAL_LINE_STATE_CONTROL = 3
