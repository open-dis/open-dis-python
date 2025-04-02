from enum import Enum

from .entity_type import EntityType
from .siso_ref_010.enums.explosive_material_categories import ExplosiveMaterialCategories

class ExplosionDescriptor( object ):
    """Explosion of a non-munition. Section 6.2.19.3"""

    def __init__(self):
        """ Initializer for ExplosionDescriptor"""
        """ Type of the object that exploded. See 6.2.30"""
        self.explodingObject = EntityType()
        # /** Material that exploded. Can be grain dust, tnt, gasoline, etc. Enumeration uid 310 */
        self.explosiveMaterial = ExplosiveMaterialCategories.default

        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ Force of explosion, in equivalent KG of TNT"""
        self.explosiveForce = 0.0

    def to_string(self) ->str:
        outputString = ""
        outputString += "ExplodingObject :" + "\n" + self.explodingObject.to_string() + "\n"
        outputString += "ExplosiveMaterialCategories : " + self.explosiveMaterial.get_description + "(" + (str(int(self.explosiveMaterial))) + ")" + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "ExplosiveForce : " + str(self.explosiveForce) + "\n"
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
        self.explodingObject.serialize(outputStream)
        self.serialize_enum(self.explosiveMaterial,outputStream)
        outputStream.write_short(int(self.padding))
        outputStream.write_float(int(self.explosiveForce))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.explodingObject.parse(inputStream)
        self.explosiveMaterial = ExplosiveMaterialCategories.get_enum(self.parse_enum(self.explosiveMaterial,inputStream))
        self.padding = inputStream.read_short()
        self.explosiveForce = inputStream.read_float()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 4

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



