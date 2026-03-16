from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .minefield_family_pdu import MinefieldFamilyPdu
from .minefield_identifier import MinefieldIdentifier
from .simulation_identifier import SimulationIdentifier

class MinefieldResponseNACKPdu( MinefieldFamilyPdu ):
    """5.10.5 Contains information about the requesting entity and the PDU(s) that were not received in response to a query. NACK = Negative Acknowledgment."""

    def __init__(self):
        """ Initializer for MinefieldResponseNACKPdu"""
        super().__init__()
        """ Minefield ID provides a unique identifier"""
        self.minefieldID = MinefieldIdentifier()
        """ entity ID making the request"""
        self.requestingEntityID = SimulationIdentifier()
        """ request ID provides a unique identifier"""
        self.requestID = 0
        """ how many pdus were missing"""
        self.numberOfMissingPdus = 0
        """ PDU sequence numbers that were missing"""
        self.missingPduSequenceNumbers =  []
        self.pduType = DisPduType.minefield_response_nack

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "MinefieldID :" + "\n" + self.minefieldID.to_string() + "\n"
        outputString += "RequestingEntityID :" + "\n" + self.requestingEntityID.to_string() + "\n"
        outputString += "RequestID : " + str(self.requestID) + "\n"
        outputString += "NumberOfMissingPdus : " + str(self.numberOfMissingPdus) + "\n"
        outputString += "MissingPduSequenceNumbers : " + "\n"
        for idx in range(0, len(self.missingPduSequenceNumbers)):
            outputString += str(self.missingPduSequenceNumbers[idx])

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
        super( MinefieldResponseNACKPdu, self ).serialize(outputStream)
        self.minefieldID.serialize(outputStream)
        self.requestingEntityID.serialize(outputStream)
        outputStream.write_byte(int(self.requestID))
        outputStream.write_byte(int(self.numberOfMissingPdus))
        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.missingPduSequenceNumbers[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( MinefieldResponseNACKPdu, self).parse(inputStream)
        self.minefieldID.parse(inputStream)
        self.requestingEntityID.parse(inputStream)
        self.requestID = inputStream.read_byte()
        self.numberOfMissingPdus = inputStream.read_byte()
        self.missingPduSequenceNumbers = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.missingPduSequenceNumbers[  idx  ] = val


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



