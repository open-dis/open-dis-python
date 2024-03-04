#
#This code is licensed under the BSD software license
#


class DataQueryDatumSpecification( object ):
    """List of fixed and variable datum records. Section 6.2.17 """

    def __init__(self,
                numberOfFixedDatums=0,
                numberOfVariableDatums=0,
                fixedDatumIDs=None,
                variableDatumIDs=None):
        """ Initializer for DataQueryDatumSpecification"""
        self.numberOfFixedDatums = numberOfFixedDatums
        """ Number of fixed datums"""
        self.numberOfVariableDatums = numberOfVariableDatums
        """ Number of variable datums"""
        self.fixedDatumIDs = fixedDatumIDs or []
        """ variable length list fixed datum IDs"""
        self.variableDatumIDs = variableDatumIDs or []
        """ variable length list variable datum IDs"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int( len(self.fixedDatumIDs))
        outputStream.write_unsigned_int( len(self.variableDatumIDs))
        for anObj in self.fixedDatumIDs:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumIDs:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.numberOfFixedDatums = inputStream.read_unsigned_int()
        self.numberOfVariableDatums = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatums):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumIDs.append(element)

        for idx in range(0, self.numberOfVariableDatums):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumIDs.append(element)




class RadioIdentifier( object ):
    """The unique designation of an attached or unattached radio in an event or exercise Section 6.2.70"""

    def __init__(self,
                 siteNumber=0,
                 applicationNumber=0,
                 referenceNumber=0,
                 radioNumber=0):
        """ Initializer for RadioIdentifier"""
        self.siteNumber = siteNumber
        """  site"""
        self.applicationNumber = applicationNumber
        """ application number"""
        self.referenceNumber = referenceNumber
        """  reference number"""
        self.radioNumber = radioNumber
        """  Radio number"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.siteNumber)
        outputStream.write_unsigned_short(self.applicationNumber)
        outputStream.write_unsigned_short(self.referenceNumber)
        outputStream.write_unsigned_short(self.radioNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.siteNumber = inputStream.read_unsigned_short()
        self.applicationNumber = inputStream.read_unsigned_short()
        self.referenceNumber = inputStream.read_unsigned_short()
        self.radioNumber = inputStream.read_unsigned_short()



class RequestID( object ):
    """A monotonically increasing number inserted into all simulation managment PDUs. This should be a hand-coded thingie, maybe a singleton. Section 6.2.75"""

    def __init__(self, requestID=0):
        """ Initializer for RequestID"""
        self.requestID = requestID
        """ monotonically increasing number"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.requestID = inputStream.read_unsigned_int()



class IFFData( object ):
    """repeating element if IFF Data specification record"""

    def __init__(self,
                 recordType=0,
                 recordLength=0,
                 iffData=None):
        """ Initializer for IFFData"""
        self.recordType = recordType
        """ enumeration for type of record"""
        self.recordLength = recordLength
        """ length of record. Should be padded to 32 bit boundary."""
        self.iffData = iffData or []
        """ IFF data."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short( len(self.iffData))
        for anObj in self.iffData:
            outputStream.write_unsigned_byte(anObj)

        """ TODO add padding to end on 32-bit boundary """

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        """ The record length includes the length of record type field (32 bits) and record length field (16 bits) so we subtract 6 bytes total for those. """
        for idx in range(0, self.recordLength - 6):
            val = inputStream.read_unsigned_byte()
            self.iffData.append(val)




class MunitionDescriptor( object ):
    """Represents the firing or detonation of a munition. Section 6.2.19.2"""

    def __init__(self,
                 munitionType=None,
                 warhead=0,
                 fuse=0,
                 quantity=0,
                 rate=0):
        """ Initializer for MunitionDescriptor"""
        self.munitionType = munitionType or EntityType()
        """ What munition was used in the burst"""
        self.warhead = warhead
        """ type of warhead enumeration"""
        self.fuse = fuse
        """ type of fuse used enumeration"""
        self.quantity = quantity
        """ how many of the munition were fired"""
        self.rate = rate
        """ rate at which the munition was fired"""

    def serialize(self, outputStream):
        """serialize the class """
        self.munitionType.serialize(outputStream)
        outputStream.write_unsigned_short(self.warhead)
        outputStream.write_unsigned_short(self.fuse)
        outputStream.write_unsigned_short(self.quantity)
        outputStream.write_unsigned_short(self.rate)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.munitionType.parse(inputStream)
        self.warhead = inputStream.read_unsigned_short()
        self.fuse = inputStream.read_unsigned_short()
        self.quantity = inputStream.read_unsigned_short()
        self.rate = inputStream.read_unsigned_short()



class MinefieldSensorType( object ):
    """Information about a minefield sensor. Section 6.2.57"""

    def __init__(self, sensorType=0):
        """ Initializer for MinefieldSensorType"""
        self.sensorType = sensorType
        """ sensor type. bit fields 0-3 are the type category, 4-15 are teh subcategory"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.sensorType)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.sensorType = inputStream.read_unsigned_short()



class GroupID( object ):
    """Unique designation of a group of entities contained in the isGroupOfPdu. Represents a group of entities rather than a single entity. Section 6.2.43"""

    def __init__(self, simulationAddress=None, groupNumber=0):
        """ Initializer for GroupID"""
        self.simulationAddress = simulationAddress or EntityType()
        """ Simulation address (site and application number)"""
        self.groupNumber = groupNumber
        """ group number"""

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.groupNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.groupNumber = inputStream.read_unsigned_short()



class LayerHeader( object ):
    """The identification of the additional information layer number, layer-specific information, and the length of the layer. Section 6.2.51"""

    def __init__(self, layerNumber=0, layerSpecificInformation=0, length=0):
        """ Initializer for LayerHeader"""
        self.layerNumber = layerNumber
        self.layerSpecificInformation = layerSpecificInformation
        """ field shall specify layer-specific information that varies by System Type (see 6.2.86) and Layer Number."""
        self.length = length
        """ This field shall specify the length in octets of the layer, including the Layer Header record"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.layerNumber)
        outputStream.write_unsigned_byte(self.layerSpecificInformation)
        outputStream.write_unsigned_short(self.length)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.layerNumber = inputStream.read_unsigned_byte()
        self.layerSpecificInformation = inputStream.read_unsigned_byte()
        self.length = inputStream.read_unsigned_short()



class UnsignedDISInteger( object ):
    """container class not in specification"""

    def __init__(self, val=0):
        """ Initializer for UnsignedDISInteger"""
        self.val = val
        """ unsigned integer"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.val)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.val = inputStream.read_unsigned_int()



class DeadReckoningParameters( object ):
    """Not specified in the standard. This is used by the ESPDU"""

    def __init__(self,
                 deadReckoningAlgorithm=0,
                 parameters=None,
                 entityLinearAcceleration=None,
                 entityAngularVelocity=None):
        """ Initializer for DeadReckoningParameters"""
        self.deadReckoningAlgorithm = deadReckoningAlgorithm
        """ Algorithm to use in computing dead reckoning. See EBV doc."""
        self.parameters =  parameters or [0] * 15
        """ Dead reckoning parameters. Contents depends on algorithm."""
        self.entityLinearAcceleration = entityLinearAcceleration or Vector3Float()
        """ Linear acceleration of the entity"""
        self.entityAngularVelocity = entityAngularVelocity or Vector3Float()
        """ Angular velocity of the entity"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.deadReckoningAlgorithm)
        for idx in range(0, 15):
            outputStream.write_unsigned_byte( self.parameters[ idx ] )

        self.entityLinearAcceleration.serialize(outputStream)
        self.entityAngularVelocity.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.deadReckoningAlgorithm = inputStream.read_unsigned_byte()
        self.parameters = [0]*15
        for idx in range(0, 15):
            val = inputStream.read_unsigned_byte()

            self.parameters[  idx  ] = val

        self.entityLinearAcceleration.parse(inputStream)
        self.entityAngularVelocity.parse(inputStream)



class ProtocolMode( object ):
    """Bit field used to identify minefield data. bits 14-15 are a 2-bit enum, other bits unused. Section 6.2.69"""

    def __init__(self, protocolMode=0):
        """ Initializer for ProtocolMode"""
        self.protocolMode = protocolMode
        """ Bitfields, 14-15 contain an enum"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.protocolMode)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.protocolMode = inputStream.read_unsigned_short()



class AngleDeception( object ):
    """The Angle Deception attribute record may be used to communicate discrete values that are associated with angle deception jamming that cannot be referenced to an emitter mode. The values provided in the record records (provided in the associated Electromagnetic Emission PDU). (The victim radar beams are those that are targeted by the jammer.) Section 6.2.21.2.2"""

    def __init__(self,
                 recordType=3501,
                 recordLength=48,
                 emitterNumber=0,
                 beamNumber=0,
                 stateIndicator=0,
                 azimuthOffset=0.0,
                 azimuthWidth=0.0,
                 azimuthPullRate=0.0,
                 azimuthPullAcceleration=0.0,
                 elevationOffset=0.0,
                 elevationWidth=0.0,
                 elevationPullRate=0.0,
                 elevationPullAcceleration=0.0):
        """ Initializer for AngleDeception"""
        self.recordType = recordType
        self.recordLength = recordLength
        self.padding = 0
        self.emitterNumber = emitterNumber
        self.beamNumber = beamNumber
        self.stateIndicator = stateIndicator
        self.padding2 = 0
        self.azimuthOffset = azimuthOffset
        self.azimuthWidth = azimuthWidth
        self.azimuthPullRate = azimuthPullRate
        self.azimuthPullAcceleration = azimuthPullAcceleration
        self.elevationOffset = elevationOffset
        self.elevationWidth = elevationWidth
        self.elevationPullRate = elevationPullRate
        self.elevationPullAcceleration = elevationPullAcceleration
        self.padding3 = 0

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_short(self.padding)
        outputStream.write_unsigned_byte(self.emitterNumber)
        outputStream.write_unsigned_byte(self.beamNumber)
        outputStream.write_unsigned_byte(self.stateIndicator)
        outputStream.write_unsigned_byte(self.padding2)
        outputStream.write_float(self.azimuthOffset)
        outputStream.write_float(self.azimuthWidth)
        outputStream.write_float(self.azimuthPullRate)
        outputStream.write_float(self.azimuthPullAcceleration)
        outputStream.write_float(self.elevationOffset)
        outputStream.write_float(self.elevationWidth)
        outputStream.write_float(self.elevationPullRate)
        outputStream.write_float(self.elevationPullAcceleration)
        outputStream.write_unsigned_int(self.padding3)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()
        self.emitterNumber = inputStream.read_unsigned_byte()
        self.beamNumber = inputStream.read_unsigned_byte()
        self.stateIndicator = inputStream.read_unsigned_byte()
        self.padding2 = inputStream.read_unsigned_byte()
        self.azimuthOffset = inputStream.read_float()
        self.azimuthWidth = inputStream.read_float()
        self.azimuthPullRate = inputStream.read_float()
        self.azimuthPullAcceleration = inputStream.read_float()
        self.elevationOffset = inputStream.read_float()
        self.elevationWidth = inputStream.read_float()
        self.elevationPullRate = inputStream.read_float()
        self.elevationPullAcceleration = inputStream.read_float()
        self.padding3 = inputStream.read_unsigned_int()



class EntityAssociation( object ):
    """Association or disassociation of two entities.  Section 6.2.94.4.3"""

    def __init__(self,
                 changeIndicator=0,
                 associationStatus=0,
                 associationType=0,
                 entityID=None,
                 ownStationLocation=0,
                 physicalConnectionType=0,
                 groupMemberType=0,
                 groupNumber=0):
        """ Initializer for EntityAssociation"""
        self.recordType = 4
        """ the identification of the Variable Parameter record. Enumeration from EBV"""
        self.changeIndicator = changeIndicator
        """ Indicates if this VP has changed since last issuance"""
        self.associationStatus = associationStatus
        """ Indicates association status between two entities; 8 bit enum"""
        self.associationType = associationType
        """ Type of association; 8 bit enum"""
        self.entityID = entityID or EntityID()
        """ Object ID of entity associated with this entity"""
        self.ownStationLocation = ownStationLocation
        """ Station location on one's own entity. EBV doc."""
        self.physicalConnectionType = physicalConnectionType
        """ Type of physical connection. EBV doc"""
        self.groupMemberType = groupMemberType
        """ Type of member the entity is within th egroup"""
        self.groupNumber = groupNumber
        """ Group if any to which the entity belongs"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.recordType)
        outputStream.write_unsigned_byte(self.changeIndicator)
        outputStream.write_unsigned_byte(self.associationStatus)
        outputStream.write_unsigned_byte(self.associationType)
        self.entityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.ownStationLocation)
        outputStream.write_unsigned_byte(self.physicalConnectionType)
        outputStream.write_unsigned_byte(self.groupMemberType)
        outputStream.write_unsigned_short(self.groupNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_byte()
        self.changeIndicator = inputStream.read_unsigned_byte()
        self.associationStatus = inputStream.read_unsigned_byte()
        self.associationType = inputStream.read_unsigned_byte()
        self.entityID.parse(inputStream)
        self.ownStationLocation = inputStream.read_unsigned_short()
        self.physicalConnectionType = inputStream.read_unsigned_byte()
        self.groupMemberType = inputStream.read_unsigned_byte()
        self.groupNumber = inputStream.read_unsigned_short()



class VectoringNozzleSystem( object ):
    """Operational data for describing the vectoring nozzle systems Section 6.2.96"""

    def __init__(self,
                 horizontalDeflectionAngle=0.0,
                 verticalDeflectionAngle=0.0):
        """ Initializer for VectoringNozzleSystem"""
        self.horizontalDeflectionAngle = horizontalDeflectionAngle
        """ In degrees"""
        self.verticalDeflectionAngle = verticalDeflectionAngle
        """ In degrees"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.horizontalDeflectionAngle)
        outputStream.write_float(self.verticalDeflectionAngle)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.horizontalDeflectionAngle = inputStream.read_float()
        self.verticalDeflectionAngle = inputStream.read_float()



class FalseTargetsAttribute( object ):
    """The False Targets attribute record shall be used to communicate discrete values that are associated with false targets jamming that cannot be referenced to an emitter mode. The values provided in the False Targets attribute record shall be considered valid only for the victim radar beams listed in the jamming beam's Track/Jam Data records (provided in the associated Electromagnetic Emission PDU). Section 6.2.21.3"""

    def __init__(self,
                 emitterNumber=0,
                 beamNumber=0,
                 stateIndicator=0,
                 falseTargetCount=0,
                 walkSpeed=0.0,
                 walkAcceleration=0.0,
                 maximumWalkDistance=0.0,
                 keepTime=0.0,
                 echoSpacing=0.0):
        """ Initializer for FalseTargetsAttribute"""
        self.recordType = 3502
        self.recordLength = 48
        self.padding = 0
        self.emitterNumber = emitterNumber
        self.beamNumber = beamNumber
        self.stateIndicator = stateIndicator
        self.padding2 = 0
        self.falseTargetCount = falseTargetCount
        self.walkSpeed = walkSpeed
        self.walkAcceleration = walkAcceleration
        self.maximumWalkDistance = maximumWalkDistance
        self.keepTime = keepTime
        self.echoSpacing = echoSpacing

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_short(self.padding)
        outputStream.write_unsigned_byte(self.emitterNumber)
        outputStream.write_unsigned_byte(self.beamNumber)
        outputStream.write_unsigned_byte(self.stateIndicator)
        outputStream.write_unsigned_byte(self.padding2)
        outputStream.write_unsigned_short(self.falseTargetCount)
        outputStream.write_float(self.walkSpeed)
        outputStream.write_float(self.walkAcceleration)
        outputStream.write_float(self.maximumWalkDistance)
        outputStream.write_float(self.keepTime)
        outputStream.write_float(self.echoSpacing)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()
        self.emitterNumber = inputStream.read_unsigned_byte()
        self.beamNumber = inputStream.read_unsigned_byte()
        self.stateIndicator = inputStream.read_unsigned_byte()
        self.padding2 = inputStream.read_unsigned_byte()
        self.falseTargetCount = inputStream.read_unsigned_short()
        self.walkSpeed = inputStream.read_float()
        self.walkAcceleration = inputStream.read_float()
        self.maximumWalkDistance = inputStream.read_float()
        self.keepTime = inputStream.read_float()
        self.echoSpacing = inputStream.read_float()



class MinefieldIdentifier( object ):
    """The unique designation of a minefield Section 6.2.56 """

    def __init__(self, simulationAddress=None, minefieldNumber=0):
        """ Initializer for MinefieldIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """ """
        self.minefieldNumber = minefieldNumber
        """ """

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.minefieldNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.minefieldNumber = inputStream.read_unsigned_short()



class RadioType( object ):
    """Identifies the type of radio. Section 6.2.71"""

    def __init__(self,
                 entityKind=0,
                 domain=0,
                 country=0,
                 category=0,
                 subcategory=0,
                 specific=0,
                 extra=0):
        """ Initializer for RadioType"""
        self.entityKind = entityKind
        """ Kind of entity"""
        self.domain = domain
        """ Domain of entity (air, surface, subsurface, space, etc)"""
        self.country = country
        """ country to which the design of the entity is attributed"""
        self.category = category
        """ category of entity"""
        self.subcategory = subcategory
        """ specific info based on subcategory field"""
        self.specific = specific
        self.extra = extra

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.entityKind)
        outputStream.write_unsigned_byte(self.domain)
        outputStream.write_unsigned_short(self.country)
        outputStream.write_unsigned_byte(self.category)
        outputStream.write_unsigned_byte(self.subcategory)
        outputStream.write_unsigned_byte(self.specific)
        outputStream.write_unsigned_byte(self.extra)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.entityKind = inputStream.read_unsigned_byte()
        self.domain = inputStream.read_unsigned_byte()
        self.country = inputStream.read_unsigned_short()
        self.category = inputStream.read_unsigned_byte()
        self.subcategory = inputStream.read_unsigned_byte()
        self.specific = inputStream.read_unsigned_byte()
        self.extra = inputStream.read_unsigned_byte()



class NamedLocationIdentification( object ):
    """Information about the discrete positional relationship of the part entity with respect to the its host entity Section 6.2.62 """

    def __init__(self, stationName=0, stationNumber=0):
        """ Initializer for NamedLocationIdentification"""
        self.stationName = stationName
        """ the station name within the host at which the part entity is located. If the part entity is On Station, this field shall specify the representation of the parts location data fields. This field shall be specified by a 16-bit enumeration """
        self.stationNumber = stationNumber
        """ the number of the particular wing station, cargo hold etc., at which the part is attached. """

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.stationName)
        outputStream.write_unsigned_short(self.stationNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.stationName = inputStream.read_unsigned_short()
        self.stationNumber = inputStream.read_unsigned_short()



class FourByteChunk( object ):
    """32 bit piece of data"""

    def __init__(self):
        """ Initializer for FourByteChunk"""
        self.otherParameters =  [ 0, 0, 0, 0]
        """ four bytes of arbitrary data"""

    def serialize(self, outputStream):
        """serialize the class """
        for idx in range(0, 4):
            outputStream.write_byte( self.otherParameters[ idx ] )



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.otherParameters = [0]*4
        for idx in range(0, 4):
            val = inputStream.read_byte()

            self.otherParameters[  idx  ] = val




class ModulationParameters( object ):
    """Modulation parameters associated with a specific radio system. INCOMPLETE. 6.2.58 """

    def __init__(self):
        """ Initializer for ModulationParameters"""

    def serialize(self, outputStream):
        """serialize the class """


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""




class OneByteChunk( object ):
    """8 bit piece of data"""

    def __init__(self):
        """ Initializer for OneByteChunk"""
        self.otherParameters =  [ 0]
        """ one byte of arbitrary data"""

    def serialize(self, outputStream):
        """serialize the class """
        for idx in range(0, 1):
            outputStream.write_byte( self.otherParameters[ idx ] )



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.otherParameters = [0]*1
        for idx in range(0, 1):
            val = inputStream.read_byte()

            self.otherParameters[  idx  ] = val




class EulerAngles( object ):
    """Three floating point values representing an orientation, psi, theta, and phi, aka the euler angles, in radians. Section 6.2.33"""

    def __init__(self, psi=0.0, theta=0.0, phi=0.0):
        """ Initializer for EulerAngles"""
        self.psi = psi
        self.theta = theta
        self.phi = phi

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.psi)
        outputStream.write_float(self.theta)
        outputStream.write_float(self.phi)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.psi = inputStream.read_float()
        self.theta = inputStream.read_float()
        self.phi = inputStream.read_float()



class DirectedEnergyPrecisionAimpoint( object ):
    """DE Precision Aimpoint Record. Section 6.2.20.3"""

    def __init__(self,
                 targetSpotLocation=None,
                 targetSpotEntityLocation=None,
                 targetSpotVelocity=None,
                 targetSpotAcceleration=None,
                 targetEntityID=None,
                 targetComponentID=0,
                 beamSpotType=0,
                 beamSpotCrossSectionSemiMajorAxis=0.0,
                 beamSpotCrossSectionSemiMinorAxis=0.0,
                 beamSpotCrossSectionOrientationAngle=0.0,
                 peakIrradiance=0.0):
        """ Initializer for DirectedEnergyPrecisionAimpoint"""
        self.recordType = 4000
        """ Type of Record"""
        self.recordLength = 88
        """ Length of Record"""
        self.padding = 0
        """ Padding"""
        self.targetSpotLocation = targetSpotLocation or Vector3Double()
        """ Position of Target Spot in World Coordinates."""
        self.targetSpotEntityLocation = targetSpotEntityLocation or Vector3Float()
        """ Position (meters) of Target Spot relative to Entity Position."""
        self.targetSpotVelocity = targetSpotVelocity or Vector3Float()
        """ Velocity (meters/sec) of Target Spot."""
        self.targetSpotAcceleration = targetSpotAcceleration or Vector3Float()
        """ Acceleration (meters/sec/sec) of Target Spot."""
        self.targetEntityID = targetEntityID or EntityID()
        """ Unique ID of the target entity."""
        self.targetComponentID = targetComponentID
        """ Target Component ID ENUM, same as in DamageDescriptionRecord."""
        self.beamSpotType = beamSpotType
        """ Spot Shape ENUM."""
        self.beamSpotCrossSectionSemiMajorAxis = beamSpotCrossSectionSemiMajorAxis
        """ Beam Spot Cross Section Semi-Major Axis."""
        self.beamSpotCrossSectionSemiMinorAxis = beamSpotCrossSectionSemiMinorAxis
        """ Beam Spot Cross Section Semi-Major Axis."""
        self.beamSpotCrossSectionOrientationAngle = beamSpotCrossSectionOrientationAngle
        """ Beam Spot Cross Section Orientation Angle."""
        self.peakIrradiance = peakIrradiance
        """ Peak irradiance"""
        self.padding2 = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_short(self.padding)
        self.targetSpotLocation.serialize(outputStream)
        self.targetSpotEntityLocation.serialize(outputStream)
        self.targetSpotVelocity.serialize(outputStream)
        self.targetSpotAcceleration.serialize(outputStream)
        self.targetEntityID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.targetComponentID)
        outputStream.write_unsigned_byte(self.beamSpotType)
        outputStream.write_float(self.beamSpotCrossSectionSemiMajorAxis)
        outputStream.write_float(self.beamSpotCrossSectionSemiMinorAxis)
        outputStream.write_float(self.beamSpotCrossSectionOrientationAngle)
        outputStream.write_float(self.peakIrradiance)
        outputStream.write_unsigned_int(self.padding2)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()
        self.targetSpotLocation.parse(inputStream)
        self.targetSpotEntityLocation.parse(inputStream)
        self.targetSpotVelocity.parse(inputStream)
        self.targetSpotAcceleration.parse(inputStream)
        self.targetEntityID.parse(inputStream)
        self.targetComponentID = inputStream.read_unsigned_byte()
        self.beamSpotType = inputStream.read_unsigned_byte()
        self.beamSpotCrossSectionSemiMajorAxis = inputStream.read_float()
        self.beamSpotCrossSectionSemiMinorAxis = inputStream.read_float()
        self.beamSpotCrossSectionOrientationAngle = inputStream.read_float()
        self.peakIrradiance = inputStream.read_float()
        self.padding2 = inputStream.read_unsigned_int()



class IffDataSpecification( object ):
    """Requires hand coding to be useful. Section 6.2.43"""

    def __init__(self, numberOfIffDataRecords=0, iffDataRecords=None):
        """ Initializer for IffDataSpecification"""
        self.numberOfIffDataRecords = numberOfIffDataRecords
        """ Number of iff records"""
        self.iffDataRecords = iffDataRecords or []
        """ IFF data records"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short( len(self.iffDataRecords))
        for anObj in self.iffDataRecords:
            anObj.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.numberOfIffDataRecords = inputStream.read_unsigned_short()
        for idx in range(0, self.numberOfIffDataRecords):
            element = IFFData()
            element.parse(inputStream)
            self.iffDataRecords.append(element)




class OwnershipStatus( object ):
    """used to convey entity and conflict status information associated with transferring ownership of an entity. Section 6.2.65"""

    def __init__(self, entityId=None, ownershipStatus=0):
        """ Initializer for OwnershipStatus"""
        self.entityId = entityId or EntityID()
        """ EntityID"""
        self.ownershipStatus = ownershipStatus
        """ The ownership and/or ownership conflict status of the entity represented by the Entity ID field."""
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        self.entityId.serialize(outputStream)
        outputStream.write_unsigned_byte(self.ownershipStatus)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.entityId.parse(inputStream)
        self.ownershipStatus = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class BeamAntennaPattern( object ):
    """Used when the antenna pattern type field has a value of 1. Specifies the direction, pattern, and polarization of radiation from an antenna. Section 6.2.9.2"""

    def __init__(self,
                 beamDirection=None,
                 azimuthBeamwidth=0.0,
                 elevationBeamwidth=0.0,
                 referenceSystem=0,
                 ez=0.0,
                 ex=0.0,
                 phase=0.0):
        """ Initializer for BeamAntennaPattern"""
        self.beamDirection = EulerAngles()
        """ The rotation that transforms the reference coordinate sytem into the beam coordinate system. Either world coordinates or entity coordinates may be used as the reference coordinate system, as specified by the reference system field of the antenna pattern record."""
        self.azimuthBeamwidth = azimuthBeamwidth
        self.elevationBeamwidth = elevationBeamwidth
        self.referenceSystem = referenceSystem
        self.padding1 = 0
        self.padding2 = 0
        self.ez = ez
        """ This field shall specify the magnitude of the Z-component (in beam coordinates) of the Electrical field at some arbitrary single point in the main beam and in the far field of the antenna. """
        self.ex = ex
        """ This field shall specify the magnitude of the X-component (in beam coordinates) of the Electrical field at some arbitrary single point in the main beam and in the far field of the antenna."""
        self.phase = phase
        """ This field shall specify the phase angle between EZ and EX in radians. If fully omni-directional antenna is modeled using beam pattern type one, the omni-directional antenna shall be represented by beam direction Euler angles psi, theta, and phi of zero, an azimuth beamwidth of 2PI, and an elevation beamwidth of PI"""
        self.padding3 = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        self.beamDirection.serialize(outputStream)
        outputStream.write_float(self.azimuthBeamwidth)
        outputStream.write_float(self.elevationBeamwidth)
        outputStream.write_unsigned_byte(self.referenceSystem)
        outputStream.write_unsigned_byte(self.padding1)
        outputStream.write_unsigned_short(self.padding2)
        outputStream.write_float(self.ez)
        outputStream.write_float(self.ex)
        outputStream.write_float(self.phase)
        outputStream.write_unsigned_int(self.padding3)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.beamDirection.parse(inputStream)
        self.azimuthBeamwidth = inputStream.read_float()
        self.elevationBeamwidth = inputStream.read_float()
        self.referenceSystem = inputStream.read_unsigned_byte()
        self.padding1 = inputStream.read_unsigned_byte()
        self.padding2 = inputStream.read_unsigned_short()
        self.ez = inputStream.read_float()
        self.ex = inputStream.read_float()
        self.phase = inputStream.read_float()
        self.padding3 = inputStream.read_unsigned_int()



class AttachedParts( object ):
    """Removable parts that may be attached to an entity.  Section 6.2.93.3"""

    def __init__(self,
                 detachedIndicator=0,
                 partAttachedTo=0,
                 parameterType=0,
                 parameterValue=0):
        """ Initializer for AttachedParts"""
        self.recordType = 1
        """ the identification of the Variable Parameter record. Enumeration from EBV"""
        self.detachedIndicator = detachedIndicator
        """ 0 = attached, 1 = detached. See I.2.3.1 for state transition diagram"""
        self.partAttachedTo = partAttachedTo
        """ the identification of the articulated part to which this articulation parameter is attached. This field shall be specified by a 16-bit unsigned integer. This field shall contain the value zero if the articulated part is attached directly to the entity."""
        self.parameterType = parameterType
        """ The location or station to which the part is attached"""
        self.parameterValue = parameterValue
        """ The definition of the 64 bits shall be determined based on the type of parameter specified in the Parameter Type field """

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.recordType)
        outputStream.write_unsigned_byte(self.detachedIndicator)
        outputStream.write_unsigned_short(self.partAttachedTo)
        outputStream.write_unsigned_int(self.parameterType)
        outputStream.write_long(self.parameterValue)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_byte()
        self.detachedIndicator = inputStream.read_unsigned_byte()
        self.partAttachedTo = inputStream.read_unsigned_short()
        self.parameterType = inputStream.read_unsigned_int()
        self.parameterValue = inputStream.read_long()



class VariableTransmitterParameters( object ):
    """Relates to radios. NOT COMPLETE. Section 6.2.94"""

    def __init__(self, recordType=0, recordLength=4):
        """ Initializer for VariableTransmitterParameters"""
        self.recordType = recordType
        """ Type of VTP. Enumeration from EBV"""
        self.recordLength = recordLength
        """ Length, in bytes"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_int(self.recordLength)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_int()



class Attribute( object ):
    """Used to convey information for one or more attributes. Attributes conform to the standard variable record format of 6.2.82. Section 6.2.10. NOT COMPLETE"""

    def __init__(self, recordType=0, recordLength=0, recordSpecificFields=0):
        """ Initializer for Attribute"""
        self.recordType = recordType
        self.recordLength = recordLength
        self.recordSpecificFields = recordSpecificFields

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_long(self.recordSpecificFields)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.recordSpecificFields = inputStream.read_long()



class RecordQuerySpecification( object ):
    """The identification of the records being queried 6.2.72"""

    def __init__(self, numberOfRecords=0, records=None):
        """ Initializer for RecordQuerySpecification"""
        self.numberOfRecords = numberOfRecords
        self.records = records or []
        """ variable length list of 32 bit records"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int( len(self.records))
        for anObj in self.records:
            outputstream.write_unsigned_int(anObj)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.numberOfRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfRecords):
            val = inputstream.read_unsigned_int()
            self.records.append(val)



