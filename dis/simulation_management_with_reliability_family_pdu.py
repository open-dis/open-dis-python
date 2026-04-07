from enum import Enum

from .simulation_identifier import SimulationIdentifier
from .pdu_base import PduBase
from .siso_ref_010.enums.disprotocol_family import DISProtocolFamily

class SimulationManagementWithReliabilityFamilyPdu( PduBase ):
    """Simulation Management with Reliability PDUs with reliability service levels in a DIS exercise are an alternative to the Simulation Management PDUs, and may or may not be required for participation in an DIS exercise,"""

    def __init__(self):
        """ Initializer for SimulationManagementWithReliabilityFamilyPdu"""
        super().__init__()
        """ IDs the simulation or entity, either a simulation or an entity. Either 6.2.80 or 6.2.28"""
        self.originatingID = SimulationIdentifier()
        """ simulation, all simulations, a special ID, or an entity. See 5.6.5 and 5.12.4"""
        self.receivingID = SimulationIdentifier()
        self.protocolFamily = DISProtocolFamily.simulation_management_with_reliability

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "OriginatingID :" + "\n" + self.originatingID.to_string() + "\n"
        outputString += "ReceivingID :" + "\n" + self.receivingID.to_string() + "\n"
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
        super( SimulationManagementWithReliabilityFamilyPdu, self ).serialize(outputStream)
        self.originatingID.serialize(outputStream)
        self.receivingID.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( SimulationManagementWithReliabilityFamilyPdu, self).parse(inputStream)
        self.originatingID.parse(inputStream)
        self.receivingID.parse(inputStream)

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



