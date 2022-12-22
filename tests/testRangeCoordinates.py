#!/usr/bin/env python3

"""
Unit test for RangeCoordinates.py

Tests the following functions:

    Test  1 : llarpy2ecef

"""
#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import unittest as _unittest
from opendis.RangeCoordinates import *
#-----------------------------------------------------------------------------
# CONSTANTS
#-----------------------------------------------------------------------------
gps = GPS()
wgs84 = WGS84()
#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# CLASSES
#-----------------------------------------------------------------------------
class SimpleTest(_unittest.TestCase):

    # set up the test
    def setUp(self):
        pass

    # Test  1: llarpy2ecef
    def test01(self):

        ######################################################################
        # test ground vehicle at prime meredian and equator pointed north
        ######################################################################
        # body latitude, longitude, altitude
        lat = deg2rad(0)
        lon = deg2rad(0)
        alt = 0

        # body pitch, roll, yaw
        pitch = deg2rad(0)
        roll = deg2rad(0)
        yaw = deg2rad(0)

        # body to ECEF
        a = gps.llarpy2ecef(lat, lon, alt, roll, pitch, yaw)

        # assert to nearest 2 decimal places (compensate for IEEE-754)
        self.assertTrue(round(a[0], 2) == round(wgs84.a, 2))
        self.assertTrue(round(a[1], 2) == 0.00)
        self.assertTrue(round(a[2], 2) == 0.00)
        self.assertTrue(round(a[3], 2) == 0.00)
        self.assertTrue(round(a[4] * 180 / pi) == -90.00)
        self.assertTrue(round(a[5], 2) == 0.00)

        ######################################################################
        # test ground vehicle at north pole pointed south
        ######################################################################
        # body latitude, longitude, altitude
        lat = deg2rad(90)
        lon = deg2rad(0)
        alt = 0

        # body pitch, roll, yaw
        pitch = deg2rad(0)
        roll = deg2rad(0)
        yaw = deg2rad(180)

        # body to ECEF
        a = gps.llarpy2ecef(lat, lon, alt, roll, pitch, yaw)

        # assert to nearest 2 decimal places (compensate for IEEE-754)
        self.assertTrue(round(a[0], 2) ==  0.00 or round(a[0], 2) == round(pi, 2))
        self.assertTrue(round(a[1], 2) == 0.00)
        self.assertTrue(round(a[2], 2) ==  6356752.31)
        self.assertTrue(round(a[3], 2) == 0.00)
        self.assertTrue(round(a[4], 2) == 0.00)
        self.assertTrue(round(a[5], 2) == 0.00 
                        or abs(round(a[5], 2)) == round(pi, 2)
                        )

        ######################################################################
        # test aircraft flying 10000 m above Adeliaide, Australia heading SE,
        # climbing at 20 deg while holding a 30 deg roll
        ######################################################################
        # body latitude, longitude, altitude
        lat = deg2rad(-34.9)
        lon = deg2rad(138.5)
        alt = 10000

        # body pitch, roll, yaw
        pitch = deg2rad(20)
        roll = deg2rad(30)
        yaw = deg2rad(135)

        # body to ECEF
        a = gps.llarpy2ecef(lat, lon, alt, roll, pitch, yaw)

        # assert to nearest decimal place (compensate for IEEE-754)
        self.assertTrue(round(a[0]) == -3928261)
        self.assertTrue(round(a[1]) == 3475431)
        self.assertTrue(round(a[2]) == -3634495)
        self.assertTrue(round(a[3] * 180 / pi) == -123)
        self.assertTrue(round(a[4] * 180 / pi) == 48)
        self.assertTrue(round(a[5] * 180 / pi) == -30)

#-----------------------------------------------------------------------------
# DO THE THING
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    _unittest.main()
#-----------------------------------------------------------------------------
