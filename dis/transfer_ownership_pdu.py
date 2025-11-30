from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.required_reliability_service import RequiredReliabilityService
from .siso_ref_010.enums.transfer_control_transfer_type import TransferControlTransferType
from .record_specification import RecordSpecification
from .entity_id import EntityID
from .entity_management_family_pdu import EntityManagementFamilyPdu

class TransferOwnershipPdu( EntityManagementFamilyPdu ):
    """ Information initiating the dyanic allocation and control of simulation entities between two simulation applications."""

    def __init__(self):
        """ Initializer for TransferOwnershipPdu"""
        super().__init__()
        """ ID of entity originating request"""
        self.originatingEntityID = EntityID()
        """ ID of entity receiving request"""
        self.receivingEntityID = EntityID()
        """ ID of request"""
        self.requestID = 0
        # /** required level of reliability service. uid 74 */
        self.requiredReliabilityService = RequiredReliabilityService.default

        # /** type of transfer desired uid 224 */
        self.transferType = TransferControlTransferType.default

        """ The entity for which control is being requested to transfer"""
        self.transferEntityID = EntityID()
        # recordSets is an undescribed parameter... 
        self.recordSets = RecordSpecification()
        self.pduType = DisPduType.transfer_ownership

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "OriginatingEntityID :" + "\n" + self.originatingEntityID.to_string() + "\n"
        outputString += "ReceivingEntityID :" + "\n" + self.receivingEntityID.to_string() + "\n"
        outputString += "RequestID : " + str(self.requestID) + "\n"
        outputString += "RequiredReliabilityService : " + self.requiredReliabilityService.get_description + "(" + (str(int(self.requiredReliabilityService))) + ")" + "\n"
        outputString += "TransferControlTransferType : " + self.transferType.get_description + "(" + (str(int(self.transferType))) + ")" + "\n"
        outputString += "TransferEntityID :" + "\n" + self.transferEntityID.to_string() + "\n"
        outputString += "RecordSets :" + "\n" + self.recordSets.to_string() + "\n"
        return outputString

    def __str__(self):
        return self.to_string()

    def serialize_enum(self, enumValue, outputStream):
        enumSize = enumValue.get_marshaled_size()
        marshallers = {8 : 'byte', 16 : 'short', 32 : 'int'}
        marshalFunction = getattr(outputStream, 'write_unsigned_' + marshallers[enumSize])
        result = marshalFunction(int(enumValue))

    def parse_enum(self, enumValue, intputStream) -> int:
        enumSize = enumValue.get_marshaled_size()
        marshallers = {8 : 'byte', 16 : 'short', 32 : 'int'}
        marshalFunction = getattr(intputStream, 'read_unsigned_' + marshallers[enumSize])
        return marshalFunction()

    def serialize(self, outputStream):
        """serialize the class """
        super( TransferOwnershipPdu, self ).serialize(outputStream)
        self.originatingEntityID.serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        outputStream.write_int(int(self.requestID))
        self.serialize_enum(self.requiredReliabilityService,outputStream)
        self.serialize_enum(self.transferType,outputStream)
        self.transferEntityID.serialize(outputStream)
        self.recordSets.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( TransferOwnershipPdu, self).parse(inputStream)
        self.originatingEntityID.parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.requestID = inputStream.read_int()
        self.requiredReliabilityService = RequiredReliabilityService.get_enum(self.parse_enum(self.requiredReliabilityService,inputStream))
        self.transferType = TransferControlTransferType.get_enum(self.parse_enum(self.transferType,inputStream))
        self.transferEntityID.parse(inputStream)
        self.recordSets.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 7

    def get_attribute_count(self) -> int:
        attrList = list()
        for attr in dir(self):
            if not callable(getattr(self, attr)):
                if not attr.startswith("__"):
                    if not hasattr(self.__class__.__base__(), attr):
                        attrList.append(attr)
        return len(attrList)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def diff(self,other) -> set:
        diffs = set()
        for key, value in self.__dict__.items():
            value2 = other.__dict__[key]
            if (value != value2):
                if type(value) is list:
                    diffs.add((key, str(value)))
                    diffs.add((key, str(value2)))
                elif (type(value).__module__ == "builtins"):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, Enum)):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, object)):
                    diffs.update(value.diff(value2))
                else:
                    diffs.add((key, value))
                    diffs.add((key, value2))
        return(diffs)



