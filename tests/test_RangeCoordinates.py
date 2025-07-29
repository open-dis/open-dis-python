#!/usr/bin/env python3

"""
Unit tests for RangeCoordinates.py



Tests the following functions:

    Test  1 : body_to_ecef_and_back which tests the following functions:
                * ecef2lla
                * ecef2llarpy
                * ecefvec2nedvec
                * lla2ecef
                * llarpy2ecef
                * rotate_3x3
                * transpose

"""
#-----------------------------------------------------------------------------
# IMPORTS
#-----------------------------------------------------------------------------
import unittest as _unittest
from random import randint
from random import random
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

    # Test  1 : llarpy2ecef and ecef2llarpy
    def test01_body_ecef_conversions(self):
        """
        Tests the following functions:
            ecef2lla
            ecef2llarpy
            ecefvec2nedvec
            lla2ecef
            llarpy2ecef
            rotate_3x3
            transpose

        First tests some simple cases and examples from the internet, then
        tests random values.
        """

        def body_to_ecef_and_back(body, ecef):
            """
            Verify llarpy2ecef() translates given body coordinates to given 
            ecef coordinates. Verify ecef2llarpy() translates those coordinates
            back to the given body coordinates.

            Input: body = (lat, lon, alt, roll, pitch, yaw)
                   ecef = (X, Y, Z, psi, theta, phi)

            Output: None
            """

            # body to ECEF
            a = gps.llarpy2ecef(*body)

            # assert to nearest 2 decimal places
            self.assertAlmostEqual(a[0], ecef[0], 2)
            self.assertAlmostEqual(a[1], ecef[1], 2)
            self.assertAlmostEqual(a[2], ecef[2], 2)
            self.assertAlmostEqual(a[3], ecef[3], 2)
            self.assertAlmostEqual(a[4], ecef[4], 2)
            self.assertAlmostEqual(a[5], ecef[5], 2)

            # ECEF back to body
            b = gps.ecef2llarpy(*a)

            # assert to nearest 2 decimal places (altitude to nearest number)
            self.assertAlmostEqual(b[0], body[0], 2)
            self.assertAlmostEqual(b[1], body[1], 2)
            self.assertAlmostEqual(b[2], body[2], 0)
            self.assertAlmostEqual(b[3], body[3], 2)
            self.assertAlmostEqual(b[4], body[4], 2)
            self.assertAlmostEqual(b[5], body[5], 2)

        ######################################################################
        # test ground vehicle at prime meridian and equator pointed north
        ######################################################################
        # define body coordinates
        lat, lon, alt, roll, pitch, yaw = 0, 0, 0, 0, 0, 0

        # define ECEF coordinates
        X, Y, Z, psi, theta, phi = wgs84.a, 0, 0, 0, -pi/2, 0

        # test
        body_to_ecef_and_back((lat, lon, alt, roll, pitch, yaw),
                              (X, Y, Z, psi, theta, phi)
                              )


        ######################################################################
        # test ground vehicle at prime meridian and equator pointed south
        ######################################################################
        # define body coordinates
        lat, lon, alt, roll, pitch, yaw = 0, 0, 0, 0, 0, deg2rad(180)

        # define ECEF coordinates 
        X, Y, Z, psi, theta, phi = wgs84.a, 0, 0, pi/2, pi/2, -pi/2

        # test
        body_to_ecef_and_back((lat, lon, alt, roll, pitch, yaw),
                              (X, Y, Z, psi, theta, phi)
                              )


        ######################################################################
        # test ground vehicle at north pole pointed south @ 180
        ######################################################################
        # define body coordinates
        lat, lon, alt, roll, pitch, yaw = deg2rad(90), 0, 0, 0, 0, deg2rad(180)

        # define ECEF coordinates
        X, Y, Z, psi, theta, phi = 0, 0, wgs84.b, 0, 0, -pi

        # test
        body_to_ecef_and_back((lat, lon, alt, roll, pitch, yaw),
                              (X, Y, Z, psi, theta, phi)
                              )


        ######################################################################
        # test aircraft flying 10000 m above Adeliaide, Australia heading SE,
        # climbing at 20 deg while holding a 30 deg roll
        ######################################################################
        # define body coordinates
        lat = deg2rad(-34.9)
        lon = deg2rad(138.5)
        alt = 10000
        pitch = deg2rad(20)
        roll = deg2rad(30)
        yaw = deg2rad(135)

        # define ECEF coordinates
        X = -3928260.52
        Y = 3475431.33
        Z = -3634495.17
        psi = deg2rad(-122.97)
        theta = deg2rad(47.79)
        phi = deg2rad(-29.67)

        # test
        body_to_ecef_and_back((lat, lon, alt, roll, pitch, yaw),
                              (X, Y, Z, psi, theta, phi)
                              )


        ######################################################################
        # test body to ecef and back with random values in range:
        #   latitude  : -89.9999 to 89.9999 deg
        #   longitude : -179.9999 to 179.9999 deg
        #   altitude  : -1000000 to 1000000 m
        #   pitch     : -89.9999 to 89.9999 deg
        #   roll      : -179.9999 to 179.9999 deg
        #   yaw       : -179.9999 to 179.9999 deg
        ######################################################################
        for _ in range(10000):

            # define body coordinates
            lat = deg2rad(randint(-89, 89) + random())
            lon = deg2rad(randint(-179, 179) + random())
            alt = randint(-1000000, 1000000)
            pitch = deg2rad(randint(-89, 89) + random())
            roll = deg2rad(randint(-179, 179) + random())
            yaw = deg2rad(randint(-179, 179) + random())

            # body to ECEF
            a = gps.llarpy2ecef(lat, lon, alt, roll, pitch, yaw)

            # ECEF back to body
            b = gps.ecef2llarpy(*a)

            # assert to nearest 2 decimal places (altitude within 5 m)
            self.assertAlmostEqual(b[0], lat, 2)
            self.assertAlmostEqual(b[1], lon, 2)
            self.assertAlmostEqual(b[2], alt, delta=5)
            self.assertAlmostEqual(b[3], roll, 2)
            self.assertAlmostEqual(b[4], pitch, 2)
            self.assertAlmostEqual(b[5], yaw, 2)

        ######################################################################
        # test ecef to body and back with random values in range:
        #   X     : -7500000 to 7500000 m
        #   Y     : -7500000 to 7500000 m
        #   Z     : -7500000 to 7500000 m
        #   psi   : -179.9999 to 179.9999 deg
        #   theta : -89.9999 to 89.9999 deg
        #   phi   : -179.9999 to 179.9999 deg
        ######################################################################
        for _ in range(10000):

            # define body coordinates
            X = randint(-7500000, 7500000)
            Y = randint(-7500000, 7500000)
            Z = randint(-7500000, 7500000)
            psi = deg2rad(randint(-179, 179) + random())
            theta = deg2rad(randint(-89, 89) + random())
            phi = deg2rad(randint(-179, 179) + random())

            # body to ECEF
            a = gps.ecef2llarpy(X, Y, Z, psi, theta, phi)

            # ECEF back to body
            b = gps.llarpy2ecef(*a)

            # assert location to nearest decimal place and Euler angles to
            # nearest 2
            self.assertAlmostEqual(b[0], X, 0)
            self.assertAlmostEqual(b[1], Y, 0)
            self.assertAlmostEqual(b[2], Z, 0)
            self.assertAlmostEqual(b[3], psi, 2)
            self.assertAlmostEqual(b[4], theta, 2)
            self.assertAlmostEqual(b[5], phi, 2)


#-----------------------------------------------------------------------------
# DO THE THING
#-----------------------------------------------------------------------------
if __name__ == "__main__":
    _unittest.main()
#-----------------------------------------------------------------------------
