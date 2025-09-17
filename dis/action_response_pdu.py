from enum import Enum

from .siso_ref_010.enums.action_response_request_status import ActionResponseRequestStatus
from .simulation_management_family_pdu import SimulationManagementFamilyPdu
from .variable_datum import VariableDatum
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .fixed_datum import FixedDatum

class ActionResponsePdu( SimulationManagementFamilyPdu ):
    """Section 7.5.8. When an entity receives an Action Request PDU, that entity shall acknowledge the receipt of the Action Request PDU with an Action Response PDU. See 5.6.5.8."""

    def __init__(self):
        """ Initializer for ActionResponsePdu"""
        super().__init__()
        """ Request ID that is unique"""
        self.requestID = 0
        # /** Status of response uid 72 */
        self.requestStatus = ActionResponseRequestStatus.default

        """ Number of fixed datum records"""
        self.numberOfFixedDatumRecords = 0
        """ Number of variable datum records, handled automatically by marshaller at run time (and not modifiable by end-user programmers)"""
        self.numberOfVariableDatumRecords = 0
        """ fixed length list of fixed datums"""
        self._fixedDatums = []
        """ variable length list of variable length datums"""
        self._variableDatums = []
        self.pduType = DisPduType.action_response


    def get_numberOfFixedDatumRecords(self):
        return len(self._fixedDatums)
    def set_numberOfFixedDatumRecords(self, value):
        numberOfFixedDatumRecords = value


    def get_numberOfVariableDatumRecords(self):
        return len(self._variableDatums)
    def set_numberOfVariableDatumRecords(self, value):
        numberOfVariableDatumRecords = value


    def get_fixedDatums(self):
        return self._fixedDatums
    def set_fixedDatums(self, value):
        self._fixedDatums = value
    fixedDatums = property(get_fixedDatums, set_fixedDatums)


    def add_fixedDatums(self, value : FixedDatum):
        self._fixedDatums.append(value)


    """
    ///            Name : fixedDatums
    ///             UID : 
    ///            Type : FixedDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : fixed length list of fixed datums
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_variableDatums(self):
        return self._variableDatums
    def set_variableDatums(self, value):
        self._variableDatums = value
    variableDatums = property(get_variableDatums, set_variableDatums)


    def add_variableDatums(self, value : VariableDatum):
        self._variableDatums.append(value)


    """
    ///            Name : variableDatums
    ///             UID : 
    ///            Type : VariableDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of variable length datums
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
        outputString += "RequestID : " + str(self.requestID) + "\n"
        outputString += "ActionResponseRequestStatus : " + self.requestStatus.get_description + "(" + (str(int(self.requestStatus))) + ")" + "\n"
        outputString += "NumberOfFixedDatumRecords : " + str(len(self._fixedDatums)) + "\n"
        outputString += "NumberOfVariableDatumRecords : " + str(len(self._variableDatums)) + "\n"
        outputString += "FixedDatums : " + "\n"
        for idx in range(0, len(self._fixedDatums)):
            outputString += self._fixedDatums[idx].to_string()

        outputString += "VariableDatums : " + "\n"
        for idx in range(0, len(self._variableDatums)):
            outputString += self._variableDatums[idx].to_string()

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
        super( ActionResponsePdu, self ).serialize(outputStream)
        outputStream.write_int(int(self.requestID))
        self.serialize_enum(self.requestStatus,outputStream)
        outputStream.write_int( len(self._fixedDatums))
        outputStream.write_int( len(self._variableDatums))
        for anObj in self._fixedDatums:
            anObj.serialize(outputStream)

        for anObj in self._variableDatums:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( ActionResponsePdu, self).parse(inputStream)
        self.requestID = inputStream.read_int()
        self.requestStatus = ActionResponseRequestStatus.get_enum(self.parse_enum(self.requestStatus,inputStream))
        self.numberOfFixedDatumRecords = inputStream.read_int()
        self.numberOfVariableDatumRecords = inputStream.read_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self._fixedDatums.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self._variableDatums.append(element)


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



