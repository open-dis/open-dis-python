from enum import Enum

from .data_filter_record import DataFilterRecord
from .minefield_sensor_type import MinefieldSensorType
from .entity_type import EntityType
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .minefield_family_pdu import MinefieldFamilyPdu
from .minefield_identifier import MinefieldIdentifier
from .entity_id import EntityID
from .vector2float import Vector2Float

class MinefieldQueryPdu( MinefieldFamilyPdu ):
    """5.10.3 Contains information about the requesting entity and the region and mine types of interest to the requesting entity."""

    def __init__(self):
        """ Initializer for MinefieldQueryPdu"""
        super().__init__()
        """ Minefield ID provides a unique identifier"""
        self.minefieldID = MinefieldIdentifier()
        """ EID of entity making the request"""
        self.requestingEntityID = EntityID()
        """ request ID provides a unique identifier"""
        self.requestID = 0
        """ Number of perimeter points for the minefield"""
        self.numberOfPerimeterPoints = 0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ Number of sensor types"""
        self.numberOfSensorTypes = 0
        """ data filter, 32 boolean fields"""
        self.dataFilter = DataFilterRecord()
        """ Entity type of mine being requested"""
        self.requestedMineType = EntityType()
        """ perimeter points of request"""
        self._requestedPerimeterPoints = []
        """ Sensor types, each 16-bits long"""
        self._sensorTypes = []
        self.pduType = DisPduType.minefield_query


    def get_numberOfPerimeterPoints(self):
        return len(self._requestedPerimeterPoints)
    def set_numberOfPerimeterPoints(self, value):
        numberOfPerimeterPoints = value


    def get_numberOfSensorTypes(self):
        return len(self._sensorTypes)
    def set_numberOfSensorTypes(self, value):
        numberOfSensorTypes = value


    def get_requestedPerimeterPoints(self):
        return self._requestedPerimeterPoints
    def set_requestedPerimeterPoints(self, value):
        self._requestedPerimeterPoints = value
    requestedPerimeterPoints = property(get_requestedPerimeterPoints, set_requestedPerimeterPoints)


    def add_requestedPerimeterPoints(self, value : Vector2Float):
        self._requestedPerimeterPoints.append(value)


    """
    ///            Name : requestedPerimeterPoints
    ///             UID : 
    ///            Type : Vector2Float
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : perimeter points of request
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_sensorTypes(self):
        return self._sensorTypes
    def set_sensorTypes(self, value):
        self._sensorTypes = value
    sensorTypes = property(get_sensorTypes, set_sensorTypes)


    def add_sensorTypes(self, value : MinefieldSensorType):
        self._sensorTypes.append(value)


    """
    ///            Name : sensorTypes
    ///             UID : 
    ///            Type : MinefieldSensorType
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Sensor types, each 16-bits long
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
        outputString += "MinefieldID :" + "\n" + self.minefieldID.to_string() + "\n"
        outputString += "RequestingEntityID :" + "\n" + self.requestingEntityID.to_string() + "\n"
        outputString += "RequestID : " + str(self.requestID) + "\n"
        outputString += "NumberOfPerimeterPoints : " + str(len(self._requestedPerimeterPoints)) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "NumberOfSensorTypes : " + str(len(self._sensorTypes)) + "\n"
        outputString += "DataFilter :" + "\n" + self.dataFilter.to_string() + "\n"
        outputString += "RequestedMineType :" + "\n" + self.requestedMineType.to_string() + "\n"
        outputString += "RequestedPerimeterPoints : " + "\n"
        for idx in range(0, len(self._requestedPerimeterPoints)):
            outputString += self._requestedPerimeterPoints[idx].to_string()

        outputString += "SensorTypes : " + "\n"
        for idx in range(0, len(self._sensorTypes)):
            outputString += self._sensorTypes[idx].to_string()

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
        super( MinefieldQueryPdu, self ).serialize(outputStream)
        self.minefieldID.serialize(outputStream)
        self.requestingEntityID.serialize(outputStream)
        outputStream.write_byte(int(self.requestID))
        outputStream.write_byte( len(self._requestedPerimeterPoints))
        outputStream.write_byte(int(self.padding))
        outputStream.write_byte( len(self._sensorTypes))
        self.dataFilter.serialize(outputStream)
        self.requestedMineType.serialize(outputStream)
        for anObj in self._requestedPerimeterPoints:
            anObj.serialize(outputStream)

        for anObj in self._sensorTypes:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( MinefieldQueryPdu, self).parse(inputStream)
        self.minefieldID.parse(inputStream)
        self.requestingEntityID.parse(inputStream)
        self.requestID = inputStream.read_byte()
        self.numberOfPerimeterPoints = inputStream.read_byte()
        self.padding = inputStream.read_byte()
        self.numberOfSensorTypes = inputStream.read_byte()
        self.dataFilter.parse(inputStream)
        self.requestedMineType.parse(inputStream)
        for idx in range(0, self.numberOfPerimeterPoints):
            element = Vector2Float()
            element.parse(inputStream)
            self._requestedPerimeterPoints.append(element)

        for idx in range(0, self.numberOfSensorTypes):
            element = MinefieldSensorType()
            element.parse(inputStream)
            self._sensorTypes.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 10

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



