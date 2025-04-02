from enum import Enum

from .siso_ref_010.enums.ioeffects_record_ioeffect import IOEffectsRecordIOEffect
from .siso_ref_010.enums.ioeffects_record_ioprocess import IOEffectsRecordIOProcess
from .iorecord import IORecord
from .siso_ref_010.enums.variable_record_type import VariableRecordType
from .siso_ref_010.enums.ioeffects_record_iostatus import IOEffectsRecordIOStatus
from .siso_ref_010.enums.ioeffects_record_iolink_type import IOEffectsRecordIOLinkType

class IOEffectRecord( IORecord ):
    """6.2.48.3"""

    def __init__(self):
        """ Initializer for IOEffectRecord"""
        super().__init__()
        # /**  uid 66 Variable Record Type values are defined by VariableRecordType enumerations */
        self.recordType = VariableRecordType.io_effect

        self.recordLength = 0
        # /**  uid 290 */
        self.ioStatus = IOEffectsRecordIOStatus.default

        # /**  uid 291 */
        self.ioLinkType = IOEffectsRecordIOLinkType.default

        # /**  uid 292 */
        self.ioEffect = IOEffectsRecordIOEffect.default

        self.ioEffectDutyCycle = 0
        self.ioEffectDuration = 0
        # /**  uid 293 */
        self.ioProcess = IOEffectsRecordIOProcess.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "VariableRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "IOEffectsRecordIOStatus : " + self.ioStatus.get_description + "(" + (str(int(self.ioStatus))) + ")" + "\n"
        outputString += "IOEffectsRecordIOLinkType : " + self.ioLinkType.get_description + "(" + (str(int(self.ioLinkType))) + ")" + "\n"
        outputString += "IOEffectsRecordIOEffect : " + self.ioEffect.get_description + "(" + (str(int(self.ioEffect))) + ")" + "\n"
        outputString += "IoEffectDutyCycle : " + str(self.ioEffectDutyCycle) + "\n"
        outputString += "IoEffectDuration : " + str(self.ioEffectDuration) + "\n"
        outputString += "IOEffectsRecordIOProcess : " + self.ioProcess.get_description + "(" + (str(int(self.ioProcess))) + ")" + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
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
        super( IOEffectRecord, self ).serialize(outputStream)
        self.serialize_enum(self.recordType,outputStream)
        outputStream.write_short(int(self.recordLength))
        self.serialize_enum(self.ioStatus,outputStream)
        self.serialize_enum(self.ioLinkType,outputStream)
        self.serialize_enum(self.ioEffect,outputStream)
        outputStream.write_byte(int(self.ioEffectDutyCycle))
        outputStream.write_short(int(self.ioEffectDuration))
        self.serialize_enum(self.ioProcess,outputStream)
        outputStream.write_short(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( IOEffectRecord, self).parse(inputStream)
        self.recordType = VariableRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.recordLength = inputStream.read_short()
        self.ioStatus = IOEffectsRecordIOStatus.get_enum(self.parse_enum(self.ioStatus,inputStream))
        self.ioLinkType = IOEffectsRecordIOLinkType.get_enum(self.parse_enum(self.ioLinkType,inputStream))
        self.ioEffect = IOEffectsRecordIOEffect.get_enum(self.parse_enum(self.ioEffect,inputStream))
        self.ioEffectDutyCycle = inputStream.read_byte()
        self.ioEffectDuration = inputStream.read_short()
        self.ioProcess = IOEffectsRecordIOProcess.get_enum(self.parse_enum(self.ioProcess,inputStream))
        self.padding = inputStream.read_short()

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



