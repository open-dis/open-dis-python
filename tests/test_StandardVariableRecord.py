#!python

import io
import unittest

from opendis.stream import DataOutputStream
from opendis.record.warfare import DirectedEnergyDamage


class TestStandardVariableRecord(unittest.TestCase):

    def test_serialize_length_matches_marshalledSize(self):
        record = DirectedEnergyDamage()
        buffer = io.BytesIO()
        record.serialize(DataOutputStream(buffer))
        self.assertEqual(record.marshalledSize(), len(buffer.getvalue()))
        self.assertEqual(record.recordLength, len(buffer.getvalue()))
        self.assertEqual(40, len(buffer.getvalue()))


if __name__ == "__main__":
    unittest.main()
