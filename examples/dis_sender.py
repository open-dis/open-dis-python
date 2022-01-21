#!python

__author__ = "DMcG"
__date__ = "$Jun 23, 2015 10:27:29 AM$"

import socket
import time
import sys, os
from io import BytesIO

# add the parent directory rather than installing via setup.py
sys.path.append(os.path.join(sys.path[0],'..'))

from opendis.pythonDis import EntityStatePdu
from opendis.DataOutputStream import DataOutputStream
from opendis.RangeCoordinates import GPS

UDP_PORT = 3001
DESTINATION_ADDRESS = "127.0.0.1"

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

gps = GPS() # conversion helper

def send():
    pdu = EntityStatePdu()
    pdu.entityID.entityID = 42
    pdu.entityID.siteID = 17
    pdu.entityID.applicationID = 23

    montereyLocation = gps.lla2ecef((36.6, -121.9, 1) ) # lat lon altitude of Monterey, CA, USA.
    pdu.entityLocation.x = montereyLocation[0]
    pdu.entityLocation.y = montereyLocation[1]
    pdu.entityLocation.z = montereyLocation[2]

    memoryStream = BytesIO()
    outputStream = DataOutputStream(memoryStream)
    pdu.serialize(outputStream)
    data = memoryStream.getvalue()

    while True:
        udpSocket.sendto(data, (DESTINATION_ADDRESS, UDP_PORT))
        print("Sent {}. {} bytes".format(pdu.__class__.__name__, len(data)))
        time.sleep(60)

send()
