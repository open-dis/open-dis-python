from enum import Enum

from .siso_ref_010.enums.force_id import ForceID
from .object_identifier import ObjectIdentifier
from .object_type import ObjectType
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .synthetic_environment_family_pdu import SyntheticEnvironmentFamilyPdu
from .simulation_address import SimulationAddress
from .linear_segment_parameter import LinearSegmentParameter

class LinearObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
    """7.10.5 Used to communicate detailed information about the addition/modification of a synthetic environment object that is geometrically anchored to the terrain with one point and has size and orientation."""

    def __init__(self):
        """ Initializer for LinearObjectStatePdu"""
        super().__init__()
        """ Object in synthetic environment"""
        self.objectID = ObjectIdentifier()
        """ Object with which this point object is associated"""
        self.referencedObjectID = ObjectIdentifier()
        """ unique update number of each state transition of an object"""
        self.updateNumber = 0
        # /** force ID provides a unique identifier uid 6 */
        self.forceID = ForceID.default

        """ number of linear segment parameters"""
        self.numberOfLinearSegments = 0
        """ requesterID"""
        self.requesterID = SimulationAddress()
        """ receiver ID provides a unique identifier"""
        self.receivingID = SimulationAddress()
        """ Object type"""
        self.objectType = ObjectType()
        """ Linear segment parameters"""
        self._linearSegmentParameters = []
        self.pduType = DisPduType.linear_object_state


    def get_numberOfLinearSegments(self):
        return len(self._linearSegmentParameters)
    def set_numberOfLinearSegments(self, value):
        numberOfLinearSegments = value


    def get_linearSegmentParameters(self):
        return self._linearSegmentParameters
    def set_linearSegmentParameters(self, value):
        self._linearSegmentParameters = value
    linearSegmentParameters = property(get_linearSegmentParameters, set_linearSegmentParameters)


    def add_linearSegmentParameters(self, value : LinearSegmentParameter):
        self._linearSegmentParameters.append(value)


    """
    ///            Name : linearSegmentParameters
    ///             UID : 
    ///            Type : LinearSegmentParameter
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Linear segment parameters
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
        outputString += "NumberOfLinearSegments : " + str(len(self._linearSegmentParameters)) + "\n"
        outputString += "RequesterID :" + "\n" + self.requesterID.to_string() + "\n"
        outputString += "ReceivingID :" + "\n" + self.receivingID.to_string() + "\n"
        outputString += "ObjectType :" + "\n" + self.objectType.to_string() + "\n"
        outputString += "LinearSegmentParameters : " + "\n"
        for idx in range(0, len(self._linearSegmentParameters)):
            outputString += self._linearSegmentParameters[idx].to_string()

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
        super( LinearObjectStatePdu, self ).serialize(outputStream)
        self.objectID.serialize(outputStream)
        self.referencedObjectID.serialize(outputStream)
        outputStream.write_short(int(self.updateNumber))
        self.serialize_enum(self.forceID,outputStream)
        outputStream.write_byte( len(self._linearSegmentParameters))
        self.requesterID.serialize(outputStream)
        self.receivingID.serialize(outputStream)
        self.objectType.serialize(outputStream)
        for anObj in self._linearSegmentParameters:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( LinearObjectStatePdu, self).parse(inputStream)
        self.objectID.parse(inputStream)
        self.referencedObjectID.parse(inputStream)
        self.updateNumber = inputStream.read_short()
        self.forceID = ForceID.get_enum(self.parse_enum(self.forceID,inputStream))
        self.numberOfLinearSegments = inputStream.read_byte()
        self.requesterID.parse(inputStream)
        self.receivingID.parse(inputStream)
        self.objectType.parse(inputStream)
        for idx in range(0, self.numberOfLinearSegments):
            element = LinearSegmentParameter()
            element.parse(inputStream)
            self._linearSegmentParameters.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 9

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



