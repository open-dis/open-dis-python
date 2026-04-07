from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_information_interaction_family_pdu import EntityInformationInteractionFamilyPdu
from .siso_ref_010.enums.variable_record_type import VariableRecordType
from .siso_ref_010.enums.disattribute_action_code import DISAttributeActionCode
from .attribute_record_set import AttributeRecordSet
from .simulation_address import SimulationAddress
from .siso_ref_010.enums.disprotocol_family import DISProtocolFamily

class AttributePdu( EntityInformationInteractionFamilyPdu ):
    """7.2.6. Information about individual attributes for a particular entity, other object, or event may be communicated using an Attribute PDU. The Attribute PDU shall not be used to exchange data available in any other PDU except where explicitly mentioned in the PDU issuance instructions within this standard. See 5.3.6."""

    def __init__(self):
        """ Initializer for AttributePdu"""
        super().__init__()
        """ This field shall identify the simulation issuing the Attribute PDU. It shall be represented by a Simulation Address record (see 6.2.79)."""
        self.originatingSimulationAddress = SimulationAddress()
        """ Padding"""
        self.padding1 = 0
        """ Padding"""
        self.padding2 = 0
        # /** This field shall represent the type of the PDU that is being extended or updated, if applicable. It shall be represented by an 8-bit enumeration. uid 4 */
        self.attributeRecordPduType = DisPduType.default

        # /** This field shall indicate the Protocol Version associated with the Attribute Record PDU Type. It shall be represented by an 8-bit enumeration. uid 5 */
        self.attributeRecordProtocolVersion = DISProtocolFamily.default

        # /** This field shall contain the Attribute record type of the Attribute records in the PDU if they all have the same Attribute record type. It shall be represented by a 32-bit enumeration. uid 66 Variable Record Type values are defined by VariableRecordType enumerations */
        self.masterAttributeRecordType = VariableRecordType.default

        # /** This field shall identify the action code applicable to this Attribute PDU. The Action Code shall apply to all Attribute records contained in the PDU. It shall be represented by an 8-bit enumeration. uid 295 */
        self.actionCode = DISAttributeActionCode.default

        """ Padding"""
        self.padding3 = 0
        """ This field shall specify the number of Attribute Record Sets that make up the remainder of the PDU. It shall be represented by a 16-bit unsigned integer."""
        self.numberAttributeRecordSet = 0
        self._attributeRecordSets = []
        self.pduType = DisPduType.attribute


    def get_numberAttributeRecordSet(self):
        return len(self._attributeRecordSets)
    def set_numberAttributeRecordSet(self, value):
        numberAttributeRecordSet = value


    def get_attributeRecordSets(self):
        return self._attributeRecordSets
    def set_attributeRecordSets(self, value):
        self._attributeRecordSets = value
    attributeRecordSets = property(get_attributeRecordSets, set_attributeRecordSets)


    def add_attributeRecordSets(self, value : AttributeRecordSet):
        self._attributeRecordSets.append(value)


    """
    ///            Name : attributeRecordSets
    ///             UID : 
    ///            Type : AttributeRecordSet
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : null
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
        outputString += "OriginatingSimulationAddress :" + "\n" + self.originatingSimulationAddress.to_string() + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Padding2 : " + str(self.padding2) + "\n"
        outputString += "DisPduType : " + self.attributeRecordPduType.get_description + "(" + (str(int(self.attributeRecordPduType))) + ")" + "\n"
        outputString += "DISProtocolFamily : " + self.attributeRecordProtocolVersion.get_description + "(" + (str(int(self.attributeRecordProtocolVersion))) + ")" + "\n"
        outputString += "VariableRecordType : " + self.masterAttributeRecordType.get_description + "(" + (str(int(self.masterAttributeRecordType))) + ")" + "\n"
        outputString += "DISAttributeActionCode : " + self.actionCode.get_description + "(" + (str(int(self.actionCode))) + ")" + "\n"
        outputString += "Padding3 : " + str(self.padding3) + "\n"
        outputString += "NumberAttributeRecordSet : " + str(len(self._attributeRecordSets)) + "\n"
        outputString += "AttributeRecordSets : " + "\n"
        for idx in range(0, len(self._attributeRecordSets)):
            outputString += self._attributeRecordSets[idx].to_string()

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
        super( AttributePdu, self ).serialize(outputStream)
        self.originatingSimulationAddress.serialize(outputStream)
        outputStream.write_int(int(self.padding1))
        outputStream.write_short(int(self.padding2))
        self.serialize_enum(self.attributeRecordPduType,outputStream)
        self.serialize_enum(self.attributeRecordProtocolVersion,outputStream)
        self.serialize_enum(self.masterAttributeRecordType,outputStream)
        self.serialize_enum(self.actionCode,outputStream)
        outputStream.write_byte(int(self.padding3))
        outputStream.write_short( len(self._attributeRecordSets))
        for anObj in self._attributeRecordSets:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( AttributePdu, self).parse(inputStream)
        self.originatingSimulationAddress.parse(inputStream)
        self.padding1 = inputStream.read_int()
        self.padding2 = inputStream.read_short()
        self.attributeRecordPduType = DisPduType.get_enum(self.parse_enum(self.attributeRecordPduType,inputStream))
        self.attributeRecordProtocolVersion = DISProtocolFamily.get_enum(self.parse_enum(self.attributeRecordProtocolVersion,inputStream))
        self.masterAttributeRecordType = VariableRecordType.get_enum(self.parse_enum(self.masterAttributeRecordType,inputStream))
        self.actionCode = DISAttributeActionCode.get_enum(self.parse_enum(self.actionCode,inputStream))
        self.padding3 = inputStream.read_byte()
        self.numberAttributeRecordSet = inputStream.read_short()
        for idx in range(0, self.numberAttributeRecordSet):
            element = AttributeRecordSet()
            element.parse(inputStream)
            self._attributeRecordSets.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 10

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



