from enum import Enum

from .simulation_management_family_pdu import SimulationManagementFamilyPdu
from .siso_ref_010.enums.stop_freeze_frozen_behavior import StopFreezeFrozenBehavior
from .clock_time import ClockTime
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.stop_freeze_reason import StopFreezeReason

class StopFreezePdu( SimulationManagementFamilyPdu ):
    """Section 7.5.5. The stopping or freezing of an entity/exercise shall be communicated using a Stop/Freeze PDU. See 5.6.5.5"""

    def __init__(self):
        """ Initializer for StopFreezePdu"""
        super().__init__()
        """ real-world(UTC) time at which the entity shall stop or freeze in the exercise"""
        self.realWorldTime = ClockTime()
        # /** Reason the simulation was stopped or frozen (see section 7 of SISO-REF-010) represented by an 8-bit enumeration uid 67 */
        self.reason = StopFreezeReason.default

        # Internal behavior of the entity (or simulation) and its appearance while frozen to the other participants uid 68
        self.frozenBehavior = StopFreezeFrozenBehavior()

        """ padding"""
        self.padding1 = 0
        """ Request ID that is unique"""
        self.requestID = 0
        self.pduType = DisPduType.stop_freeze

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "RealWorldTime :" + "\n" + self.realWorldTime.to_string() + "\n"
        outputString += "StopFreezeReason : " + self.reason.get_description + "(" + (str(int(self.reason))) + ")" + "\n"
        outputString += "StopFreezeFrozenBehavior : " + str(self.frozenBehavior) + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "RequestID : " + str(self.requestID) + "\n"
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
        super( StopFreezePdu, self ).serialize(outputStream)
        self.realWorldTime.serialize(outputStream)
        self.serialize_enum(self.reason,outputStream)
        outputStream.write_unsigned_int(int(self.frozenBehavior.asbyte))
        outputStream.write_short(int(self.padding1))
        outputStream.write_int(int(self.requestID))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( StopFreezePdu, self).parse(inputStream)
        self.realWorldTime.parse(inputStream)
        self.reason = StopFreezeReason.get_enum(self.parse_enum(self.reason,inputStream))
        self.frozenBehavior.asbyte = inputStream.read_unsigned_int()
        self.padding1 = inputStream.read_short()
        self.requestID = inputStream.read_int()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 5

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



