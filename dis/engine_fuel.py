from enum import Enum

from .siso_ref_010.enums.fuel_measurement_units import FuelMeasurementUnits
from .siso_ref_010.enums.fuel_location import FuelLocation
from .siso_ref_010.enums.supply_fuel_type import SupplyFuelType

class EngineFuel( object ):
    """Information about an entity's engine fuel. Section 6.2.24."""

    def __init__(self):
        """ Initializer for EngineFuel"""
        """ Fuel quantity, units specified by next field"""
        self.fuelQuantity = 0
        # /** Units in which the fuel is measured uid 328 */
        self.fuelMeasurementUnits = FuelMeasurementUnits.default

        # /** Type of fuel uid 413 */
        self.fuelType = SupplyFuelType.default

        # /** Location of fuel as related to entity. See section 14 of EBV document uid 329 */
        self.fuelLocation = FuelLocation.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "FuelQuantity : " + str(self.fuelQuantity) + "\n"
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
        outputStream.write_int(int(self.fuelQuantity))
        self.serialize_enum(self.fuelMeasurementUnits,outputStream)
        self.serialize_enum(self.fuelType,outputStream)
        self.serialize_enum(self.fuelLocation,outputStream)
        outputStream.write_byte(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.fuelQuantity = inputStream.read_int()
        self.fuelMeasurementUnits = FuelMeasurementUnits.get_enum(self.parse_enum(self.fuelMeasurementUnits,inputStream))
        self.fuelType = SupplyFuelType.get_enum(self.parse_enum(self.fuelType,inputStream))
        self.fuelLocation = FuelLocation.get_enum(self.parse_enum(self.fuelLocation,inputStream))
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