class ArticulatedParts( object ):
    """ articulated parts for movable parts and a combination of moveable/attached parts of an entity. Section 6.2.94.2"""

    def __init__(self,
                 recordType=0,
                 changeIndicator=0,
                 partAttachedTo=0,
                 parameterType=0,
                 parameterValue=0):
        """ Initializer for ArticulatedParts"""
        self.recordType = recordType
        """ the identification of the Variable Parameter record. Enumeration from EBV"""
        self.changeIndicator = changeIndicator
        """ indicate the change of any parameter for any articulated part. Starts at zero, incremented for each change """
        self.partAttachedTo = partAttachedTo
        """ the identification of the articulated part to which this articulation parameter is attached. This field shall be specified by a 16-bit unsigned integer. This field shall contain the value zero if the articulated part is attached directly to the entity."""
        self.parameterType = parameterType
        """ the type of parameter represented, 32 bit enumeration"""
        self.parameterValue = parameterValue
        """ The definition of the 64 bits shall be determined based on the type of parameter specified in the Parameter Type field """

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.recordType)
        outputStream.write_unsigned_byte(self.changeIndicator)
        outputStream.write_unsigned_short(self.partAttachedTo)
        outputStream.write_unsigned_int(self.parameterType)
        outputStream.write_long(self.parameterValue)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_byte()
        self.changeIndicator = inputStream.read_unsigned_byte()
        self.partAttachedTo = inputStream.read_unsigned_short()
        self.parameterType = inputStream.read_unsigned_int()
        self.parameterValue = inputStream.read_long()



class ObjectType( object ):
    """The unique designation of an environmental object. Section 6.2.64"""

    def __init__(self,
                 domain=0,
                 objectKind=0,
                 category=0,
                 subcategory=0):
        """ Initializer for ObjectType"""
        self.domain = domain
        """ Domain of entity (air, surface, subsurface, space, etc)"""
        self.objectKind = objectKind
        """ country to which the design of the entity is attributed"""
        self.category = category
        """ category of entity"""
        self.subcategory = subcategory
        """ subcategory of entity"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.domain)
        outputStream.write_unsigned_byte(self.objectKind)
        outputStream.write_unsigned_byte(self.category)
        outputStream.write_unsigned_byte(self.subcategory)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.domain = inputStream.read_unsigned_byte()
        self.objectKind = inputStream.read_unsigned_byte()
        self.category = inputStream.read_unsigned_byte()
        self.subcategory = inputStream.read_unsigned_byte()



class Association( object ):
    """An entity's associations with other entities and/or locations. For each association, this record shall specify the type of the association, the associated entity's EntityID and/or the associated location's world coordinates. This record may be used (optionally) in a transfer transaction to send internal state data from the divesting simulation to the acquiring simulation (see 5.9.4). This record may also be used for other purposes. Section 6.2.9"""

    def __init__(self,
                 associationType=0,
                 associatedEntityID=None,
                 associatedLocation=None):
        """ Initializer for Association"""
        self.associationType = associationType
        self.padding4 = 0
        self.associatedEntityID = associatedEntityID or EntityID()
        """ identity of associated entity. If none, NO_SPECIFIC_ENTITY"""
        self.associatedLocation = associatedLocation or Vector3Double()
        """ location, in world coordinates"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.associationType)
        outputStream.write_unsigned_byte(self.padding4)
        self.associatedEntityID.serialize(outputStream)
        self.associatedLocation.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.associationType = inputStream.read_unsigned_byte()
        self.padding4 = inputStream.read_unsigned_byte()
        self.associatedEntityID.parse(inputStream)
        self.associatedLocation.parse(inputStream)



class RecordSpecificationElement( object ):
    """Synthetic record, made up from section 6.2.72. This is used to acheive a repeating variable list element."""

    def __init__(self,
                 recordID=0,
                 recordSetSerialNumber=0,
                 recordLength=0,
                 recordCount=0,
                 recordValues=0):
        """ Initializer for RecordSpecificationElement"""
        self.recordID = recordID
        """ the data structure used to convey the parameter values of the record for each record. 32 bit enumeration."""
        self.recordSetSerialNumber = recordSetSerialNumber
        """ the serial number of the first record in the block of records"""
        self.recordLength = recordLength
        """  the length, in bits, of the record. Note, bits, not bytes."""
        self.recordCount = recordCount
        """  the number of records included in the record set """
        self.recordValues = recordValues
        """ the concatenated records of the format specified by the Record ID field. The length of this field is the Record Length multiplied by the Record Count, in units of bits. ^^^This is wrong--variable sized data records, bit values. THis MUST be patched after generation."""
        self.pad4 = 0
        """ Padding of 0 to 31 unused bits as required for 32-bit alignment of the Record Set field. ^^^This is wrong--variable sized padding. MUST be patched post-code generation"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordID)
        outputStream.write_unsigned_int(self.recordSetSerialNumber)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_short(self.recordCount)
        outputStream.write_unsigned_short(self.recordValues)
        outputStream.write_unsigned_byte(self.pad4)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordID = inputStream.read_unsigned_int()
        self.recordSetSerialNumber = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.recordCount = inputStream.read_unsigned_short()
        self.recordValues = inputStream.read_unsigned_short()
        self.pad4 = inputStream.read_unsigned_byte()



class EightByteChunk( object ):
    """64 bit piece of data"""

    def __init__(self):
        """ Initializer for EightByteChunk"""
        self.otherParameters =  [ 0, 0, 0, 0, 0, 0, 0, 0]
        """ Eight bytes of arbitrary data"""

    def serialize(self, outputStream):
        """serialize the class """
        for idx in range(0, 8):
            outputStream.write_byte( self.otherParameters[ idx ] )



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.otherParameters = [0] * 8
        for idx in range(0, 8):
            val = inputStream.read_byte()

            self.otherParameters[  idx  ] = val




class AntennaLocation( object ):
    """Location of the radiating portion of the antenna, specified in world coordinates and entity coordinates. Section 6.2.8"""

    def __init__(self,
                 antennaLocation=None,
                 relativeAntennaLocation=None):
        """ Initializer for AntennaLocation"""
        self.antennaLocation = antennaLocation or Vector3Double()
        """ Location of the radiating portion of the antenna in world coordinates"""
        self.relativeAntennaLocation = relativeAntennaLocation or Vector3Float()
        """ Location of the radiating portion of the antenna in entity coordinates"""

    def serialize(self, outputStream):
        """serialize the class """
        self.antennaLocation.serialize(outputStream)
        self.relativeAntennaLocation.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.antennaLocation.parse(inputStream)
        self.relativeAntennaLocation.parse(inputStream)



class ObjectIdentifier( object ):
    """The unique designation of an environmental object. Section 6.2.63"""

    def __init__(self, simulationAddress=None, objectNumber=0):
        """ Initializer for ObjectIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """  Simulation Address"""
        self.objectNumber = objectNumber
        """ object number"""

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.objectNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.objectNumber = inputStream.read_unsigned_short()



class AggregateIdentifier( object ):
    """The unique designation of each aggrgate in an exercise is specified by an aggregate identifier record. The aggregate ID is not an entity and shall not be treated as such. Section 6.2.3."""

    def __init__(self, simulationAddress=None, aggregateID=0):
        """ Initializer for AggregateIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """ Simulation address, ie site and application, the first two fields of the entity ID"""
        self.aggregateID = aggregateID
        """ the aggregate ID"""

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.aggregateID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.aggregateID = inputStream.read_unsigned_short()



class FixedDatum( object ):
    """Fixed Datum Record. Section 6.2.38"""

    def __init__(self,
                 fixedDatumID=0,
                 fixedDatumValue=0):
        """ Initializer for FixedDatum"""
        self.fixedDatumID = fixedDatumID
        """ ID of the fixed datum, an enumeration"""
        self.fixedDatumValue = fixedDatumValue
        """ Value for the fixed datum"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.fixedDatumID)
        outputStream.write_unsigned_int(self.fixedDatumValue)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.fixedDatumID = inputStream.read_unsigned_int()
        self.fixedDatumValue = inputStream.read_unsigned_int()



class VariableParameter( object ):
    """specification of additional information associated with an entity or detonation, not otherwise accounted for in a PDU 6.2.94.1"""

    def __init__(self,
                 recordType=0,
                 variableParameterFields1=0,
                 variableParameterFields2=0,
                 variableParameterFields3=0,
                 variableParameterFields4=0):
        """ Initializer for VariableParameter"""
        self.recordType = recordType
        """ the identification of the Variable Parameter record. Enumeration from EBV"""
        self.variableParameterFields1 = variableParameterFields1
        """ Variable parameter data fields. Two doubles minus one byte"""
        self.variableParameterFields2 = variableParameterFields2
        """ Variable parameter data fields. """
        self.variableParameterFields3 = variableParameterFields3
        """ Variable parameter data fields. """
        self.variableParameterFields4 = variableParameterFields4
        """ Variable parameter data fields. """

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.recordType)
        outputStream.write_double(self.variableParameterFields1)
        outputStream.write_unsigned_int(self.variableParameterFields2)
        outputStream.write_unsigned_short(self.variableParameterFields3)
        outputStream.write_unsigned_byte(self.variableParameterFields4)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_byte()
        self.variableParameterFields1 = inputStream.read_double()
        self.variableParameterFields2 = inputStream.read_unsigned_int()
        self.variableParameterFields3 = inputStream.read_unsigned_short()
        self.variableParameterFields4 = inputStream.read_unsigned_byte()



class ChangeOptions( object ):
    """This is wrong and breaks serialization. See section 6.2.13 aka B.2.41"""

    def __init__(self):
        """ Initializer for ChangeOptions"""

    def serialize(self, outputStream):
        """serialize the class """


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""




class LiveSimulationAddress( object ):
    """A simulation's designation associated with all Live Entity IDs contained in Live Entity PDUs. Section 6.2.55 """

    def __init__(self, liveSiteNumber=0, liveApplicationNumber=0):
        """ Initializer for LiveSimulationAddress"""
        self.liveSiteNumber = liveSiteNumber
        """ facility, installation, organizational unit or geographic location may have multiple sites associated with it. The Site Number is the first component of the Live Simulation Address, which defines a live simulation."""
        self.liveApplicationNumber = liveApplicationNumber
        """ An application associated with a live site is termed a live application. Each live application participating in an event """

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.liveSiteNumber)
        outputStream.write_unsigned_byte(self.liveApplicationNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.liveSiteNumber = inputStream.read_unsigned_byte()
        self.liveApplicationNumber = inputStream.read_unsigned_byte()



class EntityMarking( object ):
    """Specifies the character set used inthe first byte, followed by 11 characters of text data. Section 6.29"""

    def __init__(self, characterSet=0, characters=None):
        """ Initializer for EntityMarking"""
        self.characterSet = characterSet
        """ The character set"""
        self.characters =  characters or [0] * 11
        """ The characters"""

    def setString(self, new_str):
        for idx in range(0, 11):
          if idx < len(new_str):
            self.characters[idx] = ord(new_str[idx])
          else: 
            self.characters[idx] = 0

    # convenience method to return the marking as a string, truncated of padding.
    def charactersString(self):
        return bytes(filter(None, self.characters)).decode("utf-8")

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.characterSet)
        for idx in range(0, 11):
            outputStream.write_byte( self.characters[ idx ] )



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.characterSet = inputStream.read_unsigned_byte()
        self.characters = [0]*11
        for idx in range(0, 11):
            val = inputStream.read_byte()

            self.characters[  idx  ] = val




class UAFundamentalParameter( object ):
    """Regeneration parameters for active emission systems that are variable throughout a scenario. Section 6.2.91"""

    def __init__(self,
                 activeEmissionParameterIndex=0,
                 scanPattern=0,
                 beamCenterAzimuthHorizontal=0.0,
                 azimuthBeamwidthHorizontal=0.0,
                 beamCenterDepressionElevation=0.0,
                 beamwidthDownElevation=0.0):
        """ Initializer for UAFundamentalParameter"""
        self.activeEmissionParameterIndex = activeEmissionParameterIndex
        """ Which database record shall be used. An enumeration from EBV document"""
        self.scanPattern = scanPattern
        """ The type of scan pattern, If not used, zero. An enumeration from EBV document"""
        self.beamCenterAzimuthHorizontal = beamCenterAzimuthHorizontal
        """ center azimuth bearing of th emain beam. In radians."""
        self.azimuthalBeamwidthHorizontal = azimuthBeamwidthHorizontal
        """ Horizontal beamwidth of the main beam measured at the 3dB down point of peak radiated power. In radians."""
        self.beamCenterDepressionElevation = beamCenterDepressionElevation
        """ center of the d/e angle of th emain beam relative to the stablised de angle of the target. In radians."""
        self.beamwidthDownElevation = beamwidthDownElevation
        """ vertical beamwidth of the main beam. Measured at the 3dB down point of peak radiated power. In radians."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.activeEmissionParameterIndex)
        outputStream.write_unsigned_short(self.scanPattern)
        outputStream.write_float(self.beamCenterAzimuthHorizontal)
        outputStream.write_float(self.azimuthalBeamwidthHorizontal)
        outputStream.write_float(self.beamCenterDepressionElevation)
        outputStream.write_float(self.beamwidthDownElevation)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.activeEmissionParameterIndex = inputStream.read_unsigned_short()
        self.scanPattern = inputStream.read_unsigned_short()
        self.beamCenterAzimuthHorizontal = inputStream.read_float()
        self.azimuthalBeamwidthHorizontal = inputStream.read_float()
        self.beamCenterDepressionElevation = inputStream.read_float()
        self.beamwidthDownElevation = inputStream.read_float()



class TwoByteChunk( object ):
    """16 bit piece of data"""

    def __init__(self):
        """ Initializer for TwoByteChunk"""
        self.otherParameters =  [ 0, 0]
        """ two bytes of arbitrary data"""

    def serialize(self, outputStream):
        """serialize the class """
        for idx in range(0, 2):
            outputStream.write_byte( self.otherParameters[ idx ] )



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.otherParameters = [0]*2
        for idx in range(0, 2):
            val = inputStream.read_byte()

            self.otherParameters[  idx  ] = val




class DirectedEnergyDamage( object ):
    """Damage sustained by an entity due to directed energy. Location of the damage based on a relative x,y,z location from the center of the entity. Section 6.2.15.2"""

    def __init__(self,
                 damageLocation=None,
                 damageDiameter=0,
                 temperature=-273.15,
                 componentIdentification=0,
                 componentDamageStatus=0,
                 componentVisualDamageStatus=0,
                 componentVisualSmokeColor=0,
                 fireEventID=None):
        """ Initializer for DirectedEnergyDamage"""
        self.recordType = 4500
        """ DE Record Type."""
        self.recordLength = 40
        """ DE Record Length (bytes)."""
        self.padding = 0
        """ padding."""
        self.damageLocation = damageLocation or Vector3Float()
        """ location of damage, relative to center of entity"""
        self.damageDiameter = damageDiameter
        """ Size of damaged area, in meters."""
        self.temperature = temperature
        """ average temp of the damaged area, in degrees celsius. If firing entitty does not model this, use a value of -273.15"""
        self.componentIdentification = componentIdentification
        """ enumeration"""
        self.componentDamageStatus = componentDamageStatus
        """ enumeration"""
        self.componentVisualDamageStatus = componentVisualDamageStatus
        """ enumeration"""
        self.componentVisualSmokeColor = componentVisualSmokeColor
        """ enumeration"""
        self.fireEventID = fireEventID or EventIdentifier()
        """ For any component damage resulting this field shall be set to the fire event ID from that PDU."""
        self.padding2 = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_short(self.padding)
        self.damageLocation.serialize(outputStream)
        outputStream.write_float(self.damageDiameter)
        outputStream.write_float(self.temperature)
        outputStream.write_unsigned_byte(self.componentIdentification)
        outputStream.write_unsigned_byte(self.componentDamageStatus)
        outputStream.write_unsigned_byte(self.componentVisualDamageStatus)
        outputStream.write_unsigned_byte(self.componentVisualSmokeColor)
        self.fireEventID.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding2)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()
        self.damageLocation.parse(inputStream)
        self.damageDiameter = inputStream.read_float()
        self.temperature = inputStream.read_float()
        self.componentIdentification = inputStream.read_unsigned_byte()
        self.componentDamageStatus = inputStream.read_unsigned_byte()
        self.componentVisualDamageStatus = inputStream.read_unsigned_byte()
        self.componentVisualSmokeColor = inputStream.read_unsigned_byte()
        self.fireEventID.parse(inputStream)
        self.padding2 = inputStream.read_unsigned_short()



class ExplosionDescriptor( object ):
    """Explosion of a non-munition. Section 6.2.19.3"""

    def __init__(self,
                 explodingObject=None,
                 explosiveMaterial=0,
                 explosiveForce=0.0):
        """ Initializer for ExplosionDescriptor"""
        self.explodingObject = explodingObject or EntityType()
        """ Type of the object that exploded. See 6.2.30"""
        self.explosiveMaterial = explosiveMaterial
        """ Material that exploded. Can be grain dust, tnt, gasoline, etc. Enumeration"""
        self.padding = 0
        """ padding"""
        self.explosiveForce = explosiveForce
        """ Force of explosion, in equivalent KG of TNT"""

    def serialize(self, outputStream):
        """serialize the class """
        self.explodingObject.serialize(outputStream)
        outputStream.write_unsigned_short(self.explosiveMaterial)
        outputStream.write_unsigned_short(self.padding)
        outputStream.write_float(self.explosiveForce)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.explodingObject.parse(inputStream)
        self.explosiveMaterial = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()
        self.explosiveForce = inputStream.read_float()



class ClockTime( object ):
    """Time measurements that exceed one hour are represented by this record. The first field is the hours since the unix epoch (Jan 1 1970, used by most Unix systems and java) and the second field the timestamp units since the top of the hour. Section 6.2.14"""

    def __init__(self, hour=0, timePastHour=0):
        """ Initializer for ClockTime"""
        self.hour = hour
        """ Hours in UTC"""
        self.timePastHour = timePastHour
        """ Time past the hour"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.hour)
        outputStream.write_unsigned_int(self.timePastHour)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.hour = inputStream.read_unsigned_int()
        self.timePastHour = inputStream.read_unsigned_int()



class SecondaryOperationalData( object ):
    """Additional operational data for an IFF emitting system and the number of IFF Fundamental Parameter Data records Section 6.2.76."""

    def __init__(self,
                 operationalData1=0,
                 operationalData2=0,
                 numberOfIFFFundamentalParameterRecords=0):
        """ Initializer for SecondaryOperationalData"""
        self.operationalData1 = operationalData1
        """ additional operational characteristics of the IFF emitting system. Each 8-bit field will vary depending on the system type."""
        self.operationalData2 = operationalData2
        """ additional operational characteristics of the IFF emitting system. Each 8-bit field will vary depending on the system type."""
        self.numberOfIFFFundamentalParameterRecords = numberOfIFFFundamentalParameterRecords
        """ the number of IFF Fundamental Parameter Data records that follow"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.operationalData1)
        outputStream.write_unsigned_byte(self.operationalData2)
        outputStream.write_unsigned_short(self.numberOfIFFFundamentalParameterRecords)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.operationalData1 = inputStream.read_unsigned_byte()
        self.operationalData2 = inputStream.read_unsigned_byte()
        self.numberOfIFFFundamentalParameterRecords = inputStream.read_unsigned_short()



class EnvironmentType( object ):
    """Description of environmental data in environmental process and gridded data PDUs. Section 6.2.32"""

    def __init__(self,
                 entityKind=0,
                 domain=0,
                 entityClass=0,
                 category=0,
                 subcategory=0,
                 specific=0,
                 extra=0):
        """ Initializer for EnvironmentType"""
        self.entityKind = entityKind
        """ Kind of entity"""
        self.domain = domain
        """ Domain of entity (air, surface, subsurface, space, etc)"""
        self.entityClass = entityClass
        """ class of environmental entity"""
        self.category = category
        """ category of entity"""
        self.subcategory = subcategory
        """ subcategory of entity"""
        self.specific = specific
        """ specific info based on subcategory field"""
        self.extra = extra

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.entityKind)
        outputStream.write_unsigned_byte(self.domain)
        outputStream.write_unsigned_short(self.entityClass)
        outputStream.write_unsigned_byte(self.category)
        outputStream.write_unsigned_byte(self.subcategory)
        outputStream.write_unsigned_byte(self.specific)
        outputStream.write_unsigned_byte(self.extra)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.entityKind = inputStream.read_unsigned_byte()
        self.domain = inputStream.read_unsigned_byte()
        self.entityClass = inputStream.read_unsigned_short()
        self.category = inputStream.read_unsigned_byte()
        self.subcategory = inputStream.read_unsigned_byte()
        self.specific = inputStream.read_unsigned_byte()
        self.extra = inputStream.read_unsigned_byte()



class TotalRecordSets( object ):
    """Total number of record sets contained in a logical set of one or more PDUs. Used to transfer ownership, etc Section 6.2.88"""

    def __init__(self, totalRecordSets=0):
        """ Initializer for TotalRecordSets"""
        self.totalRecordSets = totalRecordSets
        """ Total number of record sets"""
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.totalRecordSets)
        outputStream.write_unsigned_short(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.totalRecordSets = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()



class MineEntityIdentifier( object ):
    """The unique designation of a mine contained in the Minefield Data PDU. No espdus are issued for mine entities.  Section 6.2.55 """

    def __init__(self, simulationAddress=None, mineEntityNumber=0):
        """ Initializer for MineEntityIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """ """
        self.mineEntityNumber = mineEntityNumber
        """ """

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.mineEntityNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.mineEntityNumber = inputStream.read_unsigned_short()



class Relationship( object ):
    """The relationship of the part entity to its host entity. Section 6.2.74."""

    def __init__(self, nature=0, position=0):
        """ Initializer for Relationship"""
        self.nature = nature
        """ the nature or purpose for joining of the part entity to the host entity and shall be represented by a 16-bit enumeration"""
        self.position = position
        """ the position of the part entity with respect to the host entity and shall be represented by a 16-bit enumeration"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.nature)
        outputStream.write_unsigned_short(self.position)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.nature = inputStream.read_unsigned_short()
        self.position = inputStream.read_unsigned_short()



class EEFundamentalParameterData( object ):
    """Contains electromagnetic emmission regeneration parameters that are variable throught a scenario. Section 6.2.22."""

    def __init__(self,
                 frequency=0.0,
                 frequencyRange=0,
                 effectiveRadiatedPower=0,
                 pulseRepetitionFrequency=0.0,
                 pulseWidth=0.0,
                 beamAzimuthCenter=0.0,
                 beamAzimuthSweep=0.0,
                 beamElevationCenter=0.0,
                 beamElevationSweep=0.0,
                 beamSweepSync=0.0):
        """ Initializer for EEFundamentalParameterData"""
        self.frequency = frequency
        """ center frequency of the emission in hertz."""
        self.frequencyRange = frequencyRange
        """ Bandwidth of the frequencies corresponding to the fequency field."""
        self.effectiveRadiatedPower = effectiveRadiatedPower
        """ Effective radiated power for the emission in DdBm. For a radar noise jammer, indicates the peak of the transmitted power."""
        self.pulseRepetitionFrequency = pulseRepetitionFrequency
        """ Average repetition frequency of the emission in hertz."""
        self.pulseWidth = pulseWidth
        """ Average pulse width  of the emission in microseconds."""
        self.beamAzimuthCenter = beamAzimuthCenter
        self.beamAzimuthSweep = beamAzimuthSweep
        self.beamElevationCenter = beamElevationCenter
        self.beamElevationSweep = beamElevationSweep
        self.beamSweepSync = beamSweepSync

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.frequency)
        outputStream.write_float(self.frequencyRange)
        outputStream.write_float(self.effectiveRadiatedPower)
        outputStream.write_float(self.pulseRepetitionFrequency)
        outputStream.write_float(self.pulseWidth)
        outputStream.write_float(self.beamAzimuthCenter)
        outputStream.write_float(self.beamAzimuthSweep)
        outputStream.write_float(self.beamElevationCenter)
        outputStream.write_float(self.beamElevationSweep)
        outputStream.write_float(self.beamSweepSync)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.frequency = inputStream.read_float()
        self.frequencyRange = inputStream.read_float()
        self.effectiveRadiatedPower = inputStream.read_float()
        self.pulseRepetitionFrequency = inputStream.read_float()
        self.pulseWidth = inputStream.read_float()
        self.beamAzimuthCenter = inputStream.read_float()
        self.beamAzimuthSweep = inputStream.read_float()
        self.beamElevationCenter = inputStream.read_float()
        self.beamElevationSweep = inputStream.read_float()
        self.beamSweepSync = inputStream.read_float()


class JammingTechnique( object ):
    """Jamming technique. Section 6.2.49"""

    def __init__(self, kind=0, category=0, subcategory=0, specific=0):
        """ Initializer for JammingTechnique"""
        self.kind = kind
        self.category = category
        self.subcategory = subcategory
        self.specific = specific

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.kind)
        outputStream.write_unsigned_byte(self.category)
        outputStream.write_unsigned_byte(self.subcategory)
        outputStream.write_unsigned_byte(self.specific)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.kind = inputStream.read_unsigned_byte()
        self.category = inputStream.read_unsigned_byte()
        self.subcategory = inputStream.read_unsigned_byte()
        self.specific = inputStream.read_unsigned_byte()



class DatumSpecification( object ):
    """List of fixed and variable datum records. Section 6.2.18 """

    def __init__(self,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for DatumSpecification"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Number of fixed datums"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ Number of variable datums"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ variable length list fixed datums"""
        self.variableDatumRecords = variableDatumRecords or []
        """ variable length list variable datums"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class DirectedEnergyAreaAimpoint( object ):
    """DE Precision Aimpoint Record. NOT COMPLETE. Section 6.2.20.2"""

    def __init__(self,
                 recordLength=0,
                 beamAntennaPatternRecordCount=0,
                 directedEnergyTargetEnergyDepositionRecordCount=0,
                 beamAntennaParameterList=None,
                 directedEnergyTargetEnergyDepositionList=None):
        """ Initializer for DirectedEnergyAreaAimpoint"""
        self.recordType = 4001
        """ Type of Record enumeration"""
        self.recordLength = recordLength
        """ Length of Record"""
        self.padding = 0
        """ Padding"""
        self.beamAntennaPatternRecordCount = beamAntennaPatternRecordCount
        """ Number of beam antenna pattern records"""
        self.directedEnergyTargetEnergyDepositionRecordCount = directedEnergyTargetEnergyDepositionRecordCount
        """ Number of DE target energy depositon records"""
        self.beamAntennaParameterList = beamAntennaParameterList or []
        """ list of beam antenna records. See 6.2.9.2"""
        self.directedEnergyTargetEnergyDepositionRecordList = directedEnergyTargetEnergyDepositionList or []
        """ list of DE target deposition records. See 6.2.21.4"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_short(self.padding)
        outputStream.write_unsigned_short( len(self.beamAntennaParameterList))
        outputStream.write_unsigned_short( len(self.directedEnergyTargetEnergyDepositionRecordList))
        for anObj in self.beamAntennaParameterList:
            anObj.serialize(outputStream)

        for anObj in self.directedEnergyTargetEnergyDepositionRecordList:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()
        self.beamAntennaPatternRecordCount = inputStream.read_unsigned_short()
        self.directedEnergyTargetEnergyDepositionRecordCount = inputStream.read_unsigned_short()
        for idx in range(0, self.beamAntennaPatternRecordCount):
            element = null()
            element.parse(inputStream)
            self.beamAntennaParameterList.append(element)

        for idx in range(0, self.directedEnergyTargetEnergyDepositionRecordCount):
            element = null()
            element.parse(inputStream)
            self.directedEnergyTargetEnergyDepositionRecordList.append(element)




class Vector3Float( object ):
    """Three floating point values, x, y, and z. Section 6.2.95"""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """ Initializer for Vector3Float"""
        self.x = x
        """ X value"""
        self.y = y
        """ y Value"""
        self.z = z
        """ Z value"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.x)
        outputStream.write_float(self.y)
        outputStream.write_float(self.z)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.x = inputStream.read_float()
        self.y = inputStream.read_float()
        self.z = inputStream.read_float()



class Expendable( object ):
    """An entity's expendable (chaff, flares, etc) information. Section 6.2.36"""

    def __init__(self,
                 expendable=None,
                 station=0,
                 quantity=0,
                 expendableStatus=0):
        """ Initializer for Expendable"""
        self.expendable = expendable or EntityType()
        """ Type of expendable"""
        self.station = station
        self.quantity = quantity
        self.expendableStatus = expendableStatus
        self.padding = 0

    def serialize(self, outputStream):
        """serialize the class """
        self.expendable.serialize(outputStream)
        outputStream.write_unsigned_int(self.station)
        outputStream.write_unsigned_short(self.quantity)
        outputStream.write_unsigned_byte(self.expendableStatus)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.expendable.parse(inputStream)
        self.station = inputStream.read_unsigned_int()
        self.quantity = inputStream.read_unsigned_short()
        self.expendableStatus = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class IOCommunicationsNode( object ):
    """A communications node that is part of a simulted communcations network. Section 6.2.49.2"""

    def __init__(self,
                 communicationsNodeType=0,
                 communicationsNodeID=None):
        """ Initializer for IOCommunicationsNode"""
        self.recordType = 5501
        self.recordLength = 16
        self.communcationsNodeType = communicationsNodeType
        self.padding = 0
        self.communicationsNodeID = communicationsNodeID or CommunicationsNodeID()

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_byte(self.communcationsNodeType)
        outputStream.write_unsigned_byte(self.padding)
        self.communicationsNodeID.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.communcationsNodeType = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()
        self.communicationsNodeID.parse(inputStream)



