"""emitter.py

7 Emitters
"""
import enum


# [UID 75]
class ElectromagneticEmitter(enum.IntEnum):
    """7.1 Electromagnetic Emitters [UID 75]"""
    # TODO
"""Field Value   National Nomenclature   NATO Reporting Name   Commercial Designation"""
# 50 pages of tables of emitter data follows


# [UID 144]
class AcousticEmitter(enum.IntEnum):
    """7.2 Acoustic Emitters [UID 144]"""
    OTHER = 0
    AN_BQQ_5 = 1
    AN_SSQ_62 = 2
    AN_SQS_23 = 3
    AN_SQS_26 = 4
    AN_SQS_53 = 5
    ALFS = 6
    LFA = 7
    AN_AQS_901 = 8
    AN_AQS_902 = 9


# [UID 325]
class OtherActiveSensor(enum.IntEnum):
    """7.3 Other Active Sensors [UID 325]"""
    # There are currently no enumerations defined for [UID 325]


# [UID 326]
class PassiveSensor(enum.IntEnum):
    """7.4 Passive Sensors [UID 326]"""
    ALR_400 = 60000
    AN_AAR_47 = 60001
    AN_AAR_50 = 60002
    AN_AAR_54 = 60003
    AN_AAR_56 = 60004
    AN_AAR_57 = 60005
    AN_ALQ_142 = 60006
    AN_ALR_45 = 60007
    AN_ALR_46 = 60008
    AN_ALR_56 = 60009
    AN_ALR_59 = 60010
    AN_ALR_64 = 60011
    AN_ALR_66 = 60012
    AN_ALR_67 = 60013
    AN_ALR_69 = 60014
    AN_ALR_73 = 60015
    AN_ALR_76 = 60016
    AN_ALR_91 = 60017
    AN_ALR_93 = 60018
    AN_ALR_94 = 60019
    AN_ALR_801 = 60020
    AN_APR_39 = 60021
    AN_AYR_2 = 60022
    ARI_18223 = 60023
    BOW_21 = 60024
    CHAPARRAL_IRST = 60025
    FLANKER_IRST = 60026
    FOXBAT_IRST = 60027
    FOXHOUND_IRST = 60028
    FULCRUM_IRST = 60029
    HAVOC_IRST = 60030
    HIND_IRST = 60031
    KJ_200 = 60032
    KJ_8602 = 60033
    L_150_PASTEL = 60034
    SERVAL = 60035
    SHERLOC = 60036
    SHERLOCVF = 60037
    SIRENA_2 = 60038
    SIRENA_3 = 60039
    SIRENA_3M = 60040
    SKY_GUARDIAN = 60041
    SPO_15 = 60042
    SPS_200 = 60043
    TARANG = 60044
