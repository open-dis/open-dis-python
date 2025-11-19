from enum import Enum

from .logistics_family_pdu import LogisticsFamilyPdu
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_id import EntityID

class ResupplyCancelPdu( LogisticsFamilyPdu ):
    """5.5.8 Used to communicate the canceling of a resupply service provided through logistics support."""

    def __init__(self):
        """ Initializer for ResupplyCancelPdu"""
        super().__init__()
        """ Requesting entity, Section 7.4.5"""
        self.receivingEntityID = EntityID()
        """ Supplying entity, Section 7.4.5"""
        self.supplyingEntityID = EntityID()
        self.pduType = DisPduType.resupply_cancel

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "ReceivingEntityID :" + "\n" + self.receivingEntityID.to_string() + "\n"
        outputString += "SupplyingEntityID :" + "\n" + self.supplyingEntityID.to_string() + "\n"
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
        super( ResupplyCancelPdu, self ).serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.supplyingEntityID.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( ResupplyCancelPdu, self).parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.supplyingEntityID.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 2

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



