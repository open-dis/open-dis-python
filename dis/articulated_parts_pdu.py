from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .live_entity_family_pdu import LiveEntityFamilyPdu
from .variable_parameter import VariableParameter
from .entity_id import EntityID

class ArticulatedPartsPdu( LiveEntityFamilyPdu ):
    """9.4.4 Communicate information about an entity’s articulated and attached parts."""

    def __init__(self):
        """ Initializer for ArticulatedPartsPdu"""
        super().__init__()
        # liveEntityId is an undescribed parameter... 
        self.liveEntityId = EntityID()
        self.numberOfParameterRecords = 0
        self._variableParameters = []
        self.pduType = DisPduType.articulated_parts


    def get_numberOfParameterRecords(self):
        return len(self._variableParameters)
    def set_numberOfParameterRecords(self, value):
        numberOfParameterRecords = value


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
    ///         Comment : null
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
        outputString += "LiveEntityId :" + "\n" + self.liveEntityId.to_string() + "\n"
        outputString += "NumberOfParameterRecords : " + str(len(self._variableParameters)) + "\n"
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
        super( ArticulatedPartsPdu, self ).serialize(outputStream)
        self.liveEntityId.serialize(outputStream)
        outputStream.write_byte( len(self._variableParameters))
        for anObj in self._variableParameters:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( ArticulatedPartsPdu, self).parse(inputStream)
        self.liveEntityId.parse(inputStream)
        self.numberOfParameterRecords = inputStream.read_byte()
        for idx in range(0, self.numberOfParameterRecords):
            element = VariableParameter()
            element.parse(inputStream)
            self._variableParameters.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 3

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



