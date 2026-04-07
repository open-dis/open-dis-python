from enum import Enum

from .entity_identifier import EntityIdentifier
from .siso_ref_010.enums.entity_association_association_type import EntityAssociationAssociationType
from .vector3double import Vector3Double

class Association( object ):
    """An entity's associations with other entities and/or locations. For each association, this record shall specify the type of the association, the associated entity's EntityID and/or the associated location's world coordinates. This record may be used (optionally) in a transfer transaction to send internal state data from the divesting simulation to the acquiring simulation (see 5.9.4). This record may also be used for other purposes. Section 6.2.9"""

    def __init__(self):
        """ Initializer for Association"""
        # /** This field shall indicate the type of association. It shall be represented by an 8-bit enumeration. Values for this field are found in Section 14 of SISO-REF-010 330 */
        self.associationType = EntityAssociationAssociationType.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ identity of associated entity. If none, NO_SPECIFIC_ENTITY"""
        self.associatedEntityID = EntityIdentifier()
        """ location, in world coordinates"""
        self.associatedLocation = Vector3Double()

    def to_string(self) ->str:
        outputString = ""
        outputString += "EntityAssociationAssociationType : " + self.associationType.get_description + "(" + (str(int(self.associationType))) + ")" + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "AssociatedEntityID :" + "\n" + self.associatedEntityID.to_string() + "\n"
        outputString += "AssociatedLocation :" + "\n" + self.associatedLocation.to_string() + "\n"
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
        self.serialize_enum(self.associationType,outputStream)
        outputStream.write_byte(int(self.padding))
        self.associatedEntityID.serialize(outputStream)
        self.associatedLocation.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.associationType = EntityAssociationAssociationType.get_enum(self.parse_enum(self.associationType,inputStream))
        self.padding = inputStream.read_byte()
        self.associatedEntityID.parse(inputStream)
        self.associatedLocation.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 4

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



