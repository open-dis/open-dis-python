#!python

import unittest
import io
import os

from opendis.dis7 import *
from opendis.PduFactory import *

class TestEntityStatePdu(unittest.TestCase):

    def setUp(self):
        testdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(testdir)

    def test_parse(self):
        pdu = createPduFromFilePath("EntityStatePdu-26.raw")
        self.assertEqual(6, pdu.protocolVersion)
        self.assertEqual(7, pdu.exerciseID)
        self.assertEqual(1, pdu.pduType)
        self.assertEqual(1, pdu.protocolFamily)
        #self.assertEqual(0, pdu.timestamp)
        self.assertEqual(144, pdu.length)
        self.assertEqual(0, pdu.padding)

        # Entity ID
        self.assertEqual(42, pdu.entityID.siteID)
        self.assertEqual(4, pdu.entityID.applicationID)
        self.assertEqual(26, pdu.entityID.entityID)

        # Force ID
        self.assertEqual(1, pdu.forceId)

        # Articulation Parameters
        self.assertEqual(0, pdu.numberOfVariableParameters)

        # Entity Type (aka DIS Enumeration)
        self.assertEqual(1, pdu.entityType.entityKind)
        self.assertEqual(1, pdu.entityType.domain)
        self.assertEqual(39, pdu.entityType.country)
        self.assertEqual(7, pdu.entityType.category)
        self.assertEqual(2, pdu.entityType.subcategory)
        self.assertEqual(1, pdu.entityType.specific)
        self.assertEqual(0, pdu.entityType.extra)

        # Alternative Entity Type
        self.assertEqual(1, pdu.alternativeEntityType.entityKind)
        self.assertEqual(1, pdu.alternativeEntityType.domain)
        self.assertEqual(39, pdu.alternativeEntityType.country)
        self.assertEqual(7, pdu.alternativeEntityType.category)
        self.assertEqual(2, pdu.alternativeEntityType.subcategory)
        self.assertEqual(1, pdu.alternativeEntityType.specific)
        self.assertEqual(0, pdu.alternativeEntityType.extra)

        # Entity Linear Velocity
        self.assertEqual(0, pdu.entityLinearVelocity.x, 0)
        self.assertEqual(0, pdu.entityLinearVelocity.y, 0)
        self.assertEqual(0, pdu.entityLinearVelocity.z, 0)

        # Entity Location
        self.assertAlmostEqual(4374082.80485589, pdu.entityLocation.x)
        self.assertAlmostEqual(1667679.95730107, pdu.entityLocation.y)
        self.assertAlmostEqual(4318284.36890269, pdu.entityLocation.z)

        # Entity Orientation
        self.assertAlmostEqual(1.93505, pdu.entityOrientation.psi, 5)
        self.assertAlmostEqual(0, pdu.entityOrientation.theta)
        self.assertAlmostEqual(-2.31924, pdu.entityOrientation.phi, 5)

        # Entity Appearance
        #self.assertEqual(0, pdu.entityAppearance_paintScheme)
        #self.assertEqual(0, pdu.entityAppearance_mobility)
        #self.assertEqual(0, pdu.entityAppearance_firepower)

        # Dead Reckoning Parameters
        # TODO self.assertEqual(???, pdu.deadReckoningParameters)
        
        # Entity Marking
        self.assertEqual("26",pdu.marking.charactersString())


if __name__ == '__main__':
    unittest.main()
