from enum import Enum

from .siso_ref_010.enums.fuel_measurement_units import FuelMeasurementUnits
from .siso_ref_010.enums.fuel_location import FuelLocation
from .siso_ref_010.enums.supply_fuel_type import SupplyFuelType

class EngineFuelReload( object ):
    """For each type or location of engine fuell, this record specifies the type, location, fuel measurement units, and reload quantity and maximum quantity. Section 6.2.25."""

    def __init__(self):
        """ Initializer for EngineFuelReload"""
        """ standard quantity of fuel loaded"""
        self.standardQuantity = 0
        """ maximum quantity of fuel loaded"""
        self.maximumQuantity = 0
        """ seconds normally required to to reload standard qty"""
        self.standardQuantityReloadTime = 0
        """ seconds normally required to to reload maximum qty"""
        self.maximumQuantityReloadTime = 0
        # /** Units of measure uid 328 */
        self.fuelMeasurmentUnits = FuelMeasurementUnits.default

        # /**  uid 413 */
        self.fuelType = SupplyFuelType.default

        # /** fuel  location as related to the entity uid 329 */
        self.fuelLocation = FuelLocation.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "StandardQuantity : " + str(self.standardQuantity) + "\n"
        outputString += "MaximumQuantity : " + str(self.maximumQuantity) + "\n"
        outputString += "StandardQuantityReloadTime : " + str(self.standardQuantityReloadTime) + "\n"
        outputString += "MaximumQuantityReloadTime : " + str(self.maximumQuantityReloadTime) + "\n"
        outputString += "FuelMeasurementUnits : " + self.fuelMeasurmentUnits.get_description + "(" + (str(int(self.fuelMeasurmentUnits))) + ")" + "\n"
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
        self.serialize_enum(self.fuelMeasurmentUnits,outputStream)
        self.serialize_enum(self.fuelType,outputStream)
        self.serialize_enum(self.fuelLocation,outputStream)
        outputStream.write_byte(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.standardQuantity = inputStream.read_int()
        self.maximumQuantity = inputStream.read_int()
        self.standardQuantityReloadTime = inputStream.read_int()
        self.maximumQuantityReloadTime = inputStream.read_int()
        self.fuelMeasurmentUnits = FuelMeasurementUnits.get_enum(self.parse_enum(self.fuelMeasurmentUnits,inputStream))
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