class ModulationType( object ):
    """Information about the type of modulation used for radio transmission. 6.2.59 """

    def __init__(self,
                 spreadSpectrum=0,
                 majorModulation=0,
                 detail=0,
                 radioSystem=0):
        """ Initializer for ModulationType"""
        self.spreadSpectrum = spreadSpectrum
        """ This field shall indicate the spread spectrum technique or combination of spread spectrum techniques in use. Bit field. 0=freq hopping, 1=psuedo noise, time hopping=2, reamining bits unused"""
        self.majorModulation = majorModulation
        """ the major classification of the modulation type. """
        self.detail = detail
        """ provide certain detailed information depending upon the major modulation type"""
        self.radioSystem = radioSystem
        """ the radio system associated with this Transmitter PDU and shall be used as the basis to interpret other fields whose values depend on a specific radio system."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.spreadSpectrum)
        outputStream.write_unsigned_short(self.majorModulation)
        outputStream.write_unsigned_short(self.detail)
        outputStream.write_unsigned_short(self.radioSystem)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.spreadSpectrum = inputStream.read_unsigned_short()
        self.majorModulation = inputStream.read_unsigned_short()
        self.detail = inputStream.read_unsigned_short()
        self.radioSystem = inputStream.read_unsigned_short()



class LinearSegmentParameter( object ):
    """The specification of an individual segment of a linear segment synthetic environment object in a Linear Object State PDU Section 6.2.52"""

    def __init__(self,
                 segmentNumber=0,
                 segmentModification=0,
                 generalSegmentAppearance=0,
                 specificSegmentAppearance=0,
                 segmentLocation=None,
                 segmentOrientation=None,
                 segmentLength=0.0,
                 segmentWidth=0.0,
                 segmentHeight=0.0,
                 segmentDepth=0.0):
        """ Initializer for LinearSegmentParameter"""
        self.segmentNumber = segmentNumber
        """ the individual segment of the linear segment """
        self.segmentModification = segmentModification
        """  whether a modification has been made to the point objects location or orientation"""
        self.generalSegmentAppearance = generalSegmentAppearance
        """ general dynamic appearance attributes of the segment. This record shall be defined as a 16-bit record of enumerations. The values defined for this record are included in Section 12 of SISO-REF-010."""
        self.specificSegmentAppearance = specificSegmentAppearance
        """ This field shall specify specific dynamic appearance attributes of the segment. This record shall be defined as a 32-bit record of enumerations."""
        self.segmentLocation = segmentLocation or Vector3Double()
        """ This field shall specify the location of the linear segment in the simulated world and shall be represented by a World Coordinates record """
        self.segmentOrientation = segmentOrientation or EulerAngles()
        """ orientation of the linear segment about the segment location and shall be represented by a Euler Angles record """
        self.segmentLength = segmentLength
        """ length of the linear segment, in meters, extending in the positive X direction"""
        self.segmentWidth = segmentWidth
        """ The total width of the linear segment, in meters, shall be specified by a 16-bit unsigned integer. One-half of the width shall extend in the positive Y direction, and one-half of the width shall extend in the negative Y direction."""
        self.segmentHeight = segmentHeight
        """ The height of the linear segment, in meters, above ground shall be specified by a 16-bit unsigned integer."""
        self.segmentDepth = segmentDepth
        """ The depth of the linear segment, in meters, below ground level """
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.segmentNumber)
        outputStream.write_unsigned_byte(self.segmentModification)
        outputStream.write_unsigned_short(self.generalSegmentAppearance)
        outputStream.write_unsigned_int(self.specificSegmentAppearance)
        self.segmentLocation.serialize(outputStream)
        self.segmentOrientation.serialize(outputStream)
        outputStream.write_float(self.segmentLength)
        outputStream.write_float(self.segmentWidth)
        outputStream.write_float(self.segmentHeight)
        outputStream.write_float(self.segmentDepth)
        outputStream.write_unsigned_int(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.segmentNumber = inputStream.read_unsigned_byte()
        self.segmentModification = inputStream.read_unsigned_byte()
        self.generalSegmentAppearance = inputStream.read_unsigned_short()
        self.specificSegmentAppearance = inputStream.read_unsigned_int()
        self.segmentLocation.parse(inputStream)
        self.segmentOrientation.parse(inputStream)
        self.segmentLength = inputStream.read_float()
        self.segmentWidth = inputStream.read_float()
        self.segmentHeight = inputStream.read_float()
        self.segmentDepth = inputStream.read_float()
        self.padding = inputStream.read_unsigned_int()



class SimulationAddress( object ):
    """A Simulation Address record shall consist of the Site Identification number and the Application Identification number. Section 6.2.79 """

    def __init__(self, site=0, application=0):
        """ Initializer for SimulationAddress"""
        self.site = site
        """ A site is defined as a facility, installation, organizational unit or a geographic location that has one or more simulation applications capable of participating in a distributed event. """
        self.application = application
        """ An application is defined as a software program that is used to generate and process distributed simulation data including live, virtual and constructive data."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.site)
        outputStream.write_unsigned_short(self.application)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.site = inputStream.read_unsigned_short()
        self.application = inputStream.read_unsigned_short()



class SystemIdentifier( object ):
    """The ID of the IFF emitting system. NOT COMPLETE. Section 6.2.87"""

    def __init__(self,
                 systemType=0,
                 systemName=0,
                 systemMode=0,
                 changeOptions=None):
        """ Initializer for SystemIdentifier"""
        self.systemType = systemType
        """ general type of emitting system, an enumeration"""
        self.systemName = systemName
        """ named type of system, an enumeration"""
        self.systemMode = systemMode
        """ mode of operation for the system, an enumeration"""
        self.changeOptions = changeOptions or ChangeOptions()
        """ status of this PDU, see section 6.2.15"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.systemType)
        outputStream.write_unsigned_short(self.systemName)
        outputStream.write_unsigned_short(self.systemMode)
        self.changeOptions.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.systemType = inputStream.read_unsigned_short()
        self.systemName = inputStream.read_unsigned_short()
        self.systemMode = inputStream.read_unsigned_short()
        self.changeOptions.parse(inputStream)



class TrackJamData( object ):
    """ Track-Jam data Section 6.2.89"""

    def __init__(self, entityID=None, emitterNumber=0, beamNumber=0):
        """ Initializer for TrackJamData"""
        self.entityID = entityID or EntityID()
        """ the entity tracked or illumated, or an emitter beam targeted with jamming"""
        self.emitterNumber = emitterNumber
        """ Emitter system associated with the entity"""
        self.beamNumber = beamNumber
        """ Beam associated with the entity"""

    def serialize(self, outputStream):
        """serialize the class """
        self.entityID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.emitterNumber)
        outputStream.write_unsigned_byte(self.beamNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.entityID.parse(inputStream)
        self.emitterNumber = inputStream.read_unsigned_byte()
        self.beamNumber = inputStream.read_unsigned_byte()



class AggregateType( object ):
    """Identifies the type and organization of an aggregate. Section 6.2.5"""

    def __init__(self,
                 aggregateKind=0,
                 domain=0,
                 country=0,
                 category=0,
                 subcategory=0,
                 specificInfo=0,
                 extra=0):
        """ Initializer for AggregateType"""
        self.aggregateKind = aggregateKind
        """ Grouping criterion used to group the aggregate. Enumeration from EBV document"""
        self.domain = domain
        """ Domain of entity (air, surface, subsurface, space, etc) Zero means domain does not apply."""
        self.country = country
        """ country to which the design of the entity is attributed"""
        self.category = category
        """ category of entity"""
        self.subcategory = subcategory
        """ subcategory of entity"""
        self.specificInfo = specificInfo
        """ specific info based on subcategory field. specific is a reserved word in sql."""
        self.extra = extra

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.aggregateKind)
        outputStream.write_unsigned_byte(self.domain)
        outputStream.write_unsigned_short(self.country)
        outputStream.write_unsigned_byte(self.category)
        outputStream.write_unsigned_byte(self.subcategory)
        outputStream.write_unsigned_byte(self.specificInfo)
        outputStream.write_unsigned_byte(self.extra)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.aggregateKind = inputStream.read_unsigned_byte()
        self.domain = inputStream.read_unsigned_byte()
        self.country = inputStream.read_unsigned_short()
        self.category = inputStream.read_unsigned_byte()
        self.subcategory = inputStream.read_unsigned_byte()
        self.specificInfo = inputStream.read_unsigned_byte()
        self.extra = inputStream.read_unsigned_byte()



class SimulationManagementPduHeader( object ):
    """First part of a simulation management (SIMAN) PDU and SIMAN-Reliability (SIMAN-R) PDU. Section 6.2.81"""

    def __init__(self,
                 pduHeader=None,
                 originatingID=None,
                 receivingID=None):
        """ Initializer for SimulationManagementPduHeader"""
        self.pduHeader = pduHeader or PduHeader()
        """ Conventional PDU header"""
        self.originatingID = originatingID or SimulationIdentifier()
        """ IDs the simulation or entity, etiehr a simulation or an entity. Either 6.2.80 or 6.2.28"""
        self.receivingID = receivingID or SimulationIdentifier()
        """ simulation, all simulations, a special ID, or an entity. See 5.6.5 and 5.12.4"""

    def serialize(self, outputStream):
        """serialize the class """
        self.pduHeader.serialize(outputStream)
        self.originatingID.serialize(outputStream)
        self.receivingID.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.pduHeader.parse(inputStream)
        self.originatingID.parse(inputStream)
        self.receivingID.parse(inputStream)



class BeamData( object ):
    """Describes the scan volue of an emitter beam. Section 6.2.11."""

    def __init__(self,
                 beamAzimuthCenter=0.0,
                 beamAzimuthSweep=0.0,
                 beamElevationCenter=0.0,
                 beamElevationSweep=0.0,
                 beamSweepSync=0.0):
        """ Initializer for BeamData"""
        self.beamAzimuthCenter = beamAzimuthCenter
        """ Specifies the beam azimuth an elevation centers and corresponding half-angles to describe the scan volume"""
        self.beamAzimuthSweep = beamAzimuthSweep
        """ Specifies the beam azimuth sweep to determine scan volume"""
        self.beamElevationCenter = beamElevationCenter
        """ Specifies the beam elevation center to determine scan volume"""
        self.beamElevationSweep = beamElevationSweep
        """ Specifies the beam elevation sweep to determine scan volume"""
        self.beamSweepSync = beamSweepSync
        """ allows receiver to synchronize its regenerated scan pattern to that of the emmitter. Specifies the percentage of time a scan is through its pattern from its origion."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.beamAzimuthCenter)
        outputStream.write_float(self.beamAzimuthSweep)
        outputStream.write_float(self.beamElevationCenter)
        outputStream.write_float(self.beamElevationSweep)
        outputStream.write_float(self.beamSweepSync)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.beamAzimuthCenter = inputStream.read_float()
        self.beamAzimuthSweep = inputStream.read_float()
        self.beamElevationCenter = inputStream.read_float()
        self.beamElevationSweep = inputStream.read_float()
        self.beamSweepSync = inputStream.read_float()



class EngineFuel( object ):
    """Information about an entity's engine fuel. Section 6.2.24."""

    def __init__(self,
                 fuelQuantity=0,
                 fuelMeasurementUnits=0,
                 fuelType=0,
                 fuelLocation=0):
        """ Initializer for EngineFuel"""
        self.fuelQuantity = 0
        """ Fuel quantity, units specified by next field"""
        self.fuelMeasurementUnits = 0
        """ Units in which the fuel is measured"""
        self.fuelType = 0
        """ Type of fuel"""
        self.fuelLocation = 0
        """ Location of fuel as related to entity. See section 14 of EBV document"""
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.fuelQuantity)
        outputStream.write_unsigned_byte(self.fuelMeasurementUnits)
        outputStream.write_unsigned_byte(self.fuelType)
        outputStream.write_unsigned_byte(self.fuelLocation)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.fuelQuantity = inputStream.read_unsigned_int()
        self.fuelMeasurementUnits = inputStream.read_unsigned_byte()
        self.fuelType = inputStream.read_unsigned_byte()
        self.fuelLocation = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class IOEffect( object ):
    """Effect of IO on an entity. Section 6.2.49.3"""

    def __init__(self,
                 ioStatus=0,
                 ioLinkType=0,
                 ioEffect=None,
                 ioEffectDutyCycle=0,
                 ioEffectDuration=0,
                 ioProcess=0):
        """ Initializer for IOEffect"""
        self.recordType = 5500
        self.recordLength = 16
        self.ioStatus = ioStatus
        self.ioLinkType = ioLinkType
        self.ioEffect = ioEffect or EntityID()
        self.ioEffectDutyCycle = ioEffectDutyCycle
        self.ioEffectDuration = ioEffectDuration
        self.ioProcess = ioProcess
        self.padding = 0

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_byte(self.ioStatus)
        outputStream.write_unsigned_byte(self.ioLinkType)
        self.ioEffect.serialize(outputStream)
        outputStream.write_unsigned_byte(self.ioEffectDutyCycle)
        outputStream.write_unsigned_short(self.ioEffectDuration)
        outputStream.write_unsigned_short(self.ioProcess)
        outputStream.write_unsigned_short(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.ioStatus = inputStream.read_unsigned_byte()
        self.ioLinkType = inputStream.read_unsigned_byte()
        self.ioEffect.parse(inputStream)
        self.ioEffectDutyCycle = inputStream.read_unsigned_byte()
        self.ioEffectDuration = inputStream.read_unsigned_short()
        self.ioProcess = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()



class SimulationIdentifier( object ):
    """The unique designation of a simulation when using the 48-bit identifier format shall be specified by the Simulation Identifier record. The reason that the 48-bit format is required in addition to the 32-bit simulation address format that actually identifies a specific simulation is because some 48-bit identifier fields in PDUs may contain either an Object Identifier, such as an Entity ID, or a Simulation Identifier. Section 6.2.80"""

    def __init__(self, simulationAddress=None, referenceNumber=0):
        """ Initializer for SimulationIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """ Simulation address """
        self.referenceNumber = referenceNumber
        """ This field shall be set to zero as there is no reference number associated with a Simulation Identifier."""

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.referenceNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.referenceNumber = inputStream.read_unsigned_short()



class GridAxisDescriptorVariable( object ):
    """Grid axis descriptor fo variable spacing axis data. NOT COMPLETE. Need padding to 64 bit boundary."""

    def __init__(self,
                 domainInitialXi=0.0,
                 domainFinalXi=0.0,
                 domainPointsXi=0,
                 interleafFactor=0,
                 axisType=0,
                 numberOfPointsOnXiAxis=0,
                 initialIndex=0,
                 coordinateScaleXi=0.0,
                 coordinateOffsetXi=0.0,
                 xiValues=None):
        """ Initializer for GridAxisDescriptorVariable"""
        self.domainInitialXi = domainInitialXi
        """ coordinate of the grid origin or initial value"""
        self.domainFinalXi = domainFinalXi
        """ coordinate of the endpoint or final value"""
        self.domainPointsXi = domainPointsXi
        """ The number of grid points along the Xi domain axis for the enviornmental state data"""
        self.interleafFactor = interleafFactor
        """ interleaf factor along the domain axis."""
        self.axisType = axisType
        """ type of grid axis"""
        self.numberOfPointsOnXiAxis = numberOfPointsOnXiAxis
        """ Number of grid locations along Xi axis"""
        self.initialIndex = initialIndex
        """ initial grid point for the current pdu"""
        self.coordinateScaleXi = coordinateScaleXi
        """ value that linearly scales the coordinates of the grid locations for the xi axis"""
        self.coordinateOffsetXi = coordinateOffsetXi
        """ The constant offset value that shall be applied to the grid locations for the xi axis"""
        self.xiValues = xiValues or []
        """ list of coordinates"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_double(self.domainInitialXi)
        outputStream.write_double(self.domainFinalXi)
        outputStream.write_unsigned_short(self.domainPointsXi)
        outputStream.write_unsigned_byte(self.interleafFactor)
        outputStream.write_unsigned_byte(self.axisType)
        outputStream.write_unsigned_short( len(self.xiValues))
        outputStream.write_unsigned_short(self.initialIndex)
        outputStream.write_double(self.coordinateScaleXi)
        outputStream.write_double(self.coordinateOffsetXi)
        for anObj in self.xiValues:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.domainInitialXi = inputStream.read_double()
        self.domainFinalXi = inputStream.read_double()
        self.domainPointsXi = inputStream.read_unsigned_short()
        self.interleafFactor = inputStream.read_unsigned_byte()
        self.axisType = inputStream.read_unsigned_byte()
        self.numberOfPointsOnXiAxis = inputStream.read_unsigned_short()
        self.initialIndex = inputStream.read_unsigned_short()
        self.coordinateScaleXi = inputStream.read_double()
        self.coordinateOffsetXi = inputStream.read_double()
        for idx in range(0, self.numberOfPointsOnXiAxis):
            element = null()
            element.parse(inputStream)
            self.xiValues.append(element)




class SupplyQuantity( object ):
    """ A supply, and the amount of that supply. Section 6.2.86"""

    def __init__(self, supplyType=None, quantity=0.0):
        """ Initializer for SupplyQuantity"""
        self.supplyType = supplyType or EntityType()
        """ Type of supply"""
        self.quantity = quantity
        """ the number of units of a supply type. """

    def serialize(self, outputStream):
        """serialize the class """
        self.supplyType.serialize(outputStream)
        outputStream.write_float(self.quantity)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.supplyType.parse(inputStream)
        self.quantity = inputStream.read_float()



class SilentEntitySystem( object ):
    """information abou an enitity not producing espdus. Section 6.2.79"""

    def __init__(self,
                 numberOfEntities=0,
                 numberOfAppearanceRecords=0,
                 entityType=None,
                 appearanceRecordList=None):
        """ Initializer for SilentEntitySystem"""
        self.numberOfEntities = numberOfEntities
        """ number of the type specified by the entity type field"""
        self.numberOfAppearanceRecords = numberOfAppearanceRecords
        """ number of entity appearance records that follow"""
        self.entityType = entityType or EntityType()
        """ Entity type"""
        self.appearanceRecordList = appearanceRecordList or []
        """ Variable length list of appearance records"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.numberOfEntities)
        outputStream.write_unsigned_short( len(self.appearanceRecordList))
        self.entityType.serialize(outputStream)
        for anObj in self.appearanceRecordList:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.numberOfEntities = inputStream.read_unsigned_short()
        self.numberOfAppearanceRecords = inputStream.read_unsigned_short()
        self.entityType.parse(inputStream)
        for idx in range(0, self.numberOfAppearanceRecords):
            element = null()
            element.parse(inputStream)
            self.appearanceRecordList.append(element)




class EventIdentifier( object ):
    """Identifies an event in the world. Use this format for every PDU EXCEPT the LiveEntityPdu. Section 6.2.34."""

    def __init__(self, simulationAddress=None, eventNumber=0):
        """ Initializer for EventIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """ Site and application IDs"""
        self.eventNumber = eventNumber

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.eventNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.eventNumber = inputStream.read_unsigned_short()



class BlankingSector( object ):
    """The Blanking Sector attribute record may be used to convey persistent areas within a scan volume where emitter power for a specific active emitter beam is reduced to an insignificant value. Section 6.2.21.2"""

    def __init__(self,
                 recordType=3500,
                 recordLength=40,
                 emitterNumber=0,
                 beamNumber=0,
                 stateIndicator=0,
                 leftAzimuth=0.0,
                 rightAzimuth=0.0,
                 lowerElevation=0.0,
                 upperElevation=0.0,
                 residualPower=0.0):
        """ Initializer for BlankingSector"""
        self.recordType = 3500
        self.recordLength = 40
        self.padding = 0
        self.emitterNumber = emitterNumber
        self.beamNumber = beamNumber
        self.stateIndicator = stateIndicator
        self.padding2 = 0
        self.leftAzimuth = leftAzimuth
        self.rightAzimuth = rightAzimuth
        self.lowerElevation = lowerElevation
        self.upperElevation = upperElevation
        self.residualPower = residualPower
        self.padding3 = 0
        self.padding4 = 0

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_int(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_short(self.padding)
        outputStream.write_unsigned_byte(self.emitterNumber)
        outputStream.write_unsigned_byte(self.beamNumber)
        outputStream.write_unsigned_byte(self.stateIndicator)
        outputStream.write_unsigned_byte(self.padding2)
        outputStream.write_float(self.leftAzimuth)
        outputStream.write_float(self.rightAzimuth)
        outputStream.write_float(self.lowerElevation)
        outputStream.write_float(self.upperElevation)
        outputStream.write_float(self.residualPower)
        outputStream.write_int(self.padding3)
        outputStream.write_int(self.padding4)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_int()
        self.recordLength = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()
        self.emitterNumber = inputStream.read_unsigned_byte()
        self.beamNumber = inputStream.read_unsigned_byte()
        self.stateIndicator = inputStream.read_unsigned_byte()
        self.padding2 = inputStream.read_unsigned_byte()
        self.leftAzimuth = inputStream.read_float()
        self.rightAzimuth = inputStream.read_float()
        self.lowerElevation = inputStream.read_float()
        self.upperElevation = inputStream.read_float()
        self.residualPower = inputStream.read_float()
        self.padding3 = inputStream.read_int()
        self.padding4 = inputStream.read_int()



class LaunchedMunitionRecord( object ):
    """Identity of a communications node. Section 6.2.50"""

    def __init__(self,
                 fireEventID=None,
                 firingEntityID=None,
                 targetEntityID=None,
                 targetLocation=None):
        """ Initializer for LaunchedMunitionRecord"""
        self.fireEventID = fireEventID or EventIdentifier()
        self.padding = 0
        self.firingEntityID = firingEntityID or EventIdentifier()
        self.padding2 = 0
        self.targetEntityID = targetEntityID or EventIdentifier()
        self.padding3 = 0
        self.targetLocation = targetLocation or Vector3Double()

    def serialize(self, outputStream):
        """serialize the class """
        self.fireEventID.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding)
        self.firingEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding2)
        self.targetEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding3)
        self.targetLocation.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.fireEventID.parse(inputStream)
        self.padding = inputStream.read_unsigned_short()
        self.firingEntityID.parse(inputStream)
        self.padding2 = inputStream.read_unsigned_short()
        self.targetEntityID.parse(inputStream)
        self.padding3 = inputStream.read_unsigned_short()
        self.targetLocation.parse(inputStream)



class IFFFundamentalParameterData( object ):
    """Fundamental IFF atc data. Section 6.2.45"""

    def __init__(self,
                 erp=0.0,
                 frequency=0.0,
                 pgrf=0.0,
                 pulseWidth=0.0,
                 burstLength=0,
                 applicableModes=0,
                 systemSpecificData=None):
        """ Initializer for IFFFundamentalParameterData"""
        self.erp = 0
        """ ERP"""
        self.frequency = 0
        """ frequency"""
        self.pgrf = 0
        """ pgrf"""
        self.pulseWidth = 0
        """ Pulse width"""
        self.burstLength = 0
        """ Burst length"""
        self.applicableModes = 0
        """ Applicable modes enumeration"""
        self.systemSpecificData = systemSpecificData or [0] * 3
        """ System-specific data"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.erp)
        outputStream.write_float(self.frequency)
        outputStream.write_float(self.pgrf)
        outputStream.write_float(self.pulseWidth)
        outputStream.write_unsigned_int(self.burstLength)
        outputStream.write_unsigned_byte(self.applicableModes)
        for idx in range(0, 3):
            outputStream.write_unsigned_byte( self.systemSpecificData[ idx ] )



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.erp = inputStream.read_float()
        self.frequency = inputStream.read_float()
        self.pgrf = inputStream.read_float()
        self.pulseWidth = inputStream.read_float()
        self.burstLength = inputStream.read_unsigned_int()
        self.applicableModes = inputStream.read_unsigned_byte()
        self.systemSpecificData = [0]*3
        for idx in range(0, 3):
            val = inputStream.read_unsigned_byte()

            self.systemSpecificData[  idx  ] = val




class FundamentalOperationalData( object ):
    """Basic operational data for IFF. Section 6.2.40."""

    def __init__(self,
                 systemStatus=0,
                 dataField1=0,
                 informationLayers=0,
                 dataField2=0,
                 parameter1=0,
                 parameter2=0,
                 parameter3=0,
                 parameter4=0,
                 parameter5=0,
                 parameter6=0):
        """ Initializer for FundamentalOperationalData"""
        self.systemStatus = systemStatus
        """ system status"""
        self.dataField1 = dataField1
        """ data field 1"""
        self.informationLayers = informationLayers
        """ eight boolean fields"""
        self.dataField2 = dataField2
        """ enumeration"""
        self.parameter1 = parameter1
        """ parameter, enumeration"""
        self.parameter2 = parameter2
        """ parameter, enumeration"""
        self.parameter3 = parameter3
        """ parameter, enumeration"""
        self.parameter4 = parameter4
        """ parameter, enumeration"""
        self.parameter5 = parameter5
        """ parameter, enumeration"""
        self.parameter6 = parameter6
        """ parameter, enumeration"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.systemStatus)
        outputStream.write_unsigned_byte(self.dataField1)
        outputStream.write_unsigned_byte(self.informationLayers)
        outputStream.write_unsigned_byte(self.dataField2)
        outputStream.write_unsigned_short(self.parameter1)
        outputStream.write_unsigned_short(self.parameter2)
        outputStream.write_unsigned_short(self.parameter3)
        outputStream.write_unsigned_short(self.parameter4)
        outputStream.write_unsigned_short(self.parameter5)
        outputStream.write_unsigned_short(self.parameter6)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.systemStatus = inputStream.read_unsigned_byte()
        self.dataField1 = inputStream.read_unsigned_byte()
        self.informationLayers = inputStream.read_unsigned_byte()
        self.dataField2 = inputStream.read_unsigned_byte()
        self.parameter1 = inputStream.read_unsigned_short()
        self.parameter2 = inputStream.read_unsigned_short()
        self.parameter3 = inputStream.read_unsigned_short()
        self.parameter4 = inputStream.read_unsigned_short()
        self.parameter5 = inputStream.read_unsigned_short()
        self.parameter6 = inputStream.read_unsigned_short()



class IntercomCommunicationsParameters( object ):
    """Intercom communcations parameters. Section 6.2.47.  This requires hand coding"""

    def __init__(self, recordType=0, recordLength=0, recordSpecificField=0):
        """ Initializer for IntercomCommunicationsParameters"""
        self.recordType = recordType
        """ Type of intercom parameters record"""
        self.recordLength = recordLength
        """ length of record"""
        self.recordSpecificField = recordSpecificField
        """ This is a placeholder."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.recordType)
        outputStream.write_unsigned_short(self.recordLength)
        outputStream.write_unsigned_int(self.recordSpecificField)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_short()
        self.recordLength = inputStream.read_unsigned_short()
        self.recordSpecificField = inputStream.read_unsigned_int()



class EntityType( object ):
    """Identifies the type of Entity"""

    def __init__(self,
                 entityKind=0,
                 domain=0,
                 country=0,
                 category=0,
                 subcategory=0,
                 specific=0,
                 extra=0):
        """ Initializer for EntityType"""
        self.entityKind = entityKind
        """ Kind of entity"""
        self.domain = domain
        """ Domain of entity (air, surface, subsurface, space, etc)"""
        self.country = country
        """ country to which the design of the entity is attributed"""
        self.category = category
        """ category of entity"""
        self.subcategory = subcategory
        """ subcategory of entity"""
        self.specific = specific
        """ specific info based on subcategory field. Renamed from specific because that is a reserved word in SQL."""
        self.extra = extra

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.entityKind)
        outputStream.write_unsigned_byte(self.domain)
        outputStream.write_unsigned_short(self.country)
        outputStream.write_unsigned_byte(self.category)
        outputStream.write_unsigned_byte(self.subcategory)
        outputStream.write_unsigned_byte(self.specific)
        outputStream.write_unsigned_byte(self.extra)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.entityKind = inputStream.read_unsigned_byte()
        self.domain = inputStream.read_unsigned_byte()
        self.country = inputStream.read_unsigned_short()
        self.category = inputStream.read_unsigned_byte()
        self.subcategory = inputStream.read_unsigned_byte()
        self.specific = inputStream.read_unsigned_byte()
        self.extra = inputStream.read_unsigned_byte()



class Munition( object ):
    """An entity's munition (e.g., bomb, missile) information shall be represented by one or more Munition records. For each type or location of munition, this record shall specify the type, location, quantity and status of munitions that an entity contains. Section 6.2.60 """

    def __init__(self,
                 munitionType=None,
                 station=0,
                 quantity=0,
                 munitionStatus=0):
        """ Initializer for Munition"""
        self.munitionType = munitionType or EntityType()
        """  This field shall identify the entity type of the munition. See section 6.2.30."""
        self.station = station
        """ the station or launcher to which the munition is assigned. See Annex I"""
        self.quantity = quantity
        """ the quantity remaining of this munition."""
        self.munitionStatus = munitionStatus
        """  the status of the munition. It shall be represented by an 8-bit enumeration. """
        self.padding = 0
        """ padding """

    def serialize(self, outputStream):
        """serialize the class """
        self.munitionType.serialize(outputStream)
        outputStream.write_unsigned_int(self.station)
        outputStream.write_unsigned_short(self.quantity)
        outputStream.write_unsigned_byte(self.munitionStatus)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.munitionType.parse(inputStream)
        self.station = inputStream.read_unsigned_int()
        self.quantity = inputStream.read_unsigned_short()
        self.munitionStatus = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class StandardVariableSpecification( object ):
    """Does not work, and causes failure in anything it is embedded in. Section 6.2.83"""

    def __init__(self,
                 numberOfStandardVariableRecords=0,
                 standardVariables=None):
        """ Initializer for StandardVariableSpecification"""
        self.numberOfStandardVariableRecords = numberOfStandardVariableRecords
        """ Number of static variable records"""
        self.standardVariables = standardVariables or []
        """ variable length list of standard variables, The class type and length here are WRONG and will cause the incorrect serialization of any class in whihc it is embedded."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short( len(self.standardVariables))
        for anObj in self.standardVariables:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.numberOfStandardVariableRecords = inputStream.read_unsigned_short()
        for idx in range(0, self.numberOfStandardVariableRecords):
            element = null()
            element.parse(inputStream)
            self.standardVariables.append(element)




class Vector2Float( object ):
    """Two floating point values, x, y"""

    def __init__(self, x=0.0, y=0.0):
        """ Initializer for Vector2Float"""
        self.x = x
        """ X value"""
        self.y = y
        """ y Value"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.x)
        outputStream.write_float(self.y)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.x = inputStream.read_float()
        self.y = inputStream.read_float()



class Environment( object ):
    """Incomplete environment record; requires hand coding to fix. Section 6.2.31.1"""

    def __init__(self, environmentType=0, length=0, index=0):
        """ Initializer for Environment"""
        self.environmentType = environmentType
        """ type"""
        self.length = length
        """ length, in bits, of the record"""
        self.index = index
        """ identifies the sequentially numbered record index"""
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.environmentType)
        outputStream.write_unsigned_short(self.length)
        outputStream.write_unsigned_byte(self.index)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.environmentType = inputStream.read_unsigned_int()
        self.length = inputStream.read_unsigned_short()
        self.index = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class AcousticEmitter( object ):
    """ information about a specific UA emitter. Section 6.2.2."""

    def __init__(self,
                 acousticSystemName=0,
                 acousticFunction=0,
                 acousticIDNumber=0):
        """ Initializer for AcousticEmitter"""
        self.acousticSystemName = acousticSystemName
        """ the system for a particular UA emitter, and an enumeration"""
        self.acousticFunction = acousticFunction
        """ The function of the acoustic system"""
        self.acousticIDNumber = acousticIDNumber
        """ The UA emitter identification number relative to a specific system"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.acousticSystemName)
        outputStream.write_unsigned_byte(self.acousticFunction)
        outputStream.write_unsigned_byte(self.acousticIDNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.acousticSystemName = inputStream.read_unsigned_short()
        self.acousticFunction = inputStream.read_unsigned_byte()
        self.acousticIDNumber = inputStream.read_unsigned_byte()



class AngularVelocityVector( object ):
    """Angular velocity measured in radians per second out each of the entity's own coordinate axes. Order of measurement is angular velocity around the x, y, and z axis of the entity. The positive direction is determined by the right hand rule. Section 6.2.7"""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """ Initializer for AngularVelocityVector"""
        self.x = 0
        """ velocity about the x axis"""
        self.y = 0
        """ velocity about the y axis"""
        self.z = 0
        """ velocity about the zaxis"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.x)
        outputStream.write_float(self.y)
        outputStream.write_float(self.z)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.x = inputStream.read_float()
        self.y = inputStream.read_float()
        self.z = inputStream.read_float()



class AggregateMarking( object ):
    """Specifies the character set used in the first byte, followed by up to 31 characters of text data. Section 6.2.4. """

    def __init__(self, characterSet=0, characters=None):
        """ Initializer for AggregateMarking"""
        self.characterSet = characterSet
        """ The character set"""
        self.characters =  [0] * 31
        """ The characters"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.characterSet)
        for idx in range(0, 31):
            outputStream.write_unsigned_byte( self.characters[ idx ] )



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.characterSet = inputStream.read_unsigned_byte()
        self.characters = [0]*31
        for idx in range(0, 31):
            val = inputStream.read_unsigned_byte()

            self.characters[  idx  ] = val




