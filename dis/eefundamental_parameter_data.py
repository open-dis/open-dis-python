from enum import Enum


class EEFundamentalParameterData( object ):
    """Contains electromagnetic emission regeneration parameters that are variable throught a scenario. Section 6.2.22."""

    def __init__(self):
        """ Initializer for EEFundamentalParameterData"""
        """ center frequency of the emission in hertz."""
        self.frequency = 0.0
        """ Bandwidth of the frequencies corresponding to the fequency field."""
        self.frequencyRange = 0.0
        """ Effective radiated power for the emission in DdBm. For a radar noise jammer, indicates the peak of the transmitted power."""
        self.effectiveRadiatedPower = 0.0
        """ Average repetition frequency of the emission in hertz."""
        self.pulseRepetitionFrequency = 0.0
        """ Average pulse width  of the emission in microseconds."""
        self.pulseWidth = 0.0

    def to_string(self) ->str:
        outputString = ""
        outputString += "Frequency : " + str(self.frequency) + "\n"
        outputString += "FrequencyRange : " + str(self.frequencyRange) + "\n"
        outputString += "EffectiveRadiatedPower : " + str(self.effectiveRadiatedPower) + "\n"
        outputString += "PulseRepetitionFrequency : " + str(self.pulseRepetitionFrequency) + "\n"
        outputString += "PulseWidth : " + str(self.pulseWidth) + "\n"
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
        outputStream.write_float(int(self.frequency))
        outputStream.write_float(int(self.frequencyRange))
        outputStream.write_float(int(self.effectiveRadiatedPower))
        outputStream.write_float(int(self.pulseRepetitionFrequency))
        outputStream.write_float(int(self.pulseWidth))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.frequency = inputStream.read_float()
        self.frequencyRange = inputStream.read_float()
        self.effectiveRadiatedPower = inputStream.read_float()
        self.pulseRepetitionFrequency = inputStream.read_float()
        self.pulseWidth = inputStream.read_float()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 5

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



