"""iff.py

10 Identification Friend or Foe
"""
import enum


# [UID 82]
class SystemType(enum.IntEnum):
    """10.1 System Type [UID 82]"""
    NOT_USED = 0  # Invalid Value
    MARK_X_XII_ATCRBS_TRANSPONDER = 1
    MARK_X_XII_ATCRBS_INTERROGATOR = 2
    SOVIET_TRANSPONDER = 3
    SOVIET_INTERROGATOR = 4
    RRB_TRANSPONDER = 5
    MARK_XIIA_INTERROGATOR = 6
    MODE_5_INTERROGATOR = 7
    MODE_S_INTERROGATOR = 8
    MARK_XIIA_TRANSPONDER = 9
    MODE_5_TRANSPONDER = 10
    MODE_S_TRANSPONDER = 11
    MARK_XIIA_CIT = 12
    MARK_XII_CIT = 13
    TCAS_ACAS_TRANSCEIVER = 14


# [UID 83]
class SystemName(enum.IntEnum):
    """10.2 System Name [UID 83]"""
    NOT_USED = 0  # Invalid Value
    MARK_X = 1
    MARK_XII = 2
    ATCRBS = 3
    SOVIET = 4
    MODE_S = 5
    MARK_X_XII_ATCRBS = 6
    MARK_X_XII_ATCRBS_MODE_S = 7
    ARI_5954 = 8  # (RRB)
    ARI_5983 = 9  # (RRB)
    RRB = 10
    MARK_XIIA = 11
    MODE_5 = 12
    MARK_XIIA_CTT = 13
    MARK_XII_CTT = 14
    TCAS_ACAS_I_TRANSCEIVER = 15
    TCAS_ACAS_II_TRANSCEIVER = 16
    MARK_X_A = 17
    MARK_X_SIF = 18


# [UID 84]
class SystemMode(enum.IntEnum):
    """10.3 System Mode [UID 84]"""
    NO_STATEMENT = 0
    OFF = 1
    STANDBY = 2
    NORMAL = 3
    EMERGENCY = 4
    LOW_SENSITIVITY = 5


"""10.4 Change/Options"""

# [UID 337]
class TransponderInterrogatorIndicator(enum.IntEnum):
    """10.4.1 Transponder/Interrogator Indicator [UID 337]"""
    TRANSPONDER = 0
    INTERROGATOR = 1


# [UID 339]
class IFFSimulationMode(enum.IntEnum):
    """10.4.2 IFF Simulation Mode [UID 338]"""
    REGENERATION = 0
    INTERACTIVE = 1


# [UID 96]
class AlternateMode4ChallengeReply(enum.IntEnum):
    """10.5 Alternate Mode 4 Challenge/Reply [UID 96]"""
    NO_STATEMENT = 0
    VALID = 1
    INVALID = 2
    NO_RESPONSE = 3
    UNABLE_TO_VERIFY = 4


# [UID 87]
class LayerSpecificInformation(enum.IntEnum):
    """10.6 Layer-Specific Information [UID 87]"""
    NO_LAYER_SPECIFIC_INFORMATION_IS_PRESENT = 0


# [UID 339]
class ApplicableModes(enum.IntEnum):
    """10.7 Applicable Modes [UID 339]"""
    NO_APPLICABLE_MODES_DATA = 0
    ALL_MODES = 1


# [UID 340]
class ModeCAltitudeIndicator(enum.IntEnum):
    """10.8 Mode C Altitude Indicator [UID 340]"""
    POSITIVE_ALTITUDE_ABOVE_MSL = 0
    NEGATIVE_ALTITUDE_BELOW_MSL = 1  # Use Alternate Mode C Altitude


"""10.9 TCAS/ACAS Status"""

# [UID 341]
class BasicAdvancedIndicator(enum.IntEnum):
    """10.9.1 Basic/Advanced Indicator [UID 341]"""
    BASIC = 0
    ADVANCED = 1


# [UID 342]
class TCASACASIndicator(enum.IntEnum):
    """10.9.2 TCAS/ACAS Indicator [UID 342]"""
    TCAS = 0
    ACAS = 1


# [UID 343]
class SoftwareVersion(enum.IntEnum):
    """10.9.3 Software Version [UID 343]"""
    NO_STATEMENT = 0
    VERSION_6_0_2 = 1
    VERSION_7_0 = 2


