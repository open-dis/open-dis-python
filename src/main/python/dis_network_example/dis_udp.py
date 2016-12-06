#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "DMcG"
__date__ = "$Jun 23, 2015 10:27:29 AM$"

import socket
import time
import sys


sys.path.append("../dis_io")
sys.path.append("../distributed_interactive_simulation")

from DataInputStream import DataInputStream
from DataOutputStream import DataOutputStream

from dis7 import EntityStatePdu
from io import BytesIO
from RangeCoordinates import GPS

    
UDP_PORT = 3000
DESTINATION_ADDRESS = "172.20.159.255"

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:  
    pdu = EntityStatePdu()
    pdu.entityID.entityID = 42
    pdu.entityID.siteID = 17
    pdu.entityID.applicationID = 23

    gps = GPS()
    
    montereyLocation = gps.lla2ecef((36.6, 121.9, 1) )
    pdu.entityLocation.x = montereyLocation[0]
    pdu.entityLocation.y = montereyLocation[1]
    pdu.entityLocation.z = montereyLocation[2]
    
    print "DIS location for monterey is ", montereyLocation, " ", pdu.entityLocation.x
    
    otherLocation = (montereyLocation[0], montereyLocation[1], montereyLocation[2] + 1)
    ned = gps.ecef2ned(montereyLocation, otherLocation)
    print "NED location ", ned
        
        
    #members = [attr for attr in dir(pdu) if not callable(attr) and not attr.startswith("__")]
    #print members
    
    memoryStream = BytesIO()
    outputStream = DataOutputStream(memoryStream)
    pdu.serialize(outputStream)
    data = memoryStream.getvalue()
#    print "data length is ", len(data), " ", binascii.b2a_qp(data)
#    print "pdu protocol version is ", pdu.protocolVersion
    
    udpSocket.sendto(data, (DESTINATION_ADDRESS, 3001))
    time.sleep(1)
    print "sent message"

if __name__ == "__main__":
    print "Hello World";
