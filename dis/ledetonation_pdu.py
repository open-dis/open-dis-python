from enum import Enum

from .munition_descriptor import MunitionDescriptor
from .live_entity_linear_velocity import LiveEntityLinearVelocity
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .live_entity_orientation16 import LiveEntityOrientation16
from .live_entity_family_pdu import LiveEntityFamilyPdu
from .entity_id import EntityID
from .event_identifier import EventIdentifier
from .live_entity_relative_world_coordinates import LiveEntityRelativeWorldCoordinates

class LEDetonationPdu( LiveEntityFamilyPdu ):
    """9.4.6 Communicate information associated with the impact or detonation of a munition."""

    def __init__(self):
        """ Initializer for LEDetonationPdu"""
        super().__init__()
        # firingLiveEntityId is an undescribed parameter... 
        self.firingLiveEntityId = EntityID()
        self.detonationFlag1 = 0
        self.detonationFlag2 = 0
        # targetLiveEntityId is an undescribed parameter... 
        self.targetLiveEntityId = EntityID()
        # munitionLiveEntityId is an undescribed parameter... 
        self.munitionLiveEntityId = EntityID()
        # eventId is an undescribed parameter... 
        self.eventId = EventIdentifier()
        # worldLocation is an undescribed parameter... 
        self.worldLocation = LiveEntityRelativeWorldCoordinates()
        # velocity is an undescribed parameter... 
        self.velocity = LiveEntityLinearVelocity()
        """ spec error? 16-bit fields vs. 8-bit in TspiPdu?"""
        self.munitionOrientation = LiveEntityOrientation16()
        # munitionDescriptor is an undescribed parameter... 
        self.munitionDescriptor = MunitionDescriptor()
        # entityLocation is an undescribed parameter... 
        self.entityLocation = LiveEntityLinearVelocity()
        self.detonationResult = 0
        self.pduType = DisPduType.live_entity_detonation

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "FiringLiveEntityId :" + "\n" + self.firingLiveEntityId.to_string() + "\n"
        outputString += "DetonationFlag1 : " + str(self.detonationFlag1) + "\n"
        outputString += "DetonationFlag2 : " + str(self.detonationFlag2) + "\n"
        outputString += "TargetLiveEntityId :" + "\n" + self.targetLiveEntityId.to_string() + "\n"
        outputString += "MunitionLiveEntityId :" + "\n" + self.munitionLiveEntityId.to_string() + "\n"
        outputString += "EventId :" + "\n" + self.eventId.to_string() + "\n"
        outputString += "WorldLocation :" + "\n" + self.worldLocation.to_string() + "\n"
        outputString += "Velocity :" + "\n" + self.velocity.to_string() + "\n"
        outputString += "MunitionOrientation :" + "\n" + self.munitionOrientation.to_string() + "\n"
        outputString += "MunitionDescriptor :" + "\n" + self.munitionDescriptor.to_string() + "\n"
        outputString += "EntityLocation :" + "\n" + self.entityLocation.to_string() + "\n"
        outputString += "DetonationResult : " + str(self.detonationResult) + "\n"
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
        super( LEDetonationPdu, self ).serialize(outputStream)
        self.firingLiveEntityId.serialize(outputStream)
        outputStream.write_byte(int(self.detonationFlag1))
        outputStream.write_byte(int(self.detonationFlag2))
        self.targetLiveEntityId.serialize(outputStream)
        self.munitionLiveEntityId.serialize(outputStream)
        self.eventId.serialize(outputStream)
        self.worldLocation.serialize(outputStream)
        self.velocity.serialize(outputStream)
        self.munitionOrientation.serialize(outputStream)
        self.munitionDescriptor.serialize(outputStream)
        self.entityLocation.serialize(outputStream)
        outputStream.write_byte(int(self.detonationResult))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( LEDetonationPdu, self).parse(inputStream)
        self.firingLiveEntityId.parse(inputStream)
        self.detonationFlag1 = inputStream.read_byte()
        self.detonationFlag2 = inputStream.read_byte()
        self.targetLiveEntityId.parse(inputStream)
        self.munitionLiveEntityId.parse(inputStream)
        self.eventId.parse(inputStream)
        self.worldLocation.parse(inputStream)
        self.velocity.parse(inputStream)
        self.munitionOrientation.parse(inputStream)
        self.munitionDescriptor.parse(inputStream)
        self.entityLocation.parse(inputStream)
        self.detonationResult = inputStream.read_byte()

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