# [UID 344]
class TCAS_ACAS_Type(enum.IntEnum):
    """10.9.4 TCAS/ACAS Type [UID 344]"""
    NO_STATEMENT = 0
    ACAS_I = 1
    ACAS_II = 2


# [UID 345]
class TCAS_I_II_Type(enum.IntEnum):
    """10.9.5 TCAS I/II Type [UID 345]"""
    TCAS_I_OR_NO_STATEMENT = 0
    TCAS_II = 1


# [UID 346]
class Mode5InterrogatorStatusMission(enum.IntEnum):
    """10.10 Mode 5 Interrogator Status Mission [UID 346]"""
    NO_STATEMENT = 0
    SURVEILLANCE_SHORAD = 1
    SHORAD_ASSOCIATED_WITH_WEAPONS_SYSTEM = 2
    WEAPON_SYSTEM = 3
    AIRBORNE_AND_SURFACE_SURVEILLANCE_PLATFORMS = 4
    AIRBORNE_AND_SURFACE_WEAPONS_PLATFORMS = 5
    GROUND_TO_GROUND = 6


# [UID 347]
class ModeSInterrogatorStatusTransmitState(enum.IntEnum):
    """10.11 Mode S Interrogator Status Transmit State [UID 347]"""
    NO_STATEMENT = 0
    ROLL_CALL = 1
    ALL_CALL = 2
    LOCKOUT_OVERRIDE = 3
    TEMPORARY_LOCKOUT = 4
    INTERMITTENT_LOCKOUT = 5


# [UID 348]
class ModeSInterrogatorIdentifierICType(enum.IntEnum):
    """10.12 Mode S Interrogator Identifier IC Type [UID 348]"""
    II = 0
    SI = 1


# [UID 349]
class ISLSAntennaType(enum.IntEnum):
    """10.13 ISLS Antenna Type [UID 349]"""
    NO_STATEMENT = 0
    MONOPULSE = 1

"""10.14 Mode 5 Status"""

# [UID 350]
class Mode5Reply(enum.IntEnum):
    """10.14.1 Mode 5 Reply [UID 350]"""
    NO_RESPONSE = 0
    VALID = 1
    INVALID = 2
    UNABLE_TO_VERIFY = 3


# [UID 351]
class Mode5AntennaSelection(enum.IntEnum):
    """10.14.2 Antenna Selection [UID 351]"""
    NO_STATEMENT = 0
    TOP = 1
    BOTTOM = 2
    DIVERSITY = 3


"""10.15 Mode 5 Squitter Status"""

# [UID 352]
class Mode5SquitterType(enum.IntEnum):
    """10.15.1 Mode 5 Squitter Type [UID 352]"""
    NOT_CAPABLE = 0
    SHORT = 1
    EXTENDED = 2


# [UID 353]
class Mode5Level2SquitterStatus(enum.IntEnum):
    """10.15.2 Level 2 Squitter Status [UID 353]"""
    DISABLED = 0
    ENABLED = 1


"""10.16 Mode S Status"""

# [UID 354]
class ModeSSquitterType(enum.IntEnum):
    """10.16.1 Mode S Squitter Type [UID 354]"""
    NOT_CAPABLE = 0
    ACQUISITION = 1
    EXTENDED = 2
    SHORT = 3


# [UID 355]
class ModeSSquitterRecordSource(enum.IntEnum):
    """10.16.2 Mode S Squitter Record Source [UID 355]"""
    LAYER_4_IFF_DATA_RECORDS = 0
    LAYER_5_GICB_IFF_DATA_RECORDS = 1


"""10.17 Mode S Transponder Basic Data"""

# [UID 356]
class AircraftPresentDomain(enum.IntEnum):
    """10.17.1 Aircraft Present Domain [UID 356]"""
    NO_STATEMENT = 0
    AIRBORNE = 1
    ON_GROUND = 2


# [UID 357]
class AircraftIdentificationType(enum.IntEnum):
    """10.17.2 Aircraft Identification Type [UID 357]"""
    NO_STATEMENT = 0
    FLIGHT_NUMBER = 1
    TAIL_NUMBER = 2


