#!python

__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 12:10:26 PM$"

import socket
import time
from typing import cast

from opendis.dis7 import *
from opendis.RangeCoordinates import *
from opendis.PduFactory import createPdu

UDP_PORT = 3001

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpSocket.bind(("", UDP_PORT))

print("Listening for DIS on UDP socket {}".format(UDP_PORT))

gps = GPS()

def recv():
    print('Reading from socket...')

    data = udpSocket.recv(1024) # buffer size in bytes
    pdu = createPdu(data)

    pduTypeName = pdu.__class__.__name__

    if pdu.pduType == 1: # PduTypeDecoders.EntityStatePdu:
        pdu = cast(EntityStatePdu, pdu)  # for static checkers
        loc = (pdu.entityLocation.x, 
               pdu.entityLocation.y, 
               pdu.entityLocation.z,
               pdu.entityOrientation.psi,
               pdu.entityOrientation.theta,
               pdu.entityOrientation.phi
               )

        body = gps.ecef2llarpy(*loc)

        print("Received {}\n".format(pduTypeName)
              + " Id        : {}\n".format(pdu.entityID.entityNumber)
              + " Latitude  : {:.2f} degrees\n".format(rad2deg(body[0]))
              + " Longitude : {:.2f} degrees\n".format(rad2deg(body[1]))
              + " Altitude  : {:.0f} meters\n".format(body[2])
              + " Yaw       : {:.2f} degrees\n".format(rad2deg(body[3]))
              + " Pitch     : {:.2f} degrees\n".format(rad2deg(body[4]))
              + " Roll      : {:.2f} degrees\n".format(rad2deg(body[5]))
              )
    else:
        print("Received {}, {} bytes".format(pduTypeName, len(data)), flush=True)

if __name__ == "__main__":
    while True:
        recv()
        time.sleep(.5)