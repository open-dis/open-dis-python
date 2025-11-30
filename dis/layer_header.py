from enum import Enum


class LayerHeader( object ):
    """The identification of the additional information layer number, layer-specific information, and the length of the layer. Section 6.2.51"""

    def __init__(self):
        """ Initializer for LayerHeader"""
        self.layerNumber = 0
        """ field shall specify layer-specific information that varies by System Type (see 6.2.86) and Layer Number."""
        self.layerSpecificInformation = 0
        """ This field shall specify the length in octets of the layer, including the Layer Header record"""
        self.length = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "LayerNumber : " + str(self.layerNumber) + "\n"
        outputString += "LayerSpecificInformation : " + str(self.layerSpecificInformation) + "\n"
        outputString += "Length : " + str(self.length) + "\n"
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
        outputStream.write_byte(int(self.layerNumber))
        outputStream.write_byte(int(self.layerSpecificInformation))
        outputStream.write_short(int(self.length))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.layerNumber = inputStream.read_byte()
        self.layerSpecificInformation = inputStream.read_byte()
        self.length = inputStream.read_short()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 3

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