# [UID 358]
class CapabilityReport(enum.IntEnum):
    """10.17.3 Capability Report [UID 358]"""
    NO_COMMUNICATIONS_CAPABILITY = 0
    RESERVED1 = 1
    RESERVED2 = 2
    RESERVED3 = 3
    COMM_A_B_CAPABILITY_SET_CA_7_ON_GROUND = 4
    COMM_A_B_CAPABILITY_SET_CA_7_AIRBORNE = 5
    COMM_A_B_CAPABILITY_SET_CA_7_EITHER_AIRBORNE_OR_ON_GROUND = 6
    DOWNLINK_REQUEST_FIELD_0_AND_FLIGHT_STATUS_2345_EITHER_AIRBORNE_OR_ON_GROUND = 7
    NO_STATEMENT = 255


# [UID 359]
class NavigationSource(enum.IntEnum):
    """10.18 Navigation Source [UID 359]"""
    NO_STATEMENT = 0
    GPS = 1
    INS = 2
    INS_GPS = 3


# [UID 360]
class IFFDataRecordAvailable(enum.IntEnum):
    """10.19 IFF Data Record Available [UID 360]"""
    COMPUTE_LOCALLY = 0
    IFF_DATA_RECORD_AVAILABLE = 1


# [UID 361]
class Mode5SAltitudeResolution(enum.IntEnum):
    """10.20 Mode 5/S Altitude Resolution [UID 361]"""
    _100_FOOT = 0
    _25_FOOT = 1


# [UID 362]
class DeltaMode5SAltitudePositiveNegativeIndicator(enum.IntEnum):
    """10.21 Delta Mode 5/S Altitude Positive/Negative Indicator [UID 362]"""
    POSITIVE = 0
    NEGATIVE = 1


"""10.22 Squitter Report IFF Data"""

# [UID 363]
class FormatType(enum.IntEnum):
    """10.22.1 Format Type [UID 363]"""
    NO_DATA = 0
    IDENTITY_FORMAT = 4
    SURFACE_FORMAT_5_METER_RNP = 5
    SURFACE_FORMAT_100_METER_RNP = 6
    AIRBORNE_FORMAT_5_METER_RNP_25_FOOT_BAROMETRIC_ALTITUDE = 7
    AIRBORNE_FORMAT_100_METER_RNP_25_FOOT_BAROMETRIC_ALTITUDE = 8
    AIRBORNE_FORMAT_0_25_NMI_RNP_25_FOOT_BAROMETRIC_ALTITUDE = 9
    AIRBORNE_FORMAT_1_0_NMI_RNP_25_FOOT_BAROMETRIC_ALTITUDE = 10
    AIRBORNE_FORMAT_5_METER_RNP_100_FOOT_BAROMETRIC_ALTITUDE = 11
    AIRBORNE_FORMAT_100_METER_RNP_100_FOOT_BAROMETRIC_ALTITUDE = 12
    AIRBORNE_FORMAT_0_25_NMI_RNP_100_FOOT_BAROMETRIC_ALTITUDE = 13
    AIRBORNE_FORMAT_1_0_NMI_RNP_100_FOOT_BAROMETRIC_ALTITUDE = 14
    AIRBORNE_FORMAT_5_METER_RNP_GPS_HEIGHT = 15
    AIRBORNE_FORMAT_100_METER_RNP_GPS_HEIGHT = 16


# [UID 364]
class AircraftAddressSource(enum.IntEnum):
    """10.22.2 Aircraft Address Source [UID 364]"""
    MODE_S_AIRCRAFT_ADDRESS_FIELD_VALUE = 0
    GICB_IFF_DATA_RECORD_AVAILABLE = 1


# [UID 365]
class SurveillanceStatus(enum.IntEnum):
    """10.22.3 Surveillance/Status [UID 365]"""
    NO_INFORMATION = 0
    EMERGENCY_LOSS_OF_COMMUNICATIONS = 1
    SPI = 2
    ATCRBS_CODE_CHANGE = 3


# [UID 366]
class TurnRateSource(enum.IntEnum):
    """10.22.4 Turn Rate Source [UID 366]"""
    COMPUTE_LOCALLY = 0
    LESS_THAN_1_DEGREE_TURN_OR_NOT_TURNING = 1
    ONE_DEGREE_OR_GREATER_TURN_RATE = 2


