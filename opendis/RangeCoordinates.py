#! /usr/bin/python

# Various coordinate system transform utilities. DIS uses
# an Earth-Centered, Earth-Fixed coordinate system, with the
# origin at the center of the (WGS84) earth, positive x out
# at the equator and prime meridian, z out through the north
# pole, and y out at the equator and 90 deg east. We often want
# to convert those coordinates to latitude, longitude, and altitude
# on the WGS84 globe. This utility does that. (It's swiped from
# the net, specifically the stoqs project at MBARI)

__author__ = ""
__credits = "https://github.com/GAVLab/fhwa2_viz/blob/master/fhwa2_gui/src/util.py"

"""
Container for general GPS functions and classes

Functions:
    deg2rad
    rad2deg
    euclideanDistance

Classes:
    GPS - includes functions:
        ecef2lla
        ecef2llarpy
        ecef2ned
        ecef2pae
        ecef2utm
        ecefvec2nedvec
        lla2ecef
        lla2gcc
        lla2utm
        llarpy2ecef
        ned2ecef
        ned2pae
        rotate_3x3
        transpose
        utmLetterDesignator

    WGS84 - constant parameters for GPS class - includes function:
        g0
"""
#Import required packages
from math import sqrt, pi, sin, cos, tan, atan, atan2, asin
from numpy import array, dot, identity


def deg2rad(deg: float):
    """Converts degrees to radians"""
    return deg * pi / 180


def rad2deg(rad: float):
    """Converts radians to degrees"""
    return rad * 180 / pi


def euclideanDistance(data, dataRef=None):
    """Calculates the Euclidian distance between the given data and zero.
    This works out to be equivalent to the distance between two points if their
    difference is given as the input"""
    total = 0
    for index in range(len(data)):
        if dataRef is None:
            total += data[index]**2
        else:
            total += (data[index] - dataRef[index])**2
    return sqrt(total)


class WGS84:
    """General parameters defined by the WGS84 system"""

    # Semimajor axis length (m)
    a = 6378137.0

    # Semiminor axis length (m)
    b = 6356752.3142

    # Ellipsoid flatness (unitless)
    f = (a - b) / a

    # Eccentricity (unitless)
    e = sqrt(f * (2 - f))

    # Speed of light (m/s)
    c = 299792458.

    # Relativistic constant
    F = -4.442807633e-10

    # Earth's universal gravitational constant
    mu = 3.986005e14

    # Earth rotation rate (rad/s)
    omega_ie = 7.2921151467e-5

    def g0(self, L):
        """
        acceleration due to gravity at the ellipsoid surface at latitude L
        
        Note: this is not the WGS84 models for gravity at latitude,
              it is an approximation from another source.     
        """
        return 9.7803267715 * (1 + 0.001931851353 * sin(L)**2) / \
                        sqrt(1 - 0.0066943800229 * sin(L)**2)


