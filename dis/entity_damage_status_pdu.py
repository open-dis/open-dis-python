from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .warfare_family_pdu import WarfareFamilyPdu
from .entity_id import EntityID
from .directed_energy_damage import DirectedEnergyDamage

class EntityDamageStatusPdu( WarfareFamilyPdu ):
    """7.3.5 Used to communicate detailed damage information sustained by an entity regardless of the source of the damage."""

    def __init__(self):
        """ Initializer for EntityDamageStatusPdu"""
        super().__init__()
        """ Field shall identify the damaged entity (see 6.2.28), Section 7.3.4"""
        self.damagedEntityID = EntityID()
        self.padding1 = 0
        self.padding2 = 0
        """ field shall specify the number of Damage Description records, Section 7.3.5"""
        self.numberOfDamageDescription = 0
        """ Fields shall contain one or more Damage Description records (see 6.2.17) and may contain other Standard Variable records, Section 7.3.5"""
        self._damageDescriptionRecords = []
        self.pduType = DisPduType.entity_damage_status


    def get_numberOfDamageDescription(self):
        return len(self._damageDescriptionRecords)
    def set_numberOfDamageDescription(self, value):
        numberOfDamageDescription = value


    def get_damageDescriptionRecords(self):
        return self._damageDescriptionRecords
    def set_damageDescriptionRecords(self, value):
        self._damageDescriptionRecords = value
    damageDescriptionRecords = property(get_damageDescriptionRecords, set_damageDescriptionRecords)


    def add_damageDescriptionRecords(self, value : DirectedEnergyDamage):
        self._damageDescriptionRecords.append(value)


    """
    ///            Name : damageDescriptionRecords
    ///             UID : 
    ///            Type : DirectedEnergyDamage
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Fields shall contain one or more Damage Description records (see 6.2.17) and may contain other Standard Variable records, Section 7.3.5
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """



    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "DamagedEntityID :" + "\n" + self.damagedEntityID.to_string() + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "NumberOfDamageDescription : " + str(len(self._damageDescriptionRecords)) + "\n"
        outputString += "DamageDescriptionRecords : " + "\n"
        for idx in range(0, len(self._damageDescriptionRecords)):
            outputString += self._damageDescriptionRecords[idx].to_string()

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
        super( EntityDamageStatusPdu, self ).serialize(outputStream)
        self.damagedEntityID.serialize(outputStream)
        outputStream.write_short(int(self.padding1))
        outputStream.write_short(int(self.padding2))
        outputStream.write_short( len(self._damageDescriptionRecords))
        for anObj in self._damageDescriptionRecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( EntityDamageStatusPdu, self).parse(inputStream)
        self.damagedEntityID.parse(inputStream)
        self.padding1 = inputStream.read_short()
        self.padding2 = inputStream.read_short()
        self.numberOfDamageDescription = inputStream.read_short()
        for idx in range(0, self.numberOfDamageDescription):
            element = DirectedEnergyDamage()
            element.parse(inputStream)
            self._damageDescriptionRecords.append(element)


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



