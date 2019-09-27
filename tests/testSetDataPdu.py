#!python

import unittest
import io

from opendis.dis7 import *
from opendis.PduFactory import *

class TestSetDataPdu(unittest.TestCase):

    def test_parse(self):
        pdu = createPduFromFilePath("SetDataPdu-vbs-script-cmd.raw")
        self.assertEqual(6, pdu.protocolVersion)
        self.assertEqual(1, pdu.exerciseID)
        self.assertEqual(19, pdu.pduType)
        self.assertEqual(5, pdu.protocolFamily)
        self.assertEqual(0, pdu.timestamp)
        self.assertEqual(56, pdu.length)

        self.assertEqual(0, pdu.numberOfFixedDatumRecords)
        self.assertEqual(1, pdu.numberOfVariableDatumRecords)
        self.assertEqual(0, len(pdu.fixedDatums))
        self.assertEqual(1, len(pdu.variableDatums))

        datum = pdu.variableDatums[0]
        self.assertEqual(1, datum.variableDatumID)
        self.assertEqual(64, datum.variableDatumLength)
        self.assertEqual(b'allunits', bytes(datum.variableData))

    def test_parse_multi_variable_datums(self):
        pdu = createPduFromFilePath("SetDataPdu-multi-variable-datums.raw")
        self.assertEqual(112, pdu.length)

        self.assertEqual(3, pdu.numberOfVariableDatumRecords)
        self.assertEqual(3, len(pdu.variableDatums))


if __name__ == '__main__':
    unittest.main()