class GPS:
    """Working class for GPS module"""

    wgs84 = WGS84()

    def ecef2lla(self, ecef, tolerance=1e-9):
        """Convert Earth-centered, Earth-fixed coordinates to lat, lon, alt.
        Input: ecef - (x, y, z) in (m, m, m)
        Output: lla - (lat, lon, alt) in (decimal degrees, decimal degrees, m)
        """
        # Decompose the input
        x = ecef[0]
        y = ecef[1]
        z = ecef[2]

        # Calculate lon
        lon = atan2(y, x)

        # Initialize the variables to calculate lat and alt
        alt = 0
        N = self.wgs84.a
        p = sqrt(x**2 + y**2)
        lat = 0
        previousLat = 90

        # Special case for poles (note: any longitude value is valid here)
        if x == 0 and y == 0:   
            if z > 0:
                return (90.00, 69.00, round(z - self.wgs84.b, 2))

            elif z < 0:
                return (-90.00, 69.00, round(-z - self.wgs84.b, 2))

            else:
                raise Exception("The Exact Center of the Earth has no lat/lon")

        # Iterate until tolerance is reached
        while abs(lat - previousLat) >= tolerance:
            previousLat = lat
            sinLat = z / (N * (1 - self.wgs84.e**2) + alt)
            lat = atan((z + self.wgs84.e**2 * N * sinLat) / p)
            N = self.wgs84.a / sqrt(1 - (self.wgs84.e * sinLat)**2)
            alt = p / cos(lat) - N

        # Return the lla coordinates
        return (rad2deg(lat), rad2deg(lon), alt)


    def ecef2llarpy(self, X, Y, Z, psi, theta, phi):
        """
        Convert an entities DIS standard ECEF coordinates and Euler angles into
        latitude, longitude, altitude, pitch, roll, and yaw.

        Inputs:
            X     : entities ECEF X coordinate in meters
            Y     : entities ECEF Y coordinate in meters
            Z     : entities ECEF Z coordinate in meters
            psi   : entities rotation around the ECEF Z axis
            theta : entities rotation around the ECEF Y axis
            phi   : entities rotation around the ECEF X axis

        Output:
            (lat, lon, alt, roll, pitch, yaw) where:
              lat   : latitude of the entity in radians
              lon   : longitude of the entity in radians
              alt   : altitude of the entity in meters
              roll  : roll of the entity in radians
              pitch : pitch of the entity in radians
              yaw   : yaw (heading) of the entity in radians
        """

        # get lat, lon, alt from ECEF X, Y, Z
        lat, lon, alt = self.ecef2lla((X, Y, Z))

        # Note: X = x0, Y = y0, Z = z0
        x0 = array([1, 0, 0])
        y0 = array([0, 1, 0])
        z0 = array([0, 0, 1])

        # first rotation array, z0 by psi rads
        rot_array_1 = self.rotate_3x3(psi, z0)

        # rotate
        x1 = dot(rot_array_1, x0)
        y1 = dot(rot_array_1, y0)
        z1 = dot(rot_array_1, z0)

        # second rotation array, y1 by theta rads
        rot_array_2 = self.rotate_3x3(theta, y1)

        # rotate
        x2 = dot(rot_array_2, x1)
        y2 = dot(rot_array_2, y1)
        z2 = dot(rot_array_2, z1)

        # third rotation array, x2 by phi rads
        rot_array_3 = self.rotate_3x3(phi, x2)

        # rotate
        x3 = dot(rot_array_3, x2)
        y3 = dot(rot_array_3, y2)
        z3 = dot(rot_array_3, z2)

        # get the local NED unit vectors wrt the ECEF coordinate system
        a0 = self.ecefvec2nedvec(deg2rad(lat), deg2rad(lon))
        X0 = a0[0]
        Y0 = a0[1]
        Z0 = a0[2]

        # calculate yaw and pitch
        yaw = atan2( dot(x3, Y0), dot(x3, X0) )
        pitch = atan2( -dot(x3, Z0), sqrt( (dot(x3, X0)) ** 2 + (dot(x3, Y0)) **2 ) )

        # calculate roll
        Y2 = dot(self.rotate_3x3(yaw, Z0), Y0)
        Z2 = dot(self.rotate_3x3(pitch, Y2), Z0)

        roll = atan2( dot(y3, Z2), dot(y3, Y2))


        return (deg2rad(lat), deg2rad(lon), alt, roll, pitch, yaw)


    def ecef2ned(self, ecef, origin):
        """Converts ecef coordinates into local tangent plane where the
        origin is the origin in ecef coordinates.
        Input: ecef - (x, y, z) in (m, m, m)
            origin - (x0, y0, z0) in (m, m, m)
        Output: ned - (north, east, down) in (m, m, m)
        """
        llaOrigin = self.ecef2lla(origin)
        lat = deg2rad(llaOrigin[0])
        lon = deg2rad(llaOrigin[1])
        Re2t = array([[-sin(lat)*cos(lon), -sin(lat)*sin(lon), cos(lat)],
                    [-sin(lon), cos(lon), 0],
                    [-cos(lat)*cos(lon), -cos(lat)*sin(lon), -sin(lat)]])
        return list(dot(Re2t, array(ecef) - array(origin)))


    def ecef2pae(self, ecef, origin):
        """Converts the ecef coordinates into a tangent plane with the origin
        privided, returning the range, azimuth, and elevation angles.
        This is a convenience function combining ecef2ned and ned2pae.
        Input: ecef - (x, y, z) in (m, m, m)
            origin - (x0, y0, z0) in (m, m, m)
        Output: pae - (p, alpha, epsilon) in (m, degrees, degrees)
        """
        ned = self.ecef2ned(ecef, origin)
        return self.ned2pae(ned)


    def ecef2utm(self, ecef):
        lla = self.ecef2lla(ecef)
        utm, info = self.lla2utm(lla)
        return utm, info


    def ecefvec2nedvec(self, lat, lon):
        """
        Returns the rotation matrix to translate coordinate systems between
        ECEF and NED.
        
        Inputs: latitude and longitude in radians

        Outputs: the unit vector matrix of the NED coordinate system with
        respect to the ECEF coordinate system:

            np.array( [ [ N0, N1, N2],
                        [ E0, E1, E2],
                        [ D0, D1, D2]
                      ]
                    )
        """

        return array([[-sin(lat)*cos(lon), -sin(lat)*sin(lon), cos(lat) ],
                      [-sin(lon)         , cos(lon)          , 0        ],
                      [-cos(lat)*cos(lon), -cos(lat)*sin(lon), -sin(lat)]
                     ]
                    )


    def lla2ecef(self, lla):
        """
        Convert lat, lon, alt to Earth-centered, Earth-fixed coordinates.
        Input: lla - (lat, lon, alt) in (decimal degrees, decimal degees, m)
        Output: ecef - (x, y, z) in (m, m, m)
        """
        # Decompose the input
        lat = deg2rad(lla[0])
        lon = deg2rad(lla[1])
        alt = lla[2]

        # Calculate length of the normal to the ellipsoid
        N = self.wgs84.a / sqrt(1 - (self.wgs84.e * sin(lat))**2)

        # Calculate ecef coordinates
        x = (N + alt) * cos(lat) * cos(lon)
        y = (N + alt) * cos(lat) * sin(lon)
        z = (N * (1 - self.wgs84.e**2) + alt) * sin(lat)

        # Return the ecef coordinates
        return (x, y, z)


    def lla2gcc(self, lla, geoOrigin=''):
        """
        Same as lls2ecef, but accepts an X3D-style geoOrigin string for 
        subtraction of it in ecef (gcc) cooridinates
        """
        if geoOrigin:
            lon0, lat0, a0 = [float(c) for c in geoOrigin.split()]
            x0, y0, z0 = self.lla2ecef((lat0, lon0, a0))
        else:
            x0, y0, z0 = 0, 0, 0

        x, y, z = self.lla2ecef(lla)

        return (x - x0, y - y0, z -z0)


    def lla2utm(self, lla):
        """Converts lat, lon, alt to Universal Transverse Mercator coordinates
        Input: lla - (lat, lon, alt) in (decimal degrees, decimal degrees, m)
        Output: utm - (easting, northing, upping) in (m, m, m)
            info - (zone, scale factor)
        Algorithm from:
            Snyder, J. P., Map Projections-A Working Manual, U.S. Geol. Surv.
                Prof. Pap., 1395, 1987
        Code segments from pygps project, Russ Nelson"""
        #Decompose lla
        lat = lla[0]
        lon = lla[1]
        alt = lla[2]
        #Determine the zone number
        zoneNumber = int((lon+180.)/6) + 1
        #Special zone for Norway
        if (56. <= lat < 64.) and (3. <= lon < 12.):
            zoneNumber = 32
        #Special zones for Svalbard
        if 72. <= lat < 84.:
            if 0. <= lon < 9.: zoneNumber = 31
            elif 9. <= lon < 21.: zoneNumber = 33
            elif 21. <= lon < 33.: zoneNumber = 35
            elif 33. <= lon < 42.: zoneNumber = 37
        #Format the zone
        zone = "%d%c" % (zoneNumber, self.utmLetterDesignator(lat))
        #Determine longitude origin
        lonOrigin = (zoneNumber - 1) * 6 - 180 + 3
        #Convert to radians
        latRad = deg2rad(lat)
        lonRad = deg2rad(lon)
        lonOriginRad = deg2rad(lonOrigin)
        #Conversion constants
        k0 = 0.9996
        eSquared = self.wgs84.e**2
        ePrimeSquared = eSquared/(1.-eSquared)
        N = self.wgs84.a/sqrt(1.-eSquared*sin(latRad)**2)
        T = tan(latRad)**2
        C = ePrimeSquared*cos(latRad)**2
        A = (lonRad - lonOriginRad)*cos(latRad)
        M = self.wgs84.a*( \
            (1. - \
                eSquared/4. - \
                3.*eSquared**2/64. - \
                5.*eSquared**3/256)*latRad - \
            (3.*eSquared/8. + \
                3.*eSquared**2/32. + \
                45.*eSquared**3/1024.)*sin(2.*latRad) + \
            (15.*eSquared**2/256. + \
                45.*eSquared**3/1024.)*sin(4.*latRad) - \
            (35.*eSquared**3/3072.)*sin(6.*latRad))
        M0 = 0.
        #Calculate coordinates
        x = k0*N*( \
            A+(1-T+C)*A**3/6. + \
            (5.-18.*T+T**2+72.*C-58.*ePrimeSquared)*A**5/120.) + 500000.
        y = k0*( \
            M-M0+N*tan(latRad)*( \
                A**2/2. + \
                (5.-T+9.*C+4.*C**2)*A**4/24. + \
                (61.-58.*T+T**2+600.*C-330.*ePrimeSquared)*A**6/720.))
        #Calculate scale factor
        k = k0*(1 + \
            (1+C)*A**2/2. + \
            (5.-4.*T+42.*C+13.*C**2-28.*ePrimeSquared)*A**4/24. + \
            (61.-148.*T+16.*T**2)*A**6/720.)
        utm = [x, y, alt]
        info = [zone, k]
        return utm, info


    def llarpy2ecef(self, lat, lon, alt, roll, pitch, yaw):
        """
        Convert an entities latitude, longitude, altitude, pitch, roll, and yaw
        into DIS standard ECEF coordinates and Euler angles.

        Inputs:
            lat   : latitude of the entity in radians
            lon   : longitude of the entity in radians
            alt   : altitude of the entity in meters
            roll  : roll of the entity in radians
            pitch : pitch of the entity in radians
            yaw   : yaw (heading) of the entity in radians

        Output:
            (X, Y, Z, psi, theta, phi) where:
              X     : entities ECEF X coordinate in meters
              Y     : entities ECEF Y coordinate in meters
              Z     : entities ECEF Z coordinate in meters
              psi   : entities rotation around the ECEF Z axis
              theta : entities rotation around the ECEF Y axis
              phi   : entities rotation around the ECEF X axis
        """

        # get ECEF X, Y, Z from lat, lon, alt
        X, Y, Z = self.lla2ecef((rad2deg(lat), rad2deg(lon), alt))

        # get the local NED unit vectors wrt the ECEF coordinate system
        a0 = self.ecefvec2nedvec(lat, lon)

        # Note: N = x0, E = y0, D = z0
        x0 = a0[0]
        y0 = a0[1]
        z0 = a0[2]

        # first rotation array, z0 by yaw rads
        rot_array_1 = self.rotate_3x3(yaw, z0)

        # rotate
        x1 = dot(rot_array_1, x0)
        y1 = dot(rot_array_1, y0)
        z1 = dot(rot_array_1, z0)

        # second rotation array, y1 by pitch rads
        rot_array_2 = self.rotate_3x3(pitch, y1)

        # rotate
        x2 = dot(rot_array_2, x1)
        y2 = dot(rot_array_2, y1)
        z2 = dot(rot_array_2, z1)

        # third rotation array, x2 by roll rads
        rot_array_3 = self.rotate_3x3(roll, x2)

        # rotate
        x3 = dot(rot_array_3, x2)
        y3 = dot(rot_array_3, y2)
        z3 = dot(rot_array_3, z2)

        # define ECEF unit vectors
        X0 = array([1, 0, 0])
        Y0 = array([0, 1, 0])
        Z0 = array([0, 0, 1])

        # calculate psi and theta
        psi = atan2( dot(x3, Y0), dot(x3, X0) )
        theta = atan2( -dot(x3, Z0), sqrt( (dot(x3, X0)) ** 2 + (dot(x3, Y0)) **2 ) )

        # calculate phi
        Y2 = dot(self.rotate_3x3(psi, Z0), Y0)
        Z2 = dot(self.rotate_3x3(theta, Y2), Z0)

        phi = atan2( dot(y3, Z2), dot(y3, Y2))

        return (X, Y, Z, psi, theta, phi)


    def ned2ecef(self, ned, origin):
        """Converts ned local tangent plane coordinates into ecef coordinates
        using origin as the ecef point of tangency.
        Input: ned - (north, east, down) in (m, m, m)
            origin - (x0, y0, z0) in (m, m, m)
        Output: ecef - (x, y, z) in (m, m, m)
        """
        llaOrigin = self.ecef2lla(origin)
        lat = deg2rad(llaOrigin[0])
        lon = deg2rad(llaOrigin[1])
        Rt2e = array([[-sin(lat)*cos(lon), -sin(lon), -cos(lat)*cos(lon)],
                    [-sin(lat)*sin(lon), cos(lon), -cos(lat)*sin(lon)],
                    [cos(lat), 0., -sin(lat)]])
        return list(dot(Rt2e, array(ned)) + array(origin))

    def ned2pae(self, ned):
        """Converts the local north, east, down coordinates into range, azimuth,
        and elevation angles
        Input: ned - (north, east, down) in (m, m, m)
        Output: pae - (p, alpha, epsilon) in (m, degrees, degrees)
        """
        p = euclideanDistance(ned)
        alpha = atan2(ned[1], ned[0])
        epsilon = atan2(-ned[2], sqrt(ned[0]**2 + ned[1]**2))
        return [p, rad2deg(alpha), rad2deg(epsilon)]


    def rotate_3x3(self, theta, normal_vec):
        """
        Returns a rotation matrix to rotate a 3x3 matrix theta degrees around
        normal_vec axis of rotation. Theta is in rads and normal vec is a 3x1
        matrix pointing along the axis of rotation.

        Example: get the rotation matrix to rotate a vector 30 degrees around the
                 z-axis:

                    rot_mat = rotate_3x3(30 * pi / 180, np.array([[0], [0], [1]]))

        Note: dot product a vector with the result of this function to perform
              the rotation.
        """

        n_v_t = normal_vec.transpose()

        n_x = array([[      0  , -normal_vec[2], normal_vec[1] ],
                     [normal_vec[2] ,       0  , -normal_vec[0]],
                     [-normal_vec[1], normal_vec[0] ,   0      ]
                    ]
                   )


        I = identity(3)

        nnt = normal_vec * self.transpose(normal_vec)

        return (1 - cos(theta)) * nnt + cos(theta) * I + sin(theta) * n_x


    def transpose(self, arr):
        """ 
        numpy doesn't want to transpose a 3x1 vector into a 1x3 vector. So
        we'll do it ourselves.
        """

        return array( [[arr[0]], [arr[1]], [arr[2]]])


    def utmLetterDesignator(self, lat):
        """Returns the latitude zone of the UTM coordinates"""
        if -80 <= lat < -72: return 'C'
        elif -72 <= lat < -64: return 'D'
        elif -64 <= lat < -56: return 'E'
        elif -56 <= lat < -48: return 'F'
        elif -48 <= lat < -40: return 'G'
        elif -40 <= lat < -32: return 'H'
        elif -32 <= lat < -24: return 'J'
        elif -24 <= lat < -16: return 'K'
        elif -16 <= lat < -8: return 'L'
        elif -8 <= lat < 0: return 'M'
        elif 0 <= lat < 8: return 'N'
        elif 8 <= lat < 16: return 'P'
        elif 16 <= lat < 24: return 'Q'
        elif 24 <= lat < 32: return 'R'
        elif 32 <= lat < 40: return 'S'
        elif 40 <= lat < 48: return 'T'
        elif 48 <= lat < 56: return 'U'
        elif 56 <= lat < 64: return 'V'
        elif 64 <= lat < 72: return 'W'
        elif 72 <= lat < 80: return 'X'
        else: return 'Z'


if __name__ == "__main__":
    wgs84 = WGS84()
    gps = GPS()
    lla = (34. + 0/60. + 0.00174/3600.,
        -117. - 20./60. - 0.84965/3600.,
        251.702)
    print("lla: {}".format(lla))
    ecef = gps.lla2ecef(lla)
    print("ecef: {}".format(ecef))
    print("lla: {}".format(gps.ecef2lla(ecef)))
