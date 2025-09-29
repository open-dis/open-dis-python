from enum import Enum

from .siso_ref_010.enums.system_on_off_status import SystemOnOffStatus

class FundamentalOperationalData( object ):
    """Basic operational data for IFF. Section 6.2.39"""

    def __init__(self):
        """ Initializer for FundamentalOperationalData"""
        # /** system status, IEEE DIS 7 defined uid 2120 */
        self.systemStatus = SystemOnOffStatus.default

        """ data field 1"""
        self.dataField1 = 0
        """ eight boolean fields"""
        self.informationLayers = 0
        """ enumeration"""
        self.dataField2 = 0
        """ parameter, enumeration"""
        self.parameter1 = 0
        """ parameter, enumeration"""
        self.parameter2 = 0
        """ parameter, enumeration"""
        self.parameter3 = 0
        """ parameter, enumeration"""
        self.parameter4 = 0
        """ parameter, enumeration"""
        self.parameter5 = 0
        """ parameter, enumeration"""
        self.parameter6 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "SystemOnOffStatus : " + self.systemStatus.get_description + "(" + (str(int(self.systemStatus))) + ")" + "\n"
        outputString += "DataField1 : " + str(self.dataField1) + "\n"
        outputString += "InformationLayers : " + str(self.informationLayers) + "\n"
        outputString += "DataField2 : " + str(self.dataField2) + "\n"
        outputString += "Parameter1 : " + str(self.parameter1) + "\n"
        outputString += "Parameter2 : " + str(self.parameter2) + "\n"
        outputString += "Parameter3 : " + str(self.parameter3) + "\n"
        outputString += "Parameter4 : " + str(self.parameter4) + "\n"
        outputString += "Parameter5 : " + str(self.parameter5) + "\n"
        outputString += "Parameter6 : " + str(self.parameter6) + "\n"
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
        self.serialize_enum(self.systemStatus,outputStream)
        outputStream.write_byte(int(self.dataField1))
        outputStream.write_byte(int(self.informationLayers))
        outputStream.write_byte(int(self.dataField2))
        outputStream.write_short(int(self.parameter1))
        outputStream.write_short(int(self.parameter2))
        outputStream.write_short(int(self.parameter3))
        outputStream.write_short(int(self.parameter4))
        outputStream.write_short(int(self.parameter5))
        outputStream.write_short(int(self.parameter6))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.systemStatus = SystemOnOffStatus.get_enum(self.parse_enum(self.systemStatus,inputStream))
        self.dataField1 = inputStream.read_byte()
        self.informationLayers = inputStream.read_byte()
        self.dataField2 = inputStream.read_byte()
        self.parameter1 = inputStream.read_short()
        self.parameter2 = inputStream.read_short()
        self.parameter3 = inputStream.read_short()
        self.parameter4 = inputStream.read_short()
        self.parameter5 = inputStream.read_short()
        self.parameter6 = inputStream.read_short()

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



