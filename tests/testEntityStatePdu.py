#!python

import unittest
import io

from opendis.dis7 import *
from opendis.PduFactory import *

class TestEntityStatePdu(unittest.TestCase):

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
        self.assertEqual(42, espdu.entityID.site)
        self.assertEqual(4, espdu.entityID.application)
        self.assertEqual(26, espdu.entityID.entity)

        # Force ID
        self.assertEqual(1, espdu.forceId)

        # Articulation Parameters
        self.assertEqual(0, espdu.articulationParameters.size)

        # Entity Type (aka DIS Enumeration)
        self.assertEqual(1, espdu.entityType.entityKind)
        self.assertEqual(1, espdu.entityType.domain)
        self.assertEqual(39, espdu.entityType.country)
        self.assertEqual(7, espdu.entityType.category)
        self.assertEqual(2, espdu.entityType.subcategory)
        self.assertEqual(1, espdu.entityType.spec)
        self.assertEqual(0, espdu.entityType.extra)

        # Alternative Entity Type
        self.assertEqual(1, espdu.alternativeEntityType.entityKind)
        self.assertEqual(1, espdu.alternativeEntityType.domain)
        self.assertEqual(39, espdu.alternativeEntityType.country)
        self.assertEqual(7, espdu.alternativeEntityType.category)
        self.assertEqual(2, espdu.alternativeEntityType.subcategory)
        self.assertEqual(1, espdu.alternativeEntityType.spec)
        self.assertEqual(0, espdu.alternativeEntityType.extra)

        # Entity Linear Velocity
        self.assertEqual(0, espdu.entityLinearVelocity.x, 0)
        self.assertEqual(0, espdu.entityLinearVelocity.y, 0)
        self.assertEqual(0, espdu.entityLinearVelocity.z, 0)

        # Entity Location
        self.assertEqual(4374082.80485589, espdu.entityLocation.x, 0.001)
        self.assertEqual(1667679.95730107, espdu.entityLocation.y, 0.001)
        self.assertEqual(4318284.36890269, espdu.entityLocation.z, 0.001)

        # Entity Orientation
        self.assertEqual(1.93505, espdu.entityOrientation.psi, 0.001)
        self.assertEqual(0, espdu.entityOrientation.theta, 0.001)
        self.assertEqual(-2.31924, espdu.entityOrientation.phi, 0.001)

        # Entity Appearance
        self.assertEqual(0, espdu.entityAppearance_paintScheme)
        self.assertEqual(0, espdu.entityAppearance_mobility)
        self.assertEqual(0, espdu.entityAppearance_firepower)

        # Dead Reckoning Parameters
        # TODO self.assertEqual(???, espdu.deadReckoningParameters)
        
        # Entity Marking
        self.assertEqual("26        ", espdu.marking.characters)

if __name__ == '__main__':
    unittest.main()
