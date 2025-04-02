from enum import Enum

from .siso_ref_010.enums.fuel_measurement_units import FuelMeasurementUnits
from .siso_ref_010.enums.fuel_location import FuelLocation
from .siso_ref_010.enums.supply_fuel_type import SupplyFuelType

class StorageFuelReload( object ):
    """For each type or location of Storage Fuel, this record shall specify the type, location, fuel measure- ment units, reload quantity and maximum quantity for storage fuel either for the whole entity or a specific storage fuel location (tank). Section 6.2.85."""

    def __init__(self):
        """ Initializer for StorageFuelReload"""
        """  the standard quantity of this fuel type normally loaded at this station/launcher if a station/launcher is specified. If the Station/Launcher field is set to zero, then this is the total quantity of this fuel type that would be present in a standard reload of all appli- cable stations/launchers associated with this entity."""
        self.standardQuantity = 0
        """ The maximum quantity of this fuel type that this sta- tion/launcher is capable of holding when a station/launcher is specified. This would be the value used when a maximum reload was desired to be set for this station/launcher. If the Station/launcher field is set to zero, then this is the maximum quantity of this fuel type that would be present on this entity at all stations/launchers that can accept this fuel type."""
        self.maximumQuantity = 0
        """ The seconds normally required to reload the standard quantity of this fuel type at this specific station/launcher. When the Station/Launcher field is set to zero, this shall be the time it takes to perform a standard quantity reload of this fuel type at all applicable stations/launchers for this entity."""
        self.standardQuantityReloadTime = 0
        """ The seconds normally required to reload the maximum possible quantity of this fuel type at this station/launcher. When the Station/Launcher field is set to zero, this shall be the time it takes to perform a maximum quantity load/reload of this fuel type at all applicable stations/launchers for this entity."""
        self.maximumQuantityReloadTime = 0
        # /** The fuel measurement units. Enumeration uid 328 */
        self.fuelMeasurementUnits = FuelMeasurementUnits.default

        # /** Fuel type uid 413 */
        self.fuelType = SupplyFuelType.default

        # /** Location of fuel as related to entity. See section 14 of EBV document uid 329 */
        self.fuelLocation = FuelLocation.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "StandardQuantity : " + str(self.standardQuantity) + "\n"
        outputString += "MaximumQuantity : " + str(self.maximumQuantity) + "\n"
        outputString += "StandardQuantityReloadTime : " + str(self.standardQuantityReloadTime) + "\n"
        outputString += "MaximumQuantityReloadTime : " + str(self.maximumQuantityReloadTime) + "\n"
        outputString += "FuelMeasurementUnits : " + self.fuelMeasurementUnits.get_description + "(" + (str(int(self.fuelMeasurementUnits))) + ")" + "\n"
        outputString += "SupplyFuelType : " + self.fuelType.get_description + "(" + (str(int(self.fuelType))) + ")" + "\n"
        outputString += "FuelLocation : " + self.fuelLocation.get_description + "(" + (str(int(self.fuelLocation))) + ")" + "\n"
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
        outputStream.write_int(int(self.standardQuantity))
        outputStream.write_int(int(self.maximumQuantity))
        outputStream.write_int(int(self.standardQuantityReloadTime))
        outputStream.write_int(int(self.maximumQuantityReloadTime))
        self.serialize_enum(self.fuelMeasurementUnits,outputStream)
        self.serialize_enum(self.fuelType,outputStream)
        self.serialize_enum(self.fuelLocation,outputStream)
        outputStream.write_byte(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.standardQuantity = inputStream.read_int()
        self.maximumQuantity = inputStream.read_int()
        self.standardQuantityReloadTime = inputStream.read_int()
        self.maximumQuantityReloadTime = inputStream.read_int()
        self.fuelMeasurementUnits = FuelMeasurementUnits.get_enum(self.parse_enum(self.fuelMeasurementUnits,inputStream))
        self.fuelType = SupplyFuelType.get_enum(self.parse_enum(self.fuelType,inputStream))
        self.fuelLocation = FuelLocation.get_enum(self.parse_enum(self.fuelLocation,inputStream))
        self.padding = inputStream.read_byte()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 8

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



