from enum import Enum

from .propulsion_system_data import PropulsionSystemData
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .vectoring_nozzle_system import VectoringNozzleSystem
from .entity_id import EntityID
from .distributed_emissions_regeneration_family_pdu import DistributedEmissionsRegenerationFamilyPdu

class SEESPdu( DistributedEmissionsRegenerationFamilyPdu ):
    """7.6.6 Certain supplemental information on an entity’s physical state and emissions. See 5.7.7"""

    def __init__(self):
        """ Initializer for SEESPdu"""
        super().__init__()
        """ Originating entity ID provides a unique identifier"""
        self.orginatingEntityID = EntityID()
        """ IR Signature representation index"""
        self.infraredSignatureRepresentationIndex = 0
        """ acoustic Signature representation index"""
        self.acousticSignatureRepresentationIndex = 0
        """ radar cross section representation index"""
        self.radarCrossSectionSignatureRepresentationIndex = 0
        """ how many propulsion systems"""
        self.numberOfPropulsionSystems = 0
        """ how many vectoring nozzle systems"""
        self.numberOfVectoringNozzleSystems = 0
        """ variable length list of propulsion system data"""
        self._propulsionSystemData = []
        """ variable length list of vectoring system data"""
        self._vectoringSystemData = []
        self.pduType = DisPduType.supplemental_emission_entity_state


    def get_numberOfPropulsionSystems(self):
        return len(self._propulsionSystemData)
    def set_numberOfPropulsionSystems(self, value):
        numberOfPropulsionSystems = value


    def get_numberOfVectoringNozzleSystems(self):
        return len(self._vectoringSystemData)
    def set_numberOfVectoringNozzleSystems(self, value):
        numberOfVectoringNozzleSystems = value


    def get_propulsionSystemData(self):
        return self._propulsionSystemData
    def set_propulsionSystemData(self, value):
        self._propulsionSystemData = value
    propulsionSystemData = property(get_propulsionSystemData, set_propulsionSystemData)


    def add_propulsionSystemData(self, value : PropulsionSystemData):
        self._propulsionSystemData.append(value)


    """
    ///            Name : propulsionSystemData
    ///             UID : 
    ///            Type : PropulsionSystemData
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of propulsion system data
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_vectoringSystemData(self):
        return self._vectoringSystemData
    def set_vectoringSystemData(self, value):
        self._vectoringSystemData = value
    vectoringSystemData = property(get_vectoringSystemData, set_vectoringSystemData)


    def add_vectoringSystemData(self, value : VectoringNozzleSystem):
        self._vectoringSystemData.append(value)


    """
    ///            Name : vectoringSystemData
    ///             UID : 
    ///            Type : VectoringNozzleSystem
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variable length list of vectoring system data
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
        outputString += "OrginatingEntityID :" + "\n" + self.orginatingEntityID.to_string() + "\n"
        outputString += "InfraredSignatureRepresentationIndex : " + str(self.infraredSignatureRepresentationIndex) + "\n"
        outputString += "AcousticSignatureRepresentationIndex : " + str(self.acousticSignatureRepresentationIndex) + "\n"
        outputString += "RadarCrossSectionSignatureRepresentationIndex : " + str(self.radarCrossSectionSignatureRepresentationIndex) + "\n"
        outputString += "NumberOfPropulsionSystems : " + str(len(self._propulsionSystemData)) + "\n"
        outputString += "NumberOfVectoringNozzleSystems : " + str(len(self._vectoringSystemData)) + "\n"
        outputString += "PropulsionSystemData : " + "\n"
        for idx in range(0, len(self._propulsionSystemData)):
            outputString += self._propulsionSystemData[idx].to_string()

        outputString += "VectoringSystemData : " + "\n"
        for idx in range(0, len(self._vectoringSystemData)):
            outputString += self._vectoringSystemData[idx].to_string()

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
        super( SEESPdu, self ).serialize(outputStream)
        self.orginatingEntityID.serialize(outputStream)
        outputStream.write_short(int(self.infraredSignatureRepresentationIndex))
        outputStream.write_short(int(self.acousticSignatureRepresentationIndex))
        outputStream.write_short(int(self.radarCrossSectionSignatureRepresentationIndex))
        outputStream.write_short( len(self._propulsionSystemData))
        outputStream.write_short( len(self._vectoringSystemData))
        for anObj in self._propulsionSystemData:
            anObj.serialize(outputStream)

        for anObj in self._vectoringSystemData:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( SEESPdu, self).parse(inputStream)
        self.orginatingEntityID.parse(inputStream)
        self.infraredSignatureRepresentationIndex = inputStream.read_short()
        self.acousticSignatureRepresentationIndex = inputStream.read_short()
        self.radarCrossSectionSignatureRepresentationIndex = inputStream.read_short()
        self.numberOfPropulsionSystems = inputStream.read_short()
        self.numberOfVectoringNozzleSystems = inputStream.read_short()
        for idx in range(0, self.numberOfPropulsionSystems):
            element = PropulsionSystemData()
            element.parse(inputStream)
            self._propulsionSystemData.append(element)

        for idx in range(0, self.numberOfVectoringNozzleSystems):
            element = VectoringNozzleSystem()
            element.parse(inputStream)
            self._vectoringSystemData.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 8

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



