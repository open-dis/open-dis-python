from enum import Enum

from .siso_ref_010.enums.grid_axis_descriptor_axis_type import GridAxisDescriptorAxisType

class GridAxisDescriptor( object ):
    """Detailed information about the grid dimensions (axes) and coordinates for environmental state variables"""

    def __init__(self):
        """ Initializer for GridAxisDescriptor"""
        """ coordinate of the grid origin or initial value"""
        self.domainInitialXi = 0.0
        """ coordinate of the endpoint or final value"""
        self.domainFinalXi = 0.0
        """ The number of grid points along the Xi domain axis for the enviornmental state data"""
        self.domainPointsXi = 0
        """ interleaf factor along the domain axis."""
        self.interleafFactor = 0
        # /** type of grid axis uid 377 */
        self.axisType = GridAxisDescriptorAxisType.default


    def to_string(self) ->str:
        outputString = ""
        outputString += "DomainInitialXi : " + str(self.domainInitialXi) + "\n"
        outputString += "DomainFinalXi : " + str(self.domainFinalXi) + "\n"
        outputString += "DomainPointsXi : " + str(self.domainPointsXi) + "\n"
        outputString += "InterleafFactor : " + str(self.interleafFactor) + "\n"
        outputString += "GridAxisDescriptorAxisType : " + self.axisType.get_description + "(" + (str(int(self.axisType))) + ")" + "\n"
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
        outputStream.write_double(int(self.domainInitialXi))
        outputStream.write_double(int(self.domainFinalXi))
        outputStream.write_short(int(self.domainPointsXi))
        outputStream.write_byte(int(self.interleafFactor))
        self.serialize_enum(self.axisType,outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.domainInitialXi = inputStream.read_double()
        self.domainFinalXi = inputStream.read_double()
        self.domainPointsXi = inputStream.read_short()
        self.interleafFactor = inputStream.read_byte()
        self.axisType = GridAxisDescriptorAxisType.get_enum(self.parse_enum(self.axisType,inputStream))

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 5

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



