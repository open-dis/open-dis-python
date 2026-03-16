from enum import Enum

from .layer_header import LayerHeader
from .mode_stransponder_basic_data import ModeSTransponderBasicData
from .iffdata_specification import IFFDataSpecification
from .abstract_iffpdu_layer_data import AbstractIFFPduLayerData

class IFFPduLayer4TransponderFormatData( AbstractIFFPduLayerData ):
    """7.6.5.5.3 Layer 4 Mode S transponder format"""

    def __init__(self):
        """ Initializer for IFFPduLayer4TransponderFormatData"""
        super().__init__()
        """ Layer header"""
        self.layerHeader = LayerHeader()
        """ 6.2.80 Site number, part of reporting simulation field"""
        self.siteNumber = 0
        """ 6.2.80 Application number, part of reporting simulation field"""
        self.applicationNumber = 0
        """ Mode S transponder basic data"""
        self.modeSTransponderBasicData = ModeSTransponderBasicData()
        """ Padding"""
        self.padding = 0
        self.numberOfIFFFundamentalParameterDataRecordsParameters = 0
        """ Variable length list of fundamental parameters."""
        self._IFFFundamentalParameterDataRecord = []


    def get_numberOfIFFFundamentalParameterDataRecordsParameters(self):
        return len(self._IFFFundamentalParameterDataRecord)
    def set_numberOfIFFFundamentalParameterDataRecordsParameters(self, value):
        numberOfIFFFundamentalParameterDataRecordsParameters = value


    def get_IFFFundamentalParameterDataRecord(self):
        return self._IFFFundamentalParameterDataRecord
    def set_IFFFundamentalParameterDataRecord(self, value):
        self._IFFFundamentalParameterDataRecord = value
    IFFFundamentalParameterDataRecord = property(get_IFFFundamentalParameterDataRecord, set_IFFFundamentalParameterDataRecord)


    def add_IFFFundamentalParameterDataRecord(self, value : IFFDataSpecification):
        self._IFFFundamentalParameterDataRecord.append(value)


    """
    ///            Name : IFFFundamentalParameterDataRecord
    ///             UID : 
    ///            Type : IFFDataSpecification
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Variable length list of fundamental parameters.
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
        outputString += "LayerHeader :" + "\n" + self.layerHeader.to_string() + "\n"
        outputString += "SiteNumber : " + str(self.siteNumber) + "\n"
        outputString += "ApplicationNumber : " + str(self.applicationNumber) + "\n"
        outputString += "ModeSTransponderBasicData :" + "\n" + self.modeSTransponderBasicData.to_string() + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "NumberOfIFFFundamentalParameterDataRecordsParameters : " + str(len(self._IFFFundamentalParameterDataRecord)) + "\n"
        outputString += "IFFFundamentalParameterDataRecord : " + "\n"
        for idx in range(0, len(self._IFFFundamentalParameterDataRecord)):
            outputString += self._IFFFundamentalParameterDataRecord[idx].to_string()

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
        super( IFFPduLayer4TransponderFormatData, self ).serialize(outputStream)
        self.layerHeader.serialize(outputStream)
        outputStream.write_short(int(self.siteNumber))
        outputStream.write_short(int(self.applicationNumber))
        self.modeSTransponderBasicData.serialize(outputStream)
        outputStream.write_short(int(self.padding))
        outputStream.write_short( len(self._IFFFundamentalParameterDataRecord))
        for anObj in self._IFFFundamentalParameterDataRecord:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( IFFPduLayer4TransponderFormatData, self).parse(inputStream)
        self.layerHeader.parse(inputStream)
        self.siteNumber = inputStream.read_short()
        self.applicationNumber = inputStream.read_short()
        self.modeSTransponderBasicData.parse(inputStream)
        self.padding = inputStream.read_short()
        self.numberOfIFFFundamentalParameterDataRecordsParameters = inputStream.read_short()
        for idx in range(0, self.numberOfIFFFundamentalParameterDataRecordsParameters):
            element = IFFDataSpecification()
            element.parse(inputStream)
            self._IFFFundamentalParameterDataRecord.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 7

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



