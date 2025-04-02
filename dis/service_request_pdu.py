from enum import Enum

from .supply_quantity import SupplyQuantity
from .logistics_family_pdu import LogisticsFamilyPdu
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_id import EntityID
from .siso_ref_010.enums.service_request_service_type_requested import ServiceRequestServiceTypeRequested

class ServiceRequestPdu( LogisticsFamilyPdu ):
    """5.5.5 Communicate information associated with one entity requesting a service from another."""

    def __init__(self):
        """ Initializer for ServiceRequestPdu"""
        super().__init__()
        """ Entity that is requesting service (see 6.2.28), Section 7.4.2"""
        self.requestingEntityID = EntityID()
        """ Entity that is providing the service (see 6.2.28), Section 7.4.2"""
        self.servicingEntityID = EntityID()
        # /** Type of service requested, Section 7.4.2 uid 63 */
        self.serviceTypeRequested = ServiceRequestServiceTypeRequested.default

        """ How many requested, Section 7.4.2"""
        self.numberOfSupplyTypes = 0
        self.padding1 = 0
        self._supplies = []
        self.pduType = DisPduType.service_request


    def get_numberOfSupplyTypes(self):
        return len(self._supplies)
    def set_numberOfSupplyTypes(self, value):
        numberOfSupplyTypes = value


    def get_supplies(self):
        return self._supplies
    def set_supplies(self, value):
        self._supplies = value
    supplies = property(get_supplies, set_supplies)


    def add_supplies(self, value : SupplyQuantity):
        self._supplies.append(value)


    """
    ///            Name : supplies
    ///             UID : 
    ///            Type : SupplyQuantity
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
        outputString += "RequestingEntityID :" + "\n" + self.requestingEntityID.to_string() + "\n"
        outputString += "ServicingEntityID :" + "\n" + self.servicingEntityID.to_string() + "\n"
        outputString += "ServiceRequestServiceTypeRequested : " + self.serviceTypeRequested.get_description + "(" + (str(int(self.serviceTypeRequested))) + ")" + "\n"
        outputString += "NumberOfSupplyTypes : " + str(len(self._supplies)) + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Supplies : " + "\n"
        for idx in range(0, len(self._supplies)):
            outputString += self._supplies[idx].to_string()

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
        super( ServiceRequestPdu, self ).serialize(outputStream)
        self.requestingEntityID.serialize(outputStream)
        self.servicingEntityID.serialize(outputStream)
        self.serialize_enum(self.serviceTypeRequested,outputStream)
        outputStream.write_byte( len(self._supplies))
        outputStream.write_short(int(self.padding1))
        for anObj in self._supplies:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( ServiceRequestPdu, self).parse(inputStream)
        self.requestingEntityID.parse(inputStream)
        self.servicingEntityID.parse(inputStream)
        self.serviceTypeRequested = ServiceRequestServiceTypeRequested.get_enum(self.parse_enum(self.serviceTypeRequested,inputStream))
        self.numberOfSupplyTypes = inputStream.read_byte()
        self.padding1 = inputStream.read_short()
        for idx in range(0, self.numberOfSupplyTypes):
            element = SupplyQuantity()
            element.parse(inputStream)
            self._supplies.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 6

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



