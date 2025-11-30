from enum import Enum

from .grid_axis_descriptor import GridAxisDescriptor
from .entity_type import EntityType
from .euler_angles import EulerAngles
from .clock_time import ClockTime
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .grid_data import GridData
from .synthetic_environment_family_pdu import SyntheticEnvironmentFamilyPdu
from .siso_ref_010.enums.gridded_data_coordinate_system import GriddedDataCoordinateSystem
from .siso_ref_010.enums.gridded_data_constant_grid import GriddedDataConstantGrid
from .simulation_identifier import SimulationIdentifier

class GriddedDataPdu( SyntheticEnvironmentFamilyPdu ):
    """7.10.3 Used to communicate information about global, spatially varying environmental effects."""

    def __init__(self):
        """ Initializer for GriddedDataPdu"""
        super().__init__()
        """ environmental simulation application ID provides a unique identifier"""
        self.environmentalSimulationApplicationID = SimulationIdentifier()
        """ unique identifier for each piece of environmental data"""
        self.fieldNumber = 0
        """ sequence number for the total set of PDUS used to transmit the data"""
        self.pduNumber = 0
        """ Total number of PDUS used to transmit the data"""
        self.pduTotal = 0
        # /** coordinate system of the grid uid 244 */
        self.coordinateSystem = GriddedDataCoordinateSystem.default

        """ number of grid axes for the environmental data"""
        self.numberOfGridAxes = 0
        # /** are domain grid axes identidal to those of the priveious domain update? uid 245 */
        self.constantGrid = GriddedDataConstantGrid.default

        """ type of environment"""
        self.environmentType = EntityType()
        """ orientation of the data grid"""
        self.orientation = EulerAngles()
        """ valid time of the enviormental data sample, 64-bit unsigned int"""
        self.sampleTime = ClockTime()
        """ total number of all data values for all pdus for an environmental sample"""
        self.totalValues = 0
        """ total number of data values at each grid point."""
        self.vectorDimension = 0
        """ padding"""
        self.padding1 = 0
        """ padding"""
        self.padding2 = 0
        """ """
        self._gridAxisDescriptors = []
        """ """
        self._gridDataRecords = []
        self.pduType = DisPduType.gridded_data


    def get_numberOfGridAxes(self):
        return len(self._gridDataRecords)
    def set_numberOfGridAxes(self, value):
        numberOfGridAxes = value


    def get_gridAxisDescriptors(self):
        return self._gridAxisDescriptors
    def set_gridAxisDescriptors(self, value):
        self._gridAxisDescriptors = value
    gridAxisDescriptors = property(get_gridAxisDescriptors, set_gridAxisDescriptors)


    def add_gridAxisDescriptors(self, value : GridAxisDescriptor):
        self._gridAxisDescriptors.append(value)


    """
    ///            Name : gridAxisDescriptors
    ///             UID : 
    ///            Type : GridAxisDescriptor
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : 
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_gridDataRecords(self):
        return self._gridDataRecords
    def set_gridDataRecords(self, value):
        self._gridDataRecords = value
    gridDataRecords = property(get_gridDataRecords, set_gridDataRecords)


    def add_gridDataRecords(self, value : GridData):
        self._gridDataRecords.append(value)


    """
    ///            Name : gridDataRecords
    ///             UID : 
    ///            Type : GridData
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : 
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
        outputString += "EnvironmentalSimulationApplicationID :" + "\n" + self.environmentalSimulationApplicationID.to_string() + "\n"
        outputString += "FieldNumber : " + str(self.fieldNumber) + "\n"
        outputString += "PduNumber : " + str(self.pduNumber) + "\n"
        outputString += "PduTotal : " + str(self.pduTotal) + "\n"
        outputString += "GriddedDataCoordinateSystem : " + self.coordinateSystem.get_description + "(" + (str(int(self.coordinateSystem))) + ")" + "\n"
        outputString += "NumberOfGridAxes : " + str(len(self._gridDataRecords)) + "\n"
        outputString += "GriddedDataConstantGrid : " + self.constantGrid.get_description + "(" + (str(int(self.constantGrid))) + ")" + "\n"
        outputString += "EnvironmentType :" + "\n" + self.environmentType.to_string() + "\n"
        outputString += "Orientation :" + "\n" + self.orientation.to_string() + "\n"
        outputString += "SampleTime :" + "\n" + self.sampleTime.to_string() + "\n"
        outputString += "TotalValues : " + str(self.totalValues) + "\n"
        outputString += "VectorDimension : " + str(self.vectorDimension) + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "GridAxisDescriptors : " + "\n"
        for idx in range(0, len(self._gridAxisDescriptors)):
            outputString += self._gridAxisDescriptors[idx].to_string()

        outputString += "GridDataRecords : " + "\n"
        for idx in range(0, len(self._gridDataRecords)):
            outputString += self._gridDataRecords[idx].to_string()

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
        super( GriddedDataPdu, self ).serialize(outputStream)
        self.environmentalSimulationApplicationID.serialize(outputStream)
        outputStream.write_short(int(self.fieldNumber))
        outputStream.write_short(int(self.pduNumber))
        outputStream.write_short(int(self.pduTotal))
        self.serialize_enum(self.coordinateSystem,outputStream)
        outputStream.write_byte( len(self._gridDataRecords))
        self.serialize_enum(self.constantGrid,outputStream)
        self.environmentType.serialize(outputStream)
        self.orientation.serialize(outputStream)
        self.sampleTime.serialize(outputStream)
        outputStream.write_int(int(self.totalValues))
        outputStream.write_byte(int(self.vectorDimension))
        outputStream.write_byte(int(self.padding1))
        outputStream.write_short(int(self.padding2))
        for anObj in self._gridAxisDescriptors:
            anObj.serialize(outputStream)

        for anObj in self._gridDataRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( GriddedDataPdu, self).parse(inputStream)
        self.environmentalSimulationApplicationID.parse(inputStream)
        self.fieldNumber = inputStream.read_short()
        self.pduNumber = inputStream.read_short()
        self.pduTotal = inputStream.read_short()
        self.coordinateSystem = GriddedDataCoordinateSystem.get_enum(self.parse_enum(self.coordinateSystem,inputStream))
        self.numberOfGridAxes = inputStream.read_byte()
        self.constantGrid = GriddedDataConstantGrid.get_enum(self.parse_enum(self.constantGrid,inputStream))
        self.environmentType.parse(inputStream)
        self.orientation.parse(inputStream)
        self.sampleTime.parse(inputStream)
        self.totalValues = inputStream.read_int()
        self.vectorDimension = inputStream.read_byte()
        self.padding1 = inputStream.read_byte()
        self.padding2 = inputStream.read_short()
        for idx in range(0, self.numberOfGridAxes):
            element = GridAxisDescriptor()
            element.parse(inputStream)
            self._gridAxisDescriptors.append(element)

        for idx in range(0, self.numberOfGridAxes):
            element = GridData()
            element.parse(inputStream)
            self._gridDataRecords.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 16

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



