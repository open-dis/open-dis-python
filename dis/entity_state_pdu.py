from enum import Enum

from .euler_angles import EulerAngles
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_information_interaction_family_pdu import EntityInformationInteractionFamilyPdu
from .vector3float import Vector3Float
from .dead_reckoning_parameters import DeadReckoningParameters
from .variable_parameter import VariableParameter
from .entity_id import EntityID
from .siso_ref_010.enums.entity_capability_types import EntityCapabilityTypes
from .siso_ref_010.enums.force_id import ForceID
from .entity_type import EntityType
from .entity_marking import EntityMarking
from .vector3double import Vector3Double
from .siso_ref_010.enums.land_platform_capabilities import LandPlatformCapabilities

class EntityStatePdu( EntityInformationInteractionFamilyPdu ):
    """ 7.2.2. Represents the position and state of one entity in the world. See 5.3.2."""

    def __init__(self):
        """ Initializer for EntityStatePdu"""
        super().__init__()
        """ Unique ID for an entity that is tied to this state information"""
        self.entityID = EntityID()
        # /** What force this entity is affiliated with, eg red, blue, neutral, etc uid 6 */
        self.forceId = ForceID.default

        """ How many variable parameters are in the variable length list. In earlier versions of DIS these were known as articulation parameters"""
        self.numberOfVariableParameters = 0
        """ Describes the type of entity in the world"""
        self.entityType = EntityType()
        # alternativeEntityType is an undescribed parameter... 
        self.alternativeEntityType = EntityType()
        """ Describes the speed of the entity in the world"""
        self.entityLinearVelocity = Vector3Float()
        """ describes the location of the entity in the world"""
        self.entityLocation = Vector3Double()
        """ describes the orientation of the entity, in euler angles with units of radians"""
        self.entityOrientation = EulerAngles()
        """ a series of bit flags that are used to help draw the entity, such as smoking, on fire, etc."""
        self.entityAppearance = 0
        """ parameters used for dead reckoning"""
        self.deadReckoningParameters = DeadReckoningParameters()
        """ 11 characters that can be used for entity identification, debugging, or to draw unique strings on the side of entities in the world"""
        self.marking = EntityMarking()
        # a series of bit flags uid 55
        self.capabilities = LandPlatformCapabilities()

        """ variable length list of variable parameters. In earlier DIS versions this was articulation parameters."""
        self._variableParameters = []
        self.pduType = DisPduType.entity_state


    def get_numberOfVariableParameters(self):
        return len(self._variableParameters)
    def set_numberOfVariableParameters(self, value):
        numberOfVariableParameters = value


    def get_variableParameters(self):
        return self._variableParameters
    def set_variableParameters(self, value):
        self._variableParameters = value
    variableParameters = property(get_variableParameters, set_variableParameters)


    def add_variableParameters(self, value : VariableParameter):
        self._variableParameters.append(value)


    """
    ///            Name : variableParameters
    ///             UID : 
    ///            Type : VariableParameter
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of variable parameters. In earlier DIS versions this was articulation parameters.
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
        outputString += "EntityID :" + "\n" + self.entityID.to_string() + "\n"
        outputString += "ForceID : " + self.forceId.get_description + "(" + (str(int(self.forceId))) + ")" + "\n"
        outputString += "NumberOfVariableParameters : " + str(len(self._variableParameters)) + "\n"
        outputString += "EntityType :" + "\n" + self.entityType.to_string() + "\n"
        outputString += "AlternativeEntityType :" + "\n" + self.alternativeEntityType.to_string() + "\n"
        outputString += "EntityLinearVelocity :" + "\n" + self.entityLinearVelocity.to_string() + "\n"
        outputString += "EntityLocation :" + "\n" + self.entityLocation.to_string() + "\n"
        outputString += "EntityOrientation :" + "\n" + self.entityOrientation.to_string() + "\n"
        outputString += "EntityAppearance : " + str(self.entityAppearance) + "\n"
        outputString += "DeadReckoningParameters :" + "\n" + self.deadReckoningParameters.to_string() + "\n"
        outputString += "Marking :" + "\n" + self.marking.to_string() + "\n"
        outputString += "EntityCapabilities : " + str(self.capabilities) + "\n"
        outputString += "VariableParameters : " + "\n"
        for idx in range(0, len(self._variableParameters)):
            outputString += self._variableParameters[idx].to_string()

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
        super( EntityStatePdu, self ).serialize(outputStream)
        self.entityID.serialize(outputStream)
        self.serialize_enum(self.forceId,outputStream)
        outputStream.write_byte( len(self._variableParameters))
        self.entityType.serialize(outputStream)
        self.alternativeEntityType.serialize(outputStream)
        self.entityLinearVelocity.serialize(outputStream)
        self.entityLocation.serialize(outputStream)
        self.entityOrientation.serialize(outputStream)
        outputStream.write_int(int(self.entityAppearance))
        self.deadReckoningParameters.serialize(outputStream)
        self.marking.serialize(outputStream)
        outputStream.write_unsigned_int(int(self.capabilities.asbyte))
        for anObj in self._variableParameters:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( EntityStatePdu, self).parse(inputStream)
        self.entityID.parse(inputStream)
        self.forceId = ForceID.get_enum(self.parse_enum(self.forceId,inputStream))
        self.numberOfVariableParameters = inputStream.read_byte()
        self.entityType.parse(inputStream)
        self.alternativeEntityType.parse(inputStream)
        self.entityLinearVelocity.parse(inputStream)
        self.entityLocation.parse(inputStream)
        self.entityOrientation.parse(inputStream)
        self.entityAppearance = inputStream.read_int()
        self.deadReckoningParameters.parse(inputStream)
        self.marking.parse(inputStream)
        self.capabilities.asbyte = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfVariableParameters):
            element = VariableParameter()
            element.parse(inputStream)
            self._variableParameters.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 13

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



