from enum import Enum

from .siso_ref_010.enums.designator_designator_code import DesignatorDesignatorCode
from .siso_ref_010.enums.designator_system_name import DesignatorSystemName
from .siso_ref_010.enums.dead_reckoning_algorithm import DeadReckoningAlgorithm
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .vector3float import Vector3Float
from .vector3double import Vector3Double
from .entity_id import EntityID
from .distributed_emissions_regeneration_family_pdu import DistributedEmissionsRegenerationFamilyPdu

class DesignatorPdu( DistributedEmissionsRegenerationFamilyPdu ):
    """7.6.3 Handles designating operations. See 5.3.7.2."""

    def __init__(self):
        """ Initializer for DesignatorPdu"""
        super().__init__()
        """ ID of the entity designating"""
        self.designatingEntityID = EntityID()
        # /** This field shall specify a unique emitter database number assigned to  differentiate between otherwise similar or identical emitter beams within an emitter system. uid 80 */
        self.codeName = DesignatorSystemName.default

        """ ID of the entity being designated"""
        self.designatedEntityID = EntityID()
        # /** This field shall identify the designator code being used by the designating entity  uid 81 */
        self.designatorCode = DesignatorDesignatorCode.default

        """ This field shall identify the designator output power in watts"""
        self.designatorPower = 0.0
        """ This field shall identify the designator wavelength in units of microns"""
        self.designatorWavelength = 0.0
        """ designtor spot wrt the designated entity"""
        self.designatorSpotWrtDesignated = Vector3Float()
        """ designtor spot wrt the designated entity"""
        self.designatorSpotLocation = Vector3Double()
        # /** Dead reckoning algorithm uid 44 */
        self.deadReckoningAlgorithm = DeadReckoningAlgorithm.default

        """ padding"""
        self.padding1 = 0
        """ padding"""
        self.padding2 = 0
        """ linear accelleration of entity"""
        self.entityLinearAcceleration = Vector3Float()
        self.pduType = DisPduType.designator

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "DesignatingEntityID :" + "\n" + self.designatingEntityID.to_string() + "\n"
        outputString += "DesignatorSystemName : " + self.codeName.get_description + "(" + (str(int(self.codeName))) + ")" + "\n"
        outputString += "DesignatedEntityID :" + "\n" + self.designatedEntityID.to_string() + "\n"
        outputString += "DesignatorDesignatorCode : " + self.designatorCode.get_description + "(" + (str(int(self.designatorCode))) + ")" + "\n"
        outputString += "DesignatorPower : " + str(self.designatorPower) + "\n"
        outputString += "DesignatorWavelength : " + str(self.designatorWavelength) + "\n"
        outputString += "DesignatorSpotWrtDesignated :" + "\n" + self.designatorSpotWrtDesignated.to_string() + "\n"
        outputString += "DesignatorSpotLocation :" + "\n" + self.designatorSpotLocation.to_string() + "\n"
        outputString += "DeadReckoningAlgorithm : " + self.deadReckoningAlgorithm.get_description + "(" + (str(int(self.deadReckoningAlgorithm))) + ")" + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "EntityLinearAcceleration :" + "\n" + self.entityLinearAcceleration.to_string() + "\n"
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
        super( DesignatorPdu, self ).serialize(outputStream)
        self.designatingEntityID.serialize(outputStream)
        self.serialize_enum(self.codeName,outputStream)
        self.designatedEntityID.serialize(outputStream)
        self.serialize_enum(self.designatorCode,outputStream)
        outputStream.write_float(int(self.designatorPower))
        outputStream.write_float(int(self.designatorWavelength))
        self.designatorSpotWrtDesignated.serialize(outputStream)
        self.designatorSpotLocation.serialize(outputStream)
        self.serialize_enum(self.deadReckoningAlgorithm,outputStream)
        outputStream.write_byte(int(self.padding1))
        outputStream.write_short(int(self.padding2))
        self.entityLinearAcceleration.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( DesignatorPdu, self).parse(inputStream)
        self.designatingEntityID.parse(inputStream)
        self.codeName = DesignatorSystemName.get_enum(self.parse_enum(self.codeName,inputStream))
        self.designatedEntityID.parse(inputStream)
        self.designatorCode = DesignatorDesignatorCode.get_enum(self.parse_enum(self.designatorCode,inputStream))
        self.designatorPower = inputStream.read_float()
        self.designatorWavelength = inputStream.read_float()
        self.designatorSpotWrtDesignated.parse(inputStream)
        self.designatorSpotLocation.parse(inputStream)
        self.deadReckoningAlgorithm = DeadReckoningAlgorithm.get_enum(self.parse_enum(self.deadReckoningAlgorithm,inputStream))
        self.padding1 = inputStream.read_byte()
        self.padding2 = inputStream.read_short()
        self.entityLinearAcceleration.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 12

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