class DataFilterRecord( object ):
    """identify which of the optional data fields are contained in the Minefield Data PDU or requested in the Minefield Query PDU. This is a 32-bit record. For each field, true denotes that the data is requested or present and false denotes that the data is neither requested nor present. Section 6.2.16"""

    def __init__(self, bitFlags=0):
        """ Initializer for DataFilterRecord"""
        self.bitFlags = bitFlags
        """ Bitflags field"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.bitFlags)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.bitFlags = inputStream.read_unsigned_int()



class IntercomIdentifier( object ):
    """Unique designation of an attached or unattached intercom in an event or exercise. Section 6.2.48"""

    def __init__(self,
                 siteNumber=0,
                 applicationNumber=0,
                 referenceNumber=0,
                 intercomNumber=0):
        """ Initializer for IntercomIdentifier"""
        self.siteNumber = siteNumber
        self.applicationNumber = applicationNumber
        self.referenceNumber = referenceNumber
        self.intercomNumber = intercomNumber

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.siteNumber)
        outputStream.write_unsigned_short(self.applicationNumber)
        outputStream.write_unsigned_short(self.referenceNumber)
        outputStream.write_unsigned_short(self.intercomNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.siteNumber = inputStream.read_unsigned_short()
        self.applicationNumber = inputStream.read_unsigned_short()
        self.referenceNumber = inputStream.read_unsigned_short()
        self.intercomNumber = inputStream.read_unsigned_short()



class StorageFuel( object ):
    """Information about an entity's engine fuel. Section 6.2.84."""

    def __init__(self,
                 fuelQuantity=0,
                 fuelMeasurementUnits=0,
                 fuelType=0,
                 fuelLocation=0):
        """ Initializer for StorageFuel"""
        self.fuelQuantity = fuelQuantity
        """ Fuel quantity, units specified by next field"""
        self.fuelMeasurementUnits = fuelMeasurementUnits
        """ Units in which the fuel is measured"""
        self.fuelType = fuelType
        """ Type of fuel"""
        self.fuelLocation = fuelLocation
        """ Location of fuel as related to entity. See section 14 of EBV document"""
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.fuelQuantity)
        outputStream.write_unsigned_byte(self.fuelMeasurementUnits)
        outputStream.write_unsigned_byte(self.fuelType)
        outputStream.write_unsigned_byte(self.fuelLocation)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.fuelQuantity = inputStream.read_unsigned_int()
        self.fuelMeasurementUnits = inputStream.read_unsigned_byte()
        self.fuelType = inputStream.read_unsigned_byte()
        self.fuelLocation = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class Sensor( object ):
    """An entity's sensor information.  Section 6.2.77."""

    def __init__(self,
                 sensorTypeSource=0,
                 sensorOnOffStatus=0,
                 sensorType=0,
                 station=0,
                 quantity=0):
        """ Initializer for Sensor"""
        self.sensorTypeSource = sensorTypeSource
        """  the source of the Sensor Type field """
        self.sensorOnOffStatus = sensorOnOffStatus
        """ the on/off status of the sensor"""
        self.sensorType = sensorType
        """ the sensor type and shall be represented by a 16-bit enumeration. """
        self.station = station
        """  the station to which the sensor is assigned. A zero value shall indicate that this Sensor record is not associated with any particular station and represents the total quantity of this sensor for this entity. If this field is non-zero, it shall either reference an attached part or an articulated part"""
        self.quantity = 0
        """ quantity of the sensor """
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.sensorTypeSource)
        outputStream.write_unsigned_byte(self.sensorOnOffStatus)
        outputStream.write_unsigned_short(self.sensorType)
        outputStream.write_unsigned_int(self.station)
        outputStream.write_unsigned_short(self.quantity)
        outputStream.write_unsigned_short(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.sensorTypeSource = inputStream.read_unsigned_byte()
        self.sensorOnOffStatus = inputStream.read_unsigned_byte()
        self.sensorType = inputStream.read_unsigned_short()
        self.station = inputStream.read_unsigned_int()
        self.quantity = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_short()



class MunitionReload( object ):
    """indicate weapons (munitions) previously communicated via the Munition record. Section 6.2.61 """

    def __init__(self,
                 munitionType=None,
                 station=0,
                 standardQuantity=0,
                 maximumQuantity=0,
                 standardQuantityReloadTime=0,
                 maximumQuantityReloadTime=0):
        """ Initializer for MunitionReload"""
        self.munitionType = munitionType or EntityType()
        """  This field shall identify the entity type of the munition. See section 6.2.30."""
        self.station = station
        """ the station or launcher to which the munition is assigned. See Annex I"""
        self.standardQuantity = standardQuantity
        """ the standard quantity of this munition type normally loaded at this station/launcher if a station/launcher is specified."""
        self.maximumQuantity = maximumQuantity
        """ the maximum quantity of this munition type that this station/launcher is capable of holding when a station/launcher is specified """
        self.standardQuantityReloadTime = standardQuantityReloadTime
        """ numer of seconds of sim time required to reload the std qty"""
        self.maximumQuantityReloadTime = maximumQuantityReloadTime
        """ the number of seconds of sim time required to reload the max possible quantity"""

    def serialize(self, outputStream):
        """serialize the class """
        self.munitionType.serialize(outputStream)
        outputStream.write_unsigned_int(self.station)
        outputStream.write_unsigned_short(self.standardQuantity)
        outputStream.write_unsigned_short(self.maximumQuantity)
        outputStream.write_unsigned_int(self.standardQuantityReloadTime)
        outputStream.write_unsigned_int(self.maximumQuantityReloadTime)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.munitionType.parse(inputStream)
        self.station = inputStream.read_unsigned_int()
        self.standardQuantity = inputStream.read_unsigned_short()
        self.maximumQuantity = inputStream.read_unsigned_short()
        self.standardQuantityReloadTime = inputStream.read_unsigned_int()
        self.maximumQuantityReloadTime = inputStream.read_unsigned_int()



class StorageFuelReload( object ):
    """For each type or location of Storage Fuel, this record shall specify the type, location, fuel measurement units, reload quantity and maximum quantity for storage fuel either for the whole entity or a specific storage fuel location (tank). Section 6.2.85."""

    def __init__(self,
                 standardQuantity=0,
                 maximumQuantity=0,
                 standardQuantityReloadTime=0,
                 maximumQuantityReloadTime=0,
                 fuelMeasurementUnits=0,
                 fuelType=0,
                 fuelLocation=0):
        """ Initializer for StorageFuelReload"""
        self.standardQuantity = standardQuantity
        """  the standard quantity of this fuel type normally loaded at this station/launcher if a station/launcher is specified. If the Station/Launcher field is set to zero, then this is the total quantity of this fuel type that would be present in a standard reload of all applicable stations/launchers associated with this entity."""
        self.maximumQuantity = maximumQuantity
        """ the maximum quantity of this fuel type that this station/launcher is capable of holding when a station/launcher is specified. This would be the value used when a maximum reload was desired to be set for this station/launcher. If the Station/launcher field is set to zero, then this is the maximum quantity of this fuel type that would be present on this entity at all stations/launchers that can accept this fuel type."""
        self.standardQuantityReloadTime = standardQuantityReloadTime
        """ the seconds normally required to reload the standard quantity of this fuel type at this specific station/launcher. When the Station/Launcher field is set to zero, this shall be the time it takes to perform a standard quantity reload of this fuel type at all applicable stations/launchers for this entity."""
        self.maximumQuantityReloadTime = maximumQuantityReloadTime
        """ the seconds normally required to reload the maximum possible quantity of this fuel type at this station/launcher. When the Station/Launcher field is set to zero, this shall be the time it takes to perform a maximum quantity load/reload of this fuel type at all applicable stations/launchers for this entity."""
        self.fuelMeasurementUnits = fuelMeasurementUnits
        """ the fuel measurement units. Enumeration"""
        self.fuelType = fuelType
        """ Fuel type. Enumeration"""
        self.fuelLocation = fuelLocation
        """ Location of fuel as related to entity. See section 14 of EBV document"""
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.standardQuantity)
        outputStream.write_unsigned_int(self.maximumQuantity)
        outputStream.write_unsigned_byte(self.standardQuantityReloadTime)
        outputStream.write_unsigned_byte(self.maximumQuantityReloadTime)
        outputStream.write_unsigned_byte(self.fuelMeasurementUnits)
        outputStream.write_unsigned_byte(self.fuelType)
        outputStream.write_unsigned_byte(self.fuelLocation)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.standardQuantity = inputStream.read_unsigned_int()
        self.maximumQuantity = inputStream.read_unsigned_int()
        self.standardQuantityReloadTime = inputStream.read_unsigned_byte()
        self.maximumQuantityReloadTime = inputStream.read_unsigned_byte()
        self.fuelMeasurementUnits = inputStream.read_unsigned_byte()
        self.fuelType = inputStream.read_unsigned_byte()
        self.fuelLocation = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class ExpendableReload( object ):
    """An entity's expendable (chaff, flares, etc) information. Section 6.2.37"""

    def __init__(self,
                 expendable=None,
                 station=0,
                 standardQuantity=0,
                 maximumQuantity=0,
                 standardQuantityReloadTime=0,
                 maximumQuantityReloadTime=0):
        """ Initializer for ExpendableReload"""
        self.expendable = expendable or EntityType()
        """ Type of expendable"""
        self.station = station
        self.standardQuantity = standardQuantity
        self.maximumQuantity = maximumQuantity
        self.standardQuantityReloadTime = standardQuantityReloadTime
        self.maximumQuantityReloadTime = maximumQuantityReloadTime

    def serialize(self, outputStream):
        """serialize the class """
        self.expendable.serialize(outputStream)
        outputStream.write_unsigned_int(self.station)
        outputStream.write_unsigned_short(self.standardQuantity)
        outputStream.write_unsigned_short(self.maximumQuantity)
        outputStream.write_unsigned_int(self.standardQuantityReloadTime)
        outputStream.write_unsigned_int(self.maximumQuantityReloadTime)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.expendable.parse(inputStream)
        self.station = inputStream.read_unsigned_int()
        self.standardQuantity = inputStream.read_unsigned_short()
        self.maximumQuantity = inputStream.read_unsigned_short()
        self.standardQuantityReloadTime = inputStream.read_unsigned_int()
        self.maximumQuantityReloadTime = inputStream.read_unsigned_int()



class EntityIdentifier( object ):
    """Entity Identifier. Unique ID for entities in the world. Consists of an simulation address and a entity number. Section 6.2.28."""

    def __init__(self,
                 simulationAddress=None,
                 entityNumber=0):
        """ Initializer for EntityIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """ Site and application IDs"""
        self.entityNumber = entityNumber
        """ Entity number"""

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.entityNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.entityNumber = inputStream.read_unsigned_short()



class DirectedEnergyTargetEnergyDeposition( object ):
    """DE energy depostion properties for a target entity. Section 6.2.20.4"""

    def __init__(self,
                 targetEntityID=None,
                 peakIrradiance=0.0):
        """ Initializer for DirectedEnergyTargetEnergyDeposition"""
        self.targetEntityID = targetEntityID or EntityID()
        """ Unique ID of the target entity."""
        self.padding = 0
        """ padding"""
        self.peakIrradiance = peakIrradiance
        """ Peak irrandiance"""

    def serialize(self, outputStream):
        """serialize the class """
        self.targetEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding)
        outputStream.write_float(self.peakIrradiance)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.targetEntityID.parse(inputStream)
        self.padding = inputStream.read_unsigned_short()
        self.peakIrradiance = inputStream.read_float()



class EntityID( object ):
    """more laconically named EntityIdentifier"""

    def __init__(self,
                 siteID=0,
                 applicationID=0,
                 entityID=0):
        """ Initializer for EntityID"""
        self.siteID = siteID
        """ Site ID"""
        self.applicationID = applicationID
        """ application number ID"""
        self.entityID = entityID
        """ Entity number ID"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.siteID)
        outputStream.write_unsigned_short(self.applicationID)
        outputStream.write_unsigned_short(self.entityID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.siteID = inputStream.read_unsigned_short()
        self.applicationID = inputStream.read_unsigned_short()
        self.entityID = inputStream.read_unsigned_short()



class EngineFuelReload( object ):
    """For each type or location of engine fuel, this record specifies the type, location, fuel measurement units, and reload quantity and maximum quantity. Section 6.2.25."""

    def __init__(self,
                 standardQuantity=0,
                 maximumQuantity=0,
                 standardQuantityReloadTime=0,
                 maximumQuantityReloadTime=0,
                 fuelMeasurementUnits=0,
                 fuelLocation=0):
        """ Initializer for EngineFuelReload"""
        self.standardQuantity = standardQuantity
        """ standard quantity of fuel loaded"""
        self.maximumQuantity = maximumQuantity
        """ maximum quantity of fuel loaded"""
        self.standardQuantityReloadTime = standardQuantityReloadTime
        """ seconds normally required to to reload standard qty"""
        self.maximumQuantityReloadTime = maximumQuantityReloadTime
        """ seconds normally required to to reload maximum qty"""
        self.fuelMeasurmentUnits = fuelMeasurementUnits
        """ Units of measure"""
        self.fuelLocation = fuelLocation
        """ fuel  location as related to the entity"""
        self.padding = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.standardQuantity)
        outputStream.write_unsigned_int(self.maximumQuantity)
        outputStream.write_unsigned_int(self.standardQuantityReloadTime)
        outputStream.write_unsigned_int(self.maximumQuantityReloadTime)
        outputStream.write_unsigned_byte(self.fuelMeasurmentUnits)
        outputStream.write_unsigned_byte(self.fuelLocation)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.standardQuantity = inputStream.read_unsigned_int()
        self.maximumQuantity = inputStream.read_unsigned_int()
        self.standardQuantityReloadTime = inputStream.read_unsigned_int()
        self.maximumQuantityReloadTime = inputStream.read_unsigned_int()
        self.fuelMeasurmentUnits = inputStream.read_unsigned_byte()
        self.fuelLocation = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class UnattachedIdentifier( object ):
    """The unique designation of one or more unattached radios in an event or exercise Section 6.2.91"""

    def __init__(self,
                 simulationAddress=None,
                 referenceNumber=0):
        """ Initializer for UnattachedIdentifier"""
        self.simulationAddress = simulationAddress or SimulationAddress()
        """ See 6.2.79"""
        self.referenceNumber = referenceNumber
        """ Reference number"""

    def serialize(self, outputStream):
        """serialize the class """
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.referenceNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.simulationAddress.parse(inputStream)
        self.referenceNumber = inputStream.read_unsigned_short()



class EntityTypeVP( object ):
    """Association or disassociation of two entities.  Section 6.2.94.5"""

    def __init__(self,
                 recordType=3,
                 changeIndicator=0,
                 entityType=None):
        """ Initializer for EntityTypeVP"""
        self.recordType = recordType
        """ the identification of the Variable Parameter record. Enumeration from EBV"""
        self.changeIndicator = changeIndicator
        """ Indicates if this VP has changed since last issuance"""
        self.entityType = entityType or EntityType()
        """ """
        self.padding = 0
        """ padding"""
        self.padding1 = 0
        """ padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.recordType)
        outputStream.write_unsigned_byte(self.changeIndicator)
        self.entityType.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding)
        outputStream.write_unsigned_int(self.padding1)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_byte()
        self.changeIndicator = inputStream.read_unsigned_byte()
        self.entityType.parse(inputStream)
        self.padding = inputStream.read_unsigned_short()
        self.padding1 = inputStream.read_unsigned_int()



class BeamStatus( object ):
    """Information related to the status of a beam. This is contained in the beam status field of the electromagnetic emission PDU. The first bit determines whether the beam is active (0) or deactivated (1). Section 6.2.12."""

    def __init__(self, beamState=0):
        """ Initializer for BeamStatus"""
        self.beamState = beamState
        """ First bit zero means beam is active, first bit = 1 means deactivated. The rest is padding."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.beamState)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.beamState = inputStream.read_unsigned_byte()



class EnvironmentGeneral( object ):
    """ Information about a geometry, a state associated with a geometry, a bounding volume, or an associated entity ID. NOTE: this class requires hand coding. 6.2.31"""

    def __init__(self,
                 environmentType=0,
                 length=0,
                 index=0,
                 geometry=0):
        """ Initializer for EnvironmentGeneral"""
        self.environmentType = environmentType
        """ Record type"""
        self.length = length
        """ length, in bits"""
        self.index = index
        """ Identify the sequentially numbered record index"""
        self.padding = 0
        """ padding"""
        self.geometry = geometry
        """ Geometry or state record"""
        self.padding2 = 0
        """ padding to bring the total size up to a 64 bit boundry"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.environmentType)
        outputStream.write_unsigned_byte(self.length)
        outputStream.write_unsigned_byte(self.index)
        outputStream.write_unsigned_byte(self.padding1)
        outputStream.write_unsigned_byte(self.geometry)
        outputStream.write_unsigned_byte(self.padding2)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.environmentType = inputStream.read_unsigned_int()
        self.length = inputStream.read_unsigned_byte()
        self.index = inputStream.read_unsigned_byte()
        self.padding1 = inputStream.read_unsigned_byte()
        self.geometry = inputStream.read_unsigned_byte()
        self.padding2 = inputStream.read_unsigned_byte()



class Vector3Double( object ):
    """Three double precision floating point values, x, y, and z. Used for world coordinates Section 6.2.97."""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """ Initializer for Vector3Double"""
        self.x = x
        """ X value"""
        self.y = y
        """ y Value"""
        self.z = z
        """ Z value"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_double(self.x)
        outputStream.write_double(self.y)
        outputStream.write_double(self.z)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.x = inputStream.read_double()
        self.y = inputStream.read_double()
        self.z = inputStream.read_double()



class GridAxis( object ):
    """Grid axis record for fixed data. Section 6.2.41"""

    def __init__(self,
                 domainInitialXi=0.0,
                 domainFinalXi=0.0,
                 domainPointsXi=0,
                 interleafFactor=0,
                 axisType=0,
                 numberOfPointsOnXiAxis=0,
                 initialIndex=0):
        """ Initializer for GridAxis"""
        self.domainInitialXi = domainInitialXi
        """ coordinate of the grid origin or initial value"""
        self.domainFinalXi = domainFinalXi
        """ coordinate of the endpoint or final value"""
        self.domainPointsXi = domainPointsXi
        """ The number of grid points along the Xi domain axis for the enviornmental state data"""
        self.interleafFactor = interleafFactor
        """ interleaf factor along the domain axis."""
        self.axisType = axisType
        """ type of grid axis"""
        self.numberOfPointsOnXiAxis = numberOfPointsOnXiAxis
        """ Number of grid locations along Xi axis"""
        self.initialIndex = initialIndex
        """ initial grid point for the current pdu"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_double(self.domainInitialXi)
        outputStream.write_double(self.domainFinalXi)
        outputStream.write_unsigned_short(self.domainPointsXi)
        outputStream.write_unsigned_byte(self.interleafFactor)
        outputStream.write_unsigned_byte(self.axisType)
        outputStream.write_unsigned_short(self.numberOfPointsOnXiAxis)
        outputStream.write_unsigned_short(self.initialIndex)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.domainInitialXi = inputStream.read_double()
        self.domainFinalXi = inputStream.read_double()
        self.domainPointsXi = inputStream.read_unsigned_short()
        self.interleafFactor = inputStream.read_unsigned_byte()
        self.axisType = inputStream.read_unsigned_byte()
        self.numberOfPointsOnXiAxis = inputStream.read_unsigned_short()
        self.initialIndex = inputStream.read_unsigned_short()



class RecordSpecification( object ):
    """This record shall specify the number of record sets contained in the Record Specification record and the record details. Section 6.2.73."""

    def __init__(self,
                 numberOfRecordSets=0,
                 recordSets=None):
        """ Initializer for RecordSpecification"""
        self.numberOfRecordSets = numberOfRecordSets
        """ The number of record sets"""
        self.recordSets = recordSets or []
        """ variable length list record specifications."""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int( len(self.recordSets))
        for anObj in self.recordSets:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.numberOfRecordSets = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfRecordSets):
            element = null()
            element.parse(inputStream)
            self.recordSets.append(element)




class VariableDatum( object ):
    """the variable datum type, the datum length, and the value for that variable datum type. NOT COMPLETE. Section 6.2.93"""

    def __init__(self,
                 variableDatumID=0,
                 variableDatumLength=0,
                 variableData=None):
        """ Initializer for VariableDatum"""
        self.variableDatumID = variableDatumID
        """ Type of variable datum to be transmitted. 32 bit enumeration defined in EBV"""
        self.variableDatumLength = variableDatumLength
        """ Length, IN BITS, of the variable datum."""
        self.variableData = variableData or []
        """ Variable datum. This can be any number of bits long, depending on the datum."""

    def datumPaddingSizeInBits(self):
        padding = 0
        remainder = self.variableDatumLength % 64
        if remainder != 0:
            padding = 64 - remainder
        return padding

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_int(self.variableDatumID)
        outputStream.write_unsigned_int(self.variableDatumLength)
        for x in range(self.variableDatumLength // 8): # length is in bits
            outputStream.write_byte(self.variableData[x])

        #send padding
        for x in range(self.datumPaddingSizeInBits() // 8):
            outputStream.write_byte(0)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.variableDatumID = inputStream.read_unsigned_int()
        self.variableDatumLength = inputStream.read_unsigned_int()
        for x in range(self.variableDatumLength // 8): # length is in bits
            self.variableData.append(inputStream.read_byte())

        # Skip over padding
        # "This field shall be padded at the end to make the length a multiple of 64-bits."
        for x in range(self.datumPaddingSizeInBits() // 8):
            inputStream.read_byte()



class EventIdentifierLiveEntity( object ):
    """Identifies an event in the world. Use this format for ONLY the LiveEntityPdu. Section 6.2.34."""

    def __init__(self,
                 siteNumber=0,
                 applicationNumber=0,
                 eventNumber=0):
        """ Initializer for EventIdentifierLiveEntity"""
        self.siteNumber = siteNumber
        self.applicationNumber = applicationNumber
        self.eventNumber = eventNumber

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.siteNumber)
        outputStream.write_unsigned_byte(self.applicationNumber)
        outputStream.write_unsigned_short(self.eventNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.siteNumber = inputStream.read_unsigned_byte()
        self.applicationNumber = inputStream.read_unsigned_byte()
        self.eventNumber = inputStream.read_unsigned_short()



class PduHeader( object ):
    """Not used. The PDU Header Record is directly incorporated into the PDU class. Here for completeness only. Section 6.2.66"""

    def __init__(self,
                 protocolVersion=7,
                 exerciseID=0,
                 pduType=0,
                 protocolFamily=0,
                 timestamp=0,
                 pduLength=0,
                 pduStatus=0):
        """ Initializer for PduHeader"""
        self.protocolVersion = protocolVersion
        """ The version of the protocol. 5=DIS-1995, 6=DIS-1998, 7=DIS-2009."""
        self.exerciseID = exerciseID
        """ Exercise ID"""
        self.pduType = pduType
        """ Type of pdu, unique for each PDU class"""
        self.protocolFamily = protocolFamily
        """ value that refers to the protocol family, eg SimulationManagement, etc"""
        self.timestamp = timestamp
        """ Timestamp value"""
        self.pduLength = pduLength
        """ Length, in bytes, of the PDU. Changed name from length to avoid use of Hibernate QL reserved word."""
        self.pduStatus = pduStatus
        """ PDU Status Record. Described in 6.2.67. This field is not present in earlier DIS versions """
        self.padding = 0
        """ zero filled array of padding"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.protocolVersion)
        outputStream.write_unsigned_byte(self.exerciseID)
        outputStream.write_unsigned_byte(self.pduType)
        outputStream.write_unsigned_byte(self.protocolFamily)
        outputStream.write_unsigned_int(self.timestamp)
        outputStream.write_unsigned_byte(self.pduLength)
        outputStream.write_unsigned_short(self.pduStatus)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.protocolVersion = inputStream.read_unsigned_byte()
        self.exerciseID = inputStream.read_unsigned_byte()
        self.pduType = inputStream.read_unsigned_byte()
        self.protocolFamily = inputStream.read_unsigned_byte()
        self.timestamp = inputStream.read_unsigned_int()
        self.pduLength = inputStream.read_unsigned_byte()
        self.pduStatus = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_byte()



class PduSuperclass( object ):
    """The superclass for all PDUs, including classic and Live Entity (LE) PDUs. This incorporates the PduHeader record, section 7.2.2"""

    def __init__(self,
                 protocolVersion=7,
                 exerciseID=0,
                 pduType=0,
                 protocolFamily=0,
                 timestamp=0,
                 pduLength=0,
                 pduStatus=0):
        """ Initializer for PduSuperclass"""
        self.protocolVersion = protocolVersion
        """ The version of the protocol. 5=DIS-1995, 6=DIS-1998, 7=DIS-2009."""
        self.exerciseID = exerciseID
        """ Exercise ID"""
        self.pduType = pduType
        """ Type of pdu, unique for each PDU class"""
        self.protocolFamily = protocolFamily
        """ value that refers to the protocol family, eg SimulationManagement, et"""
        self.timestamp = timestamp
        """ Timestamp value"""
        self.length = pduLength
        """ Length, in bytes, of the PDU"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.protocolVersion)
        outputStream.write_unsigned_byte(self.exerciseID)
        outputStream.write_unsigned_byte(self.pduType)
        outputStream.write_unsigned_byte(self.protocolFamily)
        outputStream.write_unsigned_int(self.timestamp)
        outputStream.write_unsigned_short(self.length)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.protocolVersion = inputStream.read_unsigned_byte()
        self.exerciseID = inputStream.read_unsigned_byte()
        self.pduType = inputStream.read_unsigned_byte()
        self.protocolFamily = inputStream.read_unsigned_byte()
        self.timestamp = inputStream.read_unsigned_int()
        self.length = inputStream.read_unsigned_short()



class CommunicationsNodeID( object ):
    """Identity of a communications node. Section 6.2.48.4"""

    def __init__(self, entityID=None, elementID=0):
        """ Initializer for CommunicationsNodeID"""
        self.entityID = entityID or EntityID()
        self.elementID = elementID

    def serialize(self, outputStream):
        """serialize the class """
        self.entityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.elementID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.entityID.parse(inputStream)
        self.elementID = inputStream.read_unsigned_short()



class ExpendableDescriptor( object ):
    """Burst of chaff or expendable device. Section 6.2.19.4"""

    def __init__(self, expendableType=None):
        """ Initializer for ExpendableDescriptor"""
        self.expendableType = expendableType or EntityType()
        """ Type of the object that exploded"""
        self.padding = 0
        """ Padding"""

    def serialize(self, outputStream):
        """serialize the class """
        self.expendableType.serialize(outputStream)
        outputStream.write_long(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.expendableType.parse(inputStream)
        self.padding = inputStream.read_long()



class PropulsionSystemData( object ):
    """contains information describing the propulsion systems of the entity. This information shall be provided for each active propulsion system defined. Section 6.2.68"""

    def __init__(self, powerSetting=0.0, engineRpm=0.0):
        """ Initializer for PropulsionSystemData"""
        self.powerSetting = powerSetting
        """ powerSetting"""
        self.engineRpm = engineRpm
        """ engine RPMs"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_float(self.powerSetting)
        outputStream.write_float(self.engineRpm)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.powerSetting = inputStream.read_float()
        self.engineRpm = inputStream.read_float()



class LiveEntityIdentifier( object ):
    """The unique designation of each entity in an event or exercise that is contained in a Live Entity PDU. Section 6.2.54 """

    def __init__(self, liveSimulationAddress=None, entityNumber=0):
        """ Initializer for LiveEntityIdentifier"""
        self.liveSimulationAddress = liveSimulationAddress or LiveSimulationAddress()
        """ Live Simulation Address record (see 6.2.54) """
        self.entityNumber = entityNumber
        """ Live entity number """

    def serialize(self, outputStream):
        """serialize the class """
        self.liveSimulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.entityNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.liveSimulationAddress.parse(inputStream)
        self.entityNumber = inputStream.read_unsigned_short()



class SeparationVP( object ):
    """Physical separation of an entity from another entity.  Section 6.2.94.6"""

    def __init__(self,
                 recordType=2,
                 reasonForSeparation=0,
                 preEntityIndicator=0,
                 padding1=0,
                 parentEntityID=None,
                 padding2=0,
                 stationLocation=0):
        """ Initializer for SeparationVP"""
        self.recordType = recordType
        """ the identification of the Variable Parameter record. Enumeration from EBV"""
        self.reasonForSeparation = reasonForSeparation
        """ Reason for separation. EBV"""
        self.preEntityIndicator = preEntityIndicator
        """ Whether the entity existed prior to separation EBV"""
        self.padding1 = padding1
        """ padding"""
        self.parentEntityID = parentEntityID or EntityID()
        """ ID of parent"""
        self.padding2 = padding2
        """ padding"""
        self.stationLocation = stationLocation
        """ Station separated from"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.recordType)
        outputStream.write_unsigned_byte(self.reasonForSeparation)
        outputStream.write_unsigned_byte(self.preEntityIndicator)
        outputStream.write_unsigned_byte(self.padding1)
        self.parentEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding2)
        outputStream.write_unsigned_int(self.stationLocation)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.recordType = inputStream.read_unsigned_byte()
        self.reasonForSeparation = inputStream.read_unsigned_byte()
        self.preEntityIndicator = inputStream.read_unsigned_byte()
        self.padding1 = inputStream.read_unsigned_byte()
        self.parentEntityID.parse(inputStream)
        self.padding2 = inputStream.read_unsigned_short()
        self.stationLocation = inputStream.read_unsigned_int()



class EmitterSystem( object ):
    """This field shall specify information about a particular emitter system. Section 6.2.23."""

    def __init__(self, emitterName=0, emitterFunction=0, emitterIDNumber=0):
        """ Initializer for EmitterSystem"""
        self.emitterName = emitterName
        """ Name of the emitter, 16 bit enumeration"""
        self.emitterFunction = emitterFunction
        """ function of the emitter, 8 bit enumeration"""
        self.emitterIDNumber = emitterIDNumber
        """ emitter ID, 8 bit enumeration"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_short(self.emitterName)
        outputStream.write_unsigned_byte(self.emitterFunction)
        outputStream.write_unsigned_byte(self.emitterIDNumber)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.emitterName = inputStream.read_unsigned_short()
        self.emitterFunction = inputStream.read_unsigned_byte()
        self.emitterIDNumber = inputStream.read_unsigned_byte()



