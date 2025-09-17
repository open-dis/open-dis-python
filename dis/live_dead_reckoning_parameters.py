from enum import Enum

from .siso_ref_010.enums.dead_reckoning_algorithm import DeadReckoningAlgorithm
from .levector3fixed_byte import LEVector3FixedByte

class LiveDeadReckoningParameters( object ):
    """16-bit fixed binaries"""

    def __init__(self):
        """ Initializer for LiveDeadReckoningParameters"""
        # /**  uid 44 */
        self.deadReckoningAlgorithm = DeadReckoningAlgorithm.default

        # entityLinearAcceleration is an undescribed parameter... 
        self.entityLinearAcceleration = LEVector3FixedByte()
        # entityAngularVelocity is an undescribed parameter... 
        self.entityAngularVelocity = LEVector3FixedByte()

    def to_string(self) ->str:
        outputString = ""
        outputString += "DeadReckoningAlgorithm : " + self.deadReckoningAlgorithm.get_description + "(" + (str(int(self.deadReckoningAlgorithm))) + ")" + "\n"
        outputString += "EntityLinearAcceleration :" + "\n" + self.entityLinearAcceleration.to_string() + "\n"
        outputString += "EntityAngularVelocity :" + "\n" + self.entityAngularVelocity.to_string() + "\n"
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
        self.serialize_enum(self.deadReckoningAlgorithm,outputStream)
        self.entityLinearAcceleration.serialize(outputStream)
        self.entityAngularVelocity.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.deadReckoningAlgorithm = DeadReckoningAlgorithm.get_enum(self.parse_enum(self.deadReckoningAlgorithm,inputStream))
        self.entityLinearAcceleration.parse(inputStream)
        self.entityAngularVelocity.parse(inputStream)

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



