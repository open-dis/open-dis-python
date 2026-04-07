from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .radio_communications_family_pdu import RadioCommunicationsFamilyPdu
from .siso_ref_010.enums.receiver_receiver_state import ReceiverReceiverState
from .entity_id import EntityID
from .radio_comms_header import RadioCommsHeader

class ReceiverPdu( RadioCommunicationsFamilyPdu ):
    """5.8.5 Communicates the state of a particular radio receiver. Its primary application is in communicating state information to radio network monitors, data loggers, and similar applications for use in debugging, supervision, and after-action review."""

    def __init__(self):
        """ Initializer for ReceiverPdu"""
        super().__init__()
        # header is an undescribed parameter... 
        self.header = RadioCommsHeader()
        # /** encoding scheme used, and enumeration uid 179 */
        self.receiverState = ReceiverReceiverState.default

        self.padding1 = 0
        """ received power"""
        self.receivedPower = 0.0
        """ ID of transmitter"""
        self.transmitterEntityId = EntityID()
        """ ID of transmitting radio"""
        self.transmitterRadioId = 0
        self.pduType = DisPduType.receiver

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "Header :" + "\n" + self.header.to_string() + "\n"
        outputString += "ReceiverReceiverState : " + self.receiverState.get_description + "(" + (str(int(self.receiverState))) + ")" + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "ReceivedPower : " + str(self.receivedPower) + "\n"
        outputString += "TransmitterEntityId :" + "\n" + self.transmitterEntityId.to_string() + "\n"
        outputString += "TransmitterRadioId : " + str(self.transmitterRadioId) + "\n"
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
        super( ReceiverPdu, self ).serialize(outputStream)
        self.header.serialize(outputStream)
        self.serialize_enum(self.receiverState,outputStream)
        outputStream.write_short(int(self.padding1))
        outputStream.write_float(int(self.receivedPower))
        self.transmitterEntityId.serialize(outputStream)
        outputStream.write_short(int(self.transmitterRadioId))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( ReceiverPdu, self).parse(inputStream)
        self.header.parse(inputStream)
        self.receiverState = ReceiverReceiverState.get_enum(self.parse_enum(self.receiverState,inputStream))
        self.padding1 = inputStream.read_short()
        self.receivedPower = inputStream.read_float()
        self.transmitterEntityId.parse(inputStream)
        self.transmitterRadioId = inputStream.read_short()

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



