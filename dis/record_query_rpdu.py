from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.required_reliability_service import RequiredReliabilityService
from .siso_ref_010.enums.record_query_revent_type import RecordQueryREventType
from .simulation_management_with_reliability_family_pdu import SimulationManagementWithReliabilityFamilyPdu
from .record_query_specification import RecordQuerySpecification

class RecordQueryRPdu( SimulationManagementWithReliabilityFamilyPdu ):
    """5.12.4.14 Used to communicate a request for data in record format."""

    def __init__(self):
        """ Initializer for RecordQueryRPdu"""
        super().__init__()
        """ request ID provides a unique identifier"""
        self.requestID = 0
        # /** level of reliability service used for this transaction uid 74 */
        self.requiredReliabilityService = RequiredReliabilityService.default

        """ padding"""
        self.pad1 = 0
        # /** event type uid 334 */
        self.eventType = RecordQueryREventType.default

        """ time"""
        self.time = 0
        """ numberOfRecords"""
        self.numberOfRecords = 0
        """ record IDs"""
        self._recordIDs = []
        self.pduType = DisPduType.record_query_reliable


    def get_numberOfRecords(self):
        return len(self._recordIDs)
    def set_numberOfRecords(self, value):
        numberOfRecords = value


    def get_recordIDs(self):
        return self._recordIDs
    def set_recordIDs(self, value):
        self._recordIDs = value
    recordIDs = property(get_recordIDs, set_recordIDs)


    def add_recordIDs(self, value : RecordQuerySpecification):
        self._recordIDs.append(value)


    """
    ///            Name : recordIDs
    ///             UID : 
    ///            Type : RecordQuerySpecification
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : record IDs
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
        outputString += "RecordQueryREventType : " + self.eventType.get_description + "(" + (str(int(self.eventType))) + ")" + "\n"
        outputString += "Time : " + str(self.time) + "\n"
        outputString += "NumberOfRecords : " + str(len(self._recordIDs)) + "\n"
        outputString += "RecordIDs : " + "\n"
        for idx in range(0, len(self._recordIDs)):
            outputString += self._recordIDs[idx].to_string()

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
        super( RecordQueryRPdu, self ).serialize(outputStream)
        outputStream.write_int(int(self.requestID))
        self.serialize_enum(self.requiredReliabilityService,outputStream)
        outputStream.write_byte(int(self.pad1))
        self.serialize_enum(self.eventType,outputStream)
        outputStream.write_int(int(self.time))
        outputStream.write_int( len(self._recordIDs))
        for anObj in self._recordIDs:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( RecordQueryRPdu, self).parse(inputStream)
        self.requestID = inputStream.read_int()
        self.requiredReliabilityService = RequiredReliabilityService.get_enum(self.parse_enum(self.requiredReliabilityService,inputStream))
        self.pad1 = inputStream.read_byte()
        self.eventType = RecordQueryREventType.get_enum(self.parse_enum(self.eventType,inputStream))
        self.time = inputStream.read_int()
        self.numberOfRecords = inputStream.read_int()
        for idx in range(0, self.numberOfRecords):
            element = RecordQuerySpecification()
            element.parse(inputStream)
            self._recordIDs.append(element)


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



