from enum import Enum

from .siso_ref_010.enums.force_id import ForceID
from .entity_type import EntityType
from .appearance import Appearance
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_marking import EntityMarking
from .live_entity_family_pdu import LiveEntityFamilyPdu
from .entity_id import EntityID
from .siso_ref_010.enums.land_platform_capabilities import LandPlatformCapabilities
from .siso_ref_010.enums.entity_capability_types import EntityCapabilityTypes

class AppearancePdu( LiveEntityFamilyPdu ):
    """9.4.3 Communicate information about the appearance of a live entity."""

    def __init__(self):
        """ Initializer for AppearancePdu"""
        super().__init__()
        # liveEntityId is an undescribed parameter... 
        self.liveEntityId = EntityID()
        """ 16-bit bit field"""
        self.appearanceFlags = 0
        # /**  uid 6 */
        self.forceId = ForceID.default

        # entityType is an undescribed parameter... 
        self.entityType = EntityType()
        # alternateEntityType is an undescribed parameter... 
        self.alternateEntityType = EntityType()
        # entityMarking is an undescribed parameter... 
        self.entityMarking = EntityMarking()
        #  uid 55
        self.capabilities = LandPlatformCapabilities()

        # appearanceFields is an undescribed parameter... 
        self.appearanceFields = Appearance()
        self.pduType = DisPduType.appearance

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "LiveEntityId :" + "\n" + self.liveEntityId.to_string() + "\n"
        outputString += "AppearanceFlags : " + str(self.appearanceFlags) + "\n"
        outputString += "ForceID : " + self.forceId.get_description + "(" + (str(int(self.forceId))) + ")" + "\n"
        outputString += "EntityType :" + "\n" + self.entityType.to_string() + "\n"
        outputString += "AlternateEntityType :" + "\n" + self.alternateEntityType.to_string() + "\n"
        outputString += "EntityMarking :" + "\n" + self.entityMarking.to_string() + "\n"
        outputString += "EntityCapabilities : " + str(self.capabilities) + "\n"
        outputString += "AppearanceFields :" + "\n" + self.appearanceFields.to_string() + "\n"
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
        super( AppearancePdu, self ).serialize(outputStream)
        self.liveEntityId.serialize(outputStream)
        outputStream.write_short(int(self.appearanceFlags))
        self.serialize_enum(self.forceId,outputStream)
        self.entityType.serialize(outputStream)
        self.alternateEntityType.serialize(outputStream)
        self.entityMarking.serialize(outputStream)
        outputStream.write_unsigned_int(int(self.capabilities.asbyte))
        self.appearanceFields.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( AppearancePdu, self).parse(inputStream)
        self.liveEntityId.parse(inputStream)
        self.appearanceFlags = inputStream.read_short()
        self.forceId = ForceID.get_enum(self.parse_enum(self.forceId,inputStream))
        self.entityType.parse(inputStream)
        self.alternateEntityType.parse(inputStream)
        self.entityMarking.parse(inputStream)
        self.capabilities.asbyte = inputStream.read_unsigned_int()
        self.appearanceFields.parse(inputStream)

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



