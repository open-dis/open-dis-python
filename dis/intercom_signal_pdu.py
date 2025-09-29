from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .radio_communications_family_pdu import RadioCommunicationsFamilyPdu
from .siso_ref_010.enums.signal_tdltype import SignalTDLType
from .intercom_reference_id import IntercomReferenceID

class IntercomSignalPdu( RadioCommunicationsFamilyPdu ):
    """5.8.6 Conveys the audio or digital data that is used to communicate between simulated intercom devices"""

    def __init__(self):
        """ Initializer for IntercomSignalPdu"""
        super().__init__()
        """ The unique designation of an attached or unattached intercom in an event or exercise"""
        self.intercomReferenceID = IntercomReferenceID()
        """ ID of communications device"""
        self.intercomNumber = 0
        """ encoding scheme"""
        self.encodingScheme = 0
        # /** tactical data link type uid 178 */
        self.tdlType = SignalTDLType.default

        """ sample rate"""
        self.sampleRate = 0
        """ data length"""
        self.dataLength = 0
        """ samples"""
        self.samples = 0
        """ data bytes"""
        self.data =  []
        self.padTo32 = [0] * 32
        self.pduType = DisPduType.intercom_signal

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "IntercomReferenceID :" + "\n" + self.intercomReferenceID.to_string() + "\n"
        outputString += "IntercomNumber : " + str(self.intercomNumber) + "\n"
        outputString += "EncodingScheme : " + str(self.encodingScheme) + "\n"
        outputString += "SignalTDLType : " + self.tdlType.get_description + "(" + (str(int(self.tdlType))) + ")" + "\n"
        outputString += "SampleRate : " + str(self.sampleRate) + "\n"
        outputString += "DataLength : " + str(self.dataLength) + "\n"
        outputString += "Samples : " + str(self.samples) + "\n"
        outputString += "Data : " + "\n"
        for idx in range(0, len(self.data)):
            outputString += str(self.data[idx])

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
        super( IntercomSignalPdu, self ).serialize(outputStream)
        self.intercomReferenceID.serialize(outputStream)
        outputStream.write_short(int(self.intercomNumber))
        outputStream.write_short(int(self.encodingScheme))
        self.serialize_enum(self.tdlType,outputStream)
        outputStream.write_int(int(self.sampleRate))
        outputStream.write_short(int(self.dataLength))
        outputStream.write_short(int(self.samples))
        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.data[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( IntercomSignalPdu, self).parse(inputStream)
        self.intercomReferenceID.parse(inputStream)
        self.intercomNumber = inputStream.read_short()
        self.encodingScheme = inputStream.read_short()
        self.tdlType = SignalTDLType.get_enum(self.parse_enum(self.tdlType,inputStream))
        self.sampleRate = inputStream.read_int()
        self.dataLength = inputStream.read_short()
        self.samples = inputStream.read_short()
        self.data = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.data[  idx  ] = val


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



