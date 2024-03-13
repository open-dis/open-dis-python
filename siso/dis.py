import enum


# [UID 3]
class ProtocolVersion(enum.IntEnum):
    OTHER = 0
    DIS_PDU_1_0 = 1  # May '92
    IEEE_1278_1993 = 2
    DIS_APPLICATIONS_2_0 = 3  # 28 May 1993
    DIS_APPLICATION_PROTOCOLS_2_0 = 4  # 16 Mar 1994
    IEEE_1278_1_1995 = 5
    IEEE_1278_1A_1998 = 6
    IEEE_1278_1_2012 = 7


# [UID 4]
class PduType(enum.IntEnum):
    OTHER = 0
    ENTITY_STATE = 1
    FIRE = 2
    DETONATION = 3
    COLLISION = 4
    SERVICE_REQUEST = 5
    RESUPPLY_OFFER = 6
    RESUPPLY_RECEIVED = 7
    RESUPPLY_CANCEL = 8
    REPAIR_COMPLETE = 9
    REPAIR_RESPONSE = 10
    CREATE_ENTITY = 11
    REMOVE_ENTITY = 12
    START_RESUME = 13
    STOP_FREEZE = 14
    ACKNOWLEDGE = 15
    ACTION_REQUEST = 16
    ACTION_RESPONSE = 17
    DATA_QUERY = 18
    SET_DATA = 19
    DATA = 20
    EVENT_REPORT = 21
    COMMENT = 22
    ELECTROMAGNETIC_EMISSION = 23
    DESIGNATOR = 24
    TRANSMITTER = 25
    SIGNAL = 26
    RECEIVER = 27
    IFF = 28
    UNDERWATER_ACOUSTIC = 29
    SUPPLEMENTAL_EMISSION___ENTITY_STATE = 30
    INTERCOM_SIGNAL = 31
    INTERCOM_CONTROL = 32
    AGGREGATE_STATE = 33
    ISGROUPOF = 34
    TRANSFER_OWNERSHIP = 35
    ISPARTOF = 36
    MINEFIELD_STATE = 37
    MINEFIELD_QUERY = 38
    MINEFIELD_DATA = 39
    MINEFIELD_RESPONSE_NACK = 40
    ENVIRONMENTAL_PROCESS = 41
    GRIDDED_DATA = 42
    POINT_OBJECT_STATE = 43
    LINEAR_OBJECT_STATE = 44
    AREAL_OBJECT_STATE = 45
    TSPI = 46
    APPEARANCE = 47
    ARTICULATED_PARTS = 48
    LE_FIRE = 49
    LE_DETONATION = 50
    CREATE_ENTITY_R = 51
    REMOVE_ENTITY_R = 52
    START_RESUME_R = 53
    STOP_FREEZE_R = 54
    ACKNOWLEDGE_R = 55
    ACTION_REQUEST_R = 56
    ACTION_RESPONSE_R = 57
    DATA_QUERY_R = 58
    SET_DATA_R = 59
    DATA_R = 60
    EVENT_REPORT_R = 61
    COMMENT_R = 62
    RECORD_R = 63
    SET_RECORD_R = 64
    RECORD_QUERY_R = 65
    COLLISION_ELASTIC = 66
    ENTITY_STATE_UPDATE = 67
    DIRECTED_ENERGY_FIRE = 68
    ENTITY_DAMAGE_STATUS = 69
    INFORMATION_OPERATIONS_ACTION = 70
    INFORMATION_OPERATIONS_REPORT = 71
    ATTRIBUTE = 72


# [UID 5]
class ProtocolFamily(enum.IntEnum):
    OTHER = 0
    ENTITY_INFORMATION_INTERACTION = 1
    WARFARE = 2
    LOGISTICS = 3
    RADIO_COMMUNICATIONS = 4
    SIMULATION_MANAGEMENT = 5
    DISTRIBUTED_EMISSION_REGENERATION = 6
    ENTITY_MANAGEMENT = 7
    MINEFIELD = 8
    SYNTHETIC_ENVIRONMENT = 9
    SIMULATION_MANAGEMENT_WITH_RELIABILITY = 10
    LIVE_ENTITY_INFORMATION_INTERACTION = 11
    NON_REAL_TIME = 12
    INFORMATION_OPERATIONS = 13