# [UID 367]
class TimeTypeSource(enum.IntEnum):
    """10.22.5 Time Type Source [UID 367]"""
    COMPUTE_LOCALLY = 0
    EVEN_SECOND = 1
    ODD_SECOND = 2


# [UID 368]
class AircraftTypeOrWake(enum.IntEnum):
    """10.22.6 Aircraft Type/Wake [UID 368]"""
    # No values are currently assigned by ICAO for this field.
    NO_STATEMENT = 0


# [UID 801]
class AircraftIDSource(enum.IntEnum):
    """10.22.7 Aircraft ID Source [UID 801]"""
    MODE_S_AIRCRAFT_IDENTIFICATION_FIELD_VALUE = 0
    GICB_IFF_DATA_RECORD_AVAILABLE = 1


# [UID 369]
class DataCategory(enum.IntEnum):
    """10.23 Data Category [UID 369]"""
    NO_STATEMENT = 0
    FUNCTIONAL_DATA = 1
    TRANSPONDER_INTERROGATOR_DATA_LINK_MESSAGES = 2


# [UID 370]
class TILinkType(enum.IntEnum):
    """10.24 T/I Link Type [UID 370]"""
    NOT_USED = 0
    GROUND_INITIATED_COMMUNICATIONS_B = 1
    AUTOMATIC_DEPENDENT_SURVEILLANCE = 2
    GLOBAL_NAVIGATION_SATELITE_SYSTEM = 3
    DATA_LINK_INITIATION_CAPABILITY = 4
    AIRCRAFT_COMMUNICATIONS_ADDRESSING_AND_REPORTING_SYSTEM = 5
    ATC_COMMUNICATIONS_MANAGEMENT = 6
    VHF_DIGITAL_LINK = 7
    AERONAUTICAL_TELECOMMUNICATION_NETWORK = 8
    MODE_SELECT = 9
    AIRBORNE_COLLISION_AVOIDANCE_SYSTEMS = 10
    TRAFFIC_COLLISION_AVOIDANCE_SYSTEMS = 11
    AUTOMATIC_DEPENDENT_SURVEILLANCE_B = 12


"""10.25 Secondary Operational Data"""

# [UID 97]
class OperationalParameter(enum.IntEnum):
    """10.25.1 Operational Parameter 1 [UID 97]"""
    """10.25.2 Operational Parameter 2 [UID 98]"""
    NO_OPERATIONAL_PARAMETER_DATA = 0


"""10.26 Other IFF"""

# [UID 371]
class AntennaStatus(enum.IntEnum):
    """10.26.1 Antenna Status [UID 371]"""
    NO_STATEMENT = 0
    NOT_ABLE_TO_EMIT = 1
    ABLE_TO_EMIT = 2


# [UID 372]
class TransmissionIndicator(enum.IntEnum):
    """10.26.2 Transmission Indicator [UID 372]"""
    NO_STATEMENT = 0
    ORIGINAL_INTERROGATION = 1
    INTERROGATION_REPLY = 2
    SQUITTER_TRANSMISSION = 3


# [UID 373]
class ReplyAmplification(enum.IntEnum):
    """10.26.3 Reply Amplification [UID 373]"""
    NO_STATEMENT = 0
    COMPLETE = 1
    LIMITED = 2
    UNABLE_TO_RESPOND = 3


# [UID 380]
class Mode5MessageFormatsStatus(enum.IntEnum):
    """10.26.4 Mode 5 Message Formats Status [UID 380]"""
    CAPABILITY = 0
    ACTIVE_INTERROGATION = 1


# [UID 396]
class Mode5PlatformType(enum.IntEnum):
    """10.26.5 Mode 5 Platform Type [UID 396]"""
    GROUND_VEHICLE = 0
    AIR_VEHICLE = 1


# [UID 412]
class Mode5LevelSelection(enum.IntEnum):
    """10.26.6 Mode 5 Level Selection [UID 412]"""
    LEVEL_1 = 0
    LEVEL_2 = 1


# [UID 423]
class Mode5LocationErrors(enum.IntEnum):
    """10.26.7 Mode 5 Location Errors [UID 423]"""
    NO_LOCATION_ERRORS = 0
    IFF_DATA_RECORD_PRESENT = 1
