from enum import Enum

from .grid_axis_descriptor import GridAxisDescriptor

class GridAxisDescriptorVariable( GridAxisDescriptor ):
    """Grid axis descriptor fo variable spacing axis data."""

    def __init__(self):
        """ Initializer for GridAxisDescriptorVariable"""
        super().__init__()
        """ Number of grid locations along Xi axis"""
        self.numberOfPointsOnXiAxis = 0
        """ initial grid point for the current pdu"""
        self.initialIndex = 0
        """ value that linearly scales the coordinates of the grid locations for the xi axis"""
        self.coordinateScaleXi = 0.0
        """ The constant offset value that shall be applied to the grid locations for the xi axis"""
        self.coordinateOffsetXi = 0.0
        """ list of coordinates"""
        self.xiValues =  []
        self.padding = [0] * 64

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "NumberOfPointsOnXiAxis : " + str(self.numberOfPointsOnXiAxis) + "\n"
        outputString += "InitialIndex : " + str(self.initialIndex) + "\n"
        outputString += "CoordinateScaleXi : " + str(self.coordinateScaleXi) + "\n"
        outputString += "CoordinateOffsetXi : " + str(self.coordinateOffsetXi) + "\n"
        outputString += "XiValues : " + "\n"
        for idx in range(0, len(self.xiValues)):
            outputString += str(self.xiValues[idx])

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
        super( GridAxisDescriptorVariable, self ).serialize(outputStream)
        outputStream.write_short(int(self.numberOfPointsOnXiAxis))
        outputStream.write_short(int(self.initialIndex))
        outputStream.write_double(int(self.coordinateScaleXi))
        outputStream.write_double(int(self.coordinateOffsetXi))
        for idx in range(0, 0):
            outputStream.write_unsigned_short( self.xiValues[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( GridAxisDescriptorVariable, self).parse(inputStream)
        self.numberOfPointsOnXiAxis = inputStream.read_short()
        self.initialIndex = inputStream.read_short()
        self.coordinateScaleXi = inputStream.read_double()
        self.coordinateOffsetXi = inputStream.read_double()
        self.xiValues = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_short()
            self.xiValues[  idx  ] = val


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 6

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



