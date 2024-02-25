#!python

import unittest
import io
import os

from opendis.dis7 import *
from opendis.PduFactory import *

class TestElectromagneticEmissionPdu(unittest.TestCase):

    def setUp(self):
        testdir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(testdir)

    def test_parse(self):
        pdu = createPduFromFilePath("ElectromagneticEmissionPdu-single-system.raw")
        self.assertEqual(6, pdu.protocolVersion)
        self.assertEqual(1, pdu.exerciseID)
        self.assertEqual(23, pdu.pduType)
        self.assertEqual(6, pdu.protocolFamily)
        #self.assertEqual(0, pdu.timestamp)
        self.assertEqual(108, pdu.length)

        self.assertEqual(23, pdu.emittingEntityID.siteID)
        self.assertEqual(1, pdu.emittingEntityID.applicationID)
        self.assertEqual(2, pdu.emittingEntityID.entityID)

        self.assertEqual(23, pdu.eventID.simulationAddress.site)
        self.assertEqual(1, pdu.eventID.simulationAddress.application)
        self.assertEqual(8, pdu.eventID.eventNumber)

        self.assertEqual(0, pdu.stateUpdateIndicator)
        self.assertEqual(1, pdu.numberOfSystems)
        self.assertEqual(0, pdu.paddingForEmissionsPdu)
        self.assertEqual(1, pdu.systems[0].numberOfBeams)
        self.assertEqual(0, pdu.systems[0].location.x)
        self.assertEqual(0, pdu.systems[0].location.y)
        self.assertEqual(0, pdu.systems[0].location.z)
        self.assertEqual(15, pdu.systems[0].beamRecords[0].beamDataLength)
        self.assertEqual(1, pdu.systems[0].beamRecords[0].beamIDNumber)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].beamParameterIndex)
        #self.assertAlmostEqual(9000000000, pdu.systems[0].fundamentalParameterData.frequency)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].fundamentalParameterData.frequencyRange)
        self.assertEqual(70000, pdu.systems[0].beamRecords[0].fundamentalParameterData.effectiveRadiatedPower)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].fundamentalParameterData.pulseRepetitionFrequency)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].fundamentalParameterData.pulseWidth)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].fundamentalParameterData.beamAzimuthCenter)
        #self.assertAlmostEqual(3.14159, pdu.systems[0].fundamentalParameterData.beamAzimuthSweep)
        #self.assertEqual(0.741765, pdu.systems[0].fundamentalParameterData.beamElevationCenter )
        #self.assertEqual(0.829031, pdu.systems[0].fundamentalParameterData.beamElevationSweep)
        self.assertEqual(1, pdu.systems[0].beamRecords[0].fundamentalParameterData.beamSweepSync)
        self.assertEqual(4, pdu.systems[0].beamRecords[0].beamFunction)
        self.assertEqual(1, pdu.systems[0].beamRecords[0].numberOfTargetsInTrackJam)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].highDensityTrackJam)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].jammingModeSequence)

        self.assertEqual(23, pdu.systems[0].beamRecords[0].trackJamRecords[0].entityID.siteID)
        self.assertEqual(1, pdu.systems[0].beamRecords[0].trackJamRecords[0].entityID.applicationID)
        self.assertEqual(1, pdu.systems[0].beamRecords[0].trackJamRecords[0].entityID.entityID)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].trackJamRecords[0].emitterNumber)
        self.assertEqual(0, pdu.systems[0].beamRecords[0].trackJamRecords[0].beamNumber)
        

if __name__ == '__main__':
    unittest.main()