class PduStatus( object ):
    """PDU Status. These are a series of bit fields. Represented here as just a byte. Section 6.2.67"""

    def __init__(self, pduStatus=0):
        """ Initializer for PduStatus"""
        self.pduStatus = pduStatus
        """ Bit fields. The semantics of the bit fields depend on the PDU type"""

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_unsigned_byte(self.pduStatus)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        self.pduStatus = inputStream.read_unsigned_byte()




class LiveEntityPdu( PduSuperclass ):
    """The live entity PDUs have a header with some different field names, but the same length. Section 9.3.2"""

    def __init__(self, subprotocolNumber=0):
        """ Initializer for LiveEntityPdu"""
        super(LiveEntityPdu, self).__init__()
        self.subprotocolNumber = subprotocolNumber
        """ Subprotocol used to decode the PDU. Section 13 of EBV."""
        self.padding = 0
        """ zero-filled array of padding"""

    def serialize(self, outputStream):
        """serialize the class """
        super( LiveEntityPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_short(self.subprotocolNumber)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( LiveEntityPdu, self).parse(inputStream)
        self.subprotocolNumber = inputStream.read_unsigned_short()
        self.padding = inputStream.read_unsigned_byte()



class Pdu( PduSuperclass ):
    """Adds some fields to the the classic PDU"""

    def __init__(self, pduStatus=0):
        """ Initializer for Pdu"""
        super(Pdu, self).__init__()
        self.pduStatus = pduStatus
        """ PDU Status Record. Described in 6.2.67. This field is not present in earlier DIS versions """
        self.padding = 0
        """ zero-filled array of padding"""

    def serialize(self, outputStream):
        """serialize the class """
        super( Pdu, self ).serialize(outputStream)
        outputStream.write_unsigned_byte(self.pduStatus)
        outputStream.write_unsigned_byte(self.padding)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( Pdu, self).parse(inputStream)
        self.pduStatus = inputStream.read_unsigned_byte()
        self.padding = inputStream.read_unsigned_byte()



class EntityInformationFamilyPdu( Pdu ):
    """Section 5.3.3. Common superclass for EntityState, Collision, collision-elastic, and entity state update PDUs. This should be abstract. COMPLETE"""

    def __init__(self):
        """ Initializer for EntityInformationFamilyPdu"""
        super(EntityInformationFamilyPdu, self).__init__()
        self.protocolFamily = 1
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( EntityInformationFamilyPdu, self ).serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( EntityInformationFamilyPdu, self).parse(inputStream)



class LogisticsFamilyPdu( Pdu ):
    """ Abstract superclass for logistics PDUs. Section 7.4 COMPLETE"""

    def __init__(self):
        """ Initializer for LogisticsFamilyPdu"""
        super(LogisticsFamilyPdu, self).__init__()
        self.protocolFamily = 3
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( LogisticsFamilyPdu, self ).serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( LogisticsFamilyPdu, self).parse(inputStream)



class EntityStateUpdatePdu( EntityInformationFamilyPdu ):
    """Nonstatic information about a particular entity may be communicated by issuing an Entity State Update PDU. Section 7.2.5. COMPLETE"""

    def __init__(self,
                 entityID=None,
                 numberOfVariableParameters=0,
                 entityLinearVelocity=None,
                 entityLocation=None,
                 entityOrientation=None,
                 entityAppearance=0,
                 variableParameters=None):
        """ Initializer for EntityStateUpdatePdu"""
        super(EntityStateUpdatePdu, self).__init__()
        self.entityID = entityID or EntityID()
        """ This field shall identify the entity issuing the PDU, and shall be represented by an Entity Identifier record (see 6.2.28)."""
        self.padding1 = 0
        """ Padding"""
        self.numberOfVariableParameters = numberOfVariableParameters
        """ This field shall specify the number of variable parameters present. This field shall be represented by an 8-bit unsigned integer (see Annex I)."""
        self.entityLinearVelocity = entityLinearVelocity or Vector3Float()
        """ This field shall specify an entitys linear velocity. The coordinate system for an entitys linear velocity depends on the dead reckoning algorithm used. This field shall be represented by a Linear Velocity Vector record [see 6.2.95 item c)])."""
        self.entityLocation = entityLocation or Vector3Double()
        """ This field shall specify an entitys physical location in the simulated world and shall be represented by a World Coordinates record (see 6.2.97)."""
        self.entityOrientation = entityOrientation or EulerAngles()
        """ This field shall specify an entitys orientation and shall be represented by an Euler Angles record (see 6.2.33)."""
        self.entityAppearance = entityAppearance
        """ This field shall specify the dynamic changes to the entity's appearance attributes. This field shall be represented by an Entity Appearance record (see 6.2.26)."""
        self.variableParameters = variableParameters or []
        """ This field shall specify the parameter values for each Variable Parameter record that is included (see 6.2.93 and Annex I)."""
        self.pduType = 67
        """ initialize value """
        self.protocolFamily = 1
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( EntityStateUpdatePdu, self ).serialize(outputStream)
        self.entityID.serialize(outputStream)
        outputStream.write_byte(self.padding1)
        outputStream.write_unsigned_byte( len(self.variableParameters))
        self.entityLinearVelocity.serialize(outputStream)
        self.entityLocation.serialize(outputStream)
        self.entityOrientation.serialize(outputStream)
        outputStream.write_unsigned_int(self.entityAppearance)
        for anObj in self.variableParameters:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( EntityStateUpdatePdu, self).parse(inputStream)
        self.entityID.parse(inputStream)
        self.padding1 = inputStream.read_byte()
        self.numberOfVariableParameters = inputStream.read_unsigned_byte()
        self.entityLinearVelocity.parse(inputStream)
        self.entityLocation.parse(inputStream)
        self.entityOrientation.parse(inputStream)
        self.entityAppearance = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfVariableParameters):
            element = VariableParameter()
            element.parse(inputStream)
            self.variableParameters.append(element)




class ServiceRequestPdu( LogisticsFamilyPdu ):
    """Service Request PDU shall be used to communicate information associated with                            one entity requesting a service from another). Section 7.4.2 COMPLETE"""

    def __init__(self,
                 requestingEntityID=None,
                 servicingEntityID=None,
                 serviceTypeRequested=0,
                 numberOfSupplyTypes=0,
                 supplies=None):
        """ Initializer for ServiceRequestPdu"""
        super(ServiceRequestPdu, self).__init__()
        self.requestingEntityID = requestingEntityID or EntityID()
        """ Entity that is requesting service (see 6.2.28), Section 7.4.2"""
        self.servicingEntityID = servicingEntityID or EntityID()
        """ Entity that is providing the service (see 6.2.28), Section 7.4.2"""
        self.serviceTypeRequested = serviceTypeRequested
        """ Type of service requested, Section 7.4.2"""
        self.numberOfSupplyTypes = numberOfSupplyTypes
        """ How many requested, Section 7.4.2"""
        self.serviceRequestPadding = 0
        """ padding"""
        self.supplies = supplies or []
        self.pduType = 5
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ServiceRequestPdu, self ).serialize(outputStream)
        self.requestingEntityID.serialize(outputStream)
        self.servicingEntityID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.serviceTypeRequested)
        outputStream.write_unsigned_byte( len(self.supplies))
        outputStream.write_short(self.serviceRequestPadding)
        for anObj in self.supplies:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ServiceRequestPdu, self).parse(inputStream)
        self.requestingEntityID.parse(inputStream)
        self.servicingEntityID.parse(inputStream)
        self.serviceTypeRequested = inputStream.read_unsigned_byte()
        self.numberOfSupplyTypes = inputStream.read_unsigned_byte()
        self.serviceRequestPadding = inputStream.read_short()
        for idx in range(0, self.numberOfSupplyTypes):
            element = null()
            element.parse(inputStream)
            self.supplies.append(element)




class RepairCompletePdu( LogisticsFamilyPdu ):
    """Section 7.4.6. Service Request PDU is received and repair is complete. COMPLETE"""

    def __init__(self,
                 receivingEntityID=None,
                 repairingEntityID=None,
                 repair=0):
        """ Initializer for RepairCompletePdu"""
        super(RepairCompletePdu, self).__init__()
        self.receivingEntityID = receivingEntityID or EntityID()
        """ Entity that is receiving service.  See 6.2.28"""
        self.repairingEntityID = repairingEntityID or EntityID()
        """ Entity that is supplying.  See 6.2.28"""
        self.repair = repair
        """ Enumeration for type of repair.  See 6.2.74"""
        self.padding4 = 0
        """ padding, number prevents conflict with superclass ivar name"""
        self.pduType = 9
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( RepairCompletePdu, self ).serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.repairingEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.repair)
        outputStream.write_short(self.padding4)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( RepairCompletePdu, self).parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.repairingEntityID.parse(inputStream)
        self.repair = inputStream.read_unsigned_short()
        self.padding4 = inputStream.read_short()



class SyntheticEnvironmentFamilyPdu( Pdu ):
    """Section 5.3.11: Abstract superclass for synthetic environment PDUs"""

    def __init__(self):
        """ Initializer for SyntheticEnvironmentFamilyPdu"""
        super(SyntheticEnvironmentFamilyPdu, self).__init__()
        self.protocolFamily = 9
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( SyntheticEnvironmentFamilyPdu, self ).serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( SyntheticEnvironmentFamilyPdu, self).parse(inputStream)



class CollisionPdu( EntityInformationFamilyPdu ):
    """Section 7.2.3 Collisions between entities shall be communicated by issuing a Collision PDU. COMPLETE"""

    def __init__(self,
                 issuingEntityID=None,
                 collidingEntityID=None,
                 eventID=None,
                 collisionType=0,
                 velocity=None,
                 mass=0.0,
                 location=None):
        """ Initializer for CollisionPdu"""
        super(CollisionPdu, self).__init__()
        self.issuingEntityID = issuingEntityID or EntityID()
        """ This field shall identify the entity that is issuing the PDU, and shall be represented by an Entity Identifier record (see 6.2.28)."""
        self.collidingEntityID = collidingEntityID or EntityID()
        """ This field shall identify the entity that has collided with the issuing entity (see 5.3.3.4). This field shall be represented by an Entity Identifier record (see 6.2.28)."""
        self.eventID = eventID or EventIdentifier()
        """ This field shall contain an identification generated by the issuing simulation application to associate related collision events. This field shall be represented by an Event Identifier record (see 6.2.34)."""
        self.collisionType = collisionType
        """ This field shall identify the type of collision. The Collision Type field shall be represented by an 8-bit record of enumerations"""
        self.pad = 0
        """ some padding"""
        self.velocity = velocity or Vector3Float()
        """ This field shall contain the velocity (at the time the collision is detected) of the issuing entity. The velocity shall be represented in world coordinates. This field shall be represented by the Linear Velocity Vector record [see 6.2.95 item c)]."""
        self.mass = mass
        """ This field shall contain the mass of the issuing entity, and shall be represented by a 32-bit floating point number representing kilograms."""
        self.location = location or Vector3Float()
        """ This field shall specify the location of the collision with respect to the entity with which the issuing entity collided. The Location field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""
        self.pduType = 4
        """ initialize value """
        self.protocolFamily = 1
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( CollisionPdu, self ).serialize(outputStream)
        self.issuingEntityID.serialize(outputStream)
        self.collidingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.collisionType)
        outputStream.write_byte(self.pad)
        self.velocity.serialize(outputStream)
        outputStream.write_float(self.mass)
        self.location.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( CollisionPdu, self).parse(inputStream)
        self.issuingEntityID.parse(inputStream)
        self.collidingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.collisionType = inputStream.read_unsigned_byte()
        self.pad = inputStream.read_byte()
        self.velocity.parse(inputStream)
        self.mass = inputStream.read_float()
        self.location.parse(inputStream)



class RepairResponsePdu( LogisticsFamilyPdu ):
    """Section 7.4.7. Sent after repair complete PDU. COMPLETE"""

    def __init__(self,
                 receivingEntityID=None,
                 repairingEntityID=None,
                 repairResult=0):
        """ Initializer for RepairResponsePdu"""
        super(RepairResponsePdu, self).__init__()
        self.receivingEntityID = receivingEntityID or EntityID()
        """ Entity that requested repairs.  See 6.2.28"""
        self.repairingEntityID = repairingEntityID or EntityID()
        """ Entity that is repairing.  See 6.2.28"""
        self.repairResult = repairResult
        """ Result of repair operation"""
        self.padding1 = 0
        """ padding"""
        self.padding2 = 0
        """ padding"""
        self.pduType = 10
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( RepairResponsePdu, self ).serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.repairingEntityID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.repairResult)
        outputStream.write_short(self.padding1)
        outputStream.write_byte(self.padding2)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( RepairResponsePdu, self).parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.repairingEntityID.parse(inputStream)
        self.repairResult = inputStream.read_unsigned_byte()
        self.padding1 = inputStream.read_short()
        self.padding2 = inputStream.read_byte()



class SimulationManagementFamilyPdu( Pdu ):
    """Section 7.5 Abstract superclass for PDUs relating to the simulation itself. COMPLETE"""

    def __init__(self, originatingEntityID=None, receivingEntityID=None):
        """ Initializer for SimulationManagementFamilyPdu"""
        super(SimulationManagementFamilyPdu, self).__init__()
        self.originatingEntityID = originatingEntityID or EntityID()
        """ Entity that is sending message"""
        self.receivingEntityID = receivingEntityID or EntityID()
        """ Entity that is intended to receive message"""
        self.protocolFamily = 5
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( SimulationManagementFamilyPdu, self ).serialize(outputStream)
        self.originatingEntityID.serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( SimulationManagementFamilyPdu, self).parse(inputStream)
        self.originatingEntityID.parse(inputStream)
        self.receivingEntityID.parse(inputStream)



class DataQueryPdu( SimulationManagementFamilyPdu ):
    """Section 7.5.9. Request for data from an entity. COMPLETE"""

    def __init__(self,
                 requestID=0,
                 timeInterval=0,
                 numberOfFixedDatumIDs=0,
                 numberOfVariableDatumIDs=0,
                 fixedDatumIDs=None,
                 variableDatumIDs=None):
        """ Initializer for DataQueryPdu"""
        super(DataQueryPdu, self).__init__()
        self.requestID = 0
        """ ID of request"""
        self.timeInterval = 0
        """ time issues between issues of Data PDUs. Zero means send once only."""
        self.numberOfFixedDatumIDs = numberOfFixedDatumIDs
        """ Number of fixed datum records"""
        self.numberOfVariableDatumIDs = numberOfVariableDatumIDs
        """ Number of variable datum records"""
        self.fixedDatumIDs = fixedDatumIDs or []
        """ variable length list of fixed datums"""
        self.variableDatumIDs = variableDatumIDs or []
        """ variable length list of variable length datums"""
        self.pduType = 18
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DataQueryPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.timeInterval)
        outputStream.write_unsigned_int( len(self.fixedDatumIDs))
        outputStream.write_unsigned_int( len(self.variableDatumIDs))
        for anObj in self.fixedDatumIDs:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumIDs:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DataQueryPdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.timeInterval = inputStream.read_unsigned_int()
        self.numberOfFixedDatumIDs = inputStream.read_unsigned_int()
        self.numberOfVariableDatumIDs = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumIDs):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumIDs.append(element)

        for idx in range(0, self.numberOfVariableDatumIDs):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumIDs.append(element)




class LinearObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
    """: Information abut the addition or modification of a synthecic enviroment object that      is anchored to the terrain with a single point and has size or orientation. Section 7.10.5 COMPLETE"""

    def __init__(self,
                 objectID=None,
                 referencedObjectID=None,
                 updateNumber=0,
                 forceID=0,
                 numberOfSegments=0,
                 requesterID=None,
                 receivingID=None,
                 objectType=None,
                 linearSegmentParameters=None):
        """ Initializer for LinearObjectStatePdu"""
        super(LinearObjectStatePdu, self).__init__()
        self.objectID = objectID or EntityID()
        """ Object in synthetic environment"""
        self.referencedObjectID = referencedObjectID or EntityID()
        """ Object with which this point object is associated"""
        self.updateNumber = updateNumber
        """ unique update number of each state transition of an object"""
        self.forceID = forceID
        """ force ID"""
        self.numberOfSegments = numberOfSegments
        """ number of linear segment parameters"""
        self.requesterID = requesterID or SimulationAddress()
        """ requesterID"""
        self.receivingID = receivingID or SimulationAddress()
        """ receiver ID"""
        self.objectType = objectType or ObjectType()
        """ Object type"""
        self.linearSegmentParameters = linearSegmentParameters or []
        """ Linear segment parameters"""
        self.pduType = 44
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( LinearObjectStatePdu, self ).serialize(outputStream)
        self.objectID.serialize(outputStream)
        self.referencedObjectID.serialize(outputStream)
        outputStream.write_unsigned_short(self.updateNumber)
        outputStream.write_unsigned_byte(self.forceID)
        outputStream.write_unsigned_byte( len(self.linearSegmentParameters))
        self.requesterID.serialize(outputStream)
        self.receivingID.serialize(outputStream)
        self.objectType.serialize(outputStream)
        for anObj in self.linearSegmentParameters:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( LinearObjectStatePdu, self).parse(inputStream)
        self.objectID.parse(inputStream)
        self.referencedObjectID.parse(inputStream)
        self.updateNumber = inputStream.read_unsigned_short()
        self.forceID = inputStream.read_unsigned_byte()
        self.numberOfSegments = inputStream.read_unsigned_byte()
        self.requesterID.parse(inputStream)
        self.receivingID.parse(inputStream)
        self.objectType.parse(inputStream)
        for idx in range(0, self.numberOfSegments):
            element = null()
            element.parse(inputStream)
            self.linearSegmentParameters.append(element)




class CreateEntityPdu( SimulationManagementFamilyPdu ):
    """Section 7.5.2. Create a new entity. COMPLETE"""

    def __init__(self, requestID=0):
        """ Initializer for CreateEntityPdu"""
        super(CreateEntityPdu, self).__init__()
        self.requestID = requestID
        """ Identifier for the request.  See 6.2.75"""
        self.pduType = 11
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( CreateEntityPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( CreateEntityPdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()



class RadioCommunicationsFamilyPdu( Pdu ):
    """ Abstract superclass for radio communications PDUs. Section 7.7"""

    def __init__(self):
        """ Initializer for RadioCommunicationsFamilyPdu"""
        super(RadioCommunicationsFamilyPdu, self).__init__()
        self.protocolFamily = 4
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( RadioCommunicationsFamilyPdu, self ).serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( RadioCommunicationsFamilyPdu, self).parse(inputStream)



class IntercomSignalPdu( RadioCommunicationsFamilyPdu ):
    """ Actual transmission of intercome voice data. Section 7.7.5. COMPLETE"""

    def __init__(self,
                 entityID=None,
                 communicationsDeviceID=0,
                 encodingScheme=0,
                 tdlType=0,
                 sampleRate=0,
                 dataLength=0,
                 samples=0,
                 data=None):
        """ Initializer for IntercomSignalPdu"""
        super(IntercomSignalPdu, self).__init__()
        self.entityID = entityID or EntityID()
        """ entity ID"""
        self.communicationsDeviceID = communicationsDeviceID
        """ ID of communications device"""
        self.encodingScheme = encodingScheme
        """ encoding scheme"""
        self.tdlType = tdlType
        """ tactical data link type"""
        self.sampleRate = sampleRate
        """ sample rate"""
        self.dataLength = dataLength
        """ data length"""
        self.samples = samples
        """ samples"""
        self.data = data or []
        """ data bytes"""
        self.pduType = 31
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( IntercomSignalPdu, self ).serialize(outputStream)
        self.entityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.communicationsDeviceID)
        outputStream.write_unsigned_short(self.encodingScheme)
        outputStream.write_unsigned_short(self.tdlType)
        outputStream.write_unsigned_int(self.sampleRate)
        outputStream.write_unsigned_short( len(self.data))
        outputStream.write_unsigned_short(self.samples)
        for anObj in self.data:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( IntercomSignalPdu, self).parse(inputStream)
        self.entityID.parse(inputStream)
        self.communicationsDeviceID = inputStream.read_unsigned_short()
        self.encodingScheme = inputStream.read_unsigned_short()
        self.tdlType = inputStream.read_unsigned_short()
        self.sampleRate = inputStream.read_unsigned_int()
        self.dataLength = inputStream.read_unsigned_short()
        self.samples = inputStream.read_unsigned_short()
        for idx in range(0, self.dataLength):
            element = null()
            element.parse(inputStream)
            self.data.append(element)




class RemoveEntityPdu( SimulationManagementFamilyPdu ):
    """Section 7.5.3 The removal of an entity from an exercise shall be communicated with a Remove Entity PDU. COMPLETE"""

    def __init__(self, requestID=0):
        """ Initializer for RemoveEntityPdu"""
        super(RemoveEntityPdu, self).__init__()
        self.requestID = requestID
        """ This field shall identify the specific and unique start/resume request being made by the SM"""
        self.pduType = 12
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( RemoveEntityPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( RemoveEntityPdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()



class ResupplyReceivedPdu( LogisticsFamilyPdu ):
    """Section 7.4.4. Receipt of supplies is communicated by issuing Resupply Received PDU. COMPLETE"""

    def __init__(self,
                 receivingEntityID=None,
                 supplyingEntityID=None,
                 numberOfSupplyTypes=0,
                 supplies=None):
        """ Initializer for ResupplyReceivedPdu"""
        super(ResupplyReceivedPdu, self).__init__()
        self.receivingEntityID = receivingEntityID or EntityID()
        """ Entity that is receiving service.  Shall be represented by Entity Identifier record (see 6.2.28)"""
        self.supplyingEntityID = supplyingEntityID or EntityID()
        """ Entity that is supplying.  Shall be represented by Entity Identifier record (see 6.2.28)"""
        self.numberOfSupplyTypes = numberOfSupplyTypes
        """ How many supplies are taken by receiving entity"""
        self.padding1 = 0
        """ padding"""
        self.padding2 = 0
        """ padding"""
        self.supplies = supplies or []
        """ Type and amount of supplies for each specified supply type.  See 6.2.85 for supply quantity record."""
        self.pduType = 7
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ResupplyReceivedPdu, self ).serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.supplyingEntityID.serialize(outputStream)
        outputStream.write_unsigned_byte( len(self.supplies))
        outputStream.write_short(self.padding1)
        outputStream.write_byte(self.padding2)
        for anObj in self.supplies:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ResupplyReceivedPdu, self).parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.supplyingEntityID.parse(inputStream)
        self.numberOfSupplyTypes = inputStream.read_unsigned_byte()
        self.padding1 = inputStream.read_short()
        self.padding2 = inputStream.read_byte()
        for idx in range(0, self.numberOfSupplyTypes):
            element = null()
            element.parse(inputStream)
            self.supplies.append(element)




class WarfareFamilyPdu( Pdu ):
    """abstract superclass for fire and detonation pdus that have shared information. Section 7.3 COMPLETE"""

    def __init__(self,
                 firingEntityID=None,
                 targetEntityID=None):
        """ Initializer for WarfareFamilyPdu"""
        super(WarfareFamilyPdu, self).__init__()
        self.firingEntityID = firingEntityID or EntityID()
        """ ID of the entity that shot"""
        self.targetEntityID = targetEntityID or EntityID()
        """ ID of the entity that is being shot at"""
        self.protocolFamily = 2
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( WarfareFamilyPdu, self ).serialize(outputStream)
        self.firingEntityID.serialize(outputStream)
        self.targetEntityID.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( WarfareFamilyPdu, self).parse(inputStream)
        self.firingEntityID.parse(inputStream)
        self.targetEntityID.parse(inputStream)



class CollisionElasticPdu( EntityInformationFamilyPdu ):
    """Information about elastic collisions in a DIS exercise shall be communicated using a Collision-Elastic PDU. Section 7.2.4. COMPLETE"""

    def __init__(self,
                 issuingEntityID=None,
                 collidingEntityID=None,
                 collisionEventID=None,
                 contactVelocity=None,
                 mass=0.0,
                 locationOfImpact=None,
                 collisionIntermediateResultXX=0.0,
                 collisionIntermediateResultXY=0.0,
                 collisionIntermediateResultXZ=0.0,
                 collisionIntermediateResultYY=0.0,
                 collisionIntermediateResultYZ=0.0,
                 collisionIntermediateResultZZ=0.0,
                 unitSurfaceNormal=None,
                 coefficientOfRestitution=0.0):
        """ Initializer for CollisionElasticPdu"""
        super(CollisionElasticPdu, self).__init__()
        self.issuingEntityID = issuingEntityID or EntityID()
        """ This field shall identify the entity that is issuing the PDU and shall be represented by an Entity Identifier record (see 6.2.28)"""
        self.collidingEntityID = collidingEntityID or EntityID()
        """ This field shall identify the entity that has collided with the issuing entity. This field shall be a valid identifier of an entity or server capable of responding to the receipt of this Collision-Elastic PDU. This field shall be represented by an Entity Identifier record (see 6.2.28)."""
        self.collisionEventID = collisionEventID or EventIdentifier()
        """ This field shall contain an identification generated by the issuing simulation application to associate related collision events. This field shall be represented by an Event Identifier record (see 6.2.34)."""
        self.pad = 0
        """ some padding"""
        self.contactVelocity = contactVelocity or Vector3Float()
        """ This field shall contain the velocity at the time the collision is detected at the point the collision is detected. The velocity shall be represented in world coordinates. This field shall be represented by the Linear Velocity Vector record [see 6.2.95 item c)]"""
        self.mass = mass
        """ This field shall contain the mass of the issuing entity and shall be represented by a 32-bit floating point number representing kilograms"""
        self.locationOfImpact = locationOfImpact or Vector3Float()
        """ This field shall specify the location of the collision with respect to the entity with which the issuing entity collided. This field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""
        self.collisionIntermediateResultXX = collisionIntermediateResultXX
        """ These six records represent the six independent components of a positive semi-definite matrix formed by pre-multiplying and post-multiplying the tensor of inertia, by the anti-symmetric matrix generated by the moment arm, and shall be represented by 32-bit floating point numbers (see 5.3.4.4)"""
        self.collisionIntermediateResultXY = collisionIntermediateResultXY
        """ tensor values"""
        self.collisionIntermediateResultXZ = collisionIntermediateResultXZ
        """ tensor values"""
        self.collisionIntermediateResultYY = collisionIntermediateResultYY
        """ tensor values"""
        self.collisionIntermediateResultYZ = collisionIntermediateResultYZ
        """ tensor values"""
        self.collisionIntermediateResultZZ = collisionIntermediateResultZZ
        """ tensor values"""
        self.unitSurfaceNormal = unitSurfaceNormal or Vector3Float()
        """ This record shall represent the normal vector to the surface at the point of collision detection. The surface normal shall be represented in world coordinates. This field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""
        self.coefficientOfRestitution = coefficientOfRestitution
        """ This field shall represent the degree to which energy is conserved in a collision and shall be represented by a 32-bit floating point number. In addition, it represents a free parameter by which simulation application developers may tune their collision interactions."""
        self.pduType = 66
        """ initialize value """
        self.protocolFamily = 1
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( CollisionElasticPdu, self ).serialize(outputStream)
        self.issuingEntityID.serialize(outputStream)
        self.collidingEntityID.serialize(outputStream)
        self.collisionEventID.serialize(outputStream)
        outputStream.write_short(self.pad)
        self.contactVelocity.serialize(outputStream)
        outputStream.write_float(self.mass)
        self.locationOfImpact.serialize(outputStream)
        outputStream.write_float(self.collisionIntermediateResultXX)
        outputStream.write_float(self.collisionIntermediateResultXY)
        outputStream.write_float(self.collisionIntermediateResultXZ)
        outputStream.write_float(self.collisionIntermediateResultYY)
        outputStream.write_float(self.collisionIntermediateResultYZ)
        outputStream.write_float(self.collisionIntermediateResultZZ)
        self.unitSurfaceNormal.serialize(outputStream)
        outputStream.write_float(self.coefficientOfRestitution)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( CollisionElasticPdu, self).parse(inputStream)
        self.issuingEntityID.parse(inputStream)
        self.collidingEntityID.parse(inputStream)
        self.collisionEventID.parse(inputStream)
        self.pad = inputStream.read_short()
        self.contactVelocity.parse(inputStream)
        self.mass = inputStream.read_float()
        self.locationOfImpact.parse(inputStream)
        self.collisionIntermediateResultXX = inputStream.read_float()
        self.collisionIntermediateResultXY = inputStream.read_float()
        self.collisionIntermediateResultXZ = inputStream.read_float()
        self.collisionIntermediateResultYY = inputStream.read_float()
        self.collisionIntermediateResultYZ = inputStream.read_float()
        self.collisionIntermediateResultZZ = inputStream.read_float()
        self.unitSurfaceNormal.parse(inputStream)
        self.coefficientOfRestitution = inputStream.read_float()



class ActionRequestPdu( SimulationManagementFamilyPdu ):
    """Section 7.5.7. Request from simulation manager to a managed entity to perform a specified action. COMPLETE"""

    def __init__(self,
                 requestID=0,
                 actionID=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecordList=None):
        """ Initializer for ActionRequestPdu"""
        super(ActionRequestPdu, self).__init__()
        self.requestID = requestID
        """ identifies the request being made by the simulaton manager"""
        self.actionID = actionID
        """ identifies the particular action being requested(see Section 7 of SISO-REF-010)."""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Number of fixed datum records"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ Number of variable datum records"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ variable length list of fixed datums"""
        self.variableDatumRecords = variableDatumRecords or []
        """ variable length list of variable length datums"""
        self.pduType = 16
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ActionRequestPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.actionID)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ActionRequestPdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.actionID = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class AcknowledgePdu( SimulationManagementFamilyPdu ):
    """Section 7.5.6. Acknowledge the receipt of a start/resume, stop/freeze, or RemoveEntityPDU. COMPLETE"""

    def __init__(self, acknowledgeFlag=0, responseFlag=0, requestID=0):
        """ Initializer for AcknowledgePdu"""
        super(AcknowledgePdu, self).__init__()
        self.acknowledgeFlag = acknowledgeFlag
        """ type of message being acknowledged"""
        self.responseFlag = responseFlag
        """ Whether or not the receiving entity was able to comply with the request"""
        self.requestID = requestID
        """ Request ID that is unique"""
        self.pduType = 15
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( AcknowledgePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_short(self.acknowledgeFlag)
        outputStream.write_unsigned_short(self.responseFlag)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( AcknowledgePdu, self).parse(inputStream)
        self.acknowledgeFlag = inputStream.read_unsigned_short()
        self.responseFlag = inputStream.read_unsigned_short()
        self.requestID = inputStream.read_unsigned_int()



class DistributedEmissionsFamilyPdu( Pdu ):
    """Section 5.3.7. Electronic Emissions. Abstract superclass for distributed emissions PDU"""

    def __init__(self):
        """ Initializer for DistributedEmissionsFamilyPdu"""
        super(DistributedEmissionsFamilyPdu, self).__init__()
        self.protocolFamily = 6
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DistributedEmissionsFamilyPdu, self ).serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DistributedEmissionsFamilyPdu, self).parse(inputStream)



