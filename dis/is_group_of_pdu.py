from enum import Enum

from .variable_datum import VariableDatum
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .siso_ref_010.enums.is_group_of_grouped_entity_category import IsGroupOfGroupedEntityCategory
from .entity_id import EntityID
from .entity_management_family_pdu import EntityManagementFamilyPdu

class IsGroupOfPdu( EntityManagementFamilyPdu ):
    """5.9.3.1 The IsGroupOf PDU shall communicate information about the individual states of a group of entities, including state information that is necessary for the receiving simulation applications to represent the issuing group of entities in the simulation applications’ own simulation."""

    def __init__(self):
        """ Initializer for IsGroupOfPdu"""
        super().__init__()
        """ ID of aggregated entities"""
        self.groupEntityID = EntityID()
        # /** type of entities constituting the group uid 213 */
        self.groupedEntityCategory = IsGroupOfGroupedEntityCategory.default

        """ Number of individual entities constituting the group"""
        self.numberOfGroupedEntities = 0
        """ padding"""
        self.pad = 0
        """ latitude"""
        self.latitude = 0.0
        """ longitude"""
        self.longitude = 0.0
        """ GED records about each individual entity in the group. Bad specing--the Group Entity Descriptions are not described."""
        self._groupedEntityDescriptions = []
        self.pduType = DisPduType.isgroupof


    def get_numberOfGroupedEntities(self):
        return len(self._groupedEntityDescriptions)
    def set_numberOfGroupedEntities(self, value):
        numberOfGroupedEntities = value


    def get_groupedEntityDescriptions(self):
        return self._groupedEntityDescriptions
    def set_groupedEntityDescriptions(self, value):
        self._groupedEntityDescriptions = value
    groupedEntityDescriptions = property(get_groupedEntityDescriptions, set_groupedEntityDescriptions)


    def add_groupedEntityDescriptions(self, value : VariableDatum):
        self._groupedEntityDescriptions.append(value)


    """
    ///            Name : groupedEntityDescriptions
    ///             UID : 
    ///            Type : VariableDatum
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : GED records about each individual entity in the group. Bad specing--the Group Entity Descriptions are not described.
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
        outputString += "GroupEntityID :" + "\n" + self.groupEntityID.to_string() + "\n"
        outputString += "IsGroupOfGroupedEntityCategory : " + self.groupedEntityCategory.get_description + "(" + (str(int(self.groupedEntityCategory))) + ")" + "\n"
        outputString += "NumberOfGroupedEntities : " + str(len(self._groupedEntityDescriptions)) + "\n"
        outputString += "Pad : " + str(self.pad) + "\n"
        outputString += "Latitude : " + str(self.latitude) + "\n"
        outputString += "Longitude : " + str(self.longitude) + "\n"
        outputString += "GroupedEntityDescriptions : " + "\n"
        for idx in range(0, len(self._groupedEntityDescriptions)):
            outputString += self._groupedEntityDescriptions[idx].to_string()

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
        super( IsGroupOfPdu, self ).serialize(outputStream)
        self.groupEntityID.serialize(outputStream)
        self.serialize_enum(self.groupedEntityCategory,outputStream)
        outputStream.write_byte( len(self._groupedEntityDescriptions))
        outputStream.write_int(int(self.pad))
        outputStream.write_double(int(self.latitude))
        outputStream.write_double(int(self.longitude))
        for anObj in self._groupedEntityDescriptions:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( IsGroupOfPdu, self).parse(inputStream)
        self.groupEntityID.parse(inputStream)
        self.groupedEntityCategory = IsGroupOfGroupedEntityCategory.get_enum(self.parse_enum(self.groupedEntityCategory,inputStream))
        self.numberOfGroupedEntities = inputStream.read_byte()
        self.pad = inputStream.read_int()
        self.latitude = inputStream.read_double()
        self.longitude = inputStream.read_double()
        for idx in range(0, self.numberOfGroupedEntities):
            element = VariableDatum()
            element.parse(inputStream)
            self._groupedEntityDescriptions.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 7

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



