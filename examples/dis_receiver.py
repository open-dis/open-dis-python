#!python

__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 12:10:26 PM$"

import socket, time, sys, os, array

# add the parent directory rather than installing via setup.py
sys.path.append(os.path.join(sys.path[0],'..'))

from opendis.pythonDis import EntityStatePdu
from opendis.RangeCoordinates import GPS
from opendis.PduFactory import createPdu

UDP_PORT = 3001

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpSocket.bind(("", UDP_PORT))

print("Listening for DIS on UDP socket {}".format(UDP_PORT))

gps = GPS();

def recv():
    data = udpSocket.recv(1024) # buffer size in bytes
    pdu = createPdu(data);
    pduTypeName = pdu.__class__.__name__

    if pdu.pduType == 1: #PduTypeDecoders.EntityStatePdu:
        loc = (pdu.entityLocation.x, pdu.entityLocation.y, pdu.entityLocation.z)
        lla = gps.ecef2lla(loc)
        print("Received {}. Id: {}, Location: {} {} {}".format(pduTypeName, pdu.entityID.entityID, lla[0], lla[1], lla[2]))
    else:
        print("Received {}, {} bytes".format(pduTypeName, len(data)), flush=True)


while True:
    recv()
