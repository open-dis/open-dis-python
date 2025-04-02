from enum import Enum

from .data_filter_record import DataFilterRecord
from .minefield_sensor_type import MinefieldSensorType
from .mine_emplacement_time import MineEmplacementTime
from .entity_type import EntityType
from .euler_angles import EulerAngles
from .siso_ref_010.enums.minefield_data_paint_scheme import MinefieldDataPaintScheme
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .minefield_family_pdu import MinefieldFamilyPdu
from .vector3float import Vector3Float
from .minefield_identifier import MinefieldIdentifier
from .simulation_identifier import SimulationIdentifier
from .siso_ref_010.enums.minefield_data_fusing import MinefieldDataFusing

class MinefieldDataPdu( MinefieldFamilyPdu ):
    """5.10.4 Information about the location and status of a collection of mines in a minefield is conveyed through the Minefield Data PDU on an individual mine basis."""

    def __init__(self):
        """ Initializer for MinefieldDataPdu"""
        super().__init__()
        """ Minefield ID provides a unique identifier"""
        self.minefieldID = MinefieldIdentifier()
        """ ID of entity making request"""
        self.requestingEntityID = SimulationIdentifier()
        """ Minefield sequence number"""
        self.minefieldSequenceNumbeer = 0
        """ request ID provides a unique identifier"""
        self.requestID = 0
        """ pdu sequence number"""
        self.pduSequenceNumber = 0
        """ number of pdus in response"""
        self.numberOfPdus = 0
        """ how many mines are in this PDU"""
        self.numberOfMinesInThisPdu = 0
        """ how many sensor type are in this PDU"""
        self.numberOfSensorTypes = 0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ 32 boolean field"""
        self.dataFilter = DataFilterRecord()
        """ Mine type"""
        self.mineType = EntityType()
        """ Sensor types, each 16-bits long"""
        self._sensorTypes = []
        self.padTo32 = [0] * 32
        """ Mine locations"""
        self._mineLocation = []
        self.groundBurialDepthOffset =  []
        self.waterBurialDepthOffset =  []
        self.snowBurialDepthOffset =  []
        self._mineOrientation = []
        self.thermalContrast =  []
        self.reflectance =  []
        self._mineEmplacementTime = []
        self.mineEntityNumber =  []
        """  uid 192"""
        self._fusing = []
        self.scalarDetectionCoefficient =  []
        """  uid 202"""
        self._paintScheme = []
        self.padTo32_2 = [0] * 32
        self.numberOfTripDetonationWires =  []
        self.padTo32_3 = [0] * 32
        self.numberOfVertices =  []
        self.pduType = DisPduType.minefield_data


    def get_numberOfSensorTypes(self):
        return len(self._sensorTypes)
    def set_numberOfSensorTypes(self, value):
        numberOfSensorTypes = value


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




    def get_mineLocation(self):
        return self._mineLocation
    def set_mineLocation(self, value):
        self._mineLocation = value
    mineLocation = property(get_mineLocation, set_mineLocation)


    def add_mineLocation(self, value : Vector3Float):
        self._mineLocation.append(value)


    """
    ///            Name : mineLocation
    ///             UID : 
    ///            Type : Vector3Float
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Mine locations
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_mineOrientation(self):
        return self._mineOrientation
    def set_mineOrientation(self, value):
        self._mineOrientation = value
    mineOrientation = property(get_mineOrientation, set_mineOrientation)


    def add_mineOrientation(self, value : EulerAngles):
        self._mineOrientation.append(value)


    """
    ///            Name : mineOrientation
    ///             UID : 
    ///            Type : EulerAngles
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




    def get_mineEmplacementTime(self):
        return self._mineEmplacementTime
    def set_mineEmplacementTime(self, value):
        self._mineEmplacementTime = value
    mineEmplacementTime = property(get_mineEmplacementTime, set_mineEmplacementTime)


    def add_mineEmplacementTime(self, value : MineEmplacementTime):
        self._mineEmplacementTime.append(value)


    """
    ///            Name : mineEmplacementTime
    ///             UID : 
    ///            Type : MineEmplacementTime
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




    def get_fusing(self):
        return self._fusing
    def set_fusing(self, value):
        self._fusing = value
    fusing = property(get_fusing, set_fusing)


    def add_fusing(self, value : MinefieldDataFusing):
        self._fusing.append(value)


    """
    ///            Name : fusing
    ///             UID : 192
    ///            Type : MinefieldDataFusing
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment :  uid 192
    ///   default value : null
    ///     is Bitfield : true
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : SISO_BITFIELD
    /// underlying Type : N/A
    """




    def get_paintScheme(self):
        return self._paintScheme
    def set_paintScheme(self, value):
        self._paintScheme = value
    paintScheme = property(get_paintScheme, set_paintScheme)


    def add_paintScheme(self, value : MinefieldDataPaintScheme):
        self._paintScheme.append(value)


    """
    ///            Name : paintScheme
    ///             UID : 202
    ///            Type : MinefieldDataPaintScheme
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment :  uid 202
    ///   default value : null
    ///     is Bitfield : true
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : SISO_BITFIELD
    /// underlying Type : N/A
    """



    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "MinefieldID :" + "\n" + self.minefieldID.to_string() + "\n"
        outputString += "RequestingEntityID :" + "\n" + self.requestingEntityID.to_string() + "\n"
        outputString += "MinefieldSequenceNumbeer : " + str(self.minefieldSequenceNumbeer) + "\n"
        outputString += "RequestID : " + str(self.requestID) + "\n"
        outputString += "PduSequenceNumber : " + str(self.pduSequenceNumber) + "\n"
        outputString += "NumberOfPdus : " + str(self.numberOfPdus) + "\n"
        outputString += "NumberOfMinesInThisPdu : " + str(self.numberOfMinesInThisPdu) + "\n"
        outputString += "NumberOfSensorTypes : " + str(len(self._sensorTypes)) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "DataFilter :" + "\n" + self.dataFilter.to_string() + "\n"
        outputString += "MineType :" + "\n" + self.mineType.to_string() + "\n"
        outputString += "SensorTypes : " + "\n"
        for idx in range(0, len(self._sensorTypes)):
            outputString += self._sensorTypes[idx].to_string()

        outputString += "MineLocation : " + "\n"
        for idx in range(0, len(self._mineLocation)):
            outputString += self._mineLocation[idx].to_string()

        outputString += "GroundBurialDepthOffset : " + "\n"
        for idx in range(0, len(self.groundBurialDepthOffset)):
            outputString += str(self.groundBurialDepthOffset[idx])

        outputString += "WaterBurialDepthOffset : " + "\n"
        for idx in range(0, len(self.waterBurialDepthOffset)):
            outputString += str(self.waterBurialDepthOffset[idx])

        outputString += "SnowBurialDepthOffset : " + "\n"
        for idx in range(0, len(self.snowBurialDepthOffset)):
            outputString += str(self.snowBurialDepthOffset[idx])

        outputString += "MineOrientation : " + "\n"
        for idx in range(0, len(self._mineOrientation)):
            outputString += self._mineOrientation[idx].to_string()

        outputString += "ThermalContrast : " + "\n"
        for idx in range(0, len(self.thermalContrast)):
            outputString += str(self.thermalContrast[idx])

        outputString += "Reflectance : " + "\n"
        for idx in range(0, len(self.reflectance)):
            outputString += str(self.reflectance[idx])

        outputString += "MineEmplacementTime : " + "\n"
        for idx in range(0, len(self._mineEmplacementTime)):
            outputString += self._mineEmplacementTime[idx].to_string()

        outputString += "MineEntityNumber : " + "\n"
        for idx in range(0, len(self.mineEntityNumber)):
            outputString += str(self.mineEntityNumber[idx])

        outputString += "Fusing : " + "\n"
        for idx in range(0, len(self._fusing)):
            outputString += self._fusing[idx].to_string()

        outputString += "ScalarDetectionCoefficient : " + "\n"
        for idx in range(0, len(self.scalarDetectionCoefficient)):
            outputString += str(self.scalarDetectionCoefficient[idx])

        outputString += "PaintScheme : " + "\n"
        for idx in range(0, len(self._paintScheme)):
            outputString += self._paintScheme[idx].to_string()

        outputString += "NumberOfTripDetonationWires : " + "\n"
        for idx in range(0, len(self.numberOfTripDetonationWires)):
            outputString += str(self.numberOfTripDetonationWires[idx])

        outputString += "NumberOfVertices : " + "\n"
        for idx in range(0, len(self.numberOfVertices)):
            outputString += str(self.numberOfVertices[idx])

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
        super( MinefieldDataPdu, self ).serialize(outputStream)
        self.minefieldID.serialize(outputStream)
        self.requestingEntityID.serialize(outputStream)
        outputStream.write_short(int(self.minefieldSequenceNumbeer))
        outputStream.write_byte(int(self.requestID))
        outputStream.write_byte(int(self.pduSequenceNumber))
        outputStream.write_byte(int(self.numberOfPdus))
        outputStream.write_byte(int(self.numberOfMinesInThisPdu))
        outputStream.write_byte( len(self._sensorTypes))
        outputStream.write_byte(int(self.padding))
        self.dataFilter.serialize(outputStream)
        self.mineType.serialize(outputStream)
        for anObj in self._sensorTypes:
            anObj.serialize(outputStream)

        for anObj in self._mineLocation:
            anObj.serialize(outputStream)

        for idx in range(0, 0):
            outputStream.write_float( self.groundBurialDepthOffset[ idx ] );

        for idx in range(0, 0):
            outputStream.write_float( self.waterBurialDepthOffset[ idx ] );

        for idx in range(0, 0):
            outputStream.write_float( self.snowBurialDepthOffset[ idx ] );

        for anObj in self._mineOrientation:
            anObj.serialize(outputStream)

        for idx in range(0, 0):
            outputStream.write_float( self.thermalContrast[ idx ] );

        for idx in range(0, 0):
            outputStream.write_float( self.reflectance[ idx ] );

        for anObj in self._mineEmplacementTime:
            anObj.serialize(outputStream)

        for idx in range(0, 0):
            outputStream.write_unsigned_short( self.mineEntityNumber[ idx ] );

        for anObj in self._fusing:
            anObj.serialize(outputStream)

        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.scalarDetectionCoefficient[ idx ] );

        for anObj in self._paintScheme:
            anObj.serialize(outputStream)

        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.numberOfTripDetonationWires[ idx ] );

        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.numberOfVertices[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( MinefieldDataPdu, self).parse(inputStream)
        self.minefieldID.parse(inputStream)
        self.requestingEntityID.parse(inputStream)
        self.minefieldSequenceNumbeer = inputStream.read_short()
        self.requestID = inputStream.read_byte()
        self.pduSequenceNumber = inputStream.read_byte()
        self.numberOfPdus = inputStream.read_byte()
        self.numberOfMinesInThisPdu = inputStream.read_byte()
        self.numberOfSensorTypes = inputStream.read_byte()
        self.padding = inputStream.read_byte()
        self.dataFilter.parse(inputStream)
        self.mineType.parse(inputStream)
        for idx in range(0, self.numberOfSensorTypes):
            element = MinefieldSensorType()
            element.parse(inputStream)
            self._sensorTypes.append(element)

        for idx in range(0, self.numberOfMinesInThisPdu):
            element = Vector3Float()
            element.parse(inputStream)
            self._mineLocation.append(element)

        self.groundBurialDepthOffset = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_float()
            self.groundBurialDepthOffset[  idx  ] = val

        self.waterBurialDepthOffset = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_float()
            self.waterBurialDepthOffset[  idx  ] = val

        self.snowBurialDepthOffset = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_float()
            self.snowBurialDepthOffset[  idx  ] = val

        for idx in range(0, self.numberOfMinesInThisPdu):
            element = EulerAngles()
            element.parse(inputStream)
            self._mineOrientation.append(element)

        self.thermalContrast = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_float()
            self.thermalContrast[  idx  ] = val

        self.reflectance = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_float()
            self.reflectance[  idx  ] = val

        for idx in range(0, self.numberOfMinesInThisPdu):
            element = MineEmplacementTime()
            element.parse(inputStream)
            self._mineEmplacementTime.append(element)

        self.mineEntityNumber = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_short()
            self.mineEntityNumber[  idx  ] = val

        for idx in range(0, self.numberOfMinesInThisPdu):
            element = MinefieldDataFusing()
            element.parse(inputStream)
            self._fusing.append(element)

        self.scalarDetectionCoefficient = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.scalarDetectionCoefficient[  idx  ] = val

        for idx in range(0, self.numberOfMinesInThisPdu):
            element = MinefieldDataPaintScheme()
            element.parse(inputStream)
            self._paintScheme.append(element)

        self.numberOfTripDetonationWires = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.numberOfTripDetonationWires[  idx  ] = val

        self.numberOfVertices = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.numberOfVertices[  idx  ] = val


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 29

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



