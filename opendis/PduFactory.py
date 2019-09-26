__author__ = "mcgredo"
__date__ = "$Jun 25, 2015 11:31:42 AM$"

from .DataInputStream import DataInputStream
from .dis7 import *
from io import BytesIO
import binascii
import io

PduTypeDecoders = {
       1 : EntityStatePdu
    ,  2 : FirePdu
    ,  3 : DetonationPdu
    ,  4 : CollisionPdu
    ,  5 : ServiceRequestPdu
    ,  6 : CollisionElasticPdu
    ,  7 : ResupplyReceivedPdu
    ,  9 : RepairCompletePdu
    , 10 : RepairResponsePdu
    , 11 : CreateEntityPdu
    , 12 : RemoveEntityPdu
    , 13 : StartResumePdu
    , 14 : StopFreezePdu
    , 15 : AcknowledgePdu
    , 16 : ActionRequestPdu
    , 17 : ActionResponsePdu
    , 18 : DataQueryPdu
    , 19 : SetDataPdu
    , 20 : DataPdu
    , 21 : EventReportPdu
    , 22 : CommentPdu
    , 23 : ElectronicEmissionsPdu
    , 24 : DesignatorPdu
    , 25 : TransmitterPdu
    , 26 : SignalPdu
    , 27 : ReceiverPdu
    , 29 : UaPdu
    , 31 : IntercomSignalPdu
    , 32 : IntercomControlPdu
    , 36 : IsPartOfPdu
    , 37 : MinefieldStatePdu
    , 40 : MinefieldResponseNackPdu
    , 41 : PointObjectStatePdu
    , 43 : PointObjectStatePdu
    , 44 : LinearObjectStatePdu
    , 45 : ArealObjectStatePdu
    , 51 : CreateEntityReliablePdu
    , 52 : RemoveEntityReliablePdu
    , 54 : StopFreezeReliablePdu
    , 55 : AcknowledgeReliablePdu
    , 56 : ActionRequestReliablePdu
    , 57 : ActionResponseReliablePdu
    , 58 : DataQueryReliablePdu
    , 59 : SetDataReliablePdu
    , 60 : DataReliablePdu
    , 61 : EventReportReliablePdu
    , 62 : CommentReliablePdu
    , 63 : RecordQueryReliablePdu
    , 66 : CollisionElasticPdu
    , 67 : EntityStateUpdatePdu
    , 69 : EntityDamageStatusPdu
 }


def getPdu(inputStream):
    # The PDU type enumeration is in the 3rd slot
    inputStream.read_unsigned_byte()
    inputStream.read_unsigned_byte()
    pduType = inputStream.read_byte()
    inputStream.stream.seek(-3, 1) # rewind

    if pduType in PduTypeDecoders.keys():
        Decoder = PduTypeDecoders[pduType]
        pdu = Decoder()
        pdu.parse(inputStream)
        return pdu

    # Punt and return none if we don't have a match on anything
    # print("Unable to find a PDU corresponding to PduType {}".format(pduType))

    return None


def createPdu(data):
    """ Create a PDU of the correct type when passed an array of binary data
        input: a bytebuffer of DIS data
        output: a python DIS pdu instance of the correct class"""

    memoryStream = BytesIO(data)
    inputStream = DataInputStream(memoryStream)

    return getPdu(inputStream)


def createPduFromFilePath(filePath):
    """ Utility written for unit tests, but could have other uses too."""
    f = io.open(filePath, "rb")
    inputStream = DataInputStream(f)
    return getPdu(inputStream)
