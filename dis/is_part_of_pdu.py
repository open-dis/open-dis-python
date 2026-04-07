from enum import Enum

from .entity_type import EntityType
from .named_location_identification import NamedLocationIdentification
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .vector3float import Vector3Float
from .entity_id import EntityID
from .relationship import Relationship
from .entity_management_family_pdu import EntityManagementFamilyPdu

class IsPartOfPdu( EntityManagementFamilyPdu ):
    """5.9.5 Used to request hierarchical linkage of separately hosted simulation entities"""

    def __init__(self):
        """ Initializer for IsPartOfPdu"""
        super().__init__()
        """ ID of entity originating PDU"""
        self.orginatingEntityID = EntityID()
        """ ID of entity receiving PDU"""
        self.receivingEntityID = EntityID()
        """ relationship of joined parts"""
        self.relationship = Relationship()
        """ location of part; centroid of part in host's coordinate system. x=range, y=bearing, z=0"""
        self.partLocation = Vector3Float()
        """ named location"""
        self.namedLocationID = NamedLocationIdentification()
        """ entity type"""
        self.partEntityType = EntityType()
        self.pduType = DisPduType.ispartof

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "OrginatingEntityID :" + "\n" + self.orginatingEntityID.to_string() + "\n"
        outputString += "ReceivingEntityID :" + "\n" + self.receivingEntityID.to_string() + "\n"
        outputString += "Relationship :" + "\n" + self.relationship.to_string() + "\n"
        outputString += "PartLocation :" + "\n" + self.partLocation.to_string() + "\n"
        outputString += "NamedLocationID :" + "\n" + self.namedLocationID.to_string() + "\n"
        outputString += "PartEntityType :" + "\n" + self.partEntityType.to_string() + "\n"
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
        super( IsPartOfPdu, self ).serialize(outputStream)
        self.orginatingEntityID.serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.relationship.serialize(outputStream)
        self.partLocation.serialize(outputStream)
        self.namedLocationID.serialize(outputStream)
        self.partEntityType.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( IsPartOfPdu, self).parse(inputStream)
        self.orginatingEntityID.parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.relationship.parse(inputStream)
        self.partLocation.parse(inputStream)
        self.namedLocationID.parse(inputStream)
        self.partEntityType.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 6

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



