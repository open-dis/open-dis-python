from enum import Enum

from .siso_ref_010.enums.entity_marking_character_set import EntityMarkingCharacterSet

class AggregateMarking( object ):
    """Specifies the character set used in the first byte, followed by up to 31 characters of text data. Section 6.2.4. """

    def __init__(self):
        """ Initializer for AggregateMarking"""
        # /** The character set uid 45 */
        self.characterSet = EntityMarkingCharacterSet.default

        """ The characters"""
        self.characters =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def to_string(self) ->str:
        outputString = ""
        outputString += "EntityMarkingCharacterSet : " + self.characterSet.get_description + "(" + (str(int(self.characterSet))) + ")" + "\n"
        outputString += "Characters : " + "\n"
        for idx in range(0, len(self.characters)):
            outputString += str(self.characters[idx])

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
        self.serialize_enum(self.characterSet,outputStream)
        for idx in range(0, 31):
            outputStream.write_unsigned_byte( self.characters[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.characterSet = EntityMarkingCharacterSet.get_enum(self.parse_enum(self.characterSet,inputStream))
        self.characters = [0]*31
        for idx in range(0, 31):
            val = inputStream.read_unsigned_byte()
            self.characters[  idx  ] = val


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 2

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



