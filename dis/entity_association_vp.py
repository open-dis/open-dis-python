from enum import Enum

from .siso_ref_010.enums.entity_association_group_member_type import EntityAssociationGroupMemberType
from .siso_ref_010.enums.is_part_of_station_name import IsPartOfStationName
from .siso_ref_010.enums.entity_vprecord_change_indicator import EntityVPRecordChangeIndicator
from .siso_ref_010.enums.entity_association_physical_connection_type import EntityAssociationPhysicalConnectionType
from .siso_ref_010.enums.variable_parameter_record_type import VariableParameterRecordType
from .siso_ref_010.enums.entity_association_association_status import EntityAssociationAssociationStatus
from .siso_ref_010.enums.entity_association_physical_association_type import EntityAssociationPhysicalAssociationType
from .entity_id import EntityID

class EntityAssociationVP( object ):
    """Association or disassociation of two entities.  Section 6.2.94.4.3"""

    def __init__(self):
        """ Initializer for EntityAssociationVP"""
        # /** The identification of the Variable Parameter record. Enumeration from EBV uid 56 */
        self.recordType = VariableParameterRecordType.entity_association

        # /** Indicates if this VP has changed since last issuance uid 320 */
        self.changeIndicator = EntityVPRecordChangeIndicator.default

        # /** Indicates association status between two entities uid 319 */
        self.associationStatus = EntityAssociationAssociationStatus.default

        # /** Type of association; 8-bit enum uid 323 */
        self.associationType = EntityAssociationPhysicalAssociationType.default

        """ Object ID of entity associated with this entity"""
        self.entityID = EntityID()
        # /** Station location on one's own entity uid 212 */
        self.ownStationLocation = IsPartOfStationName.default

        # /** Type of physical connection uid 324 */
        self.physicalConnectionType = EntityAssociationPhysicalConnectionType.default

        # /** Type of member the entity is within the group uid 321 */
        self.groupMemberType = EntityAssociationGroupMemberType.default

        """ Group if any to which the entity belongs"""
        self.groupNumber = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "VariableParameterRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "EntityVPRecordChangeIndicator : " + self.changeIndicator.get_description + "(" + (str(int(self.changeIndicator))) + ")" + "\n"
        outputString += "EntityAssociationAssociationType : " + self.associationStatus.get_description + "(" + (str(int(self.associationStatus))) + ")" + "\n"
        outputString += "EntityAssociationPhysicalAssociationType : " + self.associationType.get_description + "(" + (str(int(self.associationType))) + ")" + "\n"
        outputString += "EntityID :" + "\n" + self.entityID.to_string() + "\n"
        outputString += "IsPartOfStationName : " + self.ownStationLocation.get_description + "(" + (str(int(self.ownStationLocation))) + ")" + "\n"
        outputString += "EntityAssociationPhysicalConnectionType : " + self.physicalConnectionType.get_description + "(" + (str(int(self.physicalConnectionType))) + ")" + "\n"
        outputString += "EntityAssociationGroupMemberType : " + self.groupMemberType.get_description + "(" + (str(int(self.groupMemberType))) + ")" + "\n"
        outputString += "GroupNumber : " + str(self.groupNumber) + "\n"
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
        self.serialize_enum(self.recordType,outputStream)
        self.serialize_enum(self.changeIndicator,outputStream)
        self.serialize_enum(self.associationStatus,outputStream)
        self.serialize_enum(self.associationType,outputStream)
        self.entityID.serialize(outputStream)
        self.serialize_enum(self.ownStationLocation,outputStream)
        self.serialize_enum(self.physicalConnectionType,outputStream)
        self.serialize_enum(self.groupMemberType,outputStream)
        outputStream.write_short(int(self.groupNumber))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = VariableParameterRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.changeIndicator = EntityVPRecordChangeIndicator.get_enum(self.parse_enum(self.changeIndicator,inputStream))
        self.associationStatus = EntityAssociationAssociationType.get_enum(self.parse_enum(self.associationStatus,inputStream))
        self.associationType = EntityAssociationPhysicalAssociationType.get_enum(self.parse_enum(self.associationType,inputStream))
        self.entityID.parse(inputStream)
        self.ownStationLocation = IsPartOfStationName.get_enum(self.parse_enum(self.ownStationLocation,inputStream))
        self.physicalConnectionType = EntityAssociationPhysicalConnectionType.get_enum(self.parse_enum(self.physicalConnectionType,inputStream))
        self.groupMemberType = EntityAssociationGroupMemberType.get_enum(self.parse_enum(self.groupMemberType,inputStream))
        self.groupNumber = inputStream.read_short()

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



