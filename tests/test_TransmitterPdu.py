#!python

import unittest
import io
import os

from opendis.dis7 import *
from opendis.PduFactory import *

class TestTransmitterPdu(unittest.TestCase):

    def setUp(self):
        testdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(testdir)

    def test_parse(self):
        pdu = createPduFromFilePath("TransmitterPdu.raw")
        self.assertEqual(6, pdu.protocolVersion)
        self.assertEqual(1, pdu.exerciseID)
        self.assertEqual(25, pdu.pduType)
        self.assertEqual(4, pdu.protocolFamily)
        #self.assertEqual(0, pdu.timestamp)
        self.assertEqual(104, pdu.length)

        self.assertEqual(1677, pdu.radioReferenceID.siteID)
        self.assertEqual(1678, pdu.radioReferenceID.applicationID)
        self.assertEqual(169, pdu.radioReferenceID.entityID )
        self.assertEqual(1, pdu.radioNumber)
        self.assertEqual(2, pdu.transmitState)
        self.assertEqual(10000000000, pdu.frequency)
        self.assertEqual(20000, pdu.transmitFrequencyBandwidth)
        self.assertEqual(35, pdu.power)

if __name__ == '__main__':
    unittest.main()
