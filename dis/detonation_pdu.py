from enum import Enum

from .siso_ref_010.enums.detonation_result import DetonationResult
from .munition_descriptor import MunitionDescriptor
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .vector3float import Vector3Float
from .warfare_family_pdu import WarfareFamilyPdu
from .vector3double import Vector3Double
from .variable_parameter import VariableParameter
from .entity_id import EntityID
from .event_identifier import EventIdentifier

class DetonationPdu( WarfareFamilyPdu ):
    """7.3.3 Used to communicate the detonation or impact of munitions, as well as non-munition explosions, the burst or initial bloom of chaff, and the ignition of a flare."""

    def __init__(self):
        """ Initializer for DetonationPdu"""
        super().__init__()
        """ ID of the entity that shot"""
        self.sourceEntityID = EntityID()
        """ ID of the entity that is being shot at"""
        self.targetEntityID = EntityID()
        """ ID of the expendable entity, Section 7.3.3 """
        self.explodingEntityID = EntityID()
        """ ID of event, Section 7.3.3"""
        self.eventID = EventIdentifier()
        """ velocity of the munition immediately before detonation/impact, Section 7.3.3 """
        self.velocity = Vector3Float()
        """ location of the munition detonation, the expendable detonation, Section 7.3.3 """
        self.locationInWorldCoordinates = Vector3Double()
        """ Describes the detonation represented, Section 7.3.3 """
        self.descriptor = MunitionDescriptor()
        """ Velocity of the ammunition, Section 7.3.3 """
        self.locationOfEntityCoordinates = Vector3Float()
        # /** result of the detonation, Section 7.3.3  uid 62 */
        self.detonationResult = DetonationResult.default

        """ How many articulation parameters we have, Section 7.3.3 """
        self.numberOfVariableParameters = 0
        """ padding"""
        self.pad = 0
        """ specify the parameter values for each Variable Parameter record, Section 7.3.3 """
        self._variableParameters = []
        self.pduType = DisPduType.detonation


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
    ///         Comment : specify the parameter values for each Variable Parameter record, Section 7.3.3 
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
        outputString += "SourceEntityID :" + "\n" + self.sourceEntityID.to_string() + "\n"
        outputString += "TargetEntityID :" + "\n" + self.targetEntityID.to_string() + "\n"
        outputString += "ExplodingEntityID :" + "\n" + self.explodingEntityID.to_string() + "\n"
        outputString += "EventID :" + "\n" + self.eventID.to_string() + "\n"
        outputString += "Velocity :" + "\n" + self.velocity.to_string() + "\n"
        outputString += "LocationInWorldCoordinates :" + "\n" + self.locationInWorldCoordinates.to_string() + "\n"
        outputString += "Descriptor :" + "\n" + self.descriptor.to_string() + "\n"
        outputString += "LocationOfEntityCoordinates :" + "\n" + self.locationOfEntityCoordinates.to_string() + "\n"
        outputString += "DetonationResult : " + self.detonationResult.get_description + "(" + (str(int(self.detonationResult))) + ")" + "\n"
        outputString += "NumberOfVariableParameters : " + str(len(self._variableParameters)) + "\n"
        outputString += "Pad : " + str(self.pad) + "\n"
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
        super( DetonationPdu, self ).serialize(outputStream)
        self.sourceEntityID.serialize(outputStream)
        self.targetEntityID.serialize(outputStream)
        self.explodingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        self.velocity.serialize(outputStream)
        self.locationInWorldCoordinates.serialize(outputStream)
        self.descriptor.serialize(outputStream)
        self.locationOfEntityCoordinates.serialize(outputStream)
        self.serialize_enum(self.detonationResult,outputStream)
        outputStream.write_byte( len(self._variableParameters))
        outputStream.write_short(int(self.pad))
        for anObj in self._variableParameters:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( DetonationPdu, self).parse(inputStream)
        self.sourceEntityID.parse(inputStream)
        self.targetEntityID.parse(inputStream)
        self.explodingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.velocity.parse(inputStream)
        self.locationInWorldCoordinates.parse(inputStream)
        self.descriptor.parse(inputStream)
        self.locationOfEntityCoordinates.parse(inputStream)
        self.detonationResult = DetonationResult.get_enum(self.parse_enum(self.detonationResult,inputStream))
        self.numberOfVariableParameters = inputStream.read_byte()
        self.pad = inputStream.read_short()
        for idx in range(0, self.numberOfVariableParameters):
            element = VariableParameter()
            element.parse(inputStream)
            self._variableParameters.append(element)


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



