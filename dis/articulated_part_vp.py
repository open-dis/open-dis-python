from enum import Enum

from .siso_ref_010.enums.variable_parameter_record_type import VariableParameterRecordType

class ArticulatedPartVP( object ):
    """ articulated parts for movable parts and a combination of moveable/attached parts of an entity. Section 6.2.94.2"""

    def __init__(self):
        """ Initializer for ArticulatedPartVP"""
        # /** The identification of the Variable Parameter record. Enumeration from EBV uid 56 */
        self.recordType = VariableParameterRecordType.articulated_part

        """ indicate the change of any parameter for any articulated part. Starts at zero, incremented for each change """
        self.changeIndicator = 0
        """ The identification of the articulated part to which this articulation parameter is attached. This field shall be specified by a 16-bit unsigned integer. This field shall contain the value zero if the articulated part is attached directly to the entity."""
        self.partAttachedTo = 0
        """ The type of parameter represented, 32-bit enumeration"""
        self.parameterType = 0
        """ The definition of the 64-bits shall be determined based on the type of parameter specified in the Parameter Type field """
        self.parameterValue = 0.0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "VariableParameterRecordType : " + self.recordType.get_description + "(" + (str(int(self.recordType))) + ")" + "\n"
        outputString += "ChangeIndicator : " + str(self.changeIndicator) + "\n"
        outputString += "PartAttachedTo : " + str(self.partAttachedTo) + "\n"
        outputString += "ParameterType : " + str(self.parameterType) + "\n"
        outputString += "ParameterValue : " + str(self.parameterValue) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
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
        self.serialize_enum(self.recordType,outputStream)
        outputStream.write_byte(int(self.changeIndicator))
        outputStream.write_short(int(self.partAttachedTo))
        outputStream.write_int(int(self.parameterType))
        outputStream.write_float(int(self.parameterValue))
        outputStream.write_int(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.recordType = VariableParameterRecordType.get_enum(self.parse_enum(self.recordType,inputStream))
        self.changeIndicator = inputStream.read_byte()
        self.partAttachedTo = inputStream.read_short()
        self.parameterType = inputStream.read_int()
        self.parameterValue = inputStream.read_float()
        self.padding = inputStream.read_int()

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



