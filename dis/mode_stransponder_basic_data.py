from enum import Enum

from .siso_ref_010.enums.aircraft_identification_type import AircraftIdentificationType
from .siso_ref_010.enums.aircraft_present_domain import AircraftPresentDomain
from .siso_ref_010.enums.capability_report import CapabilityReport

class ModeSTransponderBasicData( object ):
    """B.2.41. Mode S transponder basic data"""

    def __init__(self):
        """ Initializer for ModeSTransponderBasicData"""
        """ Mode S transponder status, part of Mode S transponder basic data fields. See B.2.42."""
        self.modeSTransponderStatus = 0
        """ Mode S levels present, part of Mode S transponder basic data fields. See B.2.40."""
        self.modeSLevelsPresent = 0
        # /** aircraft present domain uid 356 */
        self.aircraftPresentDomain = AircraftPresentDomain.default

        """ Aircraft identification, part of Mode S transponder basic data fields. See B.2.35."""
        self.aircraftIdentification = 0
        """ Unique ICAO Mode S aircraft address, part of Mode S transponder basic data fields."""
        self.aircraftAddress = 0
        # /** Aircraft identification type, part of Mode S transponder basic data fields. uid 357 */
        self.aircraftIdentificationType = AircraftIdentificationType.default

        """ DAP source, part of Mode S transponder basic data fields. See B.2.6."""
        self.dapSource = 0
        """ Mode S altitude, part of Mode S transponder basic data fields. See B.2.36."""
        self.modeSAltitude = 0
        # /** Capability report, part of Mode S transponder basic data fields. uid 358 */
        self.capabilityReport = CapabilityReport.default

        """ Padding"""
        self.padding = 0
        """ Padding"""
        self.padding2 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "ModeSTransponderStatus : " + str(self.modeSTransponderStatus) + "\n"
        outputString += "ModeSLevelsPresent : " + str(self.modeSLevelsPresent) + "\n"
        outputString += "AircraftPresentDomain : " + self.aircraftPresentDomain.get_description + "(" + (str(int(self.aircraftPresentDomain))) + ")" + "\n"
        outputString += "AircraftIdentification : " + str(self.aircraftIdentification) + "\n"
        outputString += "AircraftAddress : " + str(self.aircraftAddress) + "\n"
        outputString += "AircraftIdentificationType : " + self.aircraftIdentificationType.get_description + "(" + (str(int(self.aircraftIdentificationType))) + ")" + "\n"
        outputString += "DapSource : " + str(self.dapSource) + "\n"
        outputString += "ModeSAltitude : " + str(self.modeSAltitude) + "\n"
        outputString += "CapabilityReport : " + self.capabilityReport.get_description + "(" + (str(int(self.capabilityReport))) + ")" + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
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
        outputStream.write_short(int(self.modeSTransponderStatus))
        outputStream.write_byte(int(self.modeSLevelsPresent))
        self.serialize_enum(self.aircraftPresentDomain,outputStream)
        outputStream.write_long(int(self.aircraftIdentification))
        outputStream.write_int(int(self.aircraftAddress))
        self.serialize_enum(self.aircraftIdentificationType,outputStream)
        outputStream.write_byte(int(self.dapSource))
        outputStream.write_short(int(self.modeSAltitude))
        self.serialize_enum(self.capabilityReport,outputStream)
        outputStream.write_byte(int(self.padding))
        outputStream.write_short(int(self.padding2))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.modeSTransponderStatus = inputStream.read_short()
        self.modeSLevelsPresent = inputStream.read_byte()
        self.aircraftPresentDomain = AircraftPresentDomain.get_enum(self.parse_enum(self.aircraftPresentDomain,inputStream))
        self.aircraftIdentification = inputStream.read_long()
        self.aircraftAddress = inputStream.read_int()
        self.aircraftIdentificationType = AircraftIdentificationType.get_enum(self.parse_enum(self.aircraftIdentificationType,inputStream))
        self.dapSource = inputStream.read_byte()
        self.modeSAltitude = inputStream.read_short()
        self.capabilityReport = CapabilityReport.get_enum(self.parse_enum(self.capabilityReport,inputStream))
        self.padding = inputStream.read_byte()
        self.padding2 = inputStream.read_short()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 11

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



