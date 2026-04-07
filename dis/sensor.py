from enum import Enum

from .siso_ref_010.enums.sensor_type_source import SensorTypeSource
from .siso_ref_010.enums.sensor_on_off_status import SensorOnOffStatus

class Sensor( object ):
    """An entity's sensor information.  Section 6.2.77."""

    def __init__(self):
        """ Initializer for Sensor"""
        # /**  the source of the Sensor Type field  uid 414 */
        self.sensorTypeSource = SensorTypeSource.default

        # /** The on/off status of the sensor uid 331 */
        self.sensorOnOffStatus = SensorOnOffStatus.default

        """ for Source 'other':SensorRecordOtherActiveSensors/325,'em':EmitterName/75,'passive':SensorRecordSensorTypePassiveSensors/326,'mine':6.2.57,'ua':UAAcousticSystemName/144,'lasers':DesignatorSystemName/80"""
        self.sensorType = 0
        """  the station to which the sensor is assigned. A zero value shall indi- cate that this Sensor record is not associated with any particular station and represents the total quan- tity of this sensor for this entity. If this field is non-zero, it shall either reference an attached part or an articulated part"""
        self.station = 0
        """ quantity of the sensor """
        self.quantity = 0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0

    def to_string(self) ->str:
        outputString = ""
        outputString += "SensorTypeSource : " + self.sensorTypeSource.get_description + "(" + (str(int(self.sensorTypeSource))) + ")" + "\n"
        outputString += "SensorOnOffStatus : " + self.sensorOnOffStatus.get_description + "(" + (str(int(self.sensorOnOffStatus))) + ")" + "\n"
        outputString += "SensorType : " + str(self.sensorType) + "\n"
        outputString += "Station : " + str(self.station) + "\n"
        outputString += "Quantity : " + str(self.quantity) + "\n"
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
        self.serialize_enum(self.sensorTypeSource,outputStream)
        self.serialize_enum(self.sensorOnOffStatus,outputStream)
        outputStream.write_short(int(self.sensorType))
        outputStream.write_int(int(self.station))
        outputStream.write_short(int(self.quantity))
        outputStream.write_short(int(self.padding))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.sensorTypeSource = SensorTypeSource.get_enum(self.parse_enum(self.sensorTypeSource,inputStream))
        self.sensorOnOffStatus = SensorOnOffStatus.get_enum(self.parse_enum(self.sensorOnOffStatus,inputStream))
        self.sensorType = inputStream.read_short()
        self.station = inputStream.read_int()
        self.quantity = inputStream.read_short()
        self.padding = inputStream.read_short()

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



