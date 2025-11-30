from enum import Enum

from .siso_ref_010.enums.defire_pulse_shape import DEFirePulseShape
from .entity_type import EntityType
from .clock_time import ClockTime
from .siso_ref_010.enums.defire_flags import DEFireFlags
from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .vector3float import Vector3Float
from .warfare_family_pdu import WarfareFamilyPdu
from .entity_id import EntityID
from .event_identifier import EventIdentifier
from .standard_variable_specification import StandardVariableSpecification

class DirectedEnergyFirePdu( WarfareFamilyPdu ):
    """7.3.4 Used to communicate the firing of a directed energy weapon."""

    def __init__(self):
        """ Initializer for DirectedEnergyFirePdu"""
        super().__init__()
        """ ID of the entity that shot"""
        self.firingEntityID = EntityID()
        # eventID is an undescribed parameter... 
        self.eventID = EventIdentifier()
        """ Field shall identify the munition type enumeration for the DE weapon beam, Section 7.3.4 """
        self.munitionType = EntityType()
        """ Field shall indicate the simulation time at start of the shot, Section 7.3.4 """
        self.shotStartTime = ClockTime()
        """ Field shall indicate the current cumulative duration of the shot, Section 7.3.4 """
        self.commulativeShotTime = 0.0
        """ Field shall identify the location of the DE weapon aperture/emitter, Section 7.3.4 """
        self.apertureEmitterLocation = Vector3Float()
        """ Field shall identify the beam diameter at the aperture/emitter, Section 7.3.4 """
        self.apertureDiameter = 0.0
        """ Field shall identify the emissions wavelength in units of meters, Section 7.3.4 """
        self.wavelength = 0.0
        self.pad1 = 0
        self.pulseRepititionFrequency = 0.0
        """ field shall identify the pulse width emissions in units of seconds, Section 7.3.4"""
        self.pulseWidth = 0.0
        # 16bit Boolean field shall contain various flags to indicate status information needed to process a DE, Section 7.3.4  uid 313
        self.flags = DEFireFlags()

        # /** Field shall identify the pulse shape and shall be represented as an 8-bit enumeration, Section 7.3.4  uid 312 */
        self.pulseShape = DEFirePulseShape.default

        self.pad2 = 0
        self.pad3 = 0
        self.pad4 = 0
        """ Field shall specify the number of DE records, Section 7.3.4 """
        self.numberOfDERecords = 0
        """ Fields shall contain one or more DE records, records shall conform to the variable record format (Section6.2.82), Section 7.3.4"""
        self._dERecords = []
        self.pduType = DisPduType.directed_energy_fire


    def get_numberOfDERecords(self):
        return len(self._dERecords)
    def set_numberOfDERecords(self, value):
        numberOfDERecords = value


    def get_dERecords(self):
        return self._dERecords
    def set_dERecords(self, value):
        self._dERecords = value
    dERecords = property(get_dERecords, set_dERecords)


    def add_dERecords(self, value : StandardVariableSpecification):
        self._dERecords.append(value)


    """
    ///            Name : dERecords
    ///             UID : 
    ///            Type : StandardVariableSpecification
    ///            Kind : OBJECT_LIST
    ///    Marshal Size : 8
    ///         Comment : Fields shall contain one or more DE records, records shall conform to the variable record format (Section6.2.82), Section 7.3.4
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
        outputString += "FiringEntityID :" + "\n" + self.firingEntityID.to_string() + "\n"
        outputString += "EventID :" + "\n" + self.eventID.to_string() + "\n"
        outputString += "MunitionType :" + "\n" + self.munitionType.to_string() + "\n"
        outputString += "ShotStartTime :" + "\n" + self.shotStartTime.to_string() + "\n"
        outputString += "CommulativeShotTime : " + str(self.commulativeShotTime) + "\n"
        outputString += "ApertureEmitterLocation :" + "\n" + self.apertureEmitterLocation.to_string() + "\n"
        outputString += "ApertureDiameter : " + str(self.apertureDiameter) + "\n"
        outputString += "Wavelength : " + str(self.wavelength) + "\n"
        outputString += "Pad1 : " + str(self.pad1) + "\n"
        outputString += "PulseRepititionFrequency : " + str(self.pulseRepititionFrequency) + "\n"
        outputString += "PulseWidth : " + str(self.pulseWidth) + "\n"
        outputString += "DEFireFlags : " + str(self.flags) + "\n"
        outputString += "DEFirePulseShape : " + self.pulseShape.get_description + "(" + (str(int(self.pulseShape))) + ")" + "\n"
        outputString += "Pad2 : " + str(self.pad2) + "\n"
        outputString += "Pad3 : " + str(self.pad3) + "\n"
        outputString += "Pad4 : " + str(self.pad4) + "\n"
        outputString += "NumberOfDERecords : " + str(len(self._dERecords)) + "\n"
        outputString += "DERecords : " + "\n"
        for idx in range(0, len(self._dERecords)):
            outputString += self._dERecords[idx].to_string()

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
        super( DirectedEnergyFirePdu, self ).serialize(outputStream)
        self.firingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        self.munitionType.serialize(outputStream)
        self.shotStartTime.serialize(outputStream)
        outputStream.write_float(int(self.commulativeShotTime))
        self.apertureEmitterLocation.serialize(outputStream)
        outputStream.write_float(int(self.apertureDiameter))
        outputStream.write_float(int(self.wavelength))
        outputStream.write_int(int(self.pad1))
        outputStream.write_float(int(self.pulseRepititionFrequency))
        outputStream.write_float(int(self.pulseWidth))
        outputStream.write_unsigned_int(int(self.flags.asbyte))
        self.serialize_enum(self.pulseShape,outputStream)
        outputStream.write_byte(int(self.pad2))
        outputStream.write_int(int(self.pad3))
        outputStream.write_short(int(self.pad4))
        outputStream.write_short( len(self._dERecords))
        for anObj in self._dERecords:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( DirectedEnergyFirePdu, self).parse(inputStream)
        self.firingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.munitionType.parse(inputStream)
        self.shotStartTime.parse(inputStream)
        self.commulativeShotTime = inputStream.read_float()
        self.apertureEmitterLocation.parse(inputStream)
        self.apertureDiameter = inputStream.read_float()
        self.wavelength = inputStream.read_float()
        self.pad1 = inputStream.read_int()
        self.pulseRepititionFrequency = inputStream.read_float()
        self.pulseWidth = inputStream.read_float()
        self.flags.asbyte = inputStream.read_unsigned_int()
        self.pulseShape = DEFirePulseShape.get_enum(self.parse_enum(self.pulseShape,inputStream))
        self.pad2 = inputStream.read_byte()
        self.pad3 = inputStream.read_int()
        self.pad4 = inputStream.read_short()
        self.numberOfDERecords = inputStream.read_short()
        for idx in range(0, self.numberOfDERecords):
            element = StandardVariableSpecification()
            element.parse(inputStream)
            self._dERecords.append(element)


    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 18

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



