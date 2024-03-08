"""munition.py

5.3 Munition Kind
"""
import enum


# [UID 15]
class Category(enum.IntEnum):
    OTHER = 0
    GUIDED = 1
    BALLISTIC = 2
    FIXED = 3
