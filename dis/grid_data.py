from enum import Enum

from .siso_ref_010.enums.gridded_data_data_representation import GriddedDataDataRepresentation
from .siso_ref_010.enums.gridded_data_sample_type import GriddedDataSampleType

class GridData( object ):
    """6.2.41, table 68"""

    def __init__(self):
        """ Initializer for GridData"""
        # /**  uid 246 */
        self.sampleType = GriddedDataSampleType.default

        # /**  uid 247 */
        self.dataRepresentation = GriddedDataDataRepresentation.default


    def to_string(self) ->str:
        outputString = ""
        outputString += "GriddedDataSampleType : " + self.sampleType.get_description + "(" + (str(int(self.sampleType))) + ")" + "\n"
        outputString += "GriddedDataDataRepresentation : " + self.dataRepresentation.get_description + "(" + (str(int(self.dataRepresentation))) + ")" + "\n"
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
        self.serialize_enum(self.sampleType,outputStream)
        self.serialize_enum(self.dataRepresentation,outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.sampleType = GriddedDataSampleType.get_enum(self.parse_enum(self.sampleType,inputStream))
        self.dataRepresentation = GriddedDataDataRepresentation.get_enum(self.parse_enum(self.dataRepresentation,inputStream))

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 2

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



