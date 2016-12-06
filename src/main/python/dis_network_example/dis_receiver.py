#! /usr/bin/python


__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 12:10:26 PM$"

import socket
import time
import sys

sys.path.append("../dis_io")
sys.path.append("../distributed_interactive_simulation")

from DataInputStream import DataInputStream
from DataOutputStream import DataOutputStream

from dis7 import *
from RangeCoordinates import GPS
from PduFactory import PduFactory
import binascii

UDP_PORT = 3001
DESTINATION_ADDRESS = "172.20.159.255"
LOCAL_IP = "172.20.152.34"

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
udpSocket.bind(("", UDP_PORT))
print "Created UDP socket ", UDP_PORT

pduFactory = PduFactory()

while True:
    data, addr = udpSocket.recvfrom(1024) # buffer size is 1024 bytes
    #print "received message:", len(data), " ", binascii.b2a_qp(data)
    aPdu = pduFactory.createPdu(data);
    print "Pdu location is ", aPdu.entityLocation.x, aPdu.entityLocation.y, aPdu.entityLocation.z

if __name__ == "__main__":
    print "Hello World";
