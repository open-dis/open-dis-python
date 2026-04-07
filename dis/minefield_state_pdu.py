from enum import Enum

from .siso_ref_010.enums.force_id import ForceID
from .entity_type import EntityType
from .euler_angles import EulerAngles
from .protocol_mode import ProtocolMode
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .minefield_family_pdu import MinefieldFamilyPdu
from .vector3double import Vector3Double
from .siso_ref_010.enums.minefield_state_appearance_bit_map import MinefieldStateAppearanceBitMap
from .minefield_identifier import MinefieldIdentifier
from .vector2float import Vector2Float

class MinefieldStatePdu( MinefieldFamilyPdu ):
    """5.10.2 Communicate information about the minefield, including the location, perimeter, and types of mines contained within it."""

    def __init__(self):
        """ Initializer for MinefieldStatePdu"""
        super().__init__()
        """ Minefield ID provides a unique identifier"""
        self.minefieldID = MinefieldIdentifier()
        """ Minefield sequence number shall specify a change in state of a minefield as a result of a change in minefield information or a change in the state, in accordance with the rules specified in 5.10.2.3, of any of the mines contained therein"""
        self.minefieldSequence = 0
        # /** force ID provides a unique identifier uid 6 */
        self.forceID = ForceID.default

        """ Number of permieter points"""
        self.numberOfPerimeterPoints = 0
        """ type of minefield"""
        self.minefieldType = EntityType()
        """ the number of different mine types employed in the minefield"""
        self.numberOfMineTypes = 0
        """ location of center of minefield in world coordinates"""
        self.minefieldLocation = Vector3Double()
        """ orientation of minefield"""
        self.minefieldOrientation = EulerAngles()
        # appearance bitflags information needed for displaying the symbology of the minefield as a doctrinal minefield graphic uid 190
        self.appearance = MinefieldStateAppearanceBitMap()

        """ protocolMode. First two bits are the protocol mode, 14 bits reserved."""
        self.protocolMode = ProtocolMode()
        """ location of each perimeter point, relative to the Minefield Location field. Only the x and y coordinates of each perimeter point shall be specified."""
        self._perimeterPoints = []
        """ type of each mine contained within the minefield"""
        self._mineType = []
        self.pduType = DisPduType.minefield_state


    def get_numberOfPerimeterPoints(self):
        return len(self._perimeterPoints)
    def set_numberOfPerimeterPoints(self, value):
        numberOfPerimeterPoints = value


    def get_numberOfMineTypes(self):
        return len(self._mineType)
    def set_numberOfMineTypes(self, value):
        numberOfMineTypes = value


    def get_perimeterPoints(self):
        return self._perimeterPoints
    def set_perimeterPoints(self, value):
        self._perimeterPoints = value
    perimeterPoints = property(get_perimeterPoints, set_perimeterPoints)


    def add_perimeterPoints(self, value : Vector2Float):
        self._perimeterPoints.append(value)


    """
    ///            Name : perimeterPoints
    ///             UID : 
    ///            Type : Vector2Float
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : location of each perimeter point, relative to the Minefield Location field. Only the x and y coordinates of each perimeter point shall be specified.
    ///   default value : null
    ///     is Bitfield : false
    ///     List Length : 0
    ///     Prim Length : false
    ///      Dyn Length : false
    /// Underlying Kind : CLASSREF
    /// underlying Type : N/A
    """




    def get_mineType(self):
        return self._mineType
    def set_mineType(self, value):
        self._mineType = value
    mineType = property(get_mineType, set_mineType)


    def add_mineType(self, value : EntityType):
        self._mineType.append(value)


    """
    ///            Name : mineType
    ///             UID : 
    ///            Type : EntityType
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : type of each mine contained within the minefield
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
        outputString += "MinefieldID :" + "\n" + self.minefieldID.to_string() + "\n"
        outputString += "MinefieldSequence : " + str(self.minefieldSequence) + "\n"
        outputString += "ForceID : " + self.forceID.get_description + "(" + (str(int(self.forceID))) + ")" + "\n"
        outputString += "NumberOfPerimeterPoints : " + str(len(self._perimeterPoints)) + "\n"
        outputString += "MinefieldType :" + "\n" + self.minefieldType.to_string() + "\n"
        outputString += "NumberOfMineTypes : " + str(len(self._mineType)) + "\n"
        outputString += "MinefieldLocation :" + "\n" + self.minefieldLocation.to_string() + "\n"
        outputString += "MinefieldOrientation :" + "\n" + self.minefieldOrientation.to_string() + "\n"
        outputString += "MinefieldStateAppearanceBitMap : " + str(self.appearance) + "\n"
        outputString += "ProtocolMode :" + "\n" + self.protocolMode.to_string() + "\n"
        outputString += "PerimeterPoints : " + "\n"
        for idx in range(0, len(self._perimeterPoints)):
            outputString += self._perimeterPoints[idx].to_string()

        outputString += "MineType : " + "\n"
        for idx in range(0, len(self._mineType)):
            outputString += self._mineType[idx].to_string()

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
        super( MinefieldStatePdu, self ).serialize(outputStream)
        self.minefieldID.serialize(outputStream)
        outputStream.write_short(int(self.minefieldSequence))
        self.serialize_enum(self.forceID,outputStream)
        outputStream.write_byte( len(self._perimeterPoints))
        self.minefieldType.serialize(outputStream)
        outputStream.write_short( len(self._mineType))
        self.minefieldLocation.serialize(outputStream)
        self.minefieldOrientation.serialize(outputStream)
        outputStream.write_unsigned_int(int(self.appearance.asbyte))
        self.protocolMode.serialize(outputStream)
        for anObj in self._perimeterPoints:
            anObj.serialize(outputStream)

        for anObj in self._mineType:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( MinefieldStatePdu, self).parse(inputStream)
        self.minefieldID.parse(inputStream)
        self.minefieldSequence = inputStream.read_short()
        self.forceID = ForceID.get_enum(self.parse_enum(self.forceID,inputStream))
        self.numberOfPerimeterPoints = inputStream.read_byte()
        self.minefieldType.parse(inputStream)
        self.numberOfMineTypes = inputStream.read_short()
        self.minefieldLocation.parse(inputStream)
        self.minefieldOrientation.parse(inputStream)
        self.appearance.asbyte = inputStream.read_unsigned_int()
        self.protocolMode.parse(inputStream)
        for idx in range(0, self.numberOfPerimeterPoints):
            element = Vector2Float()
            element.parse(inputStream)
            self._perimeterPoints.append(element)

        for idx in range(0, self.numberOfMineTypes):
            element = EntityType()
            element.parse(inputStream)
            self._mineType.append(element)


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



