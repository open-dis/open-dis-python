import enum


# [UID 301]
class TransferredEntityIndicator(enum.IntEnum):
    NO_DIFFERENCE = 0
    DIFFERENCE = 1


# [UID 302]
class LVCIndicator(enum.IntEnum):
    NO_STATEMENT = 0
    LIVE = 1
    VIRTUAL = 2
    CONSTRUCTIVE = 3


# [UID 303]
class CoupledExtensionIndicator(enum.IntEnum):
    NOT_COUPLED = 0
    COUPLED = 1


# [UID 304]
class FireTypeIndicator(enum.IntEnum):
    MUNITION = 0
    EXPENDABLE = 1


# [UID 305]
class DetonationTypeIndicator(enum.IntEnum):
    MUNITION = 0
    EXPENDABLE = 1
    NON_MUNITION_EXPLOSION = 2


# [UID 307]
class IntercomAttachedIndicator(enum.IntEnum):
    NO_STATEMENT = 0
    UNATTACHED = 1
    ATTACHED = 2


# [UID 308]
class IFFSimulationModeIndicator(enum.IntEnum):
    REGENERATION = 0
    INTERACTIVE = 1


# [UID 389]
class ActiveInterrogationIndicator(enum.IntEnum):
    NOT_ACTIVE = 0
    ACTIVE = 1


# [UID 295]
class AttributeActionCode(enum.IntEnum):
    NO_STATEMENT = 0


# [UID 417]
class LiveEntitySubprotocolNumber(enum.IntEnum):
    NO_SUBPROTOCOL = 0
