#! /usr/bin/python

__author__ = "DMcG"
__date__ = "$Jun 23, 2015 10:27:29 AM$"

import socket
import time
import sys

from io import BytesIO

from distributed_interactive_simulation.DataOutputStream import DataOutputStream
from distributed_interactive_simulation.dis7 import EntityStatePdu
from distributed_interactive_simulation.RangeCoordinates import GPS

UDP_PORT = 3001
DESTINATION_ADDRESS = "192.168.2.11"

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

    udpSocket.sendto(data, (DESTINATION_ADDRESS, UDP_PORT))
    print("Sent espdu. {} bytes".format(len(data)))


send()
