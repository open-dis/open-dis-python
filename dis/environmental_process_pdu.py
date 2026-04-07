from enum import Enum

from .environment import Environment
from .object_identifier import ObjectIdentifier
from .entity_type import EntityType
from .siso_ref_010.enums.environmental_process_model_type import EnvironmentalProcessModelType
from .siso_ref_010.enums.environmental_process_environment_status import EnvironmentalProcessEnvironmentStatus
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .synthetic_environment_family_pdu import SyntheticEnvironmentFamilyPdu

class EnvironmentalProcessPdu( SyntheticEnvironmentFamilyPdu ):
    """7.10.2 Used to communicate information about environmental effects and processes."""

    def __init__(self):
        """ Initializer for EnvironmentalProcessPdu"""
        super().__init__()
        """ Environmental process ID provides a unique identifier"""
        self.environementalProcessID = ObjectIdentifier()
        """ Environment type"""
        self.environmentType = EntityType()
        # /** model type uid 248 */
        self.modelType = EnvironmentalProcessModelType.default

        # Environment status uid 249
        self.environmentStatus = EnvironmentalProcessEnvironmentStatus()

        """ number of environment records """
        self.numberOfEnvironmentRecords = 0
        """ PDU sequence number for the environmental process if pdu sequencing required"""
        self.sequenceNumber = 0
        """ environmemt records"""
        self._environmentRecords = []
        self.pduType = DisPduType.environmental_process


    def get_numberOfEnvironmentRecords(self):
        return len(self._environmentRecords)
    def set_numberOfEnvironmentRecords(self, value):
        numberOfEnvironmentRecords = value


    def get_environmentRecords(self):
        return self._environmentRecords
    def set_environmentRecords(self, value):
        self._environmentRecords = value
    environmentRecords = property(get_environmentRecords, set_environmentRecords)


    def add_environmentRecords(self, value : Environment):
        self._environmentRecords.append(value)


    """
    ///            Name : environmentRecords
    ///             UID : 
    ///            Type : Environment
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : environmemt records
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
        outputString += "EnvironementalProcessID :" + "\n" + self.environementalProcessID.to_string() + "\n"
        outputString += "EnvironmentType :" + "\n" + self.environmentType.to_string() + "\n"
        outputString += "EnvironmentalProcessModelType : " + self.modelType.get_description + "(" + (str(int(self.modelType))) + ")" + "\n"
        outputString += "EnvironmentalProcessEnvironmentStatus : " + str(self.environmentStatus) + "\n"
        outputString += "NumberOfEnvironmentRecords : " + str(len(self._environmentRecords)) + "\n"
        outputString += "SequenceNumber : " + str(self.sequenceNumber) + "\n"
        outputString += "EnvironmentRecords : " + "\n"
        for idx in range(0, len(self._environmentRecords)):
            outputString += self._environmentRecords[idx].to_string()

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
        super( EnvironmentalProcessPdu, self ).serialize(outputStream)
        self.environementalProcessID.serialize(outputStream)
        self.environmentType.serialize(outputStream)
        self.serialize_enum(self.modelType,outputStream)
        outputStream.write_unsigned_int(int(self.environmentStatus.asbyte))
        outputStream.write_short( len(self._environmentRecords))
        outputStream.write_short(int(self.sequenceNumber))
        for anObj in self._environmentRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( EnvironmentalProcessPdu, self).parse(inputStream)
        self.environementalProcessID.parse(inputStream)
        self.environmentType.parse(inputStream)
        self.modelType = EnvironmentalProcessModelType.get_enum(self.parse_enum(self.modelType,inputStream))
        self.environmentStatus.asbyte = inputStream.read_unsigned_int()
        self.numberOfEnvironmentRecords = inputStream.read_short()
        self.sequenceNumber = inputStream.read_short()
        for idx in range(0, self.numberOfEnvironmentRecords):
            element = Environment()
            element.parse(inputStream)
            self._environmentRecords.append(element)


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



