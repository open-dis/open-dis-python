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
udpSocket.settimeout(3) # exit if we get nothing in this many seconds

print("Created UDP socket {}".format(UDP_PORT))

gps = GPS();

def recv():
    data = udpSocket.recv(1024) # buffer size in bytes

    aPdu = createPdu(data);

    print("Received Pdu type {}, {} bytes".format(aPdu.pduType, len(data)), flush=True)

    if aPdu.pduType == 1: #PduTypeDecoders.EntityStatePdu:
        loc = (aPdu.entityLocation.x, aPdu.entityLocation.y, aPdu.entityLocation.z)
        lla = gps.ecef2lla(loc)
        print("Pdu location is {} {} {}".format(lla[0], lla[1], lla[2]))


while True:
    recv()