class SimulationManagementWithReliabilityFamilyPdu( Pdu ):
    """Section 5.3.12: Abstract superclass for reliable simulation management PDUs"""

    def __init__(self, originatingEntityID=None, receivingEntityID=None):
        """ Initializer for SimulationManagementWithReliabilityFamilyPdu"""
        super(SimulationManagementWithReliabilityFamilyPdu, self).__init__()
        self.originatingEntityID = originatingEntityID or EntityID()
        """ Object originatig the request"""
        self.receivingEntityID = receivingEntityID or EntityID()
        """ Object with which this point object is associated"""
        self.protocolFamily = 10
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( SimulationManagementWithReliabilityFamilyPdu, self ).serialize(outputStream)
        self.originatingEntityID.serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( SimulationManagementWithReliabilityFamilyPdu, self).parse(inputStream)
        self.originatingEntityID.parse(inputStream)
        self.receivingEntityID.parse(inputStream)



class ActionRequestReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.6: request from a simulation manager to a managed entity to perform a specified action. COMPLETE"""

    def __init__(self,
                 requiredReliabilityService=0,
                 requestID=0,
                 actionID=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for ActionRequestReliablePdu"""
        super(ActionRequestReliablePdu, self).__init__()
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding"""
        self.pad2 = 0
        """ padding"""
        self.requestID = requestID
        """ request ID"""
        self.actionID = actionID
        """ request ID"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Fixed datum record count"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ variable datum record count"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ Fixed datum records"""
        self.variableDatumRecords = variableDatumRecords or []
        """ Variable datum records"""
        self.pduType = 56
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ActionRequestReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.actionID)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ActionRequestReliablePdu, self).parse(inputStream)
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.requestID = inputStream.read_unsigned_int()
        self.actionID = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class DesignatorPdu( DistributedEmissionsFamilyPdu ):
    """Section 5.3.7.2. Handles designating operations. COMPLETE"""

    def __init__(self,
                 designatingEntityID=None,
                 codeName=0,
                 designatedEntityID=None,
                 designatorCode=0,
                 designatorPower=0.0,
                 designatorWavelength=0.0,
                 designatorSpotWrtDesignated=None,
                 designatorSpotLocation=None,
                 deadReckoningAlgorithm=0,
                 entityLinearAcceleration=None):
        """ Initializer for DesignatorPdu"""
        super(DesignatorPdu, self).__init__()
        self.designatingEntityID = designatingEntityID or EntityID()
        """ ID of the entity designating"""
        self.codeName = codeName
        """ This field shall specify a unique emitter database number assigned to  differentiate between otherwise similar or identical emitter beams within an emitter system."""
        self.designatedEntityID = designatedEntityID or EntityID()
        """ ID of the entity being designated"""
        self.designatorCode = designatorCode
        """ This field shall identify the designator code being used by the designating entity """
        self.designatorPower = designatorPower
        """ This field shall identify the designator output power in watts"""
        self.designatorWavelength = designatorWavelength
        """ This field shall identify the designator wavelength in units of microns"""
        self.designatorSpotWrtDesignated = designatorSpotWrtDesignated or Vector3Float()
        """ designator spot wrt the designated entity"""
        self.designatorSpotLocation = designatorSpotLocation or Vector3Double()
        """ designator spot wrt the designated entity"""
        self.deadReckoningAlgorithm = deadReckoningAlgorithm
        """ Dead reckoning algorithm"""
        self.padding1 = 0
        """ padding"""
        self.padding2 = 0
        """ padding"""
        self.entityLinearAcceleration = entityLinearAcceleration or Vector3Float()
        """ linear acceleration of entity"""
        self.pduType = 24
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DesignatorPdu, self ).serialize(outputStream)
        self.designatingEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.codeName)
        self.designatedEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.designatorCode)
        outputStream.write_float(self.designatorPower)
        outputStream.write_float(self.designatorWavelength)
        self.designatorSpotWrtDesignated.serialize(outputStream)
        self.designatorSpotLocation.serialize(outputStream)
        outputStream.write_byte(self.deadReckoningAlgorithm)
        outputStream.write_unsigned_short(self.padding1)
        outputStream.write_byte(self.padding2)
        self.entityLinearAcceleration.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DesignatorPdu, self).parse(inputStream)
        self.designatingEntityID.parse(inputStream)
        self.codeName = inputStream.read_unsigned_short()
        self.designatedEntityID.parse(inputStream)
        self.designatorCode = inputStream.read_unsigned_short()
        self.designatorPower = inputStream.read_float()
        self.designatorWavelength = inputStream.read_float()
        self.designatorSpotWrtDesignated.parse(inputStream)
        self.designatorSpotLocation.parse(inputStream)
        self.deadReckoningAlgorithm = inputStream.read_byte()
        self.padding1 = inputStream.read_unsigned_short()
        self.padding2 = inputStream.read_byte()
        self.entityLinearAcceleration.parse(inputStream)



class StopFreezePdu( SimulationManagementFamilyPdu ):
    """Section 7.5.5. Stop or freeze an enity (or exercise). COMPLETE"""

    def __init__(self,
                 realWorldTime=None,
                 reason=0,
                 frozenBehavior=0,
                 requestID=0):
        """ Initializer for StopFreezePdu"""
        super(StopFreezePdu, self).__init__()
        self.realWorldTime = realWorldTime or ClockTime()
        """ real-world(UTC) time at which the entity shall stop or freeze in the exercise"""
        self.reason = reason
        """ Reason the simulation was stopped or frozen (see section 7 of SISO-REF-010) represented by an 8-bit enumeration"""
        self.frozenBehavior = frozenBehavior
        """ Internal behavior of the entity(or simulation) and its appearance while frozen to the other participants"""
        self.padding1 = 0
        """ padding"""
        self.requestID = requestID
        """ Request ID that is unique"""
        self.pduType = 14
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( StopFreezePdu, self ).serialize(outputStream)
        self.realWorldTime.serialize(outputStream)
        outputStream.write_unsigned_byte(self.reason)
        outputStream.write_unsigned_byte(self.frozenBehavior)
        outputStream.write_short(self.padding1)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( StopFreezePdu, self).parse(inputStream)
        self.realWorldTime.parse(inputStream)
        self.reason = inputStream.read_unsigned_byte()
        self.frozenBehavior = inputStream.read_unsigned_byte()
        self.padding1 = inputStream.read_short()
        self.requestID = inputStream.read_unsigned_int()



class EntityStatePdu( EntityInformationFamilyPdu ):
    """Represents the postion and state of one entity in the world. Section 7.2.2. COMPLETE"""

    def __init__(self,
                 entityID=None,
                 forceId=0,
                 numberOfVariableParameters=0,
                 entityType=None,
                 alternativeEntityType=None,
                 entityLinearVelocity=None,
                 entityLocation=None,
                 entityOrientation=None,
                 entityAppearance=0,
                 deadReckoningParameters=None,
                 marking=None,
                 capabilities=0,
                 variableParameters=None):
        """ Initializer for EntityStatePdu"""
        super(EntityStatePdu, self).__init__()
        self.entityID = entityID or EntityID()
        """ Unique ID for an entity that is tied to this state information"""
        self.forceId = forceId
        """ What force this entity is affiliated with, eg red, blue, neutral, etc"""
        self.numberOfVariableParameters = numberOfVariableParameters
        """ How many variable parameters are in the variable length list. In earlier versions of DIS these were known as articulation parameters"""
        self.entityType = entityType or EntityType()
        """ Describes the type of entity in the world"""
        self.alternativeEntityType = alternativeEntityType or EntityType()
        self.entityLinearVelocity = entityLinearVelocity or Vector3Float()
        """ Describes the speed of the entity in the world"""
        self.entityLocation = entityLocation or Vector3Double()
        """ describes the location of the entity in the world"""
        self.entityOrientation = entityOrientation or EulerAngles()
        """ describes the orientation of the entity, in euler angles"""
        self.entityAppearance = entityAppearance
        """ a series of bit flags that are used to help draw the entity, such as smoking, on fire, etc."""
        self.deadReckoningParameters = deadReckoningParameters or DeadReckoningParameters()
        """ parameters used for dead reckoning"""
        self.marking = marking or EntityMarking()
        """ characters that can be used for debugging, or to draw unique strings on the side of entities in the world"""
        self.capabilities = capabilities
        """ a series of bit flags"""
        self.variableParameters = variableParameters or []
        """ variable length list of variable parameters. In earlier DIS versions this was articulation parameters."""
        self.pduType = 1
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( EntityStatePdu, self ).serialize(outputStream)
        self.entityID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.forceId)
        outputStream.write_unsigned_byte( len(self.variableParameters))
        self.entityType.serialize(outputStream)
        self.alternativeEntityType.serialize(outputStream)
        self.entityLinearVelocity.serialize(outputStream)
        self.entityLocation.serialize(outputStream)
        self.entityOrientation.serialize(outputStream)
        outputStream.write_unsigned_int(self.entityAppearance)
        self.deadReckoningParameters.serialize(outputStream)
        self.marking.serialize(outputStream)
        outputStream.write_unsigned_int(self.capabilities)
        for anObj in self.variableParameters:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( EntityStatePdu, self).parse(inputStream)
        self.entityID.parse(inputStream)
        self.forceId = inputStream.read_unsigned_byte()
        self.numberOfVariableParameters = inputStream.read_unsigned_byte()
        self.entityType.parse(inputStream)
        self.alternativeEntityType.parse(inputStream)
        self.entityLinearVelocity.parse(inputStream)
        self.entityLocation.parse(inputStream)
        self.entityOrientation.parse(inputStream)
        self.entityAppearance = inputStream.read_unsigned_int()
        self.deadReckoningParameters.parse(inputStream)
        self.marking.parse(inputStream)
        self.capabilities = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfVariableParameters):
            element = VariableParameter()
            element.parse(inputStream)
            self.variableParameters.append(element)




class EntityManagementFamilyPdu( Pdu ):
    """ Management of grouping of PDUs, and more. Section 7.8"""

    def __init__(self):
        """ Initializer for EntityManagementFamilyPdu"""
        super(EntityManagementFamilyPdu, self).__init__()
        self.protocolFamily = 7
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( EntityManagementFamilyPdu, self ).serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( EntityManagementFamilyPdu, self).parse(inputStream)



class StartResumePdu( SimulationManagementFamilyPdu ):
    """Section 7.5.4. Start or resume an exercise. COMPLETE"""

    def __init__(self,
                 realWorldTime=None,
                 simulationTime=None,
                 requestID=0):
        """ Initializer for StartResumePdu"""
        super(StartResumePdu, self).__init__()
        self.realWorldTime = realWorldTime or ClockTime()
        """ This field shall specify the real-world time (UTC) at which the entity is to start/resume in the exercise. This information shall be used by the participating simulation applications to start/resume an exercise synchronously. This field shall be represented by a Clock Time record (see 6.2.16)."""
        self.simulationTime = simulationTime or ClockTime()
        """ The reference time within a simulation exercise. This time is established ahead of time by simulation management and is common to all participants in a particular exercise. Simulation time may be either Absolute Time or Relative Time. This field shall be represented by a Clock Time record (see 6.2.16)"""
        self.requestID = requestID
        """ Identifier for the specific and unique start/resume request"""
        self.pduType = 13
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( StartResumePdu, self ).serialize(outputStream)
        self.realWorldTime.serialize(outputStream)
        self.simulationTime.serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( StartResumePdu, self).parse(inputStream)
        self.realWorldTime.parse(inputStream)
        self.simulationTime.parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()



class TransmitterPdu( RadioCommunicationsFamilyPdu ):
    """Detailed information about a radio transmitter. This PDU requires manually written code to complete, since the modulation parameters are of variable length. Section 7.7.2 UNFINISHED"""

    def __init__(self,
                 radioReferenceID=None,
                 radioNumber=0,
                 radioEntityType=None,
                 transmitState=0,
                 inputSource=0,
                 variableTransmitterParameterCount=0,
                 antennaLocation=None,
                 relativeAntennaLocation=None,
                 antennaPatternType=0,
                 antennaPatternCount=0,
                 frequency=0,
                 transmitFrequencyBandwidth=0.0,
                 power=0.0,
                 modulationType=None,
                 cryptoSystem=0,
                 cryptoKeyId=0,
                 modulationParameterCount=0,
                 modulationParametersList=None,
                 antennaPatternList=None):
        """ Initializer for TransmitterPdu"""
        super(TransmitterPdu, self).__init__()
        self.radioReferenceID = radioReferenceID or EntityID()
        """ ID of the entitythat is the source of the communication"""
        self.radioNumber = radioNumber
        """ particular radio within an entity"""
        self.radioEntityType = radioEntityType or EntityType()
        """ Type of radio"""
        self.transmitState = transmitState
        """ transmit state"""
        self.inputSource = inputSource
        """ input source"""
        self.variableTransmitterParameterCount = variableTransmitterParameterCount
        """ count field"""
        self.antennaLocation = antennaLocation or Vector3Double()
        """ Location of antenna"""
        self.relativeAntennaLocation = relativeAntennaLocation or Vector3Float()
        """ relative location of antenna"""
        self.antennaPatternType = antennaPatternType
        """ antenna pattern type"""
        self.antennaPatternCount = antennaPatternCount
        """ atenna pattern length"""
        self.frequency = frequency
        """ frequency"""
        self.transmitFrequencyBandwidth = transmitFrequencyBandwidth
        """ transmit frequency Bandwidth"""
        self.power = power
        """ transmission power"""
        self.modulationType = modulationType or ModulationType()
        """ modulation"""
        self.cryptoSystem = cryptoSystem
        """ crypto system enumeration"""
        self.cryptoKeyId = cryptoKeyId
        """ crypto system key identifer"""
        self.modulationParameterCount = modulationParameterCount
        """ how many modulation parameters we have"""
        self.padding2 = 0
        """ padding2"""
        self.padding3 = 0
        """ padding3"""
        self.modulationParametersList = modulationParametersList or []
        """ variable length list of modulation parameters"""
        self.antennaPatternList = antennaPatternList or []
        """ variable length list of antenna pattern records"""
        self.pduType = 25
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( TransmitterPdu, self ).serialize(outputStream)
        self.radioReferenceID.serialize(outputStream)
        outputStream.write_unsigned_short(self.radioNumber)
        self.radioEntityType.serialize(outputStream)
        outputStream.write_unsigned_byte(self.transmitState)
        outputStream.write_unsigned_byte(self.inputSource)
        outputStream.write_unsigned_short(self.variableTransmitterParameterCount)
        self.antennaLocation.serialize(outputStream)
        self.relativeAntennaLocation.serialize(outputStream)
        outputStream.write_unsigned_short(self.antennaPatternType)
        outputStream.write_unsigned_short( len(self.antennaPatternList))
        outputStream.write_long(self.frequency)
        outputStream.write_float(self.transmitFrequencyBandwidth)
        outputStream.write_float(self.power)
        self.modulationType.serialize(outputStream)
        outputStream.write_unsigned_short(self.cryptoSystem)
        outputStream.write_unsigned_short(self.cryptoKeyId)
        outputStream.write_unsigned_byte( len(self.modulationParametersList))
        outputStream.write_unsigned_short(self.padding2)
        outputStream.write_unsigned_byte(self.padding3)
        for anObj in self.modulationParametersList:
            anObj.serialize(outputStream)

        for anObj in self.antennaPatternList:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( TransmitterPdu, self).parse(inputStream)
        self.radioReferenceID.parse(inputStream)
        self.radioNumber = inputStream.read_unsigned_short()
        self.radioEntityType.parse(inputStream)
        self.transmitState = inputStream.read_unsigned_byte()
        self.inputSource = inputStream.read_unsigned_byte()
        self.variableTransmitterParameterCount = inputStream.read_unsigned_short()
        self.antennaLocation.parse(inputStream)
        self.relativeAntennaLocation.parse(inputStream)
        self.antennaPatternType = inputStream.read_unsigned_short()
        self.antennaPatternCount = inputStream.read_unsigned_short()
        self.frequency = inputStream.read_long()
        self.transmitFrequencyBandwidth = inputStream.read_float()
        self.power = inputStream.read_float()
        self.modulationType.parse(inputStream)
        self.cryptoSystem = inputStream.read_unsigned_short()
        self.cryptoKeyId = inputStream.read_unsigned_short()
        self.modulationParameterCount = inputStream.read_unsigned_byte()
        self.padding2 = inputStream.read_unsigned_short()
        self.padding3 = inputStream.read_unsigned_byte()

        """ Vendor product MACE from BattleSpace Inc, only uses 1 byte per modulation param """
        """ SISO Spec dictates it should be 2 bytes """
        """ Instead of dumpping the packet we can make an assumption that some vendors use 1 byte per param """
        """ Although we will still send out 2 bytes per param as per spec """
        endsize = self.antennaPatternCount * 39
        mod_bytes = 2
        
        if ( self.modulationParameterCount > 0 ) :
            curr = inputStream.stream.tell()
            remaining = inputStream.stream.read(None)
            mod_bytes = (len(remaining) - endsize) / self.modulationParameterCount
            inputStream.stream.seek(curr, 0)
 
        if ( mod_bytes > 2 ) :
            print("Malformed Packet")
        else:
            for idx in range(0, self.modulationParameterCount):
                if mod_bytes == 2 :
                   element = inputStream.read_unsigned_short()
                else :
                   element = inputStream.read_unsigned_byte()
                self.modulationParametersList.append(element)
            for idx in range(0, self.antennaPatternCount):
                element = BeamAntennaPattern()
                element.parse(inputStream)
                self.antennaPatternList.append(element)



class ElectronicEmissionsPdu( DistributedEmissionsFamilyPdu ):
    """Section 5.3.7.1. Information about active electronic warfare (EW) emissions and active EW countermeasures shall be communicated using an Electromagnetic Emission PDU."""

    def __init__(self,
                 emittingEntityID=None,
                 eventID=None,
                 stateUpdateIndicator=0,
                 numberOfSystems=0,
                 systems=None):
        """ Initializer for ElectronicEmissionsPdu"""
        super(ElectronicEmissionsPdu, self).__init__()
        self.emittingEntityID = emittingEntityID or EntityID()
        """ ID of the entity emitting"""
        self.eventID = eventID or EventIdentifier()
        """ ID of event"""
        self.stateUpdateIndicator = stateUpdateIndicator
        """ This field shall be used to indicate if the data in the PDU represents a state update or just data that has changed since issuance of the last Electromagnetic Emission PDU [relative to the identified entity and emission system(s)]."""
        self.numberOfSystems = numberOfSystems
        """ This field shall specify the number of emission systems being described in the current PDU."""
        self.systems = systems or []
        """ Electronic emmissions systems THIS IS WRONG. It has the WRONG class type and will cause problems in any marshalling."""
        self.pduType = 23
        """ initialize value """
        self.paddingForEmissionsPdu = 0
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ElectronicEmissionsPdu, self ).serialize(outputStream)
        self.emittingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.stateUpdateIndicator)
        outputStream.write_unsigned_byte( len(self.systems))
        outputStream.write_unsigned_short(self.paddingForEmissionsPdu)

        for anObj in self.systems:
            anObj.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ElectronicEmissionsPdu, self).parse(inputStream)
        self.emittingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.stateUpdateIndicator = inputStream.read_unsigned_byte()
        self.numberOfSystems = inputStream.read_unsigned_byte()
        self.paddingForEmissionsPdu = inputStream.read_unsigned_short()

        for idx in range(0, self.numberOfSystems):
            element = EmissionSystemRecord()
            element.parse(inputStream)
            self.systems.append(element)

class EmissionSystemBeamRecord():
    def __init__(self,
                 beamDataLength=0,
                 beamIDNumber=0,
                 beamParameterIndex=0,
                 fundamentalParameterData=None,
                 beamFunction=0,
                 numberOfTargetsInTrackJam=0,
                 highDensityTrackJam=0,
                 jammingModeSequence=0,
                trackJamRecords=None):
        self.beamDataLength = beamDataLength
        self.beamIDNumber = beamIDNumber
        self.beamParameterIndex = beamParameterIndex
        self.fundamentalParameterData = fundamentalParameterData or EEFundamentalParameterData()
        self.beamFunction = beamFunction
        self.numberOfTargetsInTrackJam = numberOfTargetsInTrackJam
        self.highDensityTrackJam = highDensityTrackJam
        self.jammingModeSequence = jammingModeSequence
        self.trackJamRecords = trackJamRecords or []

    def serialize(self, outputStream):
        outputStream.write_unsigned_byte(self.beamDataLength)
        outputStream.write_unsigned_byte(self.beamIDNumber)
        outputStream.write_unsigned_short(self.beamParameterIndex)
        self.fundamentalParameterData.serialize(outputStream)
        outputStream.write_unsigned_byte(self.beamFunction)
        outputStream.write_unsigned_byte(self.numberOfTargetsInTrackJam)
        outputStream.write_unsigned_byte(self.highDensityTrackJam)
        outputStream.write_unsigned_byte(0) # 8 bit padding
        outputStream.write_unsigned_int(self.jammingModeSequence)

        for anObj in self.trackJamRecords:
            anObj.serialize(outputStream)

    def parse(self, inputStream):
        self.beamDataLength = inputStream.read_unsigned_byte()
        self.beamIDNumber = inputStream.read_unsigned_byte()
        self.beamParameterIndex = inputStream.read_unsigned_short()
        self.fundamentalParameterData.parse(inputStream)
        self.beamFunction = inputStream.read_unsigned_byte()
        self.numberOfTargetsInTrackJam = inputStream.read_unsigned_byte()
        self.highDensityTrackJam = inputStream.read_unsigned_byte()
        inputStream.read_unsigned_byte() # 8 bit padding
        self.jammingModeSequence = inputStream.read_unsigned_int()

        for idx in range(0, self.numberOfTargetsInTrackJam):
            element = TrackJamData()
            element.parse(inputStream)
            self.trackJamRecords.append(element)

class EmissionSystemRecord():
    def __init__(self,
                 systemDataLength=0,
                 numberOfBeams=0,
                 emitterSystem=None,
                 location=None,
                 beamRecords=None):
        self.systemDataLength = systemDataLength
        """  this field shall specify the length of this emitter system's data in 32-bit words."""
        self.numberOfBeams = numberOfBeams
        """ the number of beams being described in the current PDU for the emitter system being described. """
        self.paddingForEmissionsPdu = 0
        """ padding"""
        self.emitterSystem = emitterSystem or EmitterSystem()
        """  information about a particular emitter system and shall be represented by an Emitter System record (see 6.2.23)."""
        self.location = location or Vector3Float()
        """ the location of the antenna beam source with respect to the emitting entity's coordinate system. This location shall be the origin of the emitter coordinate system that shall have the same orientation as the entity coordinate system. This field shall be represented by an Entity Coordinate Vector record see 6.2.95 """
        self.beamRecords = beamRecords or []

    def serialize(self, outputStream):
        outputStream.write_unsigned_byte(self.systemDataLength)
        outputStream.write_unsigned_byte(self.numberOfBeams)
        outputStream.write_unsigned_short(0) # 16 bit padding
        self.emitterSystem.serialize(outputStream)
        self.location.serialize(outputStream)
        for anObj in self.beamRecords:
            anObj.serialize(outputStream)

    def parse(self, inputStream):
        self.systemDataLength = inputStream.read_unsigned_byte()
        self.numberOfBeams = inputStream.read_unsigned_byte()
        inputStream.read_unsigned_short() # 16 bit padding
        self.emitterSystem.parse(inputStream)
        self.location.parse(inputStream)
        for idx in range(0, self.numberOfBeams):
            element = EmissionSystemBeamRecord()
            element.parse(inputStream)
            self.beamRecords.append(element)

class ResupplyOfferPdu( LogisticsFamilyPdu ):
    """Information used to communicate the offer of supplies by a supplying entity to a receiving entity. Section 7.4.3 COMPLETE"""

    def __init__(self,
                 receivingEntityID=None,
                 supplyingEntityID=None,
                 numberOfSupplyTypes=0,
                 supplies=None):
        """ Initializer for ResupplyOfferPdu"""
        super(ResupplyOfferPdu, self).__init__()
        self.receivingEntityID = receivingEntityID or EntityID()
        """ Field identifies the Entity and respective Entity Record ID that is receiving service (see 6.2.28), Section 7.4.3"""
        self.supplyingEntityID = supplyingEntityID or EntityID()
        """ Identifies the Entity and respective Entity ID Record that is supplying  (see 6.2.28), Section 7.4.3"""
        self.numberOfSupplyTypes = numberOfSupplyTypes
        """ How many supplies types are being offered, Section 7.4.3"""
        self.padding1 = 0
        """ padding"""
        self.padding2 = 0
        """ padding"""
        self.supplies = supplies or []
        """ A Reord that Specifies the type of supply and the amount of that supply for each of the supply types in numberOfSupplyTypes (see 6.2.85), Section 7.4.3"""
        self.pduType = 6
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ResupplyOfferPdu, self ).serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.supplyingEntityID.serialize(outputStream)
        outputStream.write_unsigned_byte( len(self.supplies))
        outputStream.write_byte(self.padding1)
        outputStream.write_short(self.padding2)
        for anObj in self.supplies:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ResupplyOfferPdu, self).parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.supplyingEntityID.parse(inputStream)
        self.numberOfSupplyTypes = inputStream.read_unsigned_byte()
        self.padding1 = inputStream.read_byte()
        self.padding2 = inputStream.read_short()
        for idx in range(0, self.numberOfSupplyTypes):
            element = null()
            element.parse(inputStream)
            self.supplies.append(element)




class AttributePdu( EntityInformationFamilyPdu ):
    """Information about individual attributes for a particular entity, other object, or event may be communicated using an Attribute PDU. The Attribute PDU shall not be used to exchange data available in any other PDU except where explicitly mentioned in the PDU issuance instructions within this standard. See 5.3.6 for the information requirements and issuance and receipt rules for this PDU. Section 7.2.6. INCOMPLETE"""

    def __init__(self,
                 originatingSimulationAddress=None,
                 attributeRecordPduType=0,
                 attributeRecordProtocolVersion=0,
                 masterAttributeRecordType=0,
                 actionCode=0,
                 numberAttributeRecordSet=0):
        """ Initializer for AttributePdu"""
        super(AttributePdu, self).__init__()
        self.originatingSimulationAddress = originatingSimulationAddress or SimulationAddress()
        """ This field shall identify the simulation issuing the Attribute PDU. It shall be represented by a Simulation Address record (see 6.2.79)."""
        self.padding1 = 0
        """ Padding"""
        self.padding2 = 0
        """ Padding"""
        self.attributeRecordPduType = attributeRecordPduType
        """ This field shall represent the type of the PDU that is being extended or updated, if applicable. It shall be represented by an 8-bit enumeration."""
        self.attributeRecordProtocolVersion = attributeRecordProtocolVersion
        """ This field shall indicate the Protocol Version associated with the Attribute Record PDU Type. It shall be represented by an 8-bit enumeration."""
        self.masterAttributeRecordType = masterAttributeRecordType
        """ This field shall contain the Attribute record type of the Attribute records in the PDU if they all have the same Attribute record type. It shall be represented by a 32-bit enumeration."""
        self.actionCode = actionCode
        """ This field shall identify the action code applicable to this Attribute PDU. The Action Code shall apply to all Attribute records contained in the PDU. It shall be represented by an 8-bit enumeration."""
        self.padding3 = 0
        """ Padding"""
        self.numberAttributeRecordSet = numberAttributeRecordSet
        """ This field shall specify the number of Attribute Record Sets that make up the remainder of the PDU. It shall be represented by a 16-bit unsigned integer."""

    def serialize(self, outputStream):
        """serialize the class """
        super( AttributePdu, self ).serialize(outputStream)
        self.originatingSimulationAddress.serialize(outputStream)
        outputStream.write_int(self.padding1)
        outputStream.write_short(self.padding2)
        outputStream.write_unsigned_byte(self.attributeRecordPduType)
        outputStream.write_unsigned_byte(self.attributeRecordProtocolVersion)
        outputStream.write_unsigned_int(self.masterAttributeRecordType)
        outputStream.write_unsigned_byte(self.actionCode)
        outputStream.write_byte(self.padding3)
        outputStream.write_unsigned_short(self.numberAttributeRecordSet)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( AttributePdu, self).parse(inputStream)
        self.originatingSimulationAddress.parse(inputStream)
        self.padding1 = inputStream.read_int()
        self.padding2 = inputStream.read_short()
        self.attributeRecordPduType = inputStream.read_unsigned_byte()
        self.attributeRecordProtocolVersion = inputStream.read_unsigned_byte()
        self.masterAttributeRecordType = inputStream.read_unsigned_int()
        self.actionCode = inputStream.read_unsigned_byte()
        self.padding3 = inputStream.read_byte()
        self.numberAttributeRecordSet = inputStream.read_unsigned_short()



class MinefieldFamilyPdu( Pdu ):
    """ Abstract superclass for PDUs relating to minefields. Section 7.9"""

    def __init__(self):
        """ Initializer for MinefieldFamilyPdu"""
        super(MinefieldFamilyPdu, self).__init__()
        self.protocolFamily = 8
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( MinefieldFamilyPdu, self ).serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( MinefieldFamilyPdu, self).parse(inputStream)



class SetDataReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.9: initializing or chaning internal state information, reliable. Needs manual intervention to fix     padding on variable datums. UNFINISHED"""

    def __init__(self,
                 requiredReliabilityService=0,
                 requestID=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for SetDataReliablePdu"""
        super(SetDataReliablePdu, self).__init__()
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding"""
        self.pad2 = 0
        """ padding"""
        self.requestID = requestID
        """ Request ID"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Fixed datum record count"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ variable datum record count"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ Fixed datum records"""
        self.variableDatumRecords = variableDatumRecords or []
        """ Variable datum records"""
        self.pduType = 59
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( SetDataReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( SetDataReliablePdu, self).parse(inputStream)
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.requestID = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class EventReportPdu( SimulationManagementFamilyPdu ):
    """ Reports occurance of a significant event to the simulation manager. Section 7.5.12. COMPLETE"""

    def __init__(self,
                 eventType=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for EventReportPdu"""
        super(EventReportPdu, self).__init__()
        self.eventType = eventType
        """ Type of event"""
        self.padding1 = 0
        """ padding"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Number of fixed datum records"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ Number of variable datum records"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ variable length list of fixed datums"""
        self.variableDatumRecords = variableDatumRecords or []
        """ variable length list of variable length datums"""
        self.pduType = 21
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( EventReportPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.eventType)
        outputStream.write_unsigned_int(self.padding1)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( EventReportPdu, self).parse(inputStream)
        self.eventType = inputStream.read_unsigned_int()
        self.padding1 = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class PointObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
    """: Inormation abut the addition or modification of a synthecic enviroment object that is anchored to the terrain with a single point. Section 7.10.4 COMPLETE"""

    def __init__(self,
                 objectID=None,
                 referencedObjectID=None,
                 updateNumber=0,
                 forceID=0,
                 modifications=0,
                 objectType=None,
                 objectLocation=None,
                 objectOrientation=None,
                 objectAppearance=0,
                 requesterID=None,
                 receivingID=None):
        """ Initializer for PointObjectStatePdu"""
        super(PointObjectStatePdu, self).__init__()
        self.objectID = objectID or EntityID()
        """ Object in synthetic environment"""
        self.referencedObjectID = referencedObjectID or EntityID()
        """ Object with which this point object is associated"""
        self.updateNumber = updateNumber
        """ unique update number of each state transition of an object"""
        self.forceID = forceID
        """ force ID"""
        self.modifications = modifications
        """ modifications"""
        self.objectType = objectType or ObjectType()
        """ Object type"""
        self.objectLocation = objectLocation or Vector3Double()
        """ Object location"""
        self.objectOrientation = objectOrientation or EulerAngles()
        """ Object orientation"""
        self.objectAppearance = objectAppearance
        """ Object apperance"""
        self.requesterID = requesterID or SimulationAddress()
        """ requester ID"""
        self.receivingID = receivingID or SimulationAddress()
        """ receiver ID"""
        self.pad2 = 0
        """ padding"""
        self.pduType = 43
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( PointObjectStatePdu, self ).serialize(outputStream)
        self.objectID.serialize(outputStream)
        self.referencedObjectID.serialize(outputStream)
        outputStream.write_unsigned_short(self.updateNumber)
        outputStream.write_unsigned_byte(self.forceID)
        outputStream.write_unsigned_byte(self.modifications)
        self.objectType.serialize(outputStream)
        self.objectLocation.serialize(outputStream)
        self.objectOrientation.serialize(outputStream)
        outputStream.write_double(self.objectAppearance)
        self.requesterID.serialize(outputStream)
        self.receivingID.serialize(outputStream)
        outputStream.write_unsigned_int(self.pad2)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( PointObjectStatePdu, self).parse(inputStream)
        self.objectID.parse(inputStream)
        self.referencedObjectID.parse(inputStream)
        self.updateNumber = inputStream.read_unsigned_short()
        self.forceID = inputStream.read_unsigned_byte()
        self.modifications = inputStream.read_unsigned_byte()
        self.objectType.parse(inputStream)
        self.objectLocation.parse(inputStream)
        self.objectOrientation.parse(inputStream)
        self.objectAppearance = inputStream.read_double()
        self.requesterID.parse(inputStream)
        self.receivingID.parse(inputStream)
        self.pad2 = inputStream.read_unsigned_int()



class DataPdu( SimulationManagementFamilyPdu ):
    """ Information issued in response to a data query pdu or a set data pdu is communicated using a data pdu. Section 7.5.11 COMPLETE"""

    def __init__(self,
                 requestID=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for DataPdu"""
        super(DataPdu, self).__init__()
        self.requestID = requestID
        """ ID of request"""
        self.padding1 = 0
        """ padding"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Number of fixed datum records"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ Number of variable datum records"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ variable length list of fixed datums"""
        self.variableDatumRecords = variableDatumRecords or []
        """ variable length list of variable length datums"""
        self.pduType = 20
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DataPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.padding1)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DataPdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.padding1 = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class FastEntityStatePdu( EntityInformationFamilyPdu ):
    """Represents the postion and state of one entity in the world. This is identical in function to entity state pdu, but generates less garbage to collect in the Java world. Section 7.2.2. COMPLETE"""

    def __init__(self,
                 site=0,
                 application=0,
                 entity=0,
                 forceId=0,
                 numberOfVariableParameters=0,
                 entityKind=0,
                 domain=0,
                 country=0,
                 category=0,
                 subcategory=0,
                 specific=0,
                 extra=0,
                 altEntityKind=0,
                 altDomain=0,
                 altCountry=0,
                 altCategory=0,
                 altSubcategory=0,
                 altSpecific=0,
                 altExtra=0,
                 xVelocity=0,
                 yVelocity=0,
                 zVelocity=0,
                 xLocation=0,
                 yLocation=0,
                 zLocation=0,
                 psi=0,
                 theta=0,
                 phi=0,
                 entityAppearance=0,
                 deadReckoningAlgorithm=0,
                 otherParameters=None,
                 xAcceleration=0,
                 yAcceleration=0,
                 zAcceleration=0,
                 xAngularVelocity=0,
                 yAngularVelocity=0,
                 zAngularVelocity=0,
                 marking=None,
                 capabilities=0,
                 variableParameters=None):
        """ Initializer for FastEntityStatePdu"""
        super(FastEntityStatePdu, self).__init__()
        self.site = site
        """ The site ID"""
        self.application = application
        """ The application ID"""
        self.entity = entity
        """ the entity ID"""
        self.forceId = forceId
        """ what force this entity is affiliated with, eg red, blue, neutral, etc"""
        self.numberOfVariableParameters = numberOfVariableParameters
        """ How many variable (nee articulation) parameters are in the variable length list"""
        self.entityKind = entityKind
        """ Kind of entity"""
        self.domain = domain
        """ Domain of entity (air, surface, subsurface, space, etc)"""
        self.country = country
        """ country to which the design of the entity is attributed"""
        self.category = category
        """ category of entity"""
        self.subcategory = subcategory
        """ subcategory of entity"""
        self.specific = specific
        """ specific info based on subcategory field"""
        self.extra = extra
        self.altEntityKind = altEntityKind
        """ Kind of entity"""
        self.altDomain = altDomain
        """ Domain of entity (air, surface, subsurface, space, etc)"""
        self.altCountry = altCountry
        """ country to which the design of the entity is attributed"""
        self.altCategory = altCategory
        """ category of entity"""
        self.altSubcategory = altSubcategory
        """ subcategory of entity"""
        self.altSpecific = altSpecific
        """ specific info based on subcategory field"""
        self.altExtra = altExtra
        self.xVelocity = xVelocity
        """ X velo"""
        self.yVelocity = yVelocity
        """ y Value"""
        self.zVelocity = zVelocity
        """ Z value"""
        self.xLocation = xLocation
        """ X value"""
        self.yLocation = yLocation
        """ y Value"""
        self.zLocation = zLocation
        """ Z value"""
        self.psi = psi
        self.theta = theta
        self.phi = phi
        self.entityAppearance = entityAppearance
        """ a series of bit flags that are used to help draw the entity, such as smoking, on fire, etc."""
        self.deadReckoningAlgorithm = deadReckoningAlgorithm
        """ enumeration of what dead reckoning algorighm to use"""
        self.otherParameters =  otherParameters or [0] * 15
        """ other parameters to use in the dead reckoning algorithm"""
        self.xAcceleration = xAcceleration
        """ X value"""
        self.yAcceleration = yAcceleration
        """ y Value"""
        self.zAcceleration = zAcceleration
        """ Z value"""
        self.xAngularVelocity = xAngularVelocity
        """ X value"""
        self.yAngularVelocity = yAngularVelocity
        """ y Value"""
        self.zAngularVelocity = zAngularVelocity
        """ Z value"""
        self.marking = marking or [0] * 12
        """ characters that can be used for debugging, or to draw unique strings on the side of entities in the world"""
        self.capabilities = capabilities
        """ a series of bit flags"""
        self.variableParameters = variableParameters or []
        """ variable length list of variable parameters. In earlier versions of DIS these were known as articulation parameters"""
        self.pduType = 1
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( FastEntityStatePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_short(self.site)
        outputStream.write_unsigned_short(self.application)
        outputStream.write_unsigned_short(self.entity)
        outputStream.write_unsigned_byte(self.forceId)
        outputStream.write_byte( len(self.variableParameters))
        outputStream.write_unsigned_byte(self.entityKind)
        outputStream.write_unsigned_byte(self.domain)
        outputStream.write_unsigned_short(self.country)
        outputStream.write_unsigned_byte(self.category)
        outputStream.write_unsigned_byte(self.subcategory)
        outputStream.write_unsigned_byte(self.specific)
        outputStream.write_unsigned_byte(self.extra)
        outputStream.write_unsigned_byte(self.altEntityKind)
        outputStream.write_unsigned_byte(self.altDomain)
        outputStream.write_unsigned_short(self.altCountry)
        outputStream.write_unsigned_byte(self.altCategory)
        outputStream.write_unsigned_byte(self.altSubcategory)
        outputStream.write_unsigned_byte(self.altSpecific)
        outputStream.write_unsigned_byte(self.altExtra)
        outputStream.write_float(self.xVelocity)
        outputStream.write_float(self.yVelocity)
        outputStream.write_float(self.zVelocity)
        outputStream.write_double(self.xLocation)
        outputStream.write_double(self.yLocation)
        outputStream.write_double(self.zLocation)
        outputStream.write_float(self.psi)
        outputStream.write_float(self.theta)
        outputStream.write_float(self.phi)
        outputStream.write_int(self.entityAppearance)
        outputStream.write_unsigned_byte(self.deadReckoningAlgorithm)
        for idx in range(0, 15):
            outputStream.write_byte( self.otherParameters[ idx ] )

        outputStream.write_float(self.xAcceleration)
        outputStream.write_float(self.yAcceleration)
        outputStream.write_float(self.zAcceleration)
        outputStream.write_float(self.xAngularVelocity)
        outputStream.write_float(self.yAngularVelocity)
        outputStream.write_float(self.zAngularVelocity)
        for idx in range(0, 12):
            outputStream.write_byte( self.marking[ idx ] )

        outputStream.write_int(self.capabilities)
        for anObj in self.variableParameters:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( FastEntityStatePdu, self).parse(inputStream)
        self.site = inputStream.read_unsigned_short()
        self.application = inputStream.read_unsigned_short()
        self.entity = inputStream.read_unsigned_short()
        self.forceId = inputStream.read_unsigned_byte()
        self.numberOfVariableParameters = inputStream.read_byte()
        self.entityKind = inputStream.read_unsigned_byte()
        self.domain = inputStream.read_unsigned_byte()
        self.country = inputStream.read_unsigned_short()
        self.category = inputStream.read_unsigned_byte()
        self.subcategory = inputStream.read_unsigned_byte()
        self.specific = inputStream.read_unsigned_byte()
        self.extra = inputStream.read_unsigned_byte()
        self.altEntityKind = inputStream.read_unsigned_byte()
        self.altDomain = inputStream.read_unsigned_byte()
        self.altCountry = inputStream.read_unsigned_short()
        self.altCategory = inputStream.read_unsigned_byte()
        self.altSubcategory = inputStream.read_unsigned_byte()
        self.altSpecific = inputStream.read_unsigned_byte()
        self.altExtra = inputStream.read_unsigned_byte()
        self.xVelocity = inputStream.read_float()
        self.yVelocity = inputStream.read_float()
        self.zVelocity = inputStream.read_float()
        self.xLocation = inputStream.read_double()
        self.yLocation = inputStream.read_double()
        self.zLocation = inputStream.read_double()
        self.psi = inputStream.read_float()
        self.theta = inputStream.read_float()
        self.phi = inputStream.read_float()
        self.entityAppearance = inputStream.read_int()
        self.deadReckoningAlgorithm = inputStream.read_unsigned_byte()
        self.otherParameters = [0]*15
        for idx in range(0, 15):
            val = inputStream.read_byte()

            self.otherParameters[  idx  ] = val

        self.xAcceleration = inputStream.read_float()
        self.yAcceleration = inputStream.read_float()
        self.zAcceleration = inputStream.read_float()
        self.xAngularVelocity = inputStream.read_float()
        self.yAngularVelocity = inputStream.read_float()
        self.zAngularVelocity = inputStream.read_float()
        self.marking = [0]*12
        for idx in range(0, 12):
            val = inputStream.read_byte()

            self.marking[  idx  ] = val

        self.capabilities = inputStream.read_int()
        for idx in range(0, self.numberOfVariableParameters):
            element = VariableParameter()
            element.parse(inputStream)
            self.variableParameters.append(element)




class AcknowledgeReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.5: Ack receipt of a start-resume, stop-freeze, create-entity or remove enitty (reliable) pdus. COMPLETE"""

    def __init__(self,
                 acknowledgeFlag=0,
                 responseFlag=0,
                 requestID=0):
        """ Initializer for AcknowledgeReliablePdu"""
        super(AcknowledgeReliablePdu, self).__init__()
        self.acknowledgeFlag = acknowledgeFlag
        """ ack flags"""
        self.responseFlag = responseFlag
        """ response flags"""
        self.requestID = requestID
        """ Request ID"""
        self.pduType = 55
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( AcknowledgeReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_short(self.acknowledgeFlag)
        outputStream.write_unsigned_short(self.responseFlag)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( AcknowledgeReliablePdu, self).parse(inputStream)
        self.acknowledgeFlag = inputStream.read_unsigned_short()
        self.responseFlag = inputStream.read_unsigned_short()
        self.requestID = inputStream.read_unsigned_int()



class StartResumeReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.3: Start resume simulation, relaible. COMPLETE"""

    def __init__(self,
                 realWorldTime=None,
                 simulationTime=None,
                 requiredReliabilityService=0,
                 requestID=0):
        """ Initializer for StartResumeReliablePdu"""
        super(StartResumeReliablePdu, self).__init__()
        self.realWorldTime = realWorldTime or ClockTime()
        """ time in real world for this operation to happen"""
        self.simulationTime = simulationTime or ClockTime()
        """ time in simulation for the simulation to resume"""
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding"""
        self.pad2 = 0
        """ padding"""
        self.requestID = requestID
        """ Request ID"""
        self.pduType = 53
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( StartResumeReliablePdu, self ).serialize(outputStream)
        self.realWorldTime.serialize(outputStream)
        self.simulationTime.serialize(outputStream)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( StartResumeReliablePdu, self).parse(inputStream)
        self.realWorldTime.parse(inputStream)
        self.simulationTime.parse(inputStream)
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.requestID = inputStream.read_unsigned_int()



class ArealObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
    """Information about the addition/modification of an oobject that is geometrically anchored to the terrain with a set of three or more points that come to a closure. Section 7.10.6 COMPLETE"""

    def __init__(self,
                 objectID=None,
                 referencedObjectID=None,
                 updateNumber=0,
                 forceId=0,
                 modifications=0,
                 objectType=None,
                 specificObjectAppearance=0,
                 generalObjectAppearance=0,
                 numberOfPoints=0,
                 requesterID=None,
                 receivingID=None,
                 objectLocation=None):
        """ Initializer for ArealObjectStatePdu"""
        super(ArealObjectStatePdu, self).__init__()
        self.objectID = objectID or EntityID()
        """ Object in synthetic environment"""
        self.referencedObjectID = referencedObjectID or EntityID()
        """ Object with which this point object is associated"""
        self.updateNumber = updateNumber
        """ unique update number of each state transition of an object"""
        self.forceID = forceId
        """ force ID"""
        self.modifications = modifications
        """ modifications enumeration"""
        self.objectType = objectType or EntityType()
        """ Object type"""
        self.specificObjectAppearance = specificObjectAppearance
        """ Object appearance"""
        self.generalObjectAppearance = generalObjectAppearance
        """ Object appearance"""
        self.numberOfPoints = numberOfPoints
        """ Number of points"""
        self.requesterID = requesterID or SimulationAddress()
        """ requesterID"""
        self.receivingID = receivingID or SimulationAddress()
        """ receiver ID"""
        self.objectLocation = objectLocation or []
        """ location of object"""
        self.pduType = 45
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ArealObjectStatePdu, self ).serialize(outputStream)
        self.objectID.serialize(outputStream)
        self.referencedObjectID.serialize(outputStream)
        outputStream.write_unsigned_short(self.updateNumber)
        outputStream.write_unsigned_byte(self.forceID)
        outputStream.write_unsigned_byte(self.modifications)
        self.objectType.serialize(outputStream)
        outputStream.write_unsigned_int(self.specificObjectAppearance)
        outputStream.write_unsigned_short(self.generalObjectAppearance)
        outputStream.write_unsigned_short( len(self.objectLocation))
        self.requesterID.serialize(outputStream)
        self.receivingID.serialize(outputStream)
        for anObj in self.objectLocation:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ArealObjectStatePdu, self).parse(inputStream)
        self.objectID.parse(inputStream)
        self.referencedObjectID.parse(inputStream)
        self.updateNumber = inputStream.read_unsigned_short()
        self.forceID = inputStream.read_unsigned_byte()
        self.modifications = inputStream.read_unsigned_byte()
        self.objectType.parse(inputStream)
        self.specificObjectAppearance = inputStream.read_unsigned_int()
        self.generalObjectAppearance = inputStream.read_unsigned_short()
        self.numberOfPoints = inputStream.read_unsigned_short()
        self.requesterID.parse(inputStream)
        self.receivingID.parse(inputStream)
        for idx in range(0, self.numberOfPoints):
            element = null()
            element.parse(inputStream)
            self.objectLocation.append(element)




class DataQueryReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.8: request for data from an entity. COMPLETE"""

    def __init__(self,
                 requiredReliabilityService=0,
                 requestID=0,
                 timeInterval=0,
                 numberOfFixedDatumIDs=0,
                 numberOfVariableDatumIDs=0,
                 fixedDatumIDs=None,
                 variableDatumIDs=None):
        """ Initializer for DataQueryReliablePdu"""
        super(DataQueryReliablePdu, self).__init__()
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding"""
        self.pad2 = 0
        """ padding"""
        self.requestID = requestID
        """ request ID"""
        self.timeInterval = timeInterval
        """ time interval between issuing data query PDUs"""
        self.numberOfFixedDatumIDs = numberOfFixedDatumIDs
        """ Fixed datum record count"""
        self.numberOfVariableDatumIDs = numberOfVariableDatumIDs
        """ variable datum record count"""
        self.fixedDatumIDs = fixedDatumIDs or []
        """ Fixed datum records"""
        self.variableDatumIDs = variableDatumIDs or []
        """ Variable datum records"""
        self.pduType = 58
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DataQueryReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.timeInterval)
        outputStream.write_unsigned_int( len(self.fixedDatumIDs))
        outputStream.write_unsigned_int( len(self.variableDatumIDs))
        for anObj in self.fixedDatumIDs:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumIDs:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DataQueryReliablePdu, self).parse(inputStream)
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.requestID = inputStream.read_unsigned_int()
        self.timeInterval = inputStream.read_unsigned_int()
        self.numberOfFixedDatumIDs = inputStream.read_unsigned_int()
        self.numberOfVariableDatumIDs = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumIDs):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumIDs.append(element)

        for idx in range(0, self.numberOfVariableDatumIDs):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumIDs.append(element)




class MinefieldStatePdu( MinefieldFamilyPdu ):
    """information about the complete minefield. The minefield presence, perimiter, etc. Section 7.9.2 COMPLETE"""

    def __init__(self,
                 minefieldID=None,
                 minefieldSequence=0,
                 forceID=0,
                 numberOfPerimeterPoints=0,
                 minefieldType=None,
                 numberOfMineTypes=0,
                 minefieldLocation=None,
                 minefieldOrientation=None,
                 appearance=0,
                 protocolMode=0,
                 perimeterPoints=None,
                 mineTypes=None):
        """ Initializer for MinefieldStatePdu"""
        super(MinefieldStatePdu, self).__init__()
        self.minefieldID = minefieldID or MinefieldIdentifier()
        """ Minefield ID"""
        self.minefieldSequence = minefieldSequence
        """ Minefield sequence"""
        self.forceID = forceID
        """ force ID"""
        self.numberOfPerimeterPoints = numberOfPerimeterPoints
        """ Number of permieter points"""
        self.minefieldType = minefieldType or EntityType()
        """ type of minefield"""
        self.numberOfMineTypes = numberOfMineTypes
        """ how many mine types"""
        self.minefieldLocation = minefieldLocation or Vector3Double()
        """ location of center of minefield in world coords"""
        self.minefieldOrientation = minefieldOrientation or EulerAngles()
        """ orientation of minefield"""
        self.appearance = appearance
        """ appearance bitflags"""
        self.protocolMode = protocolMode
        """ protocolMode. First two bits are the protocol mode, 14 bits reserved."""
        self.perimeterPoints = perimeterPoints or []
        """ perimeter points for the minefield"""
        self.mineTypes = mineTypes or []
        """ Type of mines"""
        self.pduType = 37
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( MinefieldStatePdu, self ).serialize(outputStream)
        self.minefieldID.serialize(outputStream)
        outputStream.write_unsigned_short(self.minefieldSequence)
        outputStream.write_unsigned_byte(self.forceID)
        outputStream.write_unsigned_byte( len(self.perimeterPoints))
        self.minefieldType.serialize(outputStream)
        outputStream.write_unsigned_short( len(self.mineType))
        self.minefieldLocation.serialize(outputStream)
        self.minefieldOrientation.serialize(outputStream)
        outputStream.write_unsigned_short(self.appearance)
        outputStream.write_unsigned_short(self.protocolMode)
        for anObj in self.perimeterPoints:
            anObj.serialize(outputStream)

        for anObj in self.mineType:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( MinefieldStatePdu, self).parse(inputStream)
        self.minefieldID.parse(inputStream)
        self.minefieldSequence = inputStream.read_unsigned_short()
        self.forceID = inputStream.read_unsigned_byte()
        self.numberOfPerimeterPoints = inputStream.read_unsigned_byte()
        self.minefieldType.parse(inputStream)
        self.numberOfMineTypes = inputStream.read_unsigned_short()
        self.minefieldLocation.parse(inputStream)
        self.minefieldOrientation.parse(inputStream)
        self.appearance = inputStream.read_unsigned_short()
        self.protocolMode = inputStream.read_unsigned_short()
        for idx in range(0, self.numberOfPerimeterPoints):
            element = null()
            element.parse(inputStream)
            self.perimeterPoints.append(element)

        for idx in range(0, self.numberOfMineTypes):
            element = null()
            element.parse(inputStream)
            self.mineType.append(element)




class DataReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.10: issued in response to a data query R or set dataR pdu. Needs manual intervention      to fix padding on variable datums. UNFINSIHED"""

    def __init__(self,
                 requestID=0,
                 requiredReliabilityService=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for DataReliablePdu"""
        super(DataReliablePdu, self).__init__()
        self.requestID = requestID
        """ Request ID"""
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding"""
        self.pad2 = 0
        """ padding"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Fixed datum record count"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ variable datum record count"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ Fixed datum records"""
        self.variableDatumRecords = variableDatumRecords or []
        """ Variable datum records"""
        self.pduType = 60
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DataReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DataReliablePdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class CommentPdu( SimulationManagementFamilyPdu ):
    """ Arbitrary messages can be entered into the data stream via use of this PDU. Section 7.5.13 COMPLETE"""

    def __init__(self,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for CommentPdu"""
        super(CommentPdu, self).__init__()
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Number of fixed datum records"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ Number of variable datum records"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ variable length list of fixed datums"""
        self.variableDatumRecords = variableDatumRecords or []
        """ variable length list of variable length datums"""
        self.pduType = 22
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( CommentPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( CommentPdu, self).parse(inputStream)
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class CommentReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.12: Arbitrary messages. Only reliable this time. Needs manual intervention to fix padding in variable datums. UNFINISHED"""

    def __init__(self,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for CommentReliablePdu"""
        super(CommentReliablePdu, self).__init__()
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Fixed datum record count"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ variable datum record count"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ Fixed datum records"""
        self.variableDatumRecords = variableDatumRecords or []
        """ Variable datum records"""
        self.pduType = 62
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( CommentReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( CommentReliablePdu, self).parse(inputStream)
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class DirectedEnergyFirePdu( WarfareFamilyPdu ):
    """Firing of a directed energy weapon shall be communicated by issuing a Directed Energy Fire PDU Section 7.3.4  COMPLETE"""

    def __init__(self,
                 munitionType=None,
                 shotStartTime=None,
                 cumulativeShotTime=0.0,
                 apertureEmitterLocation=None,
                 apertureDiameter=0.0,
                 wavelength=0.0,
                 peakIrradiance=0.0,
                 pulseRepetitionFrequency=0.0,
                 pulseWidth=0,
                 flags=0,
                 pulseShape=0,
                 numberOfDERecords=0,
                 dERecords=None):
        """ Initializer for DirectedEnergyFirePdu"""
        super(DirectedEnergyFirePdu, self).__init__()
        self.munitionType = munitionType or EntityType()
        """ Field shall identify the munition type enumeration for the DE weapon beam, Section 7.3.4 """
        self.shotStartTime = shotStartTime or ClockTime()
        """ Field shall indicate the simulation time at start of the shot, Section 7.3.4 """
        self.cumulativeShotTime = cumulativeShotTime
        """ Field shall indicate the current cumulative duration of the shot, Section 7.3.4 """
        self.apertureEmitterLocation = apertureEmitterLocation or Vector3Float()
        """ Field shall identify the location of the DE weapon aperture/emitter, Section 7.3.4 """
        self.apertureDiameter = apertureDiameter
        """ Field shall identify the beam diameter at the aperture/emitter, Section 7.3.4 """
        self.wavelength = wavelength
        """ Field shall identify the emissions wavelength in units of meters, Section 7.3.4 """
        self.peakIrradiance = peakIrradiance
        """ Field shall identify the current peak irradiance of emissions in units of Watts per square meter, Section 7.3.4 """
        self.pulseRepetitionFrequency = pulseRepetitionFrequency
        """ field shall identify the current pulse repetition frequency in units of cycles per second (Hertz), Section 7.3.4 """
        self.pulseWidth = pulseWidth
        """ field shall identify the pulse width emissions in units of seconds, Section 7.3.4"""
        self.flags = flags
        """ 16bit Boolean field shall contain various flags to indicate status information needed to process a DE, Section 7.3.4 """
        self.pulseShape = pulseShape
        """ Field shall identify the pulse shape and shall be represented as an 8-bit enumeration, Section 7.3.4 """
        self.padding1 = 0
        """ padding, Section 7.3.4 """
        self.padding2 = 0
        """ padding, Section 7.3.4 """
        self.padding3 = 0
        """ padding, Section 7.3.4 """
        self.numberOfDERecords = numberOfDERecords
        """ Field shall specify the number of DE records, Section 7.3.4 """
        self.dERecords = dERecords or []
        """ Fields shall contain one or more DE records, records shall conform to the variable record format (Section6.2.82), Section 7.3.4"""
        self.pduType = 68
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DirectedEnergyFirePdu, self ).serialize(outputStream)
        self.munitionType.serialize(outputStream)
        self.shotStartTime.serialize(outputStream)
        outputStream.write_float(self.commulativeShotTime)
        self.ApertureEmitterLocation.serialize(outputStream)
        outputStream.write_float(self.apertureDiameter)
        outputStream.write_float(self.wavelength)
        outputStream.write_float(self.peakIrradiance)
        outputStream.write_float(self.pulseRepetitionFrequency)
        outputStream.write_int(self.pulseWidth)
        outputStream.write_int(self.flags)
        outputStream.write_byte(self.pulseShape)
        outputStream.write_unsigned_byte(self.padding1)
        outputStream.write_unsigned_int(self.padding2)
        outputStream.write_unsigned_short(self.padding3)
        outputStream.write_unsigned_short( len(self.dERecords))
        for anObj in self.dERecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DirectedEnergyFirePdu, self).parse(inputStream)
        self.munitionType.parse(inputStream)
        self.shotStartTime.parse(inputStream)
        self.commulativeShotTime = inputStream.read_float()
        self.ApertureEmitterLocation.parse(inputStream)
        self.apertureDiameter = inputStream.read_float()
        self.wavelength = inputStream.read_float()
        self.peakIrradiance = inputStream.read_float()
        self.pulseRepetitionFrequency = inputStream.read_float()
        self.pulseWidth = inputStream.read_int()
        self.flags = inputStream.read_int()
        self.pulseShape = inputStream.read_byte()
        self.padding1 = inputStream.read_unsigned_byte()
        self.padding2 = inputStream.read_unsigned_int()
        self.padding3 = inputStream.read_unsigned_short()
        self.numberOfDERecords = inputStream.read_unsigned_short()
        for idx in range(0, self.numberOfDERecords):
            element = null()
            element.parse(inputStream)
            self.dERecords.append(element)




class DetonationPdu( WarfareFamilyPdu ):
    """Detonation or impact of munitions, as well as, non-munition explosions, the burst or initial bloom of chaff, and the ignition of a flare shall be indicated. Section 7.3.3  COMPLETE"""

    def __init__(self,
                 explodingEntityID=None,
                 eventID=None,
                 velocity=None,
                 locationInWordCoordinates=None,
                 descriptor=None,
                 locationOfEntityCoordinates=None,
                 detonationResult=0,
                 numberOfVariableParameters=0,
                 variableParameters=None):
        """ Initializer for DetonationPdu"""
        super(DetonationPdu, self).__init__()
        self.explodingEntityID = explodingEntityID or EntityID()
        """ ID of the expendable entity, Section 7.3.3 """
        self.eventID = eventID or EventIdentifier()
        """ ID of event, Section 7.3.3"""
        self.velocity = velocity or Vector3Float()
        """ velocity of the munition immediately before detonation/impact, Section 7.3.3 """
        self.locationInWorldCoordinates = locationInWordCoordinates or Vector3Double()
        """ location of the munition detonation, the expendable detonation, Section 7.3.3 """
        self.descriptor = descriptor or MunitionDescriptor()
        """ Describes the detonation represented, Section 7.3.3 """
        self.locationOfEntityCoordinates = locationOfEntityCoordinates or Vector3Float()
        """ Velocity of the ammunition, Section 7.3.3 """
        self.detonationResult = detonationResult
        """ result of the detonation, Section 7.3.3 """
        self.numberOfVariableParameters = numberOfVariableParameters
        """ How many articulation parameters we have, Section 7.3.3 """
        self.pad = 0
        """ padding"""
        self.variableParameters = variableParameters or []
        """ specify the parameter values for each Variable Parameter record, Section 7.3.3 """
        self.pduType = 3
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( DetonationPdu, self ).serialize(outputStream)
        self.explodingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        self.velocity.serialize(outputStream)
        self.locationInWorldCoordinates.serialize(outputStream)
        self.descriptor.serialize(outputStream)
        self.locationOfEntityCoordinates.serialize(outputStream)
        outputStream.write_unsigned_byte(self.detonationResult)
        outputStream.write_unsigned_byte( len(self.variableParameters))
        outputStream.write_unsigned_short(self.pad)
        for anObj in self.variableParameters:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( DetonationPdu, self).parse(inputStream)
        self.explodingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.velocity.parse(inputStream)
        self.locationInWorldCoordinates.parse(inputStream)
        self.descriptor.parse(inputStream)
        self.locationOfEntityCoordinates.parse(inputStream)
        self.detonationResult = inputStream.read_unsigned_byte()
        self.numberOfVariableParameters = inputStream.read_unsigned_byte()
        self.pad = inputStream.read_unsigned_short()
        for idx in range(0, self.numberOfVariableParameters):
            element = VariableParameter()
            element.parse(inputStream)
            self.variableParameters.append(element)




class SetDataPdu( SimulationManagementFamilyPdu ):
    """Section 7.5.10. Change state information with the data contained in this. COMPLETE"""

    def __init__(self,
                 requestID=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for SetDataPdu"""
        super(SetDataPdu, self).__init__()
        self.requestID = requestID
        """ ID of request"""
        self.padding1 = 0
        """ padding"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Number of fixed datum records"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ Number of variable datum records"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ variable length list of fixed datums"""
        self.variableDatumRecords = variableDatumRecords or []
        """ variable length list of variable length datums"""
        self.pduType = 19
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( SetDataPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.padding1)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( SetDataPdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.padding1 = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class RecordQueryReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.13: A request for one or more records of data from an entity. COMPLETE"""

    def __init__(self,
                 requestID=0,
                 requiredReliabilityService=0,
                 eventType=0,
                 time=0,
                 numberOfRecords=0,
                 recordIDs=None):
        """ Initializer for RecordQueryReliablePdu"""
        super(RecordQueryReliablePdu, self).__init__()
        self.requestID = requestID
        """ request ID"""
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding. The spec is unclear and contradictory here."""
        self.pad2 = 0
        """ padding"""
        self.eventType = eventType
        """ event type"""
        self.time = time
        """ time"""
        self.numberOfRecords = numberOfRecords
        """ numberOfRecords"""
        self.recordIDs = recordIDs or []
        """ record IDs"""
        self.pduType = 63
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( RecordQueryReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_short(self.eventType)
        outputStream.write_unsigned_int(self.time)
        outputStream.write_unsigned_int( len(self.recordIDs))
        for anObj in self.recordIDs:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( RecordQueryReliablePdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.eventType = inputStream.read_unsigned_short()
        self.time = inputStream.read_unsigned_int()
        self.numberOfRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfRecords):
            element = null()
            element.parse(inputStream)
            self.recordIDs.append(element)




class ActionResponsePdu( SimulationManagementFamilyPdu ):
    """Section 7.5.8. response to an action request PDU. COMPLETE"""

    def __init__(self,
                 requestID=0,
                 requestStatus=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for ActionResponsePdu"""
        super(ActionResponsePdu, self).__init__()
        self.requestID = requestID
        """ Request ID that is unique"""
        self.requestStatus = requestStatus
        """ Status of response"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Number of fixed datum records"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ Number of variable datum records"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ variable length list of fixed datums"""
        self.variableDatumRecords = variableDatumRecords or []
        """ variable length list of variable length datums"""
        self.pduType = 17
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ActionResponsePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.requestStatus)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ActionResponsePdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.requestStatus = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class EntityDamageStatusPdu( WarfareFamilyPdu ):
    """shall be used to communicate detailed damage information sustained by an entity regardless of the source of the damage Section 7.3.5  COMPLETE"""

    def __init__(self,
                 damagedEntityID=None,
                 numberOfDamageDescriptions=0,
                 damageDescriptionRecords=None):
        """ Initializer for EntityDamageStatusPdu"""
        super(EntityDamageStatusPdu, self).__init__()
        self.damagedEntityID = damagedEntityID or EntityID()
        """ Field shall identify the damaged entity (see 6.2.28), Section 7.3.4 COMPLETE"""
        self.padding1 = 0
        """ Padding."""
        self.padding2 = 0
        """ Padding."""
        self.numberOfDamageDescriptions = numberOfDamageDescriptions
        """ field shall specify the number of Damage Description records, Section 7.3.5"""
        self.damageDescriptionRecords = damageDescriptionRecords or []
        """ Fields shall contain one or more Damage Description records (see 6.2.17) and may contain other Standard Variable records, Section 7.3.5"""
        self.pduType = 69
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( EntityDamageStatusPdu, self ).serialize(outputStream)
        self.damagedEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.padding1)
        outputStream.write_unsigned_short(self.padding2)
        outputStream.write_unsigned_short( len(self.damageDescriptionRecords))
        for anObj in self.damageDescriptionRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( EntityDamageStatusPdu, self).parse(inputStream)
        self.damagedEntityID.parse(inputStream)
        self.padding1 = inputStream.read_unsigned_short()
        self.padding2 = inputStream.read_unsigned_short()
        self.numberOfDamageDescription = inputStream.read_unsigned_short()
        for idx in range(0, self.numberOfDamageDescription):
            element = null()
            element.parse(inputStream)
            self.damageDescriptionRecords.append(element)




class FirePdu( WarfareFamilyPdu ):
    """ The firing of a weapon or expendable shall be communicated by issuing a Fire PDU. Sectioin 7.3.2. COMPLETE"""

    def __init__(self,
                 munitionExpendableID=None,
                 eventID=None,
                 fireMissionIndex=0,
                 locationInWorldCoordinates=None,
                 descriptor=None,
                 velocity=None,
                 range_=0.0):
        """ Initializer for FirePdu"""
        super(FirePdu, self).__init__()
        self.munitionExpendableID = munitionExpendableID or EntityID()
        """ This field shall specify the entity identification of the fired munition or expendable. This field shall be represented by an Entity Identifier record (see 6.2.28)."""
        self.eventID = eventID or EventIdentifier()
        """ This field shall contain an identification generated by the firing entity to associate related firing and detonation events. This field shall be represented by an Event Identifier record (see 6.2.34)."""
        self.fireMissionIndex = fireMissionIndex
        """ This field shall identify the fire mission (see 5.4.3.3). This field shall be representedby a 32-bit unsigned integer."""
        self.locationInWorldCoordinates = locationInWorldCoordinates or Vector3Double()
        """ This field shall specify the location, in world coordinates, from which the munition was launched, and shall be represented by a World Coordinates record (see 6.2.97)."""
        self.descriptor = descriptor or MunitionDescriptor()
        """ This field shall describe the firing or launch of a munition or expendable represented by one of the following types of Descriptor records: Munition Descriptor (6.2.20.2) or Expendable Descriptor (6.2.20.4)."""
        self.velocity = velocity or Vector3Float()
        """ This field shall specify the velocity of the fired munition at the point when the issuing simulation application intends the externally visible effects of the launch (e.g. exhaust plume or muzzle blast) to first become apparent. The velocity shall be represented in world coordinates. This field shall be represented by a Linear Velocity Vector record [see 6.2.95 item c)]."""
        self.range = range_  # range is a built-in function in Python
        """ This field shall specify the range that an entitys fire control system has assumed in computing the fire control solution. This field shall be represented by a 32-bit floating point number in meters. For systems where range is unknown or unavailable, this field shall contain a value of zero."""
        self.pduType = 2
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( FirePdu, self ).serialize(outputStream)
        self.munitionExpendibleID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        outputStream.write_unsigned_int(self.fireMissionIndex)
        self.locationInWorldCoordinates.serialize(outputStream)
        self.descriptor.serialize(outputStream)
        self.velocity.serialize(outputStream)
        outputStream.write_float(self.range)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( FirePdu, self).parse(inputStream)
        self.munitionExpendibleID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.fireMissionIndex = inputStream.read_unsigned_int()
        self.locationInWorldCoordinates.parse(inputStream)
        self.descriptor.parse(inputStream)
        self.velocity.parse(inputStream)
        self.range = inputStream.read_float()



class ReceiverPdu( RadioCommunicationsFamilyPdu ):
    """ Communication of a receiver state. Section 7.7.4 COMPLETE"""

    def __init__(self,
                 receiverState=0,
                 receivedPower=0.0,
                 transmitterEntityID=None,
                 transmitterRadioId=0):
        """ Initializer for ReceiverPdu"""
        super(ReceiverPdu, self).__init__()
        self.receiverState = receiverState
        """ encoding scheme used, and enumeration"""
        self.padding1 = 0
        """ padding"""
        self.receivedPower = receivedPower
        """ received power"""
        self.transmitterEntityID = transmitterEntityID or EntityID()
        """ ID of transmitter"""
        self.transmitterRadioId = transmitterRadioId
        """ ID of transmitting radio"""
        self.pduType = 27
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ReceiverPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_short(self.receiverState)
        outputStream.write_unsigned_short(self.padding1)
        outputStream.write_float(self.receivedPower)
        self.transmitterEntityId.serialize(outputStream)
        outputStream.write_unsigned_short(self.transmitterRadioId)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ReceiverPdu, self).parse(inputStream)
        self.receiverState = inputStream.read_unsigned_short()
        self.padding1 = inputStream.read_unsigned_short()
        self.receivedPower = inputStream.read_float()
        self.transmitterEntityId.parse(inputStream)
        self.transmitterRadioId = inputStream.read_unsigned_short()



class UaPdu( DistributedEmissionsFamilyPdu ):
    """ Information about underwater acoustic emmissions. This requires manual cleanup.  The beam data records should ALL be a the finish, rather than attached to each emitter system. Section 7.6.4. UNFINISHED"""

    def __init__(self,
                 emittingEntityID=None,
                 eventID=None,
                 stateChangeIndicator=0,
                 passiveParameterIndex=0,
                 propulsionPlantConfiguration=0,
                 numberOfShafts=0,
                 numberOfAPAs=0,
                 numberOfUAEmitterSystems=0,
                 shaftRPMs=None,
                 apaData=None,
                 emitterSystems=None):
        """ Initializer for UaPdu"""
        super(UaPdu, self).__init__()
        self.emittingEntityID = emittingEntityID or EntityID()
        """ ID of the entity that is the source of the emission"""
        self.eventID = eventID or EventIdentifier()
        """ ID of event"""
        self.stateChangeIndicator = stateChangeIndicator
        """ This field shall be used to indicate whether the data in the UA PDU represent a state update or data that have changed since issuance of the last UA PDU"""
        self.pad = 0
        """ padding"""
        self.passiveParameterIndex = passiveParameterIndex
        """ This field indicates which database record (or file) shall be used in the definition of passive signature (unintentional) emissions of the entity. The indicated database record (or  file) shall define all noise generated as a function of propulsion plant configurations and associated  auxiliaries."""
        self.propulsionPlantConfiguration = propulsionPlantConfiguration
        """ This field shall specify the entity propulsion plant configuration. This field is used to determine the passive signature characteristics of an entity."""
        self.numberOfShafts = numberOfShafts
        """  This field shall represent the number of shafts on a platform"""
        self.numberOfAPAs = numberOfAPAs
        """ This field shall indicate the number of APAs described in the current UA PDU"""
        self.numberOfUAEmitterSystems = numberOfUAEmitterSystems
        """ This field shall specify the number of UA emitter systems being described in the current UA PDU"""
        self.shaftRPMs = shaftRPMs or []
        """ shaft RPM values. THIS IS WRONG. It has the wrong class in the list."""
        self.apaData = apaData or []
        """ apaData. THIS IS WRONG. It has the worng class in the list."""
        self.emitterSystems = emitterSystems or []
        """ THIS IS WRONG. It has the wrong class in the list."""
        self.pduType = 29
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( UaPdu, self ).serialize(outputStream)
        self.emittingEntityID.serialize(outputStream)
        self.eventID.serialize(outputStream)
        outputStream.write_byte(self.stateChangeIndicator)
        outputStream.write_byte(self.pad)
        outputStream.write_unsigned_short(self.passiveParameterIndex)
        outputStream.write_unsigned_byte(self.propulsionPlantConfiguration)
        outputStream.write_unsigned_byte( len(self.shaftRPMs))
        outputStream.write_unsigned_byte( len(self.apaData))
        outputStream.write_unsigned_byte( len(self.emitterSystems))
        for anObj in self.shaftRPMs:
            anObj.serialize(outputStream)

        for anObj in self.apaData:
            anObj.serialize(outputStream)

        for anObj in self.emitterSystems:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( UaPdu, self).parse(inputStream)
        self.emittingEntityID.parse(inputStream)
        self.eventID.parse(inputStream)
        self.stateChangeIndicator = inputStream.read_byte()
        self.pad = inputStream.read_byte()
        self.passiveParameterIndex = inputStream.read_unsigned_short()
        self.propulsionPlantConfiguration = inputStream.read_unsigned_byte()
        self.numberOfShafts = inputStream.read_unsigned_byte()
        self.numberOfAPAs = inputStream.read_unsigned_byte()
        self.numberOfUAEmitterSystems = inputStream.read_unsigned_byte()
        for idx in range(0, self.numberOfShafts):
            element = null()
            element.parse(inputStream)
            self.shaftRPMs.append(element)

        for idx in range(0, self.numberOfAPAs):
            element = null()
            element.parse(inputStream)
            self.apaData.append(element)

        for idx in range(0, self.numberOfUAEmitterSystems):
            element = null()
            element.parse(inputStream)
            self.emitterSystems.append(element)




class IntercomControlPdu( RadioCommunicationsFamilyPdu ):
    """ Detailed inofrmation about the state of an intercom device and the actions it is requesting of another intercom device, or the response to a requested action. Required manual intervention to fix the intercom parameters, which can be of variable length. Section 7.7.5 UNFINSISHED"""

    def __init__(self,
                 controlType=0,
                 communicationsChannelType=0,
                 sourceEntityID=None,
                 sourceCommunicationsDeviceID=0,
                 sourceLineID=0,
                 transmitPriority=0,
                 transmitLineState=0,
                 command=0,
                 masterEntityID=None,
                 masterCommunicationsDeviceID=0,
                 intercomParametersLength=0,
                 intercomParameters=None):
        """ Initializer for IntercomControlPdu"""
        super(IntercomControlPdu, self).__init__()
        self.controlType = controlType
        """ control type"""
        self.communicationsChannelType = communicationsChannelType
        """ control type"""
        self.sourceEntityID = sourceEntityID or EntityID()
        """ Source entity ID"""
        self.sourceCommunicationsDeviceID = sourceCommunicationsDeviceID
        """ The specific intercom device being simulated within an entity."""
        self.sourceLineID = sourceLineID
        """ Line number to which the intercom control refers"""
        self.transmitPriority = transmitPriority
        """ priority of this message relative to transmissons from other intercom devices"""
        self.transmitLineState = transmitLineState
        """ current transmit state of the line"""
        self.command = command
        """ detailed type requested."""
        self.masterEntityID = masterEntityID or EntityID()
        """ eid of the entity that has created this intercom channel."""
        self.masterCommunicationsDeviceID = masterCommunicationsDeviceID
        """ specific intercom device that has created this intercom channel"""
        self.intercomParametersLength = intercomParametersLength
        """ number of intercom parameters"""
        self.intercomParameters = []
        """ ^^^This is wrong the length of the data field is variable. Using a long for now."""
        self.pduType = 32
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( IntercomControlPdu, self ).serialize(outputStream)
        outputStream.write_unsigned_byte(self.controlType)
        outputStream.write_unsigned_byte(self.communicationsChannelType)
        self.sourceEntityID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.sourceCommunicationsDeviceID)
        outputStream.write_unsigned_byte(self.sourceLineID)
        outputStream.write_unsigned_byte(self.transmitPriority)
        outputStream.write_unsigned_byte(self.transmitLineState)
        outputStream.write_unsigned_byte(self.command)
        self.masterEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.masterCommunicationsDeviceID)
        outputStream.write_unsigned_int( len(self.intercomParameters))
        for anObj in self.intercomParameters:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( IntercomControlPdu, self).parse(inputStream)
        self.controlType = inputStream.read_unsigned_byte()
        self.communicationsChannelType = inputStream.read_unsigned_byte()
        self.sourceEntityID.parse(inputStream)
        self.sourceCommunicationsDeviceID = inputStream.read_unsigned_byte()
        self.sourceLineID = inputStream.read_unsigned_byte()
        self.transmitPriority = inputStream.read_unsigned_byte()
        self.transmitLineState = inputStream.read_unsigned_byte()
        self.command = inputStream.read_unsigned_byte()
        self.masterEntityID.parse(inputStream)
        self.masterCommunicationsDeviceID = inputStream.read_unsigned_short()
        self.intercomParametersLength = inputStream.read_unsigned_int()
        for idx in range(0, self.intercomParametersLength):
            element = null()
            element.parse(inputStream)
            self.intercomParameters.append(element)




class SignalPdu( RadioCommunicationsFamilyPdu ):
    """ Detailed information about a radio transmitter. This PDU requires manually written code to complete. The encodingScheme field can be used in multiple ways, which requires hand-written code to finish. Section 7.7.3. UNFINISHED"""

    def __init__(self,
                 entityID=None,
                 radioID=0,
                 encodingScheme=0,
                 tdlType=0,
                 sampleRate=0,
                 dataLength=0,
                 samples=0,
                 data=None):
        """ Initializer for SignalPdu"""
        super(SignalPdu, self).__init__()

        self.entityID = entityID or EntityID()

        self.radioID = radioID

        self.encodingScheme = encodingScheme
        """ encoding scheme used, and enumeration"""
        self.tdlType = tdlType
        """ tdl type"""
        self.sampleRate = sampleRate
        """ sample rate"""
        self.dataLength = dataLength
        """ length od data"""
        self.samples = samples
        """ number of samples"""
        self.data = data or []
        """ list of eight bit values"""
        self.pduType = 26
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( SignalPdu, self ).serialize(outputStream)
        self.entityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.radioID)
        outputStream.write_unsigned_short(self.encodingScheme)
        outputStream.write_unsigned_short(self.tdlType)
        outputStream.write_unsigned_int(self.sampleRate)
        outputStream.write_short( len(self.data) * 8)
        outputStream.write_short(self.samples)
        for b in self.data:
            outputStream.write_byte(b)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( SignalPdu, self).parse(inputStream)
        self.entityID.parse(inputStream)
        self.radioID = inputStream.read_unsigned_short()
        self.encodingScheme = inputStream.read_unsigned_short()
        self.tdlType = inputStream.read_unsigned_short()
        self.sampleRate = inputStream.read_unsigned_int()
        self.dataLength = inputStream.read_short()
        self.samples = inputStream.read_short()
        for idx in range(0, self.dataLength // 8):
            element = inputStream.read_byte()
            self.data.append(element)




class RemoveEntityReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.2: Removal of an entity , reliable. COMPLETE"""

    def __init__(self, requiredReliabilityService=0, requestID=0):
        """ Initializer for RemoveEntityReliablePdu"""
        super(RemoveEntityReliablePdu, self).__init__()
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding"""
        self.pad2 = 0
        """ padding"""
        self.requestID = requestID
        """ Request ID"""
        self.pduType = 52
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( RemoveEntityReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( RemoveEntityReliablePdu, self).parse(inputStream)
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.requestID = inputStream.read_unsigned_int()



class SeesPdu( DistributedEmissionsFamilyPdu ):
    """ SEES PDU, supplemental emissions entity state information. Section 7.6.6 COMPLETE"""

    def __init__(self,
                 originatingEntityID=None,
                 infraredSignatureRepresentationIndex=0,
                 acousticSignatureRepresentationIndex=0,
                 radarCrossSectionSignatureRepresentationIndex=0,
                 numberOfPropulsionSystems=0,
                 numberOfVectoringNozzleSystems=0,
                 propulsionSystemData=None,
                 vectoringSystemData=None):
        """ Initializer for SeesPdu"""
        super(SeesPdu, self).__init__()
        self.orginatingEntityID = originatingEntityID or EntityID()
        """ Originating entity ID"""
        self.infraredSignatureRepresentationIndex = infraredSignatureRepresentationIndex
        """ IR Signature representation index"""
        self.acousticSignatureRepresentationIndex = acousticSignatureRepresentationIndex
        """ acoustic Signature representation index"""
        self.radarCrossSectionSignatureRepresentationIndex = radarCrossSectionSignatureRepresentationIndex
        """ radar cross section representation index"""
        self.numberOfPropulsionSystems = numberOfPropulsionSystems
        """ how many propulsion systems"""
        self.numberOfVectoringNozzleSystems = numberOfVectoringNozzleSystems
        """ how many vectoring nozzle systems"""
        self.propulsionSystemData = propulsionSystemData or []
        """ variable length list of propulsion system data"""
        self.vectoringSystemData = vectoringSystemData or []
        """ variable length list of vectoring system data"""
        self.pduType = 30
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( SeesPdu, self ).serialize(outputStream)
        self.orginatingEntityID.serialize(outputStream)
        outputStream.write_unsigned_short(self.infraredSignatureRepresentationIndex)
        outputStream.write_unsigned_short(self.acousticSignatureRepresentationIndex)
        outputStream.write_unsigned_short(self.radarCrossSectionSignatureRepresentationIndex)
        outputStream.write_unsigned_short( len(self.propulsionSystemData))
        outputStream.write_unsigned_short( len(self.vectoringSystemData))
        for anObj in self.propulsionSystemData:
            anObj.serialize(outputStream)

        for anObj in self.vectoringSystemData:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( SeesPdu, self).parse(inputStream)
        self.orginatingEntityID.parse(inputStream)
        self.infraredSignatureRepresentationIndex = inputStream.read_unsigned_short()
        self.acousticSignatureRepresentationIndex = inputStream.read_unsigned_short()
        self.radarCrossSectionSignatureRepresentationIndex = inputStream.read_unsigned_short()
        self.numberOfPropulsionSystems = inputStream.read_unsigned_short()
        self.numberOfVectoringNozzleSystems = inputStream.read_unsigned_short()
        for idx in range(0, self.numberOfPropulsionSystems):
            element = null()
            element.parse(inputStream)
            self.propulsionSystemData.append(element)

        for idx in range(0, self.numberOfVectoringNozzleSystems):
            element = null()
            element.parse(inputStream)
            self.vectoringSystemData.append(element)




class CreateEntityReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.1: creation of an entity , reliable. COMPLETE"""

    def __init__(self, requiredReliabilityService=0, requestID=0):
        """ Initializer for CreateEntityReliablePdu"""
        super(CreateEntityReliablePdu, self).__init__()
        self.requiredReliabilityService = requiredReliabilityService
        """ level of reliability service used for this transaction"""
        self.pad1 = 0
        """ padding"""
        self.pad2 = 0
        """ padding"""
        self.requestID = requestID
        """ Request ID"""
        self.pduType = 51
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( CreateEntityReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_byte(self.requiredReliabilityService)
        outputStream.write_unsigned_short(self.pad1)
        outputStream.write_unsigned_byte(self.pad2)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( CreateEntityReliablePdu, self).parse(inputStream)
        self.requiredReliabilityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_short()
        self.pad2 = inputStream.read_unsigned_byte()
        self.requestID = inputStream.read_unsigned_int()



class StopFreezeReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.4: Stop freeze simulation, relaible. COMPLETE"""

    def __init__(self,
                 realWorldTime=None,
                 reason=0,
                 frozenBehavior=0,
                 requiredReliabilityService=0,
                 requestID=0):
        """ Initializer for StopFreezeReliablePdu"""
        super(StopFreezeReliablePdu, self).__init__()
        self.realWorldTime = realWorldTime or ClockTime()
        """ time in real world for this operation to happen"""
        self.reason = reason
        """ Reason for stopping/freezing simulation"""
        self.frozenBehavior = frozenBehavior
        """ internal behvior of the simulation while frozen"""
        self.requiredReliablityService = requiredReliabilityService
        """ reliablity level"""
        self.pad1 = 0
        """ padding"""
        self.requestID = requestID
        """ Request ID"""
        self.pduType = 54
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( StopFreezeReliablePdu, self ).serialize(outputStream)
        self.realWorldTime.serialize(outputStream)
        outputStream.write_unsigned_byte(self.reason)
        outputStream.write_unsigned_byte(self.frozenBehavior)
        outputStream.write_unsigned_byte(self.requiredReliablityService)
        outputStream.write_unsigned_byte(self.pad1)
        outputStream.write_unsigned_int(self.requestID)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( StopFreezeReliablePdu, self).parse(inputStream)
        self.realWorldTime.parse(inputStream)
        self.reason = inputStream.read_unsigned_byte()
        self.frozenBehavior = inputStream.read_unsigned_byte()
        self.requiredReliablityService = inputStream.read_unsigned_byte()
        self.pad1 = inputStream.read_unsigned_byte()
        self.requestID = inputStream.read_unsigned_int()



class EventReportReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.11: reports the occurance of a significant event to the simulation manager. Needs manual intervention to fix padding in variable datums. UNFINISHED."""

    def __init__(self,
                 eventType=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for EventReportReliablePdu"""
        super(EventReportReliablePdu, self).__init__()
        self.eventType = eventType
        """ Event type"""
        self.pad1 = 0
        """ padding"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Fixed datum record count"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ variable datum record count"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ Fixed datum records"""
        self.variableDatumRecords = variableDatumRecords or []
        """ Variable datum records"""
        self.pduType = 61
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( EventReportReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_short(self.eventType)
        outputStream.write_unsigned_int(self.pad1)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( EventReportReliablePdu, self).parse(inputStream)
        self.eventType = inputStream.read_unsigned_short()
        self.pad1 = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class MinefieldResponseNackPdu( MinefieldFamilyPdu ):
    """proivde the means to request a retransmit of a minefield data pdu. Section 7.9.5 COMPLETE"""

    def __init__(self,
                 minefieldID=None,
                 requestingEntityID=None,
                 requestID=0,
                 numberOfMissingPdus=0,
                 missingPduSequenceNumbers=None):
        """ Initializer for MinefieldResponseNackPdu"""
        super(MinefieldResponseNackPdu, self).__init__()
        self.minefieldID = minefieldID or EntityID()
        """ Minefield ID"""
        self.requestingEntityID = requestingEntityID or EntityID()
        """ entity ID making the request"""
        self.requestID = requestID
        """ request ID"""
        self.numberOfMissingPdus = numberOfMissingPdus
        """ how many pdus were missing"""
        self.missingPduSequenceNumbers = missingPduSequenceNumbers or []
        """ PDU sequence numbers that were missing"""
        self.pduType = 40
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( MinefieldResponseNackPdu, self ).serialize(outputStream)
        self.minefieldID.serialize(outputStream)
        self.requestingEntityID.serialize(outputStream)
        outputStream.write_unsigned_byte(self.requestID)
        outputStream.write_unsigned_byte( len(self.missingPduSequenceNumbers))
        for anObj in self.missingPduSequenceNumbers:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( MinefieldResponseNackPdu, self).parse(inputStream)
        self.minefieldID.parse(inputStream)
        self.requestingEntityID.parse(inputStream)
        self.requestID = inputStream.read_unsigned_byte()
        self.numberOfMissingPdus = inputStream.read_unsigned_byte()
        for idx in range(0, self.numberOfMissingPdus):
            element = null()
            element.parse(inputStream)
            self.missingPduSequenceNumbers.append(element)




class ActionResponseReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
    """Section 5.3.12.7: Response from an entity to an action request PDU. COMPLETE"""

    def __init__(self,
                 requestID=0,
                 responseStatus=0,
                 numberOfFixedDatumRecords=0,
                 numberOfVariableDatumRecords=0,
                 fixedDatumRecords=None,
                 variableDatumRecords=None):
        """ Initializer for ActionResponseReliablePdu"""
        super(ActionResponseReliablePdu, self).__init__()
        self.requestID = requestID
        """ request ID"""
        self.responseStatus = responseStatus
        """ status of response"""
        self.numberOfFixedDatumRecords = numberOfFixedDatumRecords
        """ Fixed datum record count"""
        self.numberOfVariableDatumRecords = numberOfVariableDatumRecords
        """ variable datum record count"""
        self.fixedDatumRecords = fixedDatumRecords or []
        """ Fixed datum records"""
        self.variableDatumRecords = variableDatumRecords or []
        """ Variable datum records"""
        self.pduType = 57
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( ActionResponseReliablePdu, self ).serialize(outputStream)
        outputStream.write_unsigned_int(self.requestID)
        outputStream.write_unsigned_int(self.responseStatus)
        outputStream.write_unsigned_int( len(self.fixedDatumRecords))
        outputStream.write_unsigned_int( len(self.variableDatumRecords))
        for anObj in self.fixedDatumRecords:
            anObj.serialize(outputStream)

        for anObj in self.variableDatumRecords:
            anObj.serialize(outputStream)



    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( ActionResponseReliablePdu, self).parse(inputStream)
        self.requestID = inputStream.read_unsigned_int()
        self.responseStatus = inputStream.read_unsigned_int()
        self.numberOfFixedDatumRecords = inputStream.read_unsigned_int()
        self.numberOfVariableDatumRecords = inputStream.read_unsigned_int()
        for idx in range(0, self.numberOfFixedDatumRecords):
            element = FixedDatum()
            element.parse(inputStream)
            self.fixedDatumRecords.append(element)

        for idx in range(0, self.numberOfVariableDatumRecords):
            element = VariableDatum()
            element.parse(inputStream)
            self.variableDatumRecords.append(element)




class IsPartOfPdu( EntityManagementFamilyPdu ):
    """ The joining of two or more simulation entities is communicated by this PDU. Section 7.8.5 COMPLETE"""

    def __init__(self,
                 originatingEntityID=None,
                 receivingEntityID=None,
                 relationship=None,
                 partLocation=None,
                 namedLocationID=None,
                 partEntityType=None):
        """ Initializer for IsPartOfPdu"""
        super(IsPartOfPdu, self).__init__()
        self.orginatingEntityID = originatingEntityID or EntityID()
        """ ID of entity originating PDU"""
        self.receivingEntityID = receivingEntityID or EntityID()
        """ ID of entity receiving PDU"""
        self.relationship = relationship or Relationship()
        """ relationship of joined parts"""
        self.partLocation = partLocation or Vector3Float()
        """ location of part; centroid of part in host's coordinate system. x=range, y=bearing, z=0"""
        self.namedLocationID = namedLocationID or NamedLocationIdentification()
        """ named location"""
        self.partEntityType = partEntityType or EntityType()
        """ entity type"""
        self.pduType = 36
        """ initialize value """

    def serialize(self, outputStream):
        """serialize the class """
        super( IsPartOfPdu, self ).serialize(outputStream)
        self.orginatingEntityID.serialize(outputStream)
        self.receivingEntityID.serialize(outputStream)
        self.relationship.serialize(outputStream)
        self.partLocation.serialize(outputStream)
        self.namedLocationID.serialize(outputStream)
        self.partEntityType.serialize(outputStream)


    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""

        super( IsPartOfPdu, self).parse(inputStream)
        self.orginatingEntityID.parse(inputStream)
        self.receivingEntityID.parse(inputStream)
        self.relationship.parse(inputStream)
        self.partLocation.parse(inputStream)
        self.namedLocationID.parse(inputStream)
        self.partEntityType.parse(inputStream)
