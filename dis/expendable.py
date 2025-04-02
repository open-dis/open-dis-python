from enum import Enum

from .entity_type import EntityType
from .siso_ref_010.enums.munition_expendable_status import MunitionExpendableStatus

class Expendable( object ):
    """An entity's expendable (chaff, flares, etc.) information. Section 6.2.36"""

    def __init__(self):
        """ Initializer for Expendable"""
        """ Type of expendable"""
        self.expendable = EntityType()
        self.station = 0
        self.quantity = 0
        # /**  uid 327 */
        self.expendableStatus = MunitionExpendableStatus.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "Expendable :" + "\n" + self.expendable.to_string() + "\n"
        outputString += "Station : " + str(self.station) + "\n"
        outputString += "Quantity : " + str(self.quantity) + "\n"
        outputString += "MunitionExpendableStatus : " + self.expendableStatus.get_description + "(" + (str(int(self.expendableStatus))) + ")" + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
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
        self.expendable.serialize(outputStream)
        outputStream.write_int(int(self.station))
        outputStream.write_short(int(self.quantity))
        self.serialize_enum(self.expendableStatus,outputStream)
        outputStream.write_byte(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.expendable.parse(inputStream)
        self.station = inputStream.read_int()
        self.quantity = inputStream.read_short()
        self.expendableStatus = MunitionExpendableStatus.get_enum(self.parse_enum(self.expendableStatus,inputStream))
        self.padding = inputStream.read_byte()

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



