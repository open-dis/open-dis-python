from enum import Enum

from .apa import APA
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .shaft_rpm import ShaftRPM
from .siso_ref_010.enums.uastate_change_update_indicator import UAStateChangeUpdateIndicator
from .siso_ref_010.enums.uapassive_parameter_index import UAPassiveParameterIndex
from .entity_id import EntityID
from .event_identifier import EventIdentifier
from .distributed_emissions_regeneration_family_pdu import DistributedEmissionsRegenerationFamilyPdu
from .uaemitter import UAEmitter

class UnderwaterAcousticPdu( DistributedEmissionsRegenerationFamilyPdu ):
    """7.6.4 Information about underwater acoustic emmissions. See 5.7.5."""

    def __init__(self):
        """ Initializer for UnderwaterAcousticPdu"""
        super().__init__()
        """ ID of the entity that is the source of the emission"""
        self.emittingEntityID = EntityID()
        """ ID of event"""
        self.eventID = EventIdentifier()
        # /** This field shall be used to indicate whether the data in the UA PDU represent a state update or data that have changed since issuance of the last UA PDU uid 143 */
        self.stateChangeIndicator = UAStateChangeUpdateIndicator.default

        """ padding"""
        self.pad = 0
        # /** This field indicates which database record (or file) shall be used in the definition of passive signature (unintentional) emissions of the entity. The indicated database record (or  file) shall define all noise generated as a function of propulsion plant configurations and associated  auxiliaries. uid 148 */
        self.passiveParameterIndex = UAPassiveParameterIndex.default

        """ This field shall specify the entity propulsion plant configuration. This field is used to determine the passive signature characteristics of an entity."""
        self.propulsionPlantConfiguration = 0
        """  This field shall represent the number of shafts on a platform"""
        self.numberOfShafts = 0
        """ This field shall indicate the number of APAs described in the current UA PDU"""
        self.numberOfAPAs = 0
        """ This field shall specify the number of UA emitter systems being described in the current UA PDU"""
        self.numberOfUAEmitterSystems = 0
        """ shaft RPM values."""
        self._shaftRPMs = []
        """ additional passive activities"""
        self._apaData = []
        self._emitterSystems = []
        self.pduType = DisPduType.underwater_acoustic


    def get_numberOfShafts(self):
        return len(self._shaftRPMs)
    def set_numberOfShafts(self, value):
        numberOfShafts = value


    def get_numberOfAPAs(self):
        return len(self._apaData)
    def set_numberOfAPAs(self, value):
        numberOfAPAs = value


    def get_numberOfUAEmitterSystems(self):
        return len(self._emitterSystems)
    def set_numberOfUAEmitterSystems(self, value):
        numberOfUAEmitterSystems = value


    def get_shaftRPMs(self):
        return self._shaftRPMs
    def set_shaftRPMs(self, value):
        self._shaftRPMs = value
    shaftRPMs = property(get_shaftRPMs, set_shaftRPMs)


    def add_shaftRPMs(self, value : ShaftRPM):
        self._shaftRPMs.append(value)


    """
    ///            Name : shaftRPMs
    ///             UID : 
    ///            Type : ShaftRPM
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : shaft RPM values.
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_apaData(self):
        return self._apaData
    def set_apaData(self, value):
        self._apaData = value
    apaData = property(get_apaData, set_apaData)


    def add_apaData(self, value : APA):
        self._apaData.append(value)


    """
    ///            Name : apaData
    ///             UID : 
    ///            Type : APA
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : additional passive activities
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_emitterSystems(self):
        return self._emitterSystems
    def set_emitterSystems(self, value):
        self._emitterSystems = value
    emitterSystems = property(get_emitterSystems, set_emitterSystems)


    def add_emitterSystems(self, value : UAEmitter):
        self._emitterSystems.append(value)


    """
    ///            Name : emitterSystems
    ///             UID : 
    ///            Type : UAEmitter
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
        outputString += "EmittingEntityID :" + "\n" + self.emittingEntityID.to_string() + "\n"
        outputString += "EventID :" + "\n" + self.eventID.to_string() + "\n"
        outputString += "UAStateChangeUpdateIndicator : " + self.stateChangeIndicator.get_description + "(" + (str(int(self.stateChangeIndicator))) + ")" + "\n"
        outputString += "Pad : " + str(self.pad) + "\n"
        outputString += "UAPassiveParameterIndex : " + self.passiveParameterIndex.get_description + "(" + (str(int(self.passiveParameterIndex))) + ")" + "\n"
        outputString += "PropulsionPlantConfiguration : " + str(self.propulsionPlantConfiguration) + "\n"
        outputString += "NumberOfShafts : " + str(len(self._shaftRPMs)) + "\n"
        outputString += "NumberOfAPAs : " + str(len(self._apaData)) + "\n"
        outputString += "NumberOfUAEmitterSystems : " + str(len(self._emitterSystems)) + "\n"
        outputString += "ShaftRPMs : " + "\n"
        for idx in range(0, len(self._shaftRPMs)):
            outputString += self._shaftRPMs[idx].to_string()

        outputString += "ApaData : " + "\n"
        for idx in range(0, len(self._apaData)):
            outputString += self._apaData[idx].to_string()

        outputString += "EmitterSystems : " + "\n"
        for idx in range(0, len(self._emitterSystems)):
            outputString += self._emitterSystems[idx].to_string()

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
        super( UnderwaterAcousticPdu, self ).serialize(outputStream)
        self.emittingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        self.serialize_enum(self.stateChangeIndicator,outputStream)
        outputStream.write_byte(int(self.pad))
        self.serialize_enum(self.passiveParameterIndex,outputStream)
        outputStream.write_byte(int(self.propulsionPlantConfiguration))
        outputStream.write_byte( len(self._shaftRPMs))
        outputStream.write_byte( len(self._apaData))
        outputStream.write_byte( len(self._emitterSystems))
        for anObj in self._shaftRPMs:
            anObj.serialize(outputStream)

        for anObj in self._apaData:
            anObj.serialize(outputStream)

        for anObj in self._emitterSystems:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( UnderwaterAcousticPdu, self).parse(inputStream)
        self.emittingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.stateChangeIndicator = UAStateChangeUpdateIndicator.get_enum(self.parse_enum(self.stateChangeIndicator,inputStream))
        self.pad = inputStream.read_byte()
        self.passiveParameterIndex = UAPassiveParameterIndex.get_enum(self.parse_enum(self.passiveParameterIndex,inputStream))
        self.propulsionPlantConfiguration = inputStream.read_byte()
        self.numberOfShafts = inputStream.read_byte()
        self.numberOfAPAs = inputStream.read_byte()
        self.numberOfUAEmitterSystems = inputStream.read_byte()
        for idx in range(0, self.numberOfShafts):
            element = ShaftRPM()
            element.parse(inputStream)
            self._shaftRPMs.append(element)

        for idx in range(0, self.numberOfAPAs):
            element = APA()
            element.parse(inputStream)
            self._apaData.append(element)

        for idx in range(0, self.numberOfUAEmitterSystems):
            element = UAEmitter()
            element.parse(inputStream)
            self._emitterSystems.append(element)


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



