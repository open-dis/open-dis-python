from enum import Enum

from .beam_antenna_pattern import BeamAntennaPattern
from .directed_energy_target_energy_deposition import DirectedEnergyTargetEnergyDeposition

class DirectedEnergyAreaAimpoint( object ):
    """DE Precision Aimpoint Record. Section 6.2.20.2"""

    def __init__(self):
        """ Initializer for DirectedEnergyAreaAimpoint"""
        """ Type of Record enumeration"""
        self.recordType = 4001
        """ Length of Record"""
        self.recordLength = 0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        """ Number of beam antenna pattern records"""
        self.beamAntennaPatternRecordCount = 0
        """ Number of DE target energy depositon records"""
        self.directedEnergyTargetEnergyDepositionRecordCount = 0
        """ list of beam antenna records. See 6.2.9.2"""
        self._beamAntennaParameterList = []
        """ list of DE target deposition records. See 6.2.21.4"""
        self._directedEnergyTargetEnergyDepositionRecordList = []
        self.padding2 = [0] * 64


    def get_beamAntennaPatternRecordCount(self):
        return len(self._beamAntennaParameterList)
    def set_beamAntennaPatternRecordCount(self, value):
        beamAntennaPatternRecordCount = value


    def get_directedEnergyTargetEnergyDepositionRecordCount(self):
        return len(self._directedEnergyTargetEnergyDepositionRecordList)
    def set_directedEnergyTargetEnergyDepositionRecordCount(self, value):
        directedEnergyTargetEnergyDepositionRecordCount = value


    def get_beamAntennaParameterList(self):
        return self._beamAntennaParameterList
    def set_beamAntennaParameterList(self, value):
        self._beamAntennaParameterList = value
    beamAntennaParameterList = property(get_beamAntennaParameterList, set_beamAntennaParameterList)


    def add_beamAntennaParameterList(self, value : BeamAntennaPattern):
        self._beamAntennaParameterList.append(value)


    """
    ///            Name : beamAntennaParameterList
    ///             UID : 
    ///            Type : BeamAntennaPattern
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : list of beam antenna records. See 6.2.9.2
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_directedEnergyTargetEnergyDepositionRecordList(self):
        return self._directedEnergyTargetEnergyDepositionRecordList
    def set_directedEnergyTargetEnergyDepositionRecordList(self, value):
        self._directedEnergyTargetEnergyDepositionRecordList = value
    directedEnergyTargetEnergyDepositionRecordList = property(get_directedEnergyTargetEnergyDepositionRecordList, set_directedEnergyTargetEnergyDepositionRecordList)


    def add_directedEnergyTargetEnergyDepositionRecordList(self, value : DirectedEnergyTargetEnergyDeposition):
        self._directedEnergyTargetEnergyDepositionRecordList.append(value)


    """
    ///            Name : directedEnergyTargetEnergyDepositionRecordList
    ///             UID : 
    ///            Type : DirectedEnergyTargetEnergyDeposition
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : list of DE target deposition records. See 6.2.21.4
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
        outputString += "RecordType : " + str(self.recordType) + "\n"
        outputString += "RecordLength : " + str(self.recordLength) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "BeamAntennaPatternRecordCount : " + str(len(self._beamAntennaParameterList)) + "\n"
        outputString += "DirectedEnergyTargetEnergyDepositionRecordCount : " + str(len(self._directedEnergyTargetEnergyDepositionRecordList)) + "\n"
        outputString += "BeamAntennaParameterList : " + "\n"
        for idx in range(0, len(self._beamAntennaParameterList)):
            outputString += self._beamAntennaParameterList[idx].to_string()

        outputString += "DirectedEnergyTargetEnergyDepositionRecordList : " + "\n"
        for idx in range(0, len(self._directedEnergyTargetEnergyDepositionRecordList)):
            outputString += self._directedEnergyTargetEnergyDepositionRecordList[idx].to_string()

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
        outputStream.write_short( len(self._beamAntennaParameterList))
        outputStream.write_short( len(self._directedEnergyTargetEnergyDepositionRecordList))
        for anObj in self._beamAntennaParameterList:
            anObj.serialize(outputStream)

        for anObj in self._directedEnergyTargetEnergyDepositionRecordList:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = inputStream.read_int()
        self.recordLength = inputStream.read_short()
        self.padding = inputStream.read_short()
        self.beamAntennaPatternRecordCount = inputStream.read_short()
        self.directedEnergyTargetEnergyDepositionRecordCount = inputStream.read_short()
        for idx in range(0, self.beamAntennaPatternRecordCount):
            element = BeamAntennaPattern()
            element.parse(inputStream)
            self._beamAntennaParameterList.append(element)

        for idx in range(0, self.directedEnergyTargetEnergyDepositionRecordCount):
            element = DirectedEnergyTargetEnergyDeposition()
            element.parse(inputStream)
            self._directedEnergyTargetEnergyDepositionRecordList.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 8

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



