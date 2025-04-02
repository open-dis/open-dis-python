from enum import Enum

from .siso_ref_010.enums.stop_freeze_frozen_behavior import StopFreezeFrozenBehavior
from .clock_time import ClockTime
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.stop_freeze_reason import StopFreezeReason
from .siso_ref_010.enums.required_reliability_service import RequiredReliabilityService
from .simulation_management_with_reliability_family_pdu import SimulationManagementWithReliabilityFamilyPdu

class StopFreezeRPdu( SimulationManagementWithReliabilityFamilyPdu ):
    """5.12.4.5 Serves the same function as the Stop/Freeze PDU (see 5.6.5.5.1) but with the addition of reliability service levels."""

    def __init__(self):
        """ Initializer for StopFreezeRPdu"""
        super().__init__()
        """ time in real world for this operation to happen"""
        self.realWorldTime = ClockTime()
        # /** Reason for stopping/freezing simulation uid 67 */
        self.reason = StopFreezeReason.default

        # internal behvior of the simulation while frozen uid 68
        self.frozenBehavior = StopFreezeFrozenBehavior()

        # /** reliability level uid 74 */
        self.requiredReliabilityService = RequiredReliabilityService.default

        """ padding"""
        self.pad1 = 0
        """ Request ID provides a unique identifier"""
        self.requestID = 0
        self.pduType = DisPduType.stop_freeze_reliable

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "RealWorldTime :" + "\n" + self.realWorldTime.to_string() + "\n"
        outputString += "StopFreezeReason : " + self.reason.get_description + "(" + (str(int(self.reason))) + ")" + "\n"
        outputString += "StopFreezeFrozenBehavior : " + str(self.frozenBehavior) + "\n"
        outputString += "RequiredReliabilityService : " + self.requiredReliabilityService.get_description + "(" + (str(int(self.requiredReliabilityService))) + ")" + "\n"
        outputString += "Pad1 : " + str(self.pad1) + "\n"
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
        super( StopFreezeRPdu, self ).serialize(outputStream)
        self.realWorldTime.serialize(outputStream)
        self.serialize_enum(self.reason,outputStream)
        outputStream.write_unsigned_int(int(self.frozenBehavior.asbyte))
        self.serialize_enum(self.requiredReliabilityService,outputStream)
        outputStream.write_byte(int(self.pad1))
        outputStream.write_int(int(self.requestID))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( StopFreezeRPdu, self).parse(inputStream)
        self.realWorldTime.parse(inputStream)
        self.reason = StopFreezeReason.get_enum(self.parse_enum(self.reason,inputStream))
        self.frozenBehavior.asbyte = inputStream.read_unsigned_int()
        self.requiredReliabilityService = RequiredReliabilityService.get_enum(self.parse_enum(self.requiredReliabilityService,inputStream))
        self.pad1 = inputStream.read_byte()
        self.requestID = inputStream.read_int()

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



