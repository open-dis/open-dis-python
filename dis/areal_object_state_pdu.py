from enum import Enum

from .siso_ref_010.enums.force_id import ForceID
from .object_identifier import ObjectIdentifier
from .object_type import ObjectType
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .synthetic_environment_family_pdu import SyntheticEnvironmentFamilyPdu
from .siso_ref_010.enums.object_state_modification_areal_object import ObjectStateModificationArealObject
from .vector3double import Vector3Double
from .simulation_address import SimulationAddress

class ArealObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
    """7.10.6 Used to communicate detailed information about the addition/modification of a synthetic environment object that is geometrically anchored to the terrain with a set of three or more points that come to a closure."""

    def __init__(self):
        """ Initializer for ArealObjectStatePdu"""
        super().__init__()
        """ Object in synthetic environment"""
        self.objectID = ObjectIdentifier()
        """ Object with which this point object is associated"""
        self.referencedObjectID = ObjectIdentifier()
        """ unique update number of each state transition of an object"""
        self.updateNumber = 0
        # /** force ID provides a unique identifier uid 6 */
        self.forceID = ForceID.default

        # modifications enumeration uid 242
        self.modifications = ObjectStateModificationArealObject()

        """ Object type"""
        self.objectType = ObjectType()
        """ Object appearance"""
        self.specificObjectAppearance = 0
        """ Object appearance"""
        self.generalObjectAppearance = 0
        """ Number of points"""
        self.numberOfPoints = 0
        """ requesterID"""
        self.requesterID = SimulationAddress()
        """ receiver ID provides a unique identifier"""
        self.receivingID = SimulationAddress()
        """ location of object"""
        self._objectLocation = []
        self.pduType = DisPduType.areal_object_state


    def get_numberOfPoints(self):
        return len(self._objectLocation)
    def set_numberOfPoints(self, value):
        numberOfPoints = value


    def get_objectLocation(self):
        return self._objectLocation
    def set_objectLocation(self, value):
        self._objectLocation = value
    objectLocation = property(get_objectLocation, set_objectLocation)


    def add_objectLocation(self, value : Vector3Double):
        self._objectLocation.append(value)


    """
    ///            Name : objectLocation
    ///             UID : 
    ///            Type : Vector3Double
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : location of object
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """



    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "ObjectID :" + "\n" + self.objectID.to_string() + "\n"
        outputString += "ReferencedObjectID :" + "\n" + self.referencedObjectID.to_string() + "\n"
        outputString += "UpdateNumber : " + str(self.updateNumber) + "\n"
        outputString += "ForceID : " + self.forceID.get_description + "(" + (str(int(self.forceID))) + ")" + "\n"
        outputString += "ObjectStateModificationArealObject : " + str(self.modifications) + "\n"
        outputString += "ObjectType :" + "\n" + self.objectType.to_string() + "\n"
        outputString += "SpecificObjectAppearance : " + str(self.specificObjectAppearance) + "\n"
        outputString += "GeneralObjectAppearance : " + str(self.generalObjectAppearance) + "\n"
        outputString += "NumberOfPoints : " + str(len(self._objectLocation)) + "\n"
        outputString += "RequesterID :" + "\n" + self.requesterID.to_string() + "\n"
        outputString += "ReceivingID :" + "\n" + self.receivingID.to_string() + "\n"
        outputString += "ObjectLocation : " + "\n"
        for idx in range(0, len(self._objectLocation)):
            outputString += self._objectLocation[idx].to_string()

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
        super( ArealObjectStatePdu, self ).serialize(outputStream)
        self.objectID.serialize(outputStream)
        self.referencedObjectID.serialize(outputStream)
        outputStream.write_short(int(self.updateNumber))
        self.serialize_enum(self.forceID,outputStream)
        outputStream.write_unsigned_int(int(self.modifications.asbyte))
        self.objectType.serialize(outputStream)
        outputStream.write_int(int(self.specificObjectAppearance))
        outputStream.write_short(int(self.generalObjectAppearance))
        outputStream.write_short( len(self._objectLocation))
        self.requesterID.serialize(outputStream)
        self.receivingID.serialize(outputStream)
        for anObj in self._objectLocation:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( ArealObjectStatePdu, self).parse(inputStream)
        self.objectID.parse(inputStream)
        self.referencedObjectID.parse(inputStream)
        self.updateNumber = inputStream.read_short()
        self.forceID = ForceID.get_enum(self.parse_enum(self.forceID,inputStream))
        self.modifications.asbyte = inputStream.read_unsigned_int()
        self.objectType.parse(inputStream)
        self.specificObjectAppearance = inputStream.read_int()
        self.generalObjectAppearance = inputStream.read_short()
        self.numberOfPoints = inputStream.read_short()
        self.requesterID.parse(inputStream)
        self.receivingID.parse(inputStream)
        for idx in range(0, self.numberOfPoints):
            element = Vector3Double()
            element.parse(inputStream)
            self._objectLocation.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 12

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



