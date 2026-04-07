from enum import Enum

from .siso_ref_010.enums.repair_complete_repair import RepairCompleteRepair
from .logistics_family_pdu import LogisticsFamilyPdu
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_id import EntityID

class RepairResponsePdu( LogisticsFamilyPdu ):
    """5.5.11 used by the receiving entity to acknowledge the receipt of a Repair Complete PDU"""

    def __init__(self):
        """ Initializer for RepairResponsePdu"""
        super().__init__()
        """ Entity that requested repairs.  See 6.2.28"""
        self.receivingEntityID = EntityID()
        """ Entity that is repairing.  See 6.2.28"""
        self.repairingEntityID = EntityID()
        # /** Result of repair operation uid 64 */
        self.repairResult = RepairCompleteRepair.default

        """ padding"""
        self.padding1 = 0
        """ padding"""
        self.padding2 = 0
        self.pduType = DisPduType.repair_response

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "ReceivingEntityID :" + "\n" + self.receivingEntityID.to_string() + "\n"
        outputString += "RepairingEntityID :" + "\n" + self.repairingEntityID.to_string() + "\n"
        outputString += "RepairResponseRepairResult : " + self.repairResult.get_description + "(" + (str(int(self.repairResult))) + ")" + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
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
        super( RepairResponsePdu, self ).serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.repairingEntityID.serialize(outputStream)
        self.serialize_enum(self.repairResult,outputStream)
        outputStream.write_byte(int(self.padding1))
        outputStream.write_short(int(self.padding2))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( RepairResponsePdu, self).parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.repairingEntityID.parse(inputStream)
        self.repairResult = RepairResponseRepairResult.get_enum(self.parse_enum(self.repairResult,inputStream))
        self.padding1 = inputStream.read_byte()
        self.padding2 = inputStream.read_short()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 5

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



