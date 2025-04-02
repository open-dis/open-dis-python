from enum import Enum


class BeamData( object ):
    """Describes the scan volue of an emitter beam. Section 6.2.11."""

    def __init__(self):
        """ Initializer for BeamData"""
        """ Specifies the beam azimuth an elevation centers and corresponding half-angles to describe the scan volume"""
        self.beamAzimuthCenter = 0.0
        """ Specifies the beam azimuth sweep to determine scan volume"""
        self.beamAzimuthSweep = 0.0
        """ Specifies the beam elevation center to determine scan volume"""
        self.beamElevationCenter = 0.0
        """ Specifies the beam elevation sweep to determine scan volume"""
        self.beamElevationSweep = 0.0
        """ allows receiver to synchronize its regenerated scan pattern to that of the emmitter. Specifies the percentage of time a scan is through its pattern from its origion."""
        self.beamSweepSync = 0.0

    def to_string(self) ->str:
        outputString = ""
        outputString += "BeamAzimuthCenter : " + str(self.beamAzimuthCenter) + "\n"
        outputString += "BeamAzimuthSweep : " + str(self.beamAzimuthSweep) + "\n"
        outputString += "BeamElevationCenter : " + str(self.beamElevationCenter) + "\n"
        outputString += "BeamElevationSweep : " + str(self.beamElevationSweep) + "\n"
        outputString += "BeamSweepSync : " + str(self.beamSweepSync) + "\n"
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
        outputStream.write_float(int(self.beamAzimuthCenter))
        outputStream.write_float(int(self.beamAzimuthSweep))
        outputStream.write_float(int(self.beamElevationCenter))
        outputStream.write_float(int(self.beamElevationSweep))
        outputStream.write_float(int(self.beamSweepSync))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.beamAzimuthCenter = inputStream.read_float()
        self.beamAzimuthSweep = inputStream.read_float()
        self.beamElevationCenter = inputStream.read_float()
        self.beamElevationSweep = inputStream.read_float()
        self.beamSweepSync = inputStream.read_float()

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



