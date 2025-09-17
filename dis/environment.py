from enum import Enum

from .siso_ref_010.enums.environmental_process_record_type import EnvironmentalProcessRecordType

class Environment( object ):
    """ Information about a geometry, a state associated with a geometry, a bounding volume, or an associated entity ID.  6.2.31, not fully defined. 'The current definitions can be found in DIS PCR 240'"""

    def __init__(self):
        """ Initializer for Environment"""
        # /** Record type uid 250 */
        self.environmentType = EnvironmentalProcessRecordType.default

        """ length, in bits"""
        self.length = 0
        """ Identify the sequentially numbered record index"""
        self.index = 0
        """ padding"""
        self.padding1 = 0
        """ Geometry or state record"""
        self.geometry =  []
        self.padding2 = [0] * 64

    def to_string(self) ->str:
        outputString = ""
        outputString += "EnvironmentalProcessRecordType : " + self.environmentType.get_description + "(" + (str(int(self.environmentType))) + ")" + "\n"
        outputString += "Length : " + str(self.length) + "\n"
        outputString += "Index : " + str(self.index) + "\n"
        outputString += "Padding1 : " + str(self.padding1) + "\n"
        outputString += "Geometry : " + "\n"
        for idx in range(0, len(self.geometry)):
            outputString += str(self.geometry[idx])

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
        self.serialize_enum(self.environmentType,outputStream)
        outputStream.write_short(int(self.length))
        outputStream.write_byte(int(self.index))
        outputStream.write_byte(int(self.padding1))
        for idx in range(0, 0):
            outputStream.write_unsigned_byte( self.geometry[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.environmentType = EnvironmentalProcessRecordType.get_enum(self.parse_enum(self.environmentType,inputStream))
        self.length = inputStream.read_short()
        self.index = inputStream.read_byte()
        self.padding1 = inputStream.read_byte()
        self.geometry = [0]*0
        for idx in range(0, 0):
            val = inputStream.read_unsigned_byte()
            self.geometry[  idx  ] = val


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



