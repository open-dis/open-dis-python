from enum import Enum

from .siso_ref_010.enums.ioaction_iosimulation_source import IOActionIOSimulationSource
from .iorecord import IORecord
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.ioreport_ioreport_type import IOReportIOReportType
from .information_operations_family_pdu import InformationOperationsFamilyPdu
from .entity_id import EntityID

class InformationOperationsReportPdu( InformationOperationsFamilyPdu ):
    """5.13.4.1 Used to communicate the effects of an IO attack on one or more target entities."""

    def __init__(self):
        """ Initializer for InformationOperationsReportPdu"""
        super().__init__()
        # /**  uid 286 */
        self.ioSimSource = IOActionIOSimulationSource.default

        # /** request ID provides a unique identifier uid 289 */
        self.ioReportType = IOReportIOReportType.default

        self.padding1 = 0
        # ioAttackerID is an undescribed parameter... 
        self.ioAttackerID = EntityID()
        # ioPrimaryTargetID is an undescribed parameter... 
        self.ioPrimaryTargetID = EntityID()
        self.padding2 = 0
        self.padding3 = 0
        self.numberOfIORecords = 0
        self._ioRecords = []
        self.pduType = DisPduType.information_operations_report


    def get_numberOfIORecords(self):
        return len(self._ioRecords)
    def set_numberOfIORecords(self, value):
        numberOfIORecords = value


    def get_ioRecords(self):
        return self._ioRecords
    def set_ioRecords(self, value):
        self._ioRecords = value
    ioRecords = property(get_ioRecords, set_ioRecords)


    def add_ioRecords(self, value : IORecord):
        self._ioRecords.append(value)


    """
    ///            Name : ioRecords
    ///             UID : 
    ///            Type : IORecord
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
        outputString += "IOActionIOSimulationSource : " + self.ioSimSource.get_description + "(" + (str(int(self.ioSimSource))) + ")" + "\n"
        outputString += "IOReportIOReportType : " + self.ioReportType.get_description + "(" + (str(int(self.ioReportType))) + ")" + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "IoAttackerID :" + "\n" + self.ioAttackerID.to_string() + "\n"
        outputString += "IoPrimaryTargetID :" + "\n" + self.ioPrimaryTargetID.to_string() + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "Padding3 : " + str(self.padding3) + "\n"
        outputString += "NumberOfIORecords : " + str(len(self._ioRecords)) + "\n"
        outputString += "IoRecords : " + "\n"
        for idx in range(0, len(self._ioRecords)):
            outputString += self._ioRecords[idx].to_string()

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
        super( InformationOperationsReportPdu, self ).serialize(outputStream)
        self.serialize_enum(self.ioSimSource,outputStream)
        self.serialize_enum(self.ioReportType,outputStream)
        outputStream.write_byte(int(self.padding1))
        self.ioAttackerID.serialize(outputStream)
        self.ioPrimaryTargetID.serialize(outputStream)
        outputStream.write_short(int(self.padding2))
        outputStream.write_short(int(self.padding3))
        outputStream.write_short( len(self._ioRecords))
        for anObj in self._ioRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( InformationOperationsReportPdu, self).parse(inputStream)
        self.ioSimSource = IOActionIOSimulationSource.get_enum(self.parse_enum(self.ioSimSource,inputStream))
        self.ioReportType = IOReportIOReportType.get_enum(self.parse_enum(self.ioReportType,inputStream))
        self.padding1 = inputStream.read_byte()
        self.ioAttackerID.parse(inputStream)
        self.ioPrimaryTargetID.parse(inputStream)
        self.padding2 = inputStream.read_short()
        self.padding3 = inputStream.read_short()
        self.numberOfIORecords = inputStream.read_short()
        for idx in range(0, self.numberOfIORecords):
            element = IORecord()
            element.parse(inputStream)
            self._ioRecords.append(element)


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



