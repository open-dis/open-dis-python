#!python

import unittest
import io
import os

from opendis.dis7 import *
from opendis.PduFactory import *
from opendis.DataOutputStream import DataOutputStream

class TestSignalPdu(unittest.TestCase):

    def setUp(self):
        testdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(testdir)

    def test_parse_and_serialize(self):
        with open('SignalPdu.raw', 'rb') as f:
            data = f.read()
            pdu = createPdu(data)
            self.assertEqual(6, pdu.protocolVersion)
            self.assertEqual(1, pdu.exerciseID)
            self.assertEqual(26, pdu.pduType)
            self.assertEqual(4, pdu.protocolFamily)
            #self.assertEqual(0, pdu.timestamp)
            self.assertEqual(1056, pdu.length)

            self.assertEqual(1677, pdu.entityID.siteID)
            self.assertEqual(1678, pdu.entityID.applicationID)
            self.assertEqual(169, pdu.entityID.entityID )
            self.assertEqual(1, pdu.radioID)
            self.assertEqual(4, pdu.encodingScheme)
            self.assertEqual(0, pdu.tdlType)
            self.assertEqual(22050, pdu.sampleRate)
            self.assertEqual(8192, pdu.dataLength)
            self.assertEqual(512, pdu.samples)
            self.assertEqual(8192/8, len(pdu.data))

            memoryStream = io.BytesIO()
            outputStream = DataOutputStream(memoryStream)
            pdu.serialize(outputStream)

            self.assertEqual(data, memoryStream.getvalue())


if __name__ == '__main__':
    unittest.main()
