from enum import Enum

from .siso_ref_010.enums.event_report_event_type import EventReportEventType
from .variable_datum import VariableDatum
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .fixed_datum import FixedDatum
from .simulation_management_with_reliability_family_pdu import SimulationManagementWithReliabilityFamilyPdu

class EventReportRPdu( SimulationManagementWithReliabilityFamilyPdu ):
    """5.12.4.12 Contains the same information as found in the Event Report PDU."""

    def __init__(self):
        """ Initializer for EventReportRPdu"""
        super().__init__()
        # /** Event type uid 73 */
        self.eventType = EventReportEventType.default

        """ padding"""
        self.pad1 = 0
        """ Fixed datum record count"""
        self.numberOfFixedDatumRecords = 0
        """ variable datum record count"""
        self.numberOfVariableDatumRecords = 0
        """ Fixed datum records"""
        self._fixedDatumRecords = []
        """ Variable datum records"""
        self._variableDatumRecords = []
        self.pduType = DisPduType.event_report_reliable


    def get_numberOfFixedDatumRecords(self):
        return len(self._fixedDatumRecords)
    def set_numberOfFixedDatumRecords(self, value):
        numberOfFixedDatumRecords = value


    def get_numberOfVariableDatumRecords(self):
        return len(self._variableDatumRecords)
    def set_numberOfVariableDatumRecords(self, value):
        numberOfVariableDatumRecords = value


    def get_fixedDatumRecords(self):
        return self._fixedDatumRecords
    def set_fixedDatumRecords(self, value):
        self._fixedDatumRecords = value
    fixedDatumRecords = property(get_fixedDatumRecords, set_fixedDatumRecords)


    def add_fixedDatumRecords(self, value : FixedDatum):
        self._fixedDatumRecords.append(value)


    """
    ///            Name : fixedDatumRecords
    ///             UID : 
    ///            Type : FixedDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Fixed datum records
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_variableDatumRecords(self):
        return self._variableDatumRecords
    def set_variableDatumRecords(self, value):
        self._variableDatumRecords = value
    variableDatumRecords = property(get_variableDatumRecords, set_variableDatumRecords)


    def add_variableDatumRecords(self, value : VariableDatum):
        self._variableDatumRecords.append(value)


    """
    ///            Name : variableDatumRecords
    ///             UID : 
    ///            Type : VariableDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Variable datum records
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
        outputString += "EventReportEventType : " + self.eventType.get_description + "(" + (str(int(self.eventType))) + ")" + "\n"
        outputString += "Pad1 : " + str(self.pad1) + "\n"
        outputString += "NumberOfFixedDatumRecords : " + str(len(self._fixedDatumRecords)) + "\n"
        outputString += "NumberOfVariableDatumRecords : " + str(len(self._variableDatumRecords)) + "\n"
        outputString += "FixedDatumRecords : " + "\n"
        for idx in range(0, len(self._fixedDatumRecords)):
            outputString += self._fixedDatumRecords[idx].to_string()

        outputString += "VariableDatumRecords : " + "\n"
        for idx in range(0, len(self._variableDatumRecords)):
            outputString += self._variableDatumRecords[idx].to_string()

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
        super( EventReportRPdu, self ).serialize(outputStream)
        self.serialize_enum(self.eventType,outputStream)
        outputStream.write_int(int(self.pad1))
        outputStream.write_int( len(self._fixedDatumRecords))
        outputStream.write_int( len(self._variableDatumRecords))
        for anObj in self._fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self._variableDatumRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( EventReportRPdu, self).parse(inputStream)
        self.eventType = EventReportEventType.get_enum(self.parse_enum(self.eventType,inputStream))
        self.pad1 = inputStream.read_int()
        self.numberOfFixedDatumRecords = inputStream.read_int()
        self.numberOfVariableDatumRecords = inputStream.read_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self._fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self._variableDatumRecords.append(element)


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



