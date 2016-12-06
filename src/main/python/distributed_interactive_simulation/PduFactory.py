#! /usr/bin/python
__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 11:31:42 AM$"

from dis7 import *
from DataInputStream import DataInputStream
from DataOutputStream import DataOutputStream
from io import BytesIO
import binascii


class PduFactory(object):
    
    def createPdu(self, data):
        """ Create a PDU of the correct type when passed an array of binary data
            input: a bytebuffer of DIS data
            output: a python DIS pdu instance of the correct class"""
            
        memoryStream = BytesIO(data)
        inputStream = DataInputStream(memoryStream)
        
        # The PDU type enumeration is in the 3rd slot
        pduType = binascii.b2a_qp(data[2])
        
        if pduType == "=01":
            pdu = EntityStatePdu()
            pdu.parse(inputStream)
            return pdu
        
        elif pduType == "=02":
            pdu = FirePdu()
            pdu.parse(inputStream)
            return pdu
        
        elif pduType == "=03":
            pdu = DetonationPdu()
            pdu.parse(inputStream)
            return pdu
        
        elif pduType == "=04":
            pdu = CollisionPdu()
            pdu.parse(inputStream)
            return pdu
            
        # ....Other PDUs here....
        
        # Punt and return none if we don't have a match on anything
        print "Unable to find a PDU corresponding to PduType ", pduType
        
        return None
        
if __name__ == "__main__":
    print "Hello World";
