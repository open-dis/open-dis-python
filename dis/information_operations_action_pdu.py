from enum import Enum

from .siso_ref_010.enums.ioaction_iosimulation_source import IOActionIOSimulationSource
from .siso_ref_010.enums.ioaction_ioaction_phase import IOActionIOActionPhase
from .iorecord import IORecord
from .siso_ref_010.enums.ioaction_iowarfare_type import IOActionIOWarfareType
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .information_operations_family_pdu import InformationOperationsFamilyPdu
from .entity_id import EntityID
from .siso_ref_010.enums.ioaction_ioaction_type import IOActionIOActionType

class InformationOperationsActionPdu( InformationOperationsFamilyPdu ):
    """5.13.3.1 Used to communicate an IO attack or the effects of an IO attack on one or more target entities."""

    def __init__(self):
        """ Initializer for InformationOperationsActionPdu"""
        super().__init__()
        """ the simulation to which this PDU is addressed"""
        self.receivingSimID = EntityID()
        """ request ID provides a unique identifier"""
        self.requestID = 0
        # /**  uid 285 */
        self.IOWarfareType = IOActionIOWarfareType.default

        # /**  uid 286 */
        self.IOSimulationSource = IOActionIOSimulationSource.default

        # /**  uid 287 */
        self.IOActionType = IOActionIOActionType.default

        # /**  uid 288 */
        self.IOActionPhase = IOActionIOActionPhase.default

        self.padding1 = 0
        # ioAttackerID is an undescribed parameter... 
        self.ioAttackerID = EntityID()
        # ioPrimaryTargetID is an undescribed parameter... 
        self.ioPrimaryTargetID = EntityID()
        self.padding2 = 0
        self.numberOfIORecords = 0
        self._ioRecords = []
        self.pduType = DisPduType.information_operations_action


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
        outputString += "ReceivingSimID :" + "\n" + self.receivingSimID.to_string() + "\n"
        outputString += "RequestID : " + str(self.requestID) + "\n"
        outputString += "IOActionIOWarfareType : " + self.IOWarfareType.get_description + "(" + (str(int(self.IOWarfareType))) + ")" + "\n"
        outputString += "IOActionIOSimulationSource : " + self.IOSimulationSource.get_description + "(" + (str(int(self.IOSimulationSource))) + ")" + "\n"
        outputString += "IOActionIOActionType : " + self.IOActionType.get_description + "(" + (str(int(self.IOActionType))) + ")" + "\n"
        outputString += "IOActionIOActionPhase : " + self.IOActionPhase.get_description + "(" + (str(int(self.IOActionPhase))) + ")" + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "IoAttackerID :" + "\n" + self.ioAttackerID.to_string() + "\n"
        outputString += "IoPrimaryTargetID :" + "\n" + self.ioPrimaryTargetID.to_string() + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
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
        super( InformationOperationsActionPdu, self ).serialize(outputStream)
        self.receivingSimID.serialize(outputStream)
        outputStream.write_int(int(self.requestID))
        self.serialize_enum(self.IOWarfareType,outputStream)
        self.serialize_enum(self.IOSimulationSource,outputStream)
        self.serialize_enum(self.IOActionType,outputStream)
        self.serialize_enum(self.IOActionPhase,outputStream)
        outputStream.write_int(int(self.padding1))
        self.ioAttackerID.serialize(outputStream)
        self.ioPrimaryTargetID.serialize(outputStream)
        outputStream.write_short(int(self.padding2))
        outputStream.write_short( len(self._ioRecords))
        for anObj in self._ioRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( InformationOperationsActionPdu, self).parse(inputStream)
        self.receivingSimID.parse(inputStream)
        self.requestID = inputStream.read_int()
        self.IOWarfareType = IOActionIOWarfareType.get_enum(self.parse_enum(self.IOWarfareType,inputStream))
        self.IOSimulationSource = IOActionIOSimulationSource.get_enum(self.parse_enum(self.IOSimulationSource,inputStream))
        self.IOActionType = IOActionIOActionType.get_enum(self.parse_enum(self.IOActionType,inputStream))
        self.IOActionPhase = IOActionIOActionPhase.get_enum(self.parse_enum(self.IOActionPhase,inputStream))
        self.padding1 = inputStream.read_int()
        self.ioAttackerID.parse(inputStream)
        self.ioPrimaryTargetID.parse(inputStream)
        self.padding2 = inputStream.read_short()
        self.numberOfIORecords = inputStream.read_short()
        for idx in range(0, self.numberOfIORecords):
            element = IORecord()
            element.parse(inputStream)
            self._ioRecords.append(element)


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



