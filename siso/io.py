"""io.py
23 Information Operations (IO)
"""
import enum


# [UID 286]
class IOSimulationSource(enum.IntEnum):
    """23.1 IO Simulation Source [UID 286]"""
    NO_STATEMENT = 0


"""23.2 IO Action"""

# [UID 285]
class IOWarfareType(enum.IntEnum):
    """23.2.1 IO Warfare Type [UID 285]"""
    NO_STATEMENT = 0
    EW = 1  # Electronic Warfare
    CNO = 2  # Computer Network Operations
    PSYOPS = 3  # Psychological Operations
    MILDEC = 4  # Military Deception
    OPSEC = 5  # Operations Security
    PHYSICAL_ATTACK = 6


# [UID 287]
class IOActionType(enum.IntEnum):
    """23.2.2 IO Action Type [UID 287]"""
    NO_STATEMENT = 0
    PROFILE_DATA = 1  # (Parametrics)
    COMPUTED_EFFECTS = 2
    INTENT_BASED_EW = 3
    INTENT_BASED_EW_COMPUTED_EFFECTS = 4


# [UID 288]
class IOActionPhase(enum.IntEnum):
    """23.2.3 IO Action Phase [UID 288]"""
    NO_STATEMENT = 0
    START_ATTACK_PROFILE = 1
    END_ATTACK_PROFILE = 2
    CONTINUE_ATTACK_PROFILE_WITH_CHANGES = 3
    START_ATTACK_EFFECTS = 4
    END_ATTACKED_EFFECTS = 5
    CONTINUE_ATTACK_EFFECTS_WITH_CHANGES = 6


# [UID 289]
class IOReportType(enum.IntEnum):
    """23.3 IO Report Type [UID 289]"""
    NO_STATEMENT = 0
    INITIAL_REPORT = 1
    UPDATE_REPORT = 2
    FINAL_REPORT = 3


"""23.4 IO Effects Record"""

# [UID 290]
class IOStatus(enum.IntEnum):
    """23.4.1 IO Status [UID 290]"""
    NO_STATEMENT = 0
    EFFECT_ON_SENDER = 1
    EFFECT_ON_RECEIVER = 2
    EFFECT_ON_SENDER_AND_RECEIVER = 3
    EFFECT_ON_MESSAGE = 4
    EFFECT_ON_SENDER_AND_MESSAGE = 5
    EFFECT_ON_RECEIVER_AND_MESSAGE = 6
    EFFECT_ON_SENDER_RECEIVER_AND_MESSAGE = 7


# [UID 291]
class IOLinkType(enum.IntEnum):
    """23.4.2 IO Link Type [UID 291]"""
    NO_STATEMENT = 0
    LOGICAL_LINK = 1
    PHYSICAL_NODE = 2
    PHYSICAL_LINK = 3


# [UID 292]
class IOEffect(enum.IntEnum):
    """23.4.3 IO Effect [UID 292]"""
    NO_STATEMENT = 0
    DENIAL = 1
    DEGRADATION = 2
    DISRUPTION = 3
    TERMINATE_EFFECT = 255


# [UID 293]
class IOProcess(enum.IntEnum):
    """23.4.4 IO Process [UID 293]"""
    NO_STATEMENT = 0


# [UID 294]
class CommsNodeType(enum.IntEnum):
    """23.5 Comms Node Type [UID 294]"""
    NO_STATEMENT = 0
    SENDER_NODE_ID = 1
    RECEIVER_NODE_ID = 2
    SENDER_RECEIVER_NODE_ID = 3
