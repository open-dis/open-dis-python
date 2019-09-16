#! /usr/bin/python

__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 12:10:26 PM$"

import socket
import time
import sys
import array

from distributed_interactive_simulation.dis7 import *
from distributed_interactive_simulation.RangeCoordinates import GPS
from distributed_interactive_simulation.PduFactory import createPdu

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
