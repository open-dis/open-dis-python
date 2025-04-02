from enum import Enum

from .siso_ref_010.enums.iffapplicable_modes import IFFApplicableModes

class IFFFundamentalParameterData( object ):
    """Fundamental IFF atc data. Section 6.2.44"""

    def __init__(self):
        """ Initializer for IFFFundamentalParameterData"""
        """ ERP"""
        self.erp = 0.0
        """ frequency"""
        self.frequency = 0.0
        """ pgrf"""
        self.pgrf = 0.0
        """ Pulse width"""
        self.pulseWidth = 0.0
        """ Burst length"""
        self.burstLength = 0
        # /** Applicable modes enumeration uid 339 */
        self.applicableModes = IFFApplicableModes.default

        """ System-specific data"""
        self.systemSpecificData =  [ 0, 0, 0]

    def to_string(self) ->str:
        outputString = ""
        outputString += "Erp : " + str(self.erp) + "\n"
        outputString += "Frequency : " + str(self.frequency) + "\n"
        outputString += "Pgrf : " + str(self.pgrf) + "\n"
        outputString += "PulseWidth : " + str(self.pulseWidth) + "\n"
        outputString += "BurstLength : " + str(self.burstLength) + "\n"
        outputString += "IFFApplicableModes : " + self.applicableModes.get_description + "(" + (str(int(self.applicableModes))) + ")" + "\n"
        outputString += "SystemSpecificData : " + "\n"
        for idx in range(0, len(self.systemSpecificData)):
            outputString += str(self.systemSpecificData[idx])

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
        outputStream.write_float(int(self.erp))
        outputStream.write_float(int(self.frequency))
        outputStream.write_float(int(self.pgrf))
        outputStream.write_float(int(self.pulseWidth))
        outputStream.write_int(int(self.burstLength))
        self.serialize_enum(self.applicableModes,outputStream)
        for idx in range(0, 3):
            outputStream.write_unsigned_byte( self.systemSpecificData[ idx ] );


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.erp = inputStream.read_float()
        self.frequency = inputStream.read_float()
        self.pgrf = inputStream.read_float()
        self.pulseWidth = inputStream.read_float()
        self.burstLength = inputStream.read_int()
        self.applicableModes = IFFApplicableModes.get_enum(self.parse_enum(self.applicableModes,inputStream))
        self.systemSpecificData = [0]*3
        for idx in range(0, 3):
            val = inputStream.read_unsigned_byte()
            self.systemSpecificData[  idx  ] = val


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



