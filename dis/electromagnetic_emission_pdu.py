from enum import Enum

from .electronic_emitter import ElectronicEmitter
from .siso_ref_010.enums.electromagnetic_emission_state_update_indicator import ElectromagneticEmissionStateUpdateIndicator
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_id import EntityID
from .event_identifier import EventIdentifier
from .distributed_emissions_regeneration_family_pdu import DistributedEmissionsRegenerationFamilyPdu

class ElectromagneticEmissionPdu( DistributedEmissionsRegenerationFamilyPdu ):
    """7.6.2 Communicate active electromagnetic emissions, including radar and radar-related electronic warfare (e.g., jamming). Exceptions include IFF interrogations and replies, navigation aids, voice, beacon and data radio communications, directed energy weapons, and laser ranging and designation systems, which are handled by other PDUs. Section 5.3.7.1."""

    def __init__(self):
        """ Initializer for ElectromagneticEmissionPdu"""
        super().__init__()
        """ ID of the entity emitting"""
        self.emittingEntityID = EntityID()
        """ ID of event"""
        self.eventID = EventIdentifier()
        # /** This field shall be used to indicate if the data in the PDU represents a state update or just data that has changed since issuance of the last Electromagnetic Emission PDU [relative to the identified entity and emission system(s)]. uid 77 */
        self.stateUpdateIndicator = ElectromagneticEmissionStateUpdateIndicator.default

        """ This field shall specify the number of emission systems being described in the current PDU."""
        self.numberOfSystems = 0
        """ padding"""
        self.paddingForEmissionsPdu = 0
        """ Electronic emmissions systems"""
        self._systems = []
        self.pduType = DisPduType.electromagnetic_emission
        self.paddingForEmissionsPdu = 0


    def get_numberOfSystems(self):
        return len(self._systems)
    def set_numberOfSystems(self, value):
        numberOfSystems = value


    def get_systems(self):
        return self._systems
    def set_systems(self, value):
        self._systems = value
    systems = property(get_systems, set_systems)


    def add_systems(self, value : ElectronicEmitter):
        self._systems.append(value)


    """
    ///            Name : systems
    ///             UID : 
    ///            Type : ElectronicEmitter
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Electronic emmissions systems
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
        outputString += "ElectromagneticEmissionStateUpdateIndicator : " + self.stateUpdateIndicator.get_description + "(" + (str(int(self.stateUpdateIndicator))) + ")" + "\n"
        outputString += "NumberOfSystems : " + str(len(self._systems)) + "\n"
        outputString += "PaddingForEmissionsPdu : " + str(self.paddingForEmissionsPdu) + "\n"
        outputString += "Systems : " + "\n"
        for idx in range(0, len(self._systems)):
            outputString += self._systems[idx].to_string()

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
        super( ElectromagneticEmissionPdu, self ).serialize(outputStream)
        self.emittingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        self.serialize_enum(self.stateUpdateIndicator,outputStream)
        outputStream.write_byte( len(self._systems))
        outputStream.write_short(int(self.paddingForEmissionsPdu))
        for anObj in self._systems:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( ElectromagneticEmissionPdu, self).parse(inputStream)
        self.emittingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.stateUpdateIndicator = ElectromagneticEmissionStateUpdateIndicator.get_enum(self.parse_enum(self.stateUpdateIndicator,inputStream))
        self.numberOfSystems = inputStream.read_byte()
        self.paddingForEmissionsPdu = inputStream.read_short()
        for idx in range(0, self.numberOfSystems):
            element = ElectronicEmitter()
            element.parse(inputStream)
            self._systems.append(element)


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



