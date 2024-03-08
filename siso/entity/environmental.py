"""environmental.py

5.5 Environmental Kind
"""
import enum


# [UID 21]
class Size(enum.IntEnum):
    """5.5.3 Subcategory [UID 21]"""
    OTHER = 0
    VERY_SMALL = 20
    SMALL = 40
    MEDIUM = 60
    LARGE = 80
    VERY_LARGE = 100


# [UID 715]
class Island(enum.IntEnum):
    """5.5.4 Island Subcategory [UID 715]"""
    OTHER = 0
    ISLANDS_1000_2499_SQ_KM = 1
    ISLANDS_2500_4999_SQ_KM = 2
    ISLANDS_5000_9999_SQ_KM = 3
    ISLANDS_10000_24999_SQ_KM = 4
    ISLANDS_25000_99999_SQ_KM = 5
    ISLANDS_100000_SQ_KM_AND_GREATER = 6
