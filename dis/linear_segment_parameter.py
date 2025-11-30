from enum import Enum

from .siso_ref_010.enums.object_state_appearance_general import ObjectStateAppearanceGeneral
from .euler_angles import EulerAngles
from .vector3double import Vector3Double
from .siso_ref_010.enums.object_state_modification_linear_object import ObjectStateModificationLinearObject

class LinearSegmentParameter( object ):
    """The specification of an individual segment of a linear segment synthetic environment object in a Linear Object State PDU Section 6.2.52"""

    def __init__(self):
        """ Initializer for LinearSegmentParameter"""
        """ The individual segment of the linear segment"""
        self.segmentNumber = 0
        #  whether a modification has been made to the point object's location or orientation UID 241
        self.segmentModification = ObjectStateModificationLinearObject()

        # general dynamic appearance attributes of the segment. This record shall be defined as a 16-bit record of enumerations. The values defined for this record are included in Section 12 of SISO-REF-010. UID 229
        self.generalSegmentAppearance = ObjectStateAppearanceGeneral()

        """ This field shall specify specific dynamic appearance attributes of the segment. This record shall be defined as a 32-bit record of enumerations."""
        self.specificSegmentAppearance = 0
        """ This field shall specify the location of the linear segment in the simulated world and shall be represented by a World Coordinates record """
        self.segmentLocation = Vector3Double()
        """ orientation of the linear segment about the segment location and shall be represented by a Euler Angles record """
        self.segmentOrientation = EulerAngles()
        """ length of the linear segment, in meters, extending in the positive X direction"""
        self.segmentLength = 0.0
        """ The total width of the linear segment, in meters, shall be specified by a 16-bit unsigned integer. One-half of the width shall extend in the positive Y direction, and one-half of the width shall extend in the negative Y direction."""
        self.segmentWidth = 0.0
        """ The height of the linear segment, in meters, above ground shall be specified by a 16-bit unsigned integer."""
        self.segmentHeight = 0.0
        """ The depth of the linear segment, in meters, below ground level """
        self.segmentDepth = 0.0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "SegmentNumber : " + str(self.segmentNumber) + "\n"
        outputString += "ObjectStateModificationLinearObject : " + str(self.segmentModification) + "\n"
        outputString += "ObjectStateAppearanceGeneral : " + str(self.generalSegmentAppearance) + "\n"
        outputString += "SpecificSegmentAppearance : " + str(self.specificSegmentAppearance) + "\n"
        outputString += "SegmentLocation :" + "\n" + self.segmentLocation.to_string() + "\n"
        outputString += "SegmentOrientation :" + "\n" + self.segmentOrientation.to_string() + "\n"
        outputString += "SegmentLength : " + str(self.segmentLength) + "\n"
        outputString += "SegmentWidth : " + str(self.segmentWidth) + "\n"
        outputString += "SegmentHeight : " + str(self.segmentHeight) + "\n"
        outputString += "SegmentDepth : " + str(self.segmentDepth) + "\n"
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
        outputStream.write_byte(int(self.segmentNumber))
        outputStream.write_unsigned_int(int(self.segmentModification.asbyte))
        outputStream.write_unsigned_int(int(self.generalSegmentAppearance.asbyte))
        outputStream.write_int(int(self.specificSegmentAppearance))
        self.segmentLocation.serialize(outputStream)
        self.segmentOrientation.serialize(outputStream)
        outputStream.write_float(int(self.segmentLength))
        outputStream.write_float(int(self.segmentWidth))
        outputStream.write_float(int(self.segmentHeight))
        outputStream.write_float(int(self.segmentDepth))
        outputStream.write_int(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.segmentNumber = inputStream.read_byte()
        self.segmentModification.asbyte = inputStream.read_unsigned_int()
        self.generalSegmentAppearance.asbyte = inputStream.read_unsigned_int()
        self.specificSegmentAppearance = inputStream.read_int()
        self.segmentLocation.parse(inputStream)
        self.segmentOrientation.parse(inputStream)
        self.segmentLength = inputStream.read_float()
        self.segmentWidth = inputStream.read_float()
        self.segmentHeight = inputStream.read_float()
        self.segmentDepth = inputStream.read_float()
        self.padding = inputStream.read_int()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 11

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



