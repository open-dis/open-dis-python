from enum import Enum

from .euler_angles import EulerAngles
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_information_interaction_family_pdu import EntityInformationInteractionFamilyPdu
from .vector3float import Vector3Float
from .vector3double import Vector3Double
from .variable_parameter import VariableParameter
from .entity_id import EntityID

class EntityStateUpdatePdu( EntityInformationInteractionFamilyPdu ):
    """7.2.5. Nonstatic information about a particular entity may be communicated by issuing an Entity State Update PDU. 5.3.5."""

    def __init__(self):
        """ Initializer for EntityStateUpdatePdu"""
        super().__init__()
        """ This field shall identify the entity issuing the PDU, and shall be represented by an Entity Identifier record (see 6.2.28)."""
        self.entityID = EntityID()
        """ Padding"""
        self.padding1 = 0
        """ This field shall specify the number of variable parameters present. This field shall be represented by an 8-bit unsigned integer (see Annex I)."""
        self.numberOfVariableParameters = 0
        """ This field shall specify an entity's linear velocity. The coordinate system for an entity's linear velocity depends on the dead reckoning algorithm used. This field shall be represented by a Linear Velocity Vector record [see 6.2.95 item c)])."""
        self.entityLinearVelocity = Vector3Float()
        """ This field shall specify an entity's physical location in the simulated world and shall be represented by a World Coordinates record (see 6.2.97)."""
        self.entityLocation = Vector3Double()
        """ This field shall specify an entity's orientation with units of radians and shall be represented by an Euler Angles record (see 6.2.33)."""
        self.entityOrientation = EulerAngles()
        """ This field shall specify the dynamic changes to the entity's appearance attributes. This field shall be represented by an Entity Appearance record (see 6.2.26)."""
        self.entityAppearance = 0
        """ This field shall specify the parameter values for each Variable Parameter record that is included (see 6.2.93 and Annex I)."""
        self._variableParameters = []
        self.pduType = DisPduType.entity_state_update


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
    ///         Comment : This field shall specify the parameter values for each Variable Parameter record that is included (see 6.2.93 and Annex I).
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
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "NumberOfVariableParameters : " + str(len(self._variableParameters)) + "\n"
        outputString += "EntityLinearVelocity :" + "\n" + self.entityLinearVelocity.to_string() + "\n"
        outputString += "EntityLocation :" + "\n" + self.entityLocation.to_string() + "\n"
        outputString += "EntityOrientation :" + "\n" + self.entityOrientation.to_string() + "\n"
        outputString += "EntityAppearance : " + str(self.entityAppearance) + "\n"
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
        super( EntityStateUpdatePdu, self ).serialize(outputStream)
        self.entityID.serialize(outputStream)
        outputStream.write_byte(int(self.padding1))
        outputStream.write_byte( len(self._variableParameters))
        self.entityLinearVelocity.serialize(outputStream)
        self.entityLocation.serialize(outputStream)
        self.entityOrientation.serialize(outputStream)
        outputStream.write_int(int(self.entityAppearance))
        for anObj in self._variableParameters:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( EntityStateUpdatePdu, self).parse(inputStream)
        self.entityID.parse(inputStream)
        self.padding1 = inputStream.read_byte()
        self.numberOfVariableParameters = inputStream.read_byte()
        self.entityLinearVelocity.parse(inputStream)
        self.entityLocation.parse(inputStream)
        self.entityOrientation.parse(inputStream)
        self.entityAppearance = inputStream.read_int()
        for idx in range(0, self.numberOfVariableParameters):
            element = VariableParameter()
            element.parse(inputStream)
            self._variableParameters.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 8

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



