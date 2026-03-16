from enum import Enum

from .siso_ref_010.enums.intercom_control_control_type import IntercomControlControlType
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.intercom_control_command import IntercomControlCommand
from .radio_communications_family_pdu import RadioCommunicationsFamilyPdu
from .intercom_communications_parameters import IntercomCommunicationsParameters
from .entity_id import EntityID
from .siso_ref_010.enums.intercom_control_transmit_line_state import IntercomControlTransmitLineState

class IntercomControlPdu( RadioCommunicationsFamilyPdu ):
    """5.8.7 Communicates the state of a particular intercom device, request an action of another intercom device, or respond to an action request."""

    def __init__(self):
        """ Initializer for IntercomControlPdu"""
        super().__init__()
        # /** control type uid 180 */
        self.controlType = IntercomControlControlType.default

        """ control type"""
        self.communicationsChannelType = 0
        """ Source entity ID, this can also be ObjectIdentifier or UnattachedIdentifier"""
        self.sourceEntityID = EntityID()
        """ The specific intercom device being simulated within an entity."""
        self.sourceIntercomNumber = 0
        """ Line number to which the intercom control refers"""
        self.sourceLineID = 0
        """ priority of this message relative to transmissons from other intercom devices"""
        self.transmitPriority = 0
        # /** current transmit state of the line uid 183 */
        self.transmitLineState = IntercomControlTransmitLineState.default

        # /** detailed type requested. uid 182 */
        self.command = IntercomControlCommand.default

        """ eid of the entity that has created this intercom channel, same comments as sourceEntityId"""
        self.masterIntercomReferenceID = EntityID()
        """ specific intercom device that has created this intercom channel"""
        self.masterIntercomNumber = 0
        self.masterChannelID = 0
        """ number of intercom parameters"""
        self.intercomParametersLength = 0
        self._intercomParameters = []
        self.pduType = DisPduType.intercom_control


    def get_intercomParametersLength(self):
        return len(self._intercomParameters)
    def set_intercomParametersLength(self, value):
        intercomParametersLength = value


    def get_intercomParameters(self):
        return self._intercomParameters
    def set_intercomParameters(self, value):
        self._intercomParameters = value
    intercomParameters = property(get_intercomParameters, set_intercomParameters)


    def add_intercomParameters(self, value : IntercomCommunicationsParameters):
        self._intercomParameters.append(value)


    """
    ///            Name : intercomParameters
    ///             UID : 
    ///            Type : IntercomCommunicationsParameters
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
        outputString += "IntercomControlControlType : " + self.controlType.get_description + "(" + (str(int(self.controlType))) + ")" + "\n"
        outputString += "CommunicationsChannelType : " + str(self.communicationsChannelType) + "\n"
        outputString += "SourceEntityID :" + "\n" + self.sourceEntityID.to_string() + "\n"
        outputString += "SourceIntercomNumber : " + str(self.sourceIntercomNumber) + "\n"
        outputString += "SourceLineID : " + str(self.sourceLineID) + "\n"
        outputString += "TransmitPriority : " + str(self.transmitPriority) + "\n"
        outputString += "IntercomControlTransmitLineState : " + self.transmitLineState.get_description + "(" + (str(int(self.transmitLineState))) + ")" + "\n"
        outputString += "IntercomControlCommand : " + self.command.get_description + "(" + (str(int(self.command))) + ")" + "\n"
        outputString += "MasterIntercomReferenceID :" + "\n" + self.masterIntercomReferenceID.to_string() + "\n"
        outputString += "MasterIntercomNumber : " + str(self.masterIntercomNumber) + "\n"
        outputString += "MasterChannelID : " + str(self.masterChannelID) + "\n"
        outputString += "IntercomParametersLength : " + str(len(self._intercomParameters)) + "\n"
        outputString += "IntercomParameters : " + "\n"
        for idx in range(0, len(self._intercomParameters)):
            outputString += self._intercomParameters[idx].to_string()

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
        super( IntercomControlPdu, self ).serialize(outputStream)
        self.serialize_enum(self.controlType,outputStream)
        outputStream.write_byte(int(self.communicationsChannelType))
        self.sourceEntityID.serialize(outputStream)
        outputStream.write_short(int(self.sourceIntercomNumber))
        outputStream.write_byte(int(self.sourceLineID))
        outputStream.write_byte(int(self.transmitPriority))
        self.serialize_enum(self.transmitLineState,outputStream)
        self.serialize_enum(self.command,outputStream)
        self.masterIntercomReferenceID.serialize(outputStream)
        outputStream.write_short(int(self.masterIntercomNumber))
        outputStream.write_short(int(self.masterChannelID))
        outputStream.write_int( len(self._intercomParameters))
        for anObj in self._intercomParameters:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( IntercomControlPdu, self).parse(inputStream)
        self.controlType = IntercomControlControlType.get_enum(self.parse_enum(self.controlType,inputStream))
        self.communicationsChannelType = inputStream.read_byte()
        self.sourceEntityID.parse(inputStream)
        self.sourceIntercomNumber = inputStream.read_short()
        self.sourceLineID = inputStream.read_byte()
        self.transmitPriority = inputStream.read_byte()
        self.transmitLineState = IntercomControlTransmitLineState.get_enum(self.parse_enum(self.transmitLineState,inputStream))
        self.command = IntercomControlCommand.get_enum(self.parse_enum(self.command,inputStream))
        self.masterIntercomReferenceID.parse(inputStream)
        self.masterIntercomNumber = inputStream.read_short()
        self.masterChannelID = inputStream.read_short()
        self.intercomParametersLength = inputStream.read_int()
        for idx in range(0, self.intercomParametersLength):
            element = IntercomCommunicationsParameters()
            element.parse(inputStream)
            self._intercomParameters.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 13

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



