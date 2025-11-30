from enum import Enum

from .siso_ref_010.enums.navigation_source import NavigationSource

class Mode5TransponderBasicData( object ):
    """B.2.29. Mode 5 transponder basic data"""

    def __init__(self):
        """ Initializer for Mode5TransponderBasicData"""
        """ Mode 5 status, part of Mode 5 transponder basic data fields"""
        self.mode5Status = 0
        """ Personal Identification Number (PIN), part of Mode 5 transponder basic data fields"""
        self.personalIdentificationNumber = 0
        """ Mode 5 Message Formats Present, part of Mode 5 transponder basic data fields"""
        self.mode5MessageFormatsPresent = 0
        """ Enhanced Mode 1, part of Mode 5 transponder basic data fields"""
        self.enhancedMode1 = 0
        """ National Origin, part of Mode 5 transponder basic data fields"""
        self.nationalOrigin = 0
        """ Supplemental Data, part of Mode 5 transponder basic data fields"""
        self.supplementalData = 0
        # /** Navigation Source, part of Mode 5 transponder basic data fields UID 359 */
        self.navigationSource = NavigationSource.default

        """ Figure of merit, part of Mode 5 transponder basic data fields"""
        self.figureOfMerit = 0
        """ Padding, part of Mode 5 transponder basic data fields"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "Mode5Status : " + str(self.mode5Status) + "\n"
        outputString += "PersonalIdentificationNumber : " + str(self.personalIdentificationNumber) + "\n"
        outputString += "Mode5MessageFormatsPresent : " + str(self.mode5MessageFormatsPresent) + "\n"
        outputString += "EnhancedMode1 : " + str(self.enhancedMode1) + "\n"
        outputString += "NationalOrigin : " + str(self.nationalOrigin) + "\n"
        outputString += "SupplementalData : " + str(self.supplementalData) + "\n"
        outputString += "NavigationSource : " + self.navigationSource.get_description + "(" + (str(int(self.navigationSource))) + ")" + "\n"
        outputString += "FigureOfMerit : " + str(self.figureOfMerit) + "\n"
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
        outputStream.write_short(int(self.mode5Status))
        outputStream.write_short(int(self.personalIdentificationNumber))
        outputStream.write_int(int(self.mode5MessageFormatsPresent))
        outputStream.write_short(int(self.enhancedMode1))
        outputStream.write_short(int(self.nationalOrigin))
        outputStream.write_byte(int(self.supplementalData))
        self.serialize_enum(self.navigationSource,outputStream)
        outputStream.write_byte(int(self.figureOfMerit))
        outputStream.write_byte(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.mode5Status = inputStream.read_short()
        self.personalIdentificationNumber = inputStream.read_short()
        self.mode5MessageFormatsPresent = inputStream.read_int()
        self.enhancedMode1 = inputStream.read_short()
        self.nationalOrigin = inputStream.read_short()
        self.supplementalData = inputStream.read_byte()
        self.navigationSource = NavigationSource.get_enum(self.parse_enum(self.navigationSource,inputStream))
        self.figureOfMerit = inputStream.read_byte()
        self.padding = inputStream.read_byte()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 9

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



