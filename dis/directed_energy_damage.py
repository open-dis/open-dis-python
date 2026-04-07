from enum import Enum

from .siso_ref_010.enums.dedamage_description_component_damage_status import DEDamageDescriptionComponentDamageStatus
from .siso_ref_010.enums.dedamage_description_component_visual_smoke_color import DEDamageDescriptionComponentVisualSmokeColor
from .vector3float import Vector3Float
from .siso_ref_010.enums.dedamage_description_component_visual_damage_status import DEDamageDescriptionComponentVisualDamageStatus
from .event_identifier import EventIdentifier
from .siso_ref_010.enums.entity_damage_status_component_identification import EntityDamageStatusComponentIdentification

class DirectedEnergyDamage( object ):
    """Damage sustained by an entity due to directed energy. Location of the damage based on a relative x,y,z location from the center of the entity. Section 6.2.15.2"""

    def __init__(self):
        """ Initializer for DirectedEnergyDamage"""
        """ DE Record Type."""
        self.recordType = 4500
        """ DE Record Length (bytes)"""
        self.recordLength = 40
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ location of damage, relative to center of entity"""
        self.damageLocation = Vector3Float()
        """ Size of damaged area, in meters"""
        self.damageDiameter = 0.0
        """ average temp of the damaged area, in degrees celsius. If firing entitty does not model this, use a value of -273.15"""
        self.temperature = -273.15
        # /** enumeration uid 314 */
        self.componentIdentification = EntityDamageStatusComponentIdentification.default

        # /** enumeration uid 315 */
        self.componentDamageStatus = DEDamageDescriptionComponentDamageStatus.default

        # enumeration uid 317
        self.componentVisualDamageStatus = DEDamageDescriptionComponentVisualDamageStatus()

        # /** enumeration uid 316 */
        self.componentVisualSmokeColor = DEDamageDescriptionComponentVisualSmokeColor.default

        """ For any component damage resulting this field shall be set to the fire event ID from that PDU."""
        self.fireEventID = EventIdentifier()
        """ padding"""
        self.padding2 = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "RecordType : " + str(self.recordType) + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "DamageLocation :" + "\n" + self.damageLocation.to_string() + "\n"
        outputString += "DamageDiameter : " + str(self.damageDiameter) + "\n"
        outputString += "Temperature : " + str(self.temperature) + "\n"
        outputString += "EntityDamageStatusComponentIdentification : " + self.componentIdentification.get_description + "(" + (str(int(self.componentIdentification))) + ")" + "\n"
        outputString += "DEDamageDescriptionComponentDamageStatus : " + self.componentDamageStatus.get_description + "(" + (str(int(self.componentDamageStatus))) + ")" + "\n"
        outputString += "DEDamageDescriptionComponentVisualDamageStatus : " + str(self.componentVisualDamageStatus) + "\n"
        outputString += "DEDamageDescriptionComponentVisualSmokeColor : " + self.componentVisualSmokeColor.get_description + "(" + (str(int(self.componentVisualSmokeColor))) + ")" + "\n"
        outputString += "FireEventID :" + "\n" + self.fireEventID.to_string() + "\n"
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
        outputStream.write_int(int(self.recordType))
        outputStream.write_short(int(self.recordLength))
        outputStream.write_short(int(self.padding))
        self.damageLocation.serialize(outputStream)
        outputStream.write_float(int(self.damageDiameter))
        outputStream.write_float(int(self.temperature))
        self.serialize_enum(self.componentIdentification,outputStream)
        self.serialize_enum(self.componentDamageStatus,outputStream)
        outputStream.write_unsigned_int(int(self.componentVisualDamageStatus.asbyte))
        self.serialize_enum(self.componentVisualSmokeColor,outputStream)
        self.fireEventID.serialize(outputStream)
        outputStream.write_short(int(self.padding2))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = inputStream.read_int()
        self.recordLength = inputStream.read_short()
        self.padding = inputStream.read_short()
        self.damageLocation.parse(inputStream)
        self.damageDiameter = inputStream.read_float()
        self.temperature = inputStream.read_float()
        self.componentIdentification = EntityDamageStatusComponentIdentification.get_enum(self.parse_enum(self.componentIdentification,inputStream))
        self.componentDamageStatus = DEDamageDescriptionComponentDamageStatus.get_enum(self.parse_enum(self.componentDamageStatus,inputStream))
        self.componentVisualDamageStatus.asbyte = inputStream.read_unsigned_int()
        self.componentVisualSmokeColor = DEDamageDescriptionComponentVisualSmokeColor.get_enum(self.parse_enum(self.componentVisualSmokeColor,inputStream))
        self.fireEventID.parse(inputStream)
        self.padding2 = inputStream.read_short()

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



