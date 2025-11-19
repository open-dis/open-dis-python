from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.required_reliability_service import RequiredReliabilityService
from .simulation_management_with_reliability_family_pdu import SimulationManagementWithReliabilityFamilyPdu
from .record_specification import RecordSpecification

class SetRecordRPdu( SimulationManagementWithReliabilityFamilyPdu ):
    """5.12.4.15 Used to set or change certain parameter values. These parameter values are contained within a record format as compared to the datum format used in the Set Data-R PDU."""

    def __init__(self):
        """ Initializer for SetRecordRPdu"""
        super().__init__()
        """ request ID provides a unique identifier"""
        self.requestID = 0
        # /** level of reliability service used for this transaction uid 74 */
        self.requiredReliabilityService = RequiredReliabilityService.default

        self.pad1 = 0
        self.pad2 = 0
        self.pad3 = 0
        """ Number of record sets in list"""
        self.numberOfRecordSets = 0
        """ record sets"""
        self._recordSets = []
        self.pduType = DisPduType.set_record_reliable


    def get_numberOfRecordSets(self):
        return len(self._recordSets)
    def set_numberOfRecordSets(self, value):
        numberOfRecordSets = value


    def get_recordSets(self):
        return self._recordSets
    def set_recordSets(self, value):
        self._recordSets = value
    recordSets = property(get_recordSets, set_recordSets)


    def add_recordSets(self, value : RecordSpecification):
        self._recordSets.append(value)


    """
    ///            Name : recordSets
    ///             UID : 
    ///            Type : RecordSpecification
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : record sets
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
        outputString += "RequiredReliabilityService : " + self.requiredReliabilityService.get_description + "(" + (str(int(self.requiredReliabilityService))) + ")" + "\n"
        outputString += "Pad1 : " + str(self.pad1) + "\n"
        outputString += "Pad2 : " + str(self.pad2) + "\n"
        outputString += "Pad3 : " + str(self.pad3) + "\n"
        outputString += "NumberOfRecordSets : " + str(len(self._recordSets)) + "\n"
        outputString += "RecordSets : " + "\n"
        for idx in range(0, len(self._recordSets)):
            outputString += self._recordSets[idx].to_string()

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
        super( SetRecordRPdu, self ).serialize(outputStream)
        outputStream.write_int(int(self.requestID))
        self.serialize_enum(self.requiredReliabilityService,outputStream)
        outputStream.write_byte(int(self.pad1))
        outputStream.write_short(int(self.pad2))
        outputStream.write_int(int(self.pad3))
        outputStream.write_int( len(self._recordSets))
        for anObj in self._recordSets:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( SetRecordRPdu, self).parse(inputStream)
        self.requestID = inputStream.read_int()
        self.requiredReliabilityService = RequiredReliabilityService.get_enum(self.parse_enum(self.requiredReliabilityService,inputStream))
        self.pad1 = inputStream.read_byte()
        self.pad2 = inputStream.read_short()
        self.pad3 = inputStream.read_int()
        self.numberOfRecordSets = inputStream.read_int()
        for idx in range(0, self.numberOfRecordSets):
            element = RecordSpecification()
            element.parse(inputStream)
            self._recordSets.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 7

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



