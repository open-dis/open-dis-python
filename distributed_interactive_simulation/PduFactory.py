#! /usr/bin/python
__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 11:31:42 AM$"

from distributed_interactive_simulation.dis7 import PduTypeDecoders
from dis_io.DataInputStream import DataInputStream
from dis_io.DataOutputStream import DataOutputStream
from io import BytesIO
import binascii

def createPdu(data):
  """ Create a PDU of the correct type when passed an array of binary data
      input: a bytebuffer of DIS data
      output: a python DIS pdu instance of the correct class"""

  memoryStream = BytesIO(data)
  inputStream = DataInputStream(memoryStream)

  # The PDU type enumeration is in the 3rd slot
  pduType = data[2]

  if pduType in PduTypeDecoders.keys():
      Decoder = PduTypeDecoders[pduType]
      pdu = Decoder()
      pdu.parse(inputStream)
      return pdu

  # Punt and return none if we don't have a match on anything
  # print("Unable to find a PDU corresponding to PduType {}".format(pduType))

  return None


if __name__ == "__main__":
    print("Hello World")
