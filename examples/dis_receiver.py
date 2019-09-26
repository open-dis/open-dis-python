#!python

__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 12:10:26 PM$"

import socket
import time
import sys
import array

from opendis.dis7 import *
from opendis.RangeCoordinates import GPS
from opendis.PduFactory import createPdu

UDP_PORT = 3001

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udpSocket.bind(("", UDP_PORT))
print("Created UDP socket {}".format(UDP_PORT))

gps = GPS();

def recv():
    data, addr = udpSocket.recvfrom(1024) # buffer size in bytes
    print("Received {} bytes".format(len(data)))

    aPdu = createPdu(data);
    if aPdu.pduType == 1: #PduTypeDecoders.EntityStatePdu:
        loc = (aPdu.entityLocation.x, aPdu.entityLocation.y, aPdu.entityLocation.z)
        lla = gps.ecef2lla(loc)
        print("Pdu location is {} {} {}".format(lla[0], lla[1], lla[2]))


recv()
