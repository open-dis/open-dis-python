from enum import Enum

from .siso_ref_010.enums.force_id import ForceID
from .siso_ref_010.enums.object_state_modification_point_object import ObjectStateModificationPointObject
from .object_identifier import ObjectIdentifier
from .euler_angles import EulerAngles
from .siso_ref_010.enums.object_state_appearance_general import ObjectStateAppearanceGeneral
from .object_type import ObjectType
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .synthetic_environment_family_pdu import SyntheticEnvironmentFamilyPdu
from .vector3double import Vector3Double
from .entity_id import EntityID
from .simulation_address import SimulationAddress

class PointObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
    """7.10.4 Used to communicate detailed information about the addition/modification of a synthetic environment object that is geometrically anchored to the terrain with a single point."""

    def __init__(self):
        """ Initializer for PointObjectStatePdu"""
        super().__init__()
        """ Object in synthetic environment"""
        self.objectID = EntityID()
        """ Object with which this point object is associated"""
        self.referencedObjectID = ObjectIdentifier()
        """ unique update number of each state transition of an object"""
        self.updateNumber = 0
        # /** force ID provides a unique identifier uid 6 */
        self.forceID = ForceID.default

        # modifications uid 240
        self.modifications = ObjectStateModificationPointObject()

        """ Object type"""
        self.objectType = ObjectType()
        """ Object location"""
        self.objectLocation = Vector3Double()
        """ Object orientation"""
        self.objectOrientation = EulerAngles()
        """ Specific object apperance"""
        self.specificObjectAppearance = 0
        # General object apperance uid 229
        self.generObjectAppearance = ObjectStateAppearanceGeneral()

        self.padding1 = 0
        """ requesterID"""
        self.requesterID = SimulationAddress()
        """ receiver ID provides a unique identifier"""
        self.receivingID = SimulationAddress()
        """ padding"""
        self.pad2 = 0
        self.pduType = DisPduType.point_object_state

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "ObjectID :" + "\n" + self.objectID.to_string() + "\n"
        outputString += "ReferencedObjectID :" + "\n" + self.referencedObjectID.to_string() + "\n"
        outputString += "UpdateNumber : " + str(self.updateNumber) + "\n"
        outputString += "ForceID : " + self.forceID.get_description + "(" + (str(int(self.forceID))) + ")" + "\n"
        outputString += "ObjectStateModificationPointObject : " + str(self.modifications) + "\n"
        outputString += "ObjectType :" + "\n" + self.objectType.to_string() + "\n"
        outputString += "ObjectLocation :" + "\n" + self.objectLocation.to_string() + "\n"
        outputString += "ObjectOrientation :" + "\n" + self.objectOrientation.to_string() + "\n"
        outputString += "SpecificObjectAppearance : " + str(self.specificObjectAppearance) + "\n"
        outputString += "ObjectStateAppearanceGeneral : " + str(self.generObjectAppearance) + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "RequesterID :" + "\n" + self.requesterID.to_string() + "\n"
        outputString += "ReceivingID :" + "\n" + self.receivingID.to_string() + "\n"
        outputString += "Pad2 : " + str(self.pad2) + "\n"
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
        super( PointObjectStatePdu, self ).serialize(outputStream)
        self.objectID.serialize(outputStream)
        self.referencedObjectID.serialize(outputStream)
        outputStream.write_int(int(self.updateNumber))
        self.serialize_enum(self.forceID,outputStream)
        outputStream.write_unsigned_int(int(self.modifications.asbyte))
        self.objectType.serialize(outputStream)
        self.objectLocation.serialize(outputStream)
        self.objectOrientation.serialize(outputStream)
        outputStream.write_int(int(self.specificObjectAppearance))
        outputStream.write_unsigned_int(int(self.generObjectAppearance.asbyte))
        outputStream.write_short(int(self.padding1))
        self.requesterID.serialize(outputStream)
        self.receivingID.serialize(outputStream)
        outputStream.write_int(int(self.pad2))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( PointObjectStatePdu, self).parse(inputStream)
        self.objectID.parse(inputStream)
        self.referencedObjectID.parse(inputStream)
        self.updateNumber = inputStream.read_int()
        self.forceID = ForceID.get_enum(self.parse_enum(self.forceID,inputStream))
        self.modifications.asbyte = inputStream.read_unsigned_int()
        self.objectType.parse(inputStream)
        self.objectLocation.parse(inputStream)
        self.objectOrientation.parse(inputStream)
        self.specificObjectAppearance = inputStream.read_int()
        self.generObjectAppearance.asbyte = inputStream.read_unsigned_int()
        self.padding1 = inputStream.read_short()
        self.requesterID.parse(inputStream)
        self.receivingID.parse(inputStream)
        self.pad2 = inputStream.read_int()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 14

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



