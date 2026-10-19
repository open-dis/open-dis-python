"""Backwards compatibility of the EntityID name and its flat field names.

The type of EntityStatePdu.entityID changed from the flat EntityID class to
EntityIdentifier (see issue #88). EntityID is an alias of EntityIdentifier
and the flat field names delegate to it, restoring pre-1.1 code without
changing the wire format.
"""

import io
import os
import unittest

from opendis.dis7 import EntityID, EntityIdentifier
from opendis.PduFactory import createPduFromFilePath
from opendis.stream import DataOutputStream


class TestEntityIDCompat(unittest.TestCase):

    def setUp(self):
        testdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(testdir)

    def test_alias_identity(self):
        self.assertIs(EntityID, EntityIdentifier)

    def test_flat_fields_write_through(self):
        entityID = EntityID()
        entityID.siteID = 17
        entityID.applicationID = 23
        entityID.entityID = 42
        self.assertEqual(17, entityID.simulationAddress.site)
        self.assertEqual(23, entityID.simulationAddress.application)
        self.assertEqual(42, entityID.entityNumber)

    def test_wire_format_unchanged(self):
        entityID = EntityID()
        entityID.siteID = 17
        entityID.applicationID = 23
        entityID.entityID = 42
        buffer = io.BytesIO()
        entityID.serialize(DataOutputStream(buffer))
        # site 17, application 23, entity number 42, as three big-endian u16
        self.assertEqual(b"\x00\x11\x00\x17\x00\x2a", buffer.getvalue())

    def test_flat_reads_on_parsed_pdu(self):
        pdu = createPduFromFilePath("EntityStatePdu-26.raw")
        self.assertEqual(42, pdu.entityID.siteID)
        self.assertEqual(4, pdu.entityID.applicationID)
        self.assertEqual(26, pdu.entityID.entityID)


if __name__ == "__main__":
    unittest.main()
