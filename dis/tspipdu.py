from enum import Enum

from .live_entity_position_error import LiveEntityPositionError
from .live_entity_orientation_error import LiveEntityOrientationError
from .live_dead_reckoning_parameters import LiveDeadReckoningParameters
from .live_entity_linear_velocity import LiveEntityLinearVelocity
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .live_entity_family_pdu import LiveEntityFamilyPdu
from .entity_id import EntityID
from .live_entity_relative_world_coordinates import LiveEntityRelativeWorldCoordinates
from .live_entity_orientation import LiveEntityOrientation

class TSPIPdu( LiveEntityFamilyPdu ):
    """9.4.2 The Time Space Position Information (TSPI) PDU shall communicate information about the LE’s state vector."""

    def __init__(self):
        """ Initializer for TSPIPdu"""
        super().__init__()
        # liveEntityId is an undescribed parameter... 
        self.liveEntityId = EntityID()
        """ bit field"""
        self.TSPIFlag = 0
        # entityLocation is an undescribed parameter... 
        self.entityLocation = LiveEntityRelativeWorldCoordinates()
        # entityLinearVelocity is an undescribed parameter... 
        self.entityLinearVelocity = LiveEntityLinearVelocity()
        # entityOrientation is an undescribed parameter... 
        self.entityOrientation = LiveEntityOrientation()
        # positionError is an undescribed parameter... 
        self.positionError = LiveEntityPositionError()
        # orientationError is an undescribed parameter... 
        self.orientationError = LiveEntityOrientationError()
        # deadReckoningParameters is an undescribed parameter... 
        self.deadReckoningParameters = LiveDeadReckoningParameters()
        self.measuredSpeed = 0
        self.systemSpecificDataLength = 0
        self.systemSpecificData =  []
        self.pduType = DisPduType.time_space_position_information

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "LiveEntityId :" + "\n" + self.liveEntityId.to_string() + "\n"
        outputString += "TSPIFlag : " + str(self.TSPIFlag) + "\n"
        outputString += "EntityLocation :" + "\n" + self.entityLocation.to_string() + "\n"
        outputString += "EntityLinearVelocity :" + "\n" + self.entityLinearVelocity.to_string() + "\n"
        outputString += "EntityOrientation :" + "\n" + self.entityOrientation.to_string() + "\n"
        outputString += "PositionError :" + "\n" + self.positionError.to_string() + "\n"
        outputString += "OrientationError :" + "\n" + self.orientationError.to_string() + "\n"
        outputString += "DeadReckoningParameters :" + "\n" + self.deadReckoningParameters.to_string() + "\n"
        outputString += "MeasuredSpeed : " + str(self.measuredSpeed) + "\n"
        outputString += "SystemSpecificDataLength : " + str(self.systemSpecificDataLength) + "\n"
        outputString += "SystemSpecificData : " + "\n"
        for idx in range(0, len(self.systemSpecificData)):
            outputString += str(self.systemSpecificData[idx])

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
        super( TSPIPdu, self ).serialize(outputStream)
        self.liveEntityId.serialize(outputStream)
        outputStream.write_byte(int(self.TSPIFlag))
        self.entityLocation.serialize(outputStream)
        self.entityLinearVelocity.serialize(outputStream)
        self.entityOrientation.serialize(outputStream)
        self.positionError.serialize(outputStream)
        self.orientationError.serialize(outputStream)
        self.deadReckoningParameters.serialize(outputStream)
        outputStream.write_short(int(self.measuredSpeed))
        outputStream.write_byte(int(self.systemSpecificDataLength))
        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.systemSpecificData[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( TSPIPdu, self).parse(inputStream)
        self.liveEntityId.parse(inputStream)
        self.TSPIFlag = inputStream.read_byte()
        self.entityLocation.parse(inputStream)
        self.entityLinearVelocity.parse(inputStream)
        self.entityOrientation.parse(inputStream)
        self.positionError.parse(inputStream)
        self.orientationError.parse(inputStream)
        self.deadReckoningParameters.parse(inputStream)
        self.measuredSpeed = inputStream.read_short()
        self.systemSpecificDataLength = inputStream.read_byte()
        self.systemSpecificData = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.systemSpecificData[  idx  ] = val


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 11

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



