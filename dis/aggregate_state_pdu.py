from enum import Enum

from .variable_datum import VariableDatum
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .vector3float import Vector3Float
from .siso_ref_010.enums.aggregate_state_formation import AggregateStateFormation
from .entity_id import EntityID
from .siso_ref_010.enums.aggregate_state_aggregate_state import AggregateStateAggregateState
from .entity_management_family_pdu import EntityManagementFamilyPdu
from .siso_ref_010.enums.force_id import ForceID
from .entity_type import EntityType
from .aggregate_identifier import AggregateIdentifier
from .vector3double import Vector3Double
from .aggregate_marking import AggregateMarking
from .aggregate_type import AggregateType

class AggregateStatePdu( EntityManagementFamilyPdu ):
    """5.9.2.2 The Aggregate State PDU shall be used to communicate the state and other pertinent information about an aggregated unit."""

    def __init__(self):
        """ Initializer for AggregateStatePdu"""
        super().__init__()
        """ ID of aggregated entities"""
        self.aggregateID = AggregateIdentifier()
        # /** force ID provides a unique identifier uid 6 */
        self.forceID = ForceID.default

        # /** state of aggregate uid 204 */
        self.aggregateState = AggregateStateAggregateState.default

        """ entity type of the aggregated entities"""
        self.aggregateType = AggregateType()
        # /** formation of aggregated entities uid 205 */
        self.formation = AggregateStateFormation.default

        """ marking for aggregate; first char is charset type, rest is char data"""
        self.aggregateMarking = AggregateMarking()
        """ dimensions of bounding box for the aggregated entities, origin at the center of mass"""
        self.dimensions = Vector3Float()
        """ orientation of the bounding box"""
        self.orientation = Vector3Float()
        """ center of mass of the aggregation"""
        self.centerOfMass = Vector3Double()
        """ velocity of aggregation"""
        self.velocity = Vector3Float()
        """ number of aggregates"""
        self.numberOfDisAggregates = 0
        """ number of entities"""
        self.numberOfDisEntities = 0
        """ number of silent aggregate types"""
        self.numberOfSilentAggregateTypes = 0
        """ Number of silent entity types, handled automatically by marshaller at run time (and not modifiable by end-user programmers)"""
        self.numberOfSilentEntityTypes = 0
        """ aggregates  list"""
        self._aggregateIDList = []
        """ entity ID list"""
        self._entityIDList = []
        self.padTo32 = [0] * 32
        """ silent entity types"""
        self._silentAggregateSystemList = []
        """ silent entity types"""
        self._silentEntitySystemList = []
        """ Number of variable datum records, handled automatically by marshaller at run time (and not modifiable by end-user programmers)"""
        self.numberOfVariableDatumRecords = 0
        """ variableDatums"""
        self._variableDatumList = []
        self.pduType = DisPduType.aggregate_state


    def get_numberOfDisAggregates(self):
        return len(self._aggregateIDList)
    def set_numberOfDisAggregates(self, value):
        numberOfDisAggregates = value


    def get_numberOfDisEntities(self):
        return len(self._entityIDList)
    def set_numberOfDisEntities(self, value):
        numberOfDisEntities = value


    def get_numberOfSilentAggregateTypes(self):
        return len(self._silentAggregateSystemList)
    def set_numberOfSilentAggregateTypes(self, value):
        numberOfSilentAggregateTypes = value


    def get_numberOfSilentEntityTypes(self):
        return len(self._silentEntitySystemList)
    def set_numberOfSilentEntityTypes(self, value):
        numberOfSilentEntityTypes = value


    def get_aggregateIDList(self):
        return self._aggregateIDList
    def set_aggregateIDList(self, value):
        self._aggregateIDList = value
    aggregateIDList = property(get_aggregateIDList, set_aggregateIDList)


    def add_aggregateIDList(self, value : AggregateIdentifier):
        self._aggregateIDList.append(value)


    """
    ///            Name : aggregateIDList
    ///             UID : 
    ///            Type : AggregateIdentifier
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : aggregates  list
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_entityIDList(self):
        return self._entityIDList
    def set_entityIDList(self, value):
        self._entityIDList = value
    entityIDList = property(get_entityIDList, set_entityIDList)


    def add_entityIDList(self, value : EntityID):
        self._entityIDList.append(value)


    """
    ///            Name : entityIDList
    ///             UID : 
    ///            Type : EntityID
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : entity ID list
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_silentAggregateSystemList(self):
        return self._silentAggregateSystemList
    def set_silentAggregateSystemList(self, value):
        self._silentAggregateSystemList = value
    silentAggregateSystemList = property(get_silentAggregateSystemList, set_silentAggregateSystemList)


    def add_silentAggregateSystemList(self, value : EntityType):
        self._silentAggregateSystemList.append(value)


    """
    ///            Name : silentAggregateSystemList
    ///             UID : 
    ///            Type : EntityType
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : silent entity types
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_silentEntitySystemList(self):
        return self._silentEntitySystemList
    def set_silentEntitySystemList(self, value):
        self._silentEntitySystemList = value
    silentEntitySystemList = property(get_silentEntitySystemList, set_silentEntitySystemList)


    def add_silentEntitySystemList(self, value : EntityType):
        self._silentEntitySystemList.append(value)


    """
    ///            Name : silentEntitySystemList
    ///             UID : 
    ///            Type : EntityType
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : silent entity types
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_numberOfVariableDatumRecords(self):
        return len(self._variableDatumList)
    def set_numberOfVariableDatumRecords(self, value):
        numberOfVariableDatumRecords = value


    def get_variableDatumList(self):
        return self._variableDatumList
    def set_variableDatumList(self, value):
        self._variableDatumList = value
    variableDatumList = property(get_variableDatumList, set_variableDatumList)


    def add_variableDatumList(self, value : VariableDatum):
        self._variableDatumList.append(value)


    """
    ///            Name : variableDatumList
    ///             UID : 
    ///            Type : VariableDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : variableDatums
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
        outputString += "AggregateID :" + "\n" + self.aggregateID.to_string() + "\n"
        outputString += "ForceID : " + self.forceID.get_description + "(" + (str(int(self.forceID))) + ")" + "\n"
        outputString += "AggregateStateAggregateState : " + self.aggregateState.get_description + "(" + (str(int(self.aggregateState))) + ")" + "\n"
        outputString += "AggregateType :" + "\n" + self.aggregateType.to_string() + "\n"
        outputString += "AggregateStateFormation : " + self.formation.get_description + "(" + (str(int(self.formation))) + ")" + "\n"
        outputString += "AggregateMarking :" + "\n" + self.aggregateMarking.to_string() + "\n"
        outputString += "Dimensions :" + "\n" + self.dimensions.to_string() + "\n"
        outputString += "Orientation :" + "\n" + self.orientation.to_string() + "\n"
        outputString += "CenterOfMass :" + "\n" + self.centerOfMass.to_string() + "\n"
        outputString += "Velocity :" + "\n" + self.velocity.to_string() + "\n"
        outputString += "NumberOfDisAggregates : " + str(len(self._aggregateIDList)) + "\n"
        outputString += "NumberOfDisEntities : " + str(len(self._entityIDList)) + "\n"
        outputString += "NumberOfSilentAggregateTypes : " + str(len(self._silentAggregateSystemList)) + "\n"
        outputString += "NumberOfSilentEntityTypes : " + str(len(self._silentEntitySystemList)) + "\n"
        outputString += "AggregateIDList : " + "\n"
        for idx in range(0, len(self._aggregateIDList)):
            outputString += self._aggregateIDList[idx].to_string()

        outputString += "EntityIDList : " + "\n"
        for idx in range(0, len(self._entityIDList)):
            outputString += self._entityIDList[idx].to_string()

        outputString += "SilentAggregateSystemList : " + "\n"
        for idx in range(0, len(self._silentAggregateSystemList)):
            outputString += self._silentAggregateSystemList[idx].to_string()

        outputString += "SilentEntitySystemList : " + "\n"
        for idx in range(0, len(self._silentEntitySystemList)):
            outputString += self._silentEntitySystemList[idx].to_string()

        outputString += "NumberOfVariableDatumRecords : " + str(len(self._variableDatumList)) + "\n"
        outputString += "VariableDatumList : " + "\n"
        for idx in range(0, len(self._variableDatumList)):
            outputString += self._variableDatumList[idx].to_string()

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
        super( AggregateStatePdu, self ).serialize(outputStream)
        self.aggregateID.serialize(outputStream)
        self.serialize_enum(self.forceID,outputStream)
        self.serialize_enum(self.aggregateState,outputStream)
        self.aggregateType.serialize(outputStream)
        self.serialize_enum(self.formation,outputStream)
        self.aggregateMarking.serialize(outputStream)
        self.dimensions.serialize(outputStream)
        self.orientation.serialize(outputStream)
        self.centerOfMass.serialize(outputStream)
        self.velocity.serialize(outputStream)
        outputStream.write_short( len(self._aggregateIDList))
        outputStream.write_short( len(self._entityIDList))
        outputStream.write_short( len(self._silentAggregateSystemList))
        outputStream.write_short( len(self._silentEntitySystemList))
        for anObj in self._aggregateIDList:
            anObj.serialize(outputStream)

        for anObj in self._entityIDList:
            anObj.serialize(outputStream)

        for anObj in self._silentAggregateSystemList:
            anObj.serialize(outputStream)

        for anObj in self._silentEntitySystemList:
            anObj.serialize(outputStream)

        outputStream.write_int( len(self._variableDatumList))
        for anObj in self._variableDatumList:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( AggregateStatePdu, self).parse(inputStream)
        self.aggregateID.parse(inputStream)
        self.forceID = ForceID.get_enum(self.parse_enum(self.forceID,inputStream))
        self.aggregateState = AggregateStateAggregateState.get_enum(self.parse_enum(self.aggregateState,inputStream))
        self.aggregateType.parse(inputStream)
        self.formation = AggregateStateFormation.get_enum(self.parse_enum(self.formation,inputStream))
        self.aggregateMarking.parse(inputStream)
        self.dimensions.parse(inputStream)
        self.orientation.parse(inputStream)
        self.centerOfMass.parse(inputStream)
        self.velocity.parse(inputStream)
        self.numberOfDisAggregates = inputStream.read_short()
        self.numberOfDisEntities = inputStream.read_short()
        self.numberOfSilentAggregateTypes = inputStream.read_short()
        self.numberOfSilentEntityTypes = inputStream.read_short()
        for idx in range(0, self.numberOfDisAggregates):
            element = AggregateIdentifier()
            element.parse(inputStream)
            self._aggregateIDList.append(element)

        for idx in range(0, self.numberOfDisEntities):
            element = EntityID()
            element.parse(inputStream)
            self._entityIDList.append(element)

        for idx in range(0, self.numberOfSilentAggregateTypes):
            element = EntityType()
            element.parse(inputStream)
            self._silentAggregateSystemList.append(element)

        for idx in range(0, self.numberOfSilentEntityTypes):
            element = EntityType()
            element.parse(inputStream)
            self._silentEntitySystemList.append(element)

        self.numberOfVariableDatumRecords = inputStream.read_int()
        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self._variableDatumList.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 21

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



