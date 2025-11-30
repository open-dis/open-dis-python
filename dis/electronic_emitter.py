from enum import Enum

from .emitter_system import EmitterSystem
from .emitter_beam import EmitterBeam
from .vector3float import Vector3Float

class ElectronicEmitter( object ):
    """A device that is able to discharge detectable electromagnetic energy."""

    def __init__(self):
        """ Initializer for ElectronicEmitter"""
        """  this field shall specify the length of this emitter system's data in 32-bit words."""
        self.systemDataLength = 0
        """ the number of beams being described in the current PDU for the emitter system being described. """
        self.numberOfBeams = 0
        """ padding"""
        self.padding = 0
        """  information about a particular emitter system and shall be represented by an Emitter System record (see 6.2.23)."""
        self.emitterSystem = EmitterSystem()
        """ the location of the antenna beam source with respect to the emitting entity's coordinate system. This location shall be the origin of the emitter coordinate system that shall have the same orientation as the entity coordinate system. This field shall be represented by an Entity Coordinate Vector record see 6.2.95 """
        self.location = Vector3Float()
        """ Electronic emission beams"""
        self._beams = []


    def get_numberOfBeams(self):
        return len(self._beams)
    def set_numberOfBeams(self, value):
        numberOfBeams = value


    def get_beams(self):
        return self._beams
    def set_beams(self, value):
        self._beams = value
    beams = property(get_beams, set_beams)


    def add_beams(self, value : EmitterBeam):
        self._beams.append(value)


    """
    ///            Name : beams
    ///             UID : 
    ///            Type : EmitterBeam
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Electronic emission beams
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
        outputString += "SystemDataLength : " + str(self.systemDataLength) + "\n"
        outputString += "NumberOfBeams : " + str(len(self._beams)) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "EmitterSystem :" + "\n" + self.emitterSystem.to_string() + "\n"
        outputString += "Location :" + "\n" + self.location.to_string() + "\n"
        outputString += "Beams : " + "\n"
        for idx in range(0, len(self._beams)):
            outputString += self._beams[idx].to_string()

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
        outputStream.write_byte(int(self.systemDataLength))
        outputStream.write_byte( len(self._beams))
        outputStream.write_short(int(self.padding))
        self.emitterSystem.serialize(outputStream)
        self.location.serialize(outputStream)
        for anObj in self._beams:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.systemDataLength = inputStream.read_byte()
        self.numberOfBeams = inputStream.read_byte()
        self.padding = inputStream.read_short()
        self.emitterSystem.parse(inputStream)
        self.location.parse(inputStream)
        for idx in range(0, self.numberOfBeams):
            element = EmitterBeam()
            element.parse(inputStream)
            self._beams.append(element)


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



