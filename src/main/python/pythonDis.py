#
#This code is licensed under the BSD software license
#

class DataQueryDatumSpecification( object ):
"""List of fixed and variable datum records. Section 6.2.17 
"""

    def __init__(self):
    """ Initializer for DataQueryDatumSpecification"""
            super(DataQueryDatumSpecification, self).__init__()
            self.numberOfFixedDatums = 0
            """ Number of fixed datums"""
            self.numberOfVariableDatums = 0
            """ Number of variable datums"""
            fixedDatumIDList = []
            """ variable length list fixed datum IDs"""
            variableDatumIDList = []
            """ variable length list variable datum IDs"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class StartResumeReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.3: Start resume simulation, relaible. COMPLETE
"""

    def __init__(self):
    """ Initializer for StartResumeReliablePdu"""
            super(StartResumeReliablePdu, self).__init__()
            realWorldTime = ClockTime();
            """ time in real world for this operation to happen"""
            simulationTime = ClockTime();
            """ time in simulation for the simulation to resume"""
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding"""
            self.pad2 = 0
            """ padding"""
            self.requestID = 0
            """ Request ID"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ArealObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
"""Information about the addition/modification of an oobject that is geometrically anchored to the terrain with a set of three or more points that come to a closure. Section 7.10.6 COMPLETE
"""

    def __init__(self):
    """ Initializer for ArealObjectStatePdu"""
            super(ArealObjectStatePdu, self).__init__()
            objectID = EntityID();
            """ Object in synthetic environment"""
            referencedObjectID = EntityID();
            """ Object with which this point object is associated"""
            self.updateNumber = 0
            """ unique update number of each state transition of an object"""
            self.forceID = 0
            """ force ID"""
            self.modifications = 0
            """ modifications enumeration"""
            objectType = EntityType();
            """ Object type"""
            self.specificObjectAppearance = 0
            """ Object appearance"""
            self.generalObjectAppearance = 0
            """ Object appearance"""
            self.numberOfPoints = 0
            """ Number of points"""
            requesterID = SimulationAddress();
            """ requesterID"""
            receivingID = SimulationAddress();
            """ receiver ID"""
            objectLocation = []
            """ location of object"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RadioIdentifier( object ):
"""The unique designation of an attached or unattached radio in an event or exercise Section 6.2.70
"""

    def __init__(self):
    """ Initializer for RadioIdentifier"""
            super(RadioIdentifier, self).__init__()
            self.siteNumber = 0
            """  site"""
            self.applicationNumber = 0
            """ application number"""
            self.referenceNumber = 0
            """  reference number"""
            self.radioNumber = 0
            """  Radio number"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RequestID( object ):
"""A monotonically increasing number inserted into all simulation managment PDUs. This should be a hand-coded thingie, maybe a singleton. Section 6.2.75
"""

    def __init__(self):
    """ Initializer for RequestID"""
            super(RequestID, self).__init__()
            self.requestID = 0
            """ monotonically increasing number"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LiveEntityPdu( PduSuperclass ):
"""The live entity PDUs have a header with some different field names, but the same length. Section 9.3.2
"""

    def __init__(self):
    """ Initializer for LiveEntityPdu"""
            super(LiveEntityPdu, self).__init__()
            self.subprotocolNumber = 0
            """ Subprotocol used to decode the PDU. Section 13 of EBV."""
            self.padding = 0
            """ zero-filled array of padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IFFData( object ):
"""repeating element if IFF Data specification record
"""

    def __init__(self):
    """ Initializer for IFFData"""
            super(IFFData, self).__init__()
            self.recordType = 0
            """ enumeration for type of record"""
            self.recordLength = 0
            """ length of record. Should be padded to 32 bit boundary."""
            iffData = []
            """ IFF data."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MunitionDescriptor( object ):
"""Represents the firing or detonation of a munition. Section 6.2.19.2
"""

    def __init__(self):
    """ Initializer for MunitionDescriptor"""
            super(MunitionDescriptor, self).__init__()
            munitionType = EntityType();
            """ What munition was used in the burst"""
            self.warhead = 0
            """ type of warhead enumeration"""
            self.fuse = 0
            """ type of fuse used enumeration"""
            self.quantity = 0
            """ how many of the munition were fired"""
            self.rate = 0
            """ rate at which the munition was fired"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MinefieldSensorType( object ):
"""Information about a minefield sensor. Section 6.2.57
"""

    def __init__(self):
    """ Initializer for MinefieldSensorType"""
            super(MinefieldSensorType, self).__init__()
            self.sensorType = 0
            """ sensor type. bit fields 0-3 are the type category, 4-15 are teh subcategory"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DataQueryReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.8: request for data from an entity. COMPLETE
"""

    def __init__(self):
    """ Initializer for DataQueryReliablePdu"""
            super(DataQueryReliablePdu, self).__init__()
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding"""
            self.pad2 = 0
            """ padding"""
            self.requestID = 0
            """ request ID"""
            self.timeInterval = 0
            """ time interval between issuing data query PDUs"""
            self.numberOfFixedDatumRecords = 0
            """ Fixed datum record count"""
            self.numberOfVariableDatumRecords = 0
            """ variable datum record count"""
            fixedDatumRecords = []
            """ Fixed datum records"""
            variableDatumRecords = []
            """ Variable datum records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class PduStream( object ):
"""Non-DIS class, used to describe streams of PDUS when logging data to a SQL database. This is not in the DIS standard but can be helpful when logging to a Hibernate sql database
"""

    def __init__(self):
    """ Initializer for PduStream"""
            super(PduStream, self).__init__()
            description =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            """ Longish description of this PDU stream"""
            name =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            """ short description of this PDU stream"""
            self.startTime = 0
            """ Start time of recording, in Unix time (seconds since epoch)"""
            self.stopTime = 0
            """ stop time of recording, in Unix time (seconds since epoch)"""
            self.pduCount = 0
            """ how many PDUs in this stream"""
            pdusInStream = []
            """ variable length list of PDUs"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class GroupID( object ):
"""Unique designation of a group of entities contained in the isGroupOfPdu. Represents a group of entities rather than a single entity. Section 6.2.43
"""

    def __init__(self):
    """ Initializer for GroupID"""
            super(GroupID, self).__init__()
            simulationAddress = EntityType();
            """ Simulation address (site and application number)"""
            self.groupNumber = 0
            """ group number"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LogisticsFamilyPdu( Pdu ):
""" Abstract superclass for logistics PDUs. Section 7.4 COMPLETE
"""

    def __init__(self):
    """ Initializer for LogisticsFamilyPdu"""
            super(LogisticsFamilyPdu, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityStateUpdatePdu( EntityInformationFamilyPdu ):
"""Nonstatic information about a particular entity may be communicated by issuing an Entity State Update PDU. Section 7.2.5. COMPLETE
"""

    def __init__(self):
    """ Initializer for EntityStateUpdatePdu"""
            super(EntityStateUpdatePdu, self).__init__()
            entityID = EntityID();
            """ This field shall identify the entity issuing the PDU, and shall be represented by an Entity Identifier record (see 6.2.28)."""
            self.padding1 = 0
            """ Padding"""
            self.numberOfVariableParameters = 0
            """ This field shall specify the number of variable parameters present. This field shall be represented by an 8-bit unsigned integer (see Annex I)."""
            entityLinearVelocity = Vector3Float();
            """ This field shall specify an entity’s linear velocity. The coordinate system for an entity’s linear velocity depends on the dead reckoning algorithm used. This field shall be represented by a Linear Velocity Vector record [see 6.2.95 item c)])."""
            entityLocation = Vector3Double();
            """ This field shall specify an entity’s physical location in the simulated world and shall be represented by a World Coordinates record (see 6.2.97)."""
            entityOrientation = EulerAngles();
            """ This field shall specify an entity’s orientation and shall be represented by an Euler Angles record (see 6.2.33)."""
            self.entityAppearance = 0
            """ This field shall specify the dynamic changes to the entity’s appearance attributes. This field shall be represented by an Entity Appearance record (see 6.2.26)."""
            variableParameters = []
            """ This field shall specify the parameter values for each Variable Parameter record that is included (see 6.2.93 and Annex I)."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MinefieldStatePdu( MinefieldFamilyPdu ):
"""information about the complete minefield. The minefield presence, perimiter, etc. Section 7.9.2 COMPLETE
"""

    def __init__(self):
    """ Initializer for MinefieldStatePdu"""
            super(MinefieldStatePdu, self).__init__()
            minefieldID = MinefieldIdentifier();
            """ Minefield ID"""
            self.minefieldSequence = 0
            """ Minefield sequence"""
            self.forceID = 0
            """ force ID"""
            self.numberOfPerimeterPoints = 0
            """ Number of permieter points"""
            minefieldType = EntityType();
            """ type of minefield"""
            self.numberOfMineTypes = 0
            """ how many mine types"""
            minefieldLocation = Vector3Double();
            """ location of center of minefield in world coords"""
            minefieldOrientation = EulerAngles();
            """ orientation of minefield"""
            self.appearance = 0
            """ appearance bitflags"""
            self.protocolMode = 0
            """ protocolMode. First two bits are the protocol mode, 14 bits reserved."""
            perimeterPoints = []
            """ perimeter points for the minefield"""
            mineType = []
            """ Type of mines"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LayerHeader( object ):
"""The identification of the additional information layer number, layer-specific information, and the length of the layer. Section 6.2.51
"""

    def __init__(self):
    """ Initializer for LayerHeader"""
            super(LayerHeader, self).__init__()
            self.layerNumber = 0
            self.layerSpecificInformation = 0
            """ field shall specify layer-specific information that varies by System Type (see 6.2.86) and Layer Number."""
            self.length = 0
            """ This field shall specify the length in octets of the layer, including the Layer Header record"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class UnsignedDISInteger( object ):
"""container class not in specification
"""

    def __init__(self):
    """ Initializer for UnsignedDISInteger"""
            super(UnsignedDISInteger, self).__init__()
            self.val = 0
            """ unsigned integer"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DeadReckoningParameters( object ):
"""Not specified in the standard. This is used by the ESPDU
"""

    def __init__(self):
    """ Initializer for DeadReckoningParameters"""
            super(DeadReckoningParameters, self).__init__()
            self.deadReckoningAlgorithm = 0
            """ Algorithm to use in computing dead reckoning. See EBV doc."""
            parameters =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            """ Dead reckoning parameters. Contents depends on algorithm."""
            entityLinearAcceleration = Vector3Float();
            """ Linear acceleration of the entity"""
            entityAngularVelocity = Vector3Float();
            """ Angular velocity of the entity"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ProtocolMode( object ):
"""Bit field used to identify minefield data. bits 14-15 are a 2-bit enum, other bits unused. Section 6.2.69
"""

    def __init__(self):
    """ Initializer for ProtocolMode"""
            super(ProtocolMode, self).__init__()
            self.protocolMode = 0
            """ Bitfields, 14-15 contain an enum"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AngleDeception( object ):
"""The Angle Deception attribute record may be used to communicate discrete values that are associated with angle deception jamming that cannot be referenced to an emitter mode. The values provided in the record records (provided in the associated Electromagnetic Emission PDU). (The victim radar beams are those that are targeted by the jammer.) Section 6.2.21.2.2
"""

    def __init__(self):
    """ Initializer for AngleDeception"""
            super(AngleDeception, self).__init__()
            self.recordType = 3501
            self.recordLength = 48
            self.padding = 0
            self.emitterNumber = 0
            self.beamNumber = 0
            self.stateIndicator = 0
            self.padding2 = 0
            self.azimuthOffset = 0
            self.azimuthWidth = 0
            self.azimuthPullRate = 0
            self.azimuthPullAcceleration = 0
            self.elevationOffset = 0
            self.elevationWidth = 0
            self.elevationPullRate = 0
            self.elevationPullAcceleration = 0
            self.padding3 = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityAssociation( object ):
"""Association or disassociation of two entities.  Section 6.2.94.4.3
"""

    def __init__(self):
    """ Initializer for EntityAssociation"""
            super(EntityAssociation, self).__init__()
            self.recordType = 4
            """ the identification of the Variable Parameter record. Enumeration from EBV"""
            self.changeIndicator = 0
            """ Indicates if this VP has changed since last issuance"""
            self.associationStatus = 0
            """ Indicates association status between two entities; 8 bit enum"""
            self.associationType = 0
            """ Type of association; 8 bit enum"""
            entityID = EntityID();
            """ Object ID of entity associated with this entity"""
            self.ownStationLocation = 0
            """ Station location on one's own entity. EBV doc."""
            self.physicalConnectionType = 0
            """ Type of physical connection. EBV doc"""
            self.groupMemberType = 0
            """ Type of member the entity is within th egroup"""
            self.groupNumber = 0
            """ Group if any to which the entity belongs"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class VectoringNozzleSystem( object ):
"""Operational data for describing the vectoring nozzle systems Section 6.2.96
"""

    def __init__(self):
    """ Initializer for VectoringNozzleSystem"""
            super(VectoringNozzleSystem, self).__init__()
            self.horizontalDeflectionAngle = 0
            """ In degrees"""
            self.verticalDeflectionAngle = 0
            """ In degrees"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DataReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.10: issued in response to a data query R or set dataR pdu. Needs manual intervention      to fix padding on variable datums. UNFINSIHED
"""

    def __init__(self):
    """ Initializer for DataReliablePdu"""
            super(DataReliablePdu, self).__init__()
            self.requestID = 0
            """ Request ID"""
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding"""
            self.pad2 = 0
            """ padding"""
            self.numberOfFixedDatumRecords = 0
            """ Fixed datum record count"""
            self.numberOfVariableDatumRecords = 0
            """ variable datum record count"""
            fixedDatumRecords = []
            """ Fixed datum records"""
            variableDatumRecords = []
            """ Variable datum records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class FalseTargetsAttribute( object ):
"""The False Targets attribute record shall be used to communicate discrete values that are associated with false targets jamming that cannot be referenced to an emitter mode. The values provided in the False Targets attri- bute record shall be considered valid only for the victim radar beams listed in the jamming beam's Track/Jam Data records (provided in the associated Electromagnetic Emission PDU). Section 6.2.21.3
"""

    def __init__(self):
    """ Initializer for FalseTargetsAttribute"""
            super(FalseTargetsAttribute, self).__init__()
            self.recordType = 3502
            self.recordLength = 40
            self.padding = 0
            self.emitterNumber = 0
            self.beamNumber = 0
            self.stateIndicator = 0
            self.padding2 = 0
            self.falseTargetCount = 0
            self.walkSpeed = 0
            self.walkAcceleration = 0
            self.maximumWalkDistance = 0
            self.keepTime = 0
            self.echoSpacing = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ServiceRequestPdu( LogisticsFamilyPdu ):
"""Service Request PDU shall be used to communicate information associated with                            one entity requesting a service from another). Section 7.4.2 COMPLETE
"""

    def __init__(self):
    """ Initializer for ServiceRequestPdu"""
            super(ServiceRequestPdu, self).__init__()
            requestingEntityID = EntityID();
            """ Entity that is requesting service (see 6.2.28), Section 7.4.2"""
            servicingEntityID = EntityID();
            """ Entity that is providing the service (see 6.2.28), Section 7.4.2"""
            self.serviceTypeRequested = 0
            """ Type of service requested, Section 7.4.2"""
            self.numberOfSupplyTypes = 0
            """ How many requested, Section 7.4.2"""
            self.serviceRequestPadding = 0
            """ padding"""
            supplies = []

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MinefieldIdentifier( object ):
"""The unique designation of a minefield Section 6.2.56 
"""

    def __init__(self):
    """ Initializer for MinefieldIdentifier"""
            super(MinefieldIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """ """
            self.minefieldNumber = 0
            """ """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RepairCompletePdu( LogisticsFamilyPdu ):
"""Section 7.4.6. Service Request PDU is received and repair is complete. COMPLETE
"""

    def __init__(self):
    """ Initializer for RepairCompletePdu"""
            super(RepairCompletePdu, self).__init__()
            receivingEntityID = EntityID();
            """ Entity that is receiving service.  See 6.2.28"""
            repairingEntityID = EntityID();
            """ Entity that is supplying.  See 6.2.28"""
            self.repair = 0
            """ Enumeration for type of repair.  See 6.2.74"""
            self.padding4 = 0
            """ padding, number prevents conflict with superclass ivar name"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RadioType( object ):
"""Identifies the type of radio. Section 6.2.71
"""

    def __init__(self):
    """ Initializer for RadioType"""
            super(RadioType, self).__init__()
            self.entityKind = 0
            """ Kind of entity"""
            self.domain = 0
            """ Domain of entity (air, surface, subsurface, space, etc)"""
            self.country = 0
            """ country to which the design of the entity is attributed"""
            self.category = 0
            """ category of entity"""
            self.subcategory = 0
            """ specific info based on subcategory field"""
            self.specific = 0
            self.extra = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class NamedLocationIdentification( object ):
"""Information about the discrete positional relationship of the part entity with respect to the its host entity Section 6.2.62 
"""

    def __init__(self):
    """ Initializer for NamedLocationIdentification"""
            super(NamedLocationIdentification, self).__init__()
            self.stationName = 0
            """ the station name within the host at which the part entity is located. If the part entity is On Station, this field shall specify the representation of the part’s location data fields. This field shall be specified by a 16-bit enumeration """
            self.stationNumber = 0
            """ the number of the particular wing station, cargo hold etc., at which the part is attached. """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class FourByteChunk( object ):
"""32 bit piece of data
"""

    def __init__(self):
    """ Initializer for FourByteChunk"""
            super(FourByteChunk, self).__init__()
            otherParameters =  [ 0, 0, 0, 0]
            """ four bytes of arbitrary data"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class CommentPdu( SimulationManagementFamilyPdu ):
""" Arbitrary messages can be entered into the data stream via use of this PDU. Section 7.5.13 COMPLETE
"""

    def __init__(self):
    """ Initializer for CommentPdu"""
            super(CommentPdu, self).__init__()
            self.numberOfFixedDatumRecords = 0
            """ Number of fixed datum records"""
            self.numberOfVariableDatumRecords = 0
            """ Number of variable datum records"""
            fixedDatums = []
            """ variable length list of fixed datums"""
            variableDatums = []
            """ variable length list of variable length datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ModulationParameters( object ):
"""Modulation parameters associated with a specific radio system. INCOMPLETE. 6.2.58 
"""

    def __init__(self):
    """ Initializer for ModulationParameters"""
            super(ModulationParameters, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class CommentReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.12: Arbitrary messages. Only reliable this time. Neds manual intervention     to fix padding in variable datums. UNFINISHED
"""

    def __init__(self):
    """ Initializer for CommentReliablePdu"""
            super(CommentReliablePdu, self).__init__()
            self.numberOfFixedDatumRecords = 0
            """ Fixed datum record count"""
            self.numberOfVariableDatumRecords = 0
            """ variable datum record count"""
            fixedDatumRecords = []
            """ Fixed datum records"""
            variableDatumRecords = []
            """ Variable datum records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class OneByteChunk( object ):
"""8 bit piece of data
"""

    def __init__(self):
    """ Initializer for OneByteChunk"""
            super(OneByteChunk, self).__init__()
            otherParameters =  [ 0]
            """ one byte of arbitrary data"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EulerAngles( object ):
"""Three floating point values representing an orientation, psi, theta, and phi, aka the euler angles, in radians. Section 6.2.33
"""

    def __init__(self):
    """ Initializer for EulerAngles"""
            super(EulerAngles, self).__init__()
            self.psi = 0
            self.theta = 0
            self.phi = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DirectedEnergyFirePdu( WarfareFamilyPdu ):
"""Firing of a directed energy weapon shall be communicated by issuing a Directed Energy Fire PDU Section 7.3.4  COMPLETE
"""

    def __init__(self):
    """ Initializer for DirectedEnergyFirePdu"""
            super(DirectedEnergyFirePdu, self).__init__()
            munitionType = EntityType();
            """ Field shall identify the munition type enumeration for the DE weapon beam, Section 7.3.4 """
            shotStartTime = ClockTime();
            """ Field shall indicate the simulation time at start of the shot, Section 7.3.4 """
            self.commulativeShotTime = 0
            """ Field shall indicate the current cumulative duration of the shot, Section 7.3.4 """
            ApertureEmitterLocation = Vector3Float();
            """ Field shall identify the location of the DE weapon aperture/emitter, Section 7.3.4 """
            self.apertureDiameter = 0
            """ Field shall identify the beam diameter at the aperture/emitter, Section 7.3.4 """
            self.wavelength = 0
            """ Field shall identify the emissions wavelength in units of meters, Section 7.3.4 """
            self.peakIrradiance = 0
            """ Field shall identify the current peak irradiance of emissions in units of Watts per square meter, Section 7.3.4 """
            self.pulseRepetitionFrequency = 0
            """ field shall identify the current pulse repetition frequency in units of cycles per second (Hertz), Section 7.3.4 """
            self.pulseWidth = 0
            """ field shall identify the pulse width emissions in units of seconds, Section 7.3.4"""
            self.flags = 0
            """ 16bit Boolean field shall contain various flags to indicate status information needed to process a DE, Section 7.3.4 """
            self.pulseShape = 0
            """ Field shall identify the pulse shape and shall be represented as an 8-bit enumeration, Section 7.3.4 """
            self.padding1 = 0
            """ padding, Section 7.3.4 """
            self.padding2 = 0
            """ padding, Section 7.3.4 """
            self.padding3 = 0
            """ padding, Section 7.3.4 """
            self.numberOfDERecords = 0
            """ Field shall specify the number of DE records, Section 7.3.4 """
            dERecords = []
            """ Fields shall contain one or more DE records, records shall conform to the variable record format (Section6.2.82), Section 7.3.4"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DirectedEnergyPrecisionAimpoint( object ):
"""DE Precision Aimpoint Record. Section 6.2.20.3
"""

    def __init__(self):
    """ Initializer for DirectedEnergyPrecisionAimpoint"""
            super(DirectedEnergyPrecisionAimpoint, self).__init__()
            self.recordType = 4000
            """ Type of Record"""
            self.recordLength = 88
            """ Length of Record"""
            self.padding = 0
            """ Padding"""
            targetSpotLocation = Vector3Double();
            """ Position of Target Spot in World Coordinates."""
            targetSpotEntityLocation = Vector3Float();
            """ Position (meters) of Target Spot relative to Entity Position."""
            targetSpotVelocity = Vector3Float();
            """ Velocity (meters/sec) of Target Spot."""
            targetSpotAcceleration = Vector3Float();
            """ Acceleration (meters/sec/sec) of Target Spot."""
            targetEntityID = EntityID();
            """ Unique ID of the target entity."""
            self.targetComponentID = 0
            """ Target Component ID ENUM, same as in DamageDescriptionRecord."""
            self.beamSpotType = 0
            """ Spot Shape ENUM."""
            self.beamSpotCrossSectionSemiMajorAxis = 0
            """ Beam Spot Cross Section Semi-Major Axis."""
            self.beamSpotCrossSectionSemiMinorAxis = 0
            """ Beam Spot Cross Section Semi-Major Axis."""
            self.beamSpotCrossSectionOrientationAngle = 0
            """ Beam Spot Cross Section Orientation Angle."""
            self.peakIrradiance = 0
            """ Peak irradiance"""
            self.padding2 = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DetonationPdu( WarfareFamilyPdu ):
"""Detonation or impact of munitions, as well as, non-munition explosions, the burst or initial bloom of chaff, and the ignition of a flare shall be indicated. Section 7.3.3  COMPLETE
"""

    def __init__(self):
    """ Initializer for DetonationPdu"""
            super(DetonationPdu, self).__init__()
            explodingEntityID = EntityID();
            """ ID of the expendable entity, Section 7.3.3 """
            eventID = EventIdentifier();
            """ ID of event, Section 7.3.3"""
            velocity = Vector3Float();
            """ velocity of the munition immediately before detonation/impact, Section 7.3.3 """
            locationInWorldCoordinates = Vector3Double();
            """ location of the munition detonation, the expendable detonation, Section 7.3.3 """
            descriptor = MunitionDescriptor();
            """ Describes the detonation represented, Section 7.3.3 """
            locationOfEntityCoordinates = Vector3Float();
            """ Velocity of the ammunition, Section 7.3.3 """
            self.detonationResult = 0
            """ result of the detonation, Section 7.3.3 """
            self.numberOfVariableParameters = 0
            """ How many articulation parameters we have, Section 7.3.3 """
            self.pad = 0
            """ padding"""
            variableParameters = []
            """ specify the parameter values for each Variable Parameter record, Section 7.3.3 """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IffDataSpecification( object ):
"""Requires hand coding to be useful. Section 6.2.43
"""

    def __init__(self):
    """ Initializer for IffDataSpecification"""
            super(IffDataSpecification, self).__init__()
            self.numberOfIffDataRecords = 0
            """ Number of iff records"""
            iffDataRecords = []
            """ IFF data records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class OwnershipStatus( object ):
"""used to convey entity and conflict status information associated with transferring ownership of an entity. Section 6.2.65
"""

    def __init__(self):
    """ Initializer for OwnershipStatus"""
            super(OwnershipStatus, self).__init__()
            entityId = EntityID();
            """ EntityID"""
            self.ownershipStatus = 0
            """ The ownership and/or ownership conflict status of the entity represented by the Entity ID field."""
            self.padding = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class BeamAntennaPattern( object ):
"""Used when the antenna pattern type field has a value of 1. Specifies the direction, pattern, and polarization of radiation from an antenna. Section 6.2.9.2
"""

    def __init__(self):
    """ Initializer for BeamAntennaPattern"""
            super(BeamAntennaPattern, self).__init__()
            beamDirection = EulerAngles();
            """ The rotation that transforms the reference coordinate sytem into the beam coordinate system. Either world coordinates or entity coordinates may be used as the reference coordinate system, as specified by the reference system field of the antenna pattern record."""
            self.azimuthBeamwidth = 0
            self.elevationBeamwidth = 0
            self.referenceSystem = 0
            self.padding1 = 0
            self.padding2 = 0
            self.ez = 0.0
            """ This field shall specify the magnitude of the Z-component (in beam coordinates) of the Electrical field at some arbitrary single point in the main beam and in the far field of the antenna. """
            self.ex = 0.0
            """ This field shall specify the magnitude of the X-component (in beam coordinates) of the Electri- cal field at some arbitrary single point in the main beam and in the far field of the antenna."""
            self.phase = 0.0
            """ This field shall specify the phase angle between EZ and EX in radians. If fully omni-direc- tional antenna is modeled using beam pattern type one, the omni-directional antenna shall be repre- sented by beam direction Euler angles psi, theta, and phi of zero, an azimuth beamwidth of 2PI, and an elevation beamwidth of PI"""
            self.padding3 = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SetDataPdu( SimulationManagementFamilyPdu ):
"""Section 7.5.10. Change state information with the data contained in this. COMPLETE
"""

    def __init__(self):
    """ Initializer for SetDataPdu"""
            super(SetDataPdu, self).__init__()
            self.requestID = 0
            """ ID of request"""
            self.padding1 = 0
            """ padding"""
            self.numberOfFixedDatumRecords = 0
            """ Number of fixed datum records"""
            self.numberOfVariableDatumRecords = 0
            """ Number of variable datum records"""
            fixedDatums = []
            """ variable length list of fixed datums"""
            variableDatums = []
            """ variable length list of variable length datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SyntheticEnvironmentFamilyPdu( Pdu ):
"""Section 5.3.11: Abstract superclass for synthetic environment PDUs
"""

    def __init__(self):
    """ Initializer for SyntheticEnvironmentFamilyPdu"""
            super(SyntheticEnvironmentFamilyPdu, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RecordQueryReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.13: A request for one or more records of data from an entity. COMPLETE
"""

    def __init__(self):
    """ Initializer for RecordQueryReliablePdu"""
            super(RecordQueryReliablePdu, self).__init__()
            self.requestID = 0
            """ request ID"""
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding. The spec is unclear and contradictory here."""
            self.pad2 = 0
            """ padding"""
            self.eventType = 0
            """ event type"""
            self.time = 0
            """ time"""
            self.numberOfRecords = 0
            """ numberOfRecords"""
            recordIDs = []
            """ record IDs"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AttachedParts( object ):
"""Removable parts that may be attached to an entity.  Section 6.2.93.3
"""

    def __init__(self):
    """ Initializer for AttachedParts"""
            super(AttachedParts, self).__init__()
            self.recordType = 1
            """ the identification of the Variable Parameter record. Enumeration from EBV"""
            self.detachedIndicator = 0
            """ 0 = attached, 1 = detached. See I.2.3.1 for state transition diagram"""
            self.partAttachedTo = 0
            """ the identification of the articulated part to which this articulation parameter is attached. This field shall be specified by a 16-bit unsigned integer. This field shall contain the value zero if the articulated part is attached directly to the entity."""
            self.parameterType = 0
            """ The location or station to which the part is attached"""
            self.parameterValue = 0
            """ The definition of the 64 bits shall be determined based on the type of parameter specified in the Parameter Type field """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class VariableTransmitterParameters( object ):
"""Relates to radios. NOT COMPLETE. Section 6.2.94
"""

    def __init__(self):
    """ Initializer for VariableTransmitterParameters"""
            super(VariableTransmitterParameters, self).__init__()
            self.recordType = 0
            """ Type of VTP. Enumeration from EBV"""
            self.recordLength = 4
            """ Length, in bytes"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Attribute( object ):
"""Used to convey information for one or more attributes. Attributes conform to the standard variable record format of 6.2.82. Section 6.2.10. NOT COMPLETE
"""

    def __init__(self):
    """ Initializer for Attribute"""
            super(Attribute, self).__init__()
            self.recordType = 0
            self.recordLength = 0
            self.recordSpecificFields = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RecordQuerySpecification( object ):
"""The identification of the records being queried 6.2.72
"""

    def __init__(self):
    """ Initializer for RecordQuerySpecification"""
            super(RecordQuerySpecification, self).__init__()
            self.numberOfRecords = 0
            records = []
            """ variable length list of 32 bit records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class CollisionPdu( EntityInformationFamilyPdu ):
"""Section 7.2.3 Collisions between entities shall be communicated by issuing a Collision PDU. COMPLETE
"""

    def __init__(self):
    """ Initializer for CollisionPdu"""
            super(CollisionPdu, self).__init__()
            issuingEntityID = EntityID();
            """ This field shall identify the entity that is issuing the PDU, and shall be represented by an Entity Identifier record (see 6.2.28)."""
            collidingEntityID = EntityID();
            """ This field shall identify the entity that has collided with the issuing entity (see 5.3.3.4). This field shall be represented by an Entity Identifier record (see 6.2.28)."""
            eventID = EventIdentifier();
            """ This field shall contain an identification generated by the issuing simulation application to associate related collision events. This field shall be represented by an Event Identifier record (see 6.2.34)."""
            self.collisionType = 0
            """ This field shall identify the type of collision. The Collision Type field shall be represented by an 8-bit record of enumerations"""
            self.pad = 0
            """ some padding"""
            velocity = Vector3Float();
            """ This field shall contain the velocity (at the time the collision is detected) of the issuing entity. The velocity shall be represented in world coordinates. This field shall be represented by the Linear Velocity Vector record [see 6.2.95 item c)]."""
            self.mass = 0
            """ This field shall contain the mass of the issuing entity, and shall be represented by a 32-bit floating point number representing kilograms."""
            location = Vector3Float();
            """ This field shall specify the location of the collision with respect to the entity with which the issuing entity collided. The Location field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RepairResponsePdu( LogisticsFamilyPdu ):
"""Section 7.4.7. Sent after repair complete PDU. COMPLETE
"""

    def __init__(self):
    """ Initializer for RepairResponsePdu"""
            super(RepairResponsePdu, self).__init__()
            receivingEntityID = EntityID();
            """ Entity that requested repairs.  See 6.2.28"""
            repairingEntityID = EntityID();
            """ Entity that is repairing.  See 6.2.28"""
            self.repairResult = 0
            """ Result of repair operation"""
            self.padding1 = 0
            """ padding"""
            self.padding2 = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ArticulatedParts( object ):
""" articulated parts for movable parts and a combination of moveable/attached parts of an entity. Section 6.2.94.2
"""

    def __init__(self):
    """ Initializer for ArticulatedParts"""
            super(ArticulatedParts, self).__init__()
            self.recordType = 0
            """ the identification of the Variable Parameter record. Enumeration from EBV"""
            self.changeIndicator = 0
            """ indicate the change of any parameter for any articulated part. Starts at zero, incremented for each change """
            self.partAttachedTo = 0
            """ the identification of the articulated part to which this articulation parameter is attached. This field shall be specified by a 16-bit unsigned integer. This field shall contain the value zero if the articulated part is attached directly to the entity."""
            self.parameterType = 0
            """ the type of parameter represented, 32 bit enumeration"""
            self.parameterValue = 0
            """ The definition of the 64 bits shall be determined based on the type of parameter specified in the Parameter Type field """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ObjectType( object ):
"""The unique designation of an environmental object. Section 6.2.64
"""

    def __init__(self):
    """ Initializer for ObjectType"""
            super(ObjectType, self).__init__()
            self.domain = 0
            """ Domain of entity (air, surface, subsurface, space, etc)"""
            self.objectKind = 0
            """ country to which the design of the entity is attributed"""
            self.category = 0
            """ category of entity"""
            self.subcategory = 0
            """ subcategory of entity"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ActionResponsePdu( SimulationManagementFamilyPdu ):
"""Section 7.5.8. response to an action request PDU. COMPLETE
"""

    def __init__(self):
    """ Initializer for ActionResponsePdu"""
            super(ActionResponsePdu, self).__init__()
            originatingID = EntityID();
            """ Identifier for originating entity(or simulation)"""
            receivingID = EntityID();
            """ Identifier for the receiving entity(or simulation)"""
            self.requestID = 0
            """ Request ID that is unique"""
            self.requestStatus = 0
            """ Status of response"""
            self.numberOfFixedDatumRecords = 0
            """ Number of fixed datum records"""
            self.numberOfVariableDatumRecords = 0
            """ Number of variable datum records"""
            fixedDatums = []
            """ variable length list of fixed datums"""
            variableDatums = []
            """ variable length list of variable length datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Association( object ):
"""An entity's associations with other entities and/or locations. For each association, this record shall specify the type of the association, the associated entity's EntityID and/or the associated location's world coordinates. This record may be used (optionally) in a transfer transaction to send internal state data from the divesting simulation to the acquiring simulation (see 5.9.4). This record may also be used for other purposes. Section 6.2.9
"""

    def __init__(self):
    """ Initializer for Association"""
            super(Association, self).__init__()
            self.associationType = 0
            self.padding4 = 0
            associatedEntityID = EntityID();
            """ identity of associated entity. If none, NO_SPECIFIC_ENTITY"""
            associatedLocation = Vector3Double();
            """ location, in world coordinates"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityDamageStatusPdu( WarfareFamilyPdu ):
"""shall be used to communicate detailed damage information sustained by an entity regardless of the source of the damage Section 7.3.5  COMPLETE
"""

    def __init__(self):
    """ Initializer for EntityDamageStatusPdu"""
            super(EntityDamageStatusPdu, self).__init__()
            damagedEntityID = EntityID();
            """ Field shall identify the damaged entity (see 6.2.28), Section 7.3.4 COMPLETE"""
            self.padding1 = 0
            """ Padding."""
            self.padding2 = 0
            """ Padding."""
            self.numberOfDamageDescription = 0
            """ field shall specify the number of Damage Description records, Section 7.3.5"""
            damageDescriptionRecords = []
            """ Fields shall contain one or more Damage Description records (see 6.2.17) and may contain other Standard Variable records, Section 7.3.5"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SimulationManagementFamilyPdu( Pdu ):
"""Section 7.5 Abstract superclass for PDUs relating to the simulation itself. COMPLETE
"""

    def __init__(self):
    """ Initializer for SimulationManagementFamilyPdu"""
            super(SimulationManagementFamilyPdu, self).__init__()
            originatingEntityID = EntityID();
            """ Entity that is sending message"""
            receivingEntityID = EntityID();
            """ Entity that is intended to receive message"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RecordSpecificationElement( object ):
"""Synthetic record, made up from section 6.2.72. This is used to acheive a repeating variable list element.
"""

    def __init__(self):
    """ Initializer for RecordSpecificationElement"""
            super(RecordSpecificationElement, self).__init__()
            self.recordID = 0
            """ the data structure used to convey the parameter values of the record for each record. 32 bit enumeration."""
            self.recordSetSerialNumber = 0
            """ the serial number of the first record in the block of records"""
            self.recordLength = 0
            """  the length, in bits, of the record. Note, bits, not bytes."""
            self.recordCount = 0
            """  the number of records included in the record set """
            self.recordValues = 0
            """ the concatenated records of the format specified by the Record ID field. The length of this field is the Record Length multiplied by the Record Count, in units of bits. ^^^This is wrong--variable sized data records, bit values. THis MUST be patched after generation."""
            self.pad4 = 0
            """ Padding of 0 to 31 unused bits as required for 32-bit alignment of the Record Set field. ^^^This is wrong--variable sized padding. MUST be patched post-code generation"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EightByteChunk( object ):
"""64 bit piece of data
"""

    def __init__(self):
    """ Initializer for EightByteChunk"""
            super(EightByteChunk, self).__init__()
            otherParameters =  [ 0, 0, 0, 0, 0, 0, 0, 0]
            """ Eight bytes of arbitrary data"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AntennaLocation( object ):
"""Location of the radiating portion of the antenna, specified in world coordinates and entity coordinates. Section 6.2.8
"""

    def __init__(self):
    """ Initializer for AntennaLocation"""
            super(AntennaLocation, self).__init__()
            antennaLocation = Vector3Double();
            """ Location of the radiating portion of the antenna in world    coordinates"""
            relativeAntennaLocation = Vector3Float();
            """ Location of the radiating portion of the antenna     in entity coordinates"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class FirePdu( WarfareFamilyPdu ):
""" The firing of a weapon or expendable shall be communicated by issuing a Fire PDU. Sectioin 7.3.2. COMPLETE
"""

    def __init__(self):
    """ Initializer for FirePdu"""
            super(FirePdu, self).__init__()
            munitionExpendibleID = EntityID();
            """ This field shall specify the entity identification of the fired munition or expendable. This field shall be represented by an Entity Identifier record (see 6.2.28)."""
            eventID = EventIdentifier();
            """ This field shall contain an identification generated by the firing entity to associate related firing and detonation events. This field shall be represented by an Event Identifier record (see 6.2.34)."""
            self.fireMissionIndex = 0
            """ This field shall identify the fire mission (see 5.4.3.3). This field shall be representedby a 32-bit unsigned integer."""
            locationInWorldCoordinates = Vector3Double();
            """ This field shall specify the location, in world coordinates, from which the munition was launched, and shall be represented by a World Coordinates record (see 6.2.97)."""
            descriptor = MunitionDescriptor();
            """ This field shall describe the firing or launch of a munition or expendable represented by one of the following types of Descriptor records: Munition Descriptor (6.2.20.2) or Expendable Descriptor (6.2.20.4)."""
            velocity = Vector3Float();
            """ This field shall specify the velocity of the fired munition at the point when the issuing simulation application intends the externally visible effects of the launch (e.g. exhaust plume or muzzle blast) to first become apparent. The velocity shall be represented in world coordinates. This field shall be represented by a Linear Velocity Vector record [see 6.2.95 item c)]."""
            self.range = 0
            """ This field shall specify the range that an entity’s fire control system has assumed in computing the fire control solution. This field shall be represented by a 32-bit floating point number in meters. For systems where range is unknown or unavailable, this field shall contain a value of zero."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DataQueryPdu( SimulationManagementFamilyPdu ):
"""Section 7.5.9. Request for data from an entity. COMPLETE
"""

    def __init__(self):
    """ Initializer for DataQueryPdu"""
            super(DataQueryPdu, self).__init__()
            self.requestID = 0
            """ ID of request"""
            self.timeInterval = 0
            """ time issues between issues of Data PDUs. Zero means send once only."""
            self.numberOfFixedDatumRecords = 0
            """ Number of fixed datum records"""
            self.numberOfVariableDatumRecords = 0
            """ Number of variable datum records"""
            fixedDatums = []
            """ variable length list of fixed datums"""
            variableDatums = []
            """ variable length list of variable length datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ObjectIdentifier( object ):
"""The unique designation of an environmental object. Section 6.2.63
"""

    def __init__(self):
    """ Initializer for ObjectIdentifier"""
            super(ObjectIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """  Simulation Address"""
            self.objectNumber = 0
            """ object number"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AggregateIdentifier( object ):
"""The unique designation of each aggrgate in an exercise is specified by an aggregate identifier record. The aggregate ID is not an entity and shall not be treated as such. Section 6.2.3.
"""

    def __init__(self):
    """ Initializer for AggregateIdentifier"""
            super(AggregateIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """ Simulation address, ie site and application, the first two fields of the entity ID"""
            self.aggregateID = 0
            """ the aggregate ID"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class FixedDatum( object ):
"""Fixed Datum Record. Section 6.2.38
"""

    def __init__(self):
    """ Initializer for FixedDatum"""
            super(FixedDatum, self).__init__()
            self.fixedDatumID = 0
            """ ID of the fixed datum, an enumeration"""
            self.fixedDatumValue = 0
            """ Value for the fixed datum"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class VariableParameter( object ):
"""specification of additional information associated with an entity or detonation, not otherwise accounted for in a PDU 6.2.94.1
"""

    def __init__(self):
    """ Initializer for VariableParameter"""
            super(VariableParameter, self).__init__()
            self.recordType = 0
            """ the identification of the Variable Parameter record. Enumeration from EBV"""
            self.variableParameterFields1 = 0
            """ Variable parameter data fields. Two doubles minus one byte"""
            self.variableParameterFields2 = 0
            """ Variable parameter data fields. """
            self.variableParameterFields3 = 0
            """ Variable parameter data fields. """
            self.variableParameterFields4 = 0
            """ Variable parameter data fields. """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ChangeOptions( object ):
"""This is wrong and breaks serialization. See section 6.2.13 aka B.2.41
"""

    def __init__(self):
    """ Initializer for ChangeOptions"""
            super(ChangeOptions, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LiveSimulationAddress( object ):
"""A simulation's designation associated with all Live Entity IDs contained in Live Entity PDUs. Section 6.2.55 
"""

    def __init__(self):
    """ Initializer for LiveSimulationAddress"""
            super(LiveSimulationAddress, self).__init__()
            self.liveSiteNumber = 0
            """ facility, installation, organizational unit or geographic location may have multiple sites associated with it. The Site Number is the first component of the Live Simulation Address, which defines a live simulation."""
            self.liveApplicationNumber = 0
            """ An application associated with a live site is termed a live application. Each live application participating in an event """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ReceiverPdu( RadioCommunicationsFamilyPdu ):
""" Communication of a receiver state. Section 7.7.4 COMPLETE
"""

    def __init__(self):
    """ Initializer for ReceiverPdu"""
            super(ReceiverPdu, self).__init__()
            self.receiverState = 0
            """ encoding scheme used, and enumeration"""
            self.padding1 = 0
            """ padding"""
            self.receivedPoser = 0
            """ received power"""
            transmitterEntityId = EntityID();
            """ ID of transmitter"""
            self.transmitterRadioId = 0
            """ ID of transmitting radio"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityMarking( object ):
"""Specifies the character set used inthe first byte, followed by 11 characters of text data. Section 6.29
"""

    def __init__(self):
    """ Initializer for EntityMarking"""
            super(EntityMarking, self).__init__()
            self.characterSet = 0
            """ The character set"""
            characters =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            """ The characters"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LinearObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
""": Information abut the addition or modification of a synthecic enviroment object that      is anchored to the terrain with a single point and has size or orientation. Section 7.10.5 COMPLETE
"""

    def __init__(self):
    """ Initializer for LinearObjectStatePdu"""
            super(LinearObjectStatePdu, self).__init__()
            objectID = EntityID();
            """ Object in synthetic environment"""
            referencedObjectID = EntityID();
            """ Object with which this point object is associated"""
            self.updateNumber = 0
            """ unique update number of each state transition of an object"""
            self.forceID = 0
            """ force ID"""
            self.numberOfSegments = 0
            """ number of linear segment parameters"""
            requesterID = SimulationAddress();
            """ requesterID"""
            receivingID = SimulationAddress();
            """ receiver ID"""
            objectType = ObjectType();
            """ Object type"""
            linearSegmentParameters = []
            """ Linear segment parameters"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class UAFundamentalParameter( object ):
"""Regeneration parameters for active emission systems that are variable throughout a scenario. Section 6.2.91
"""

    def __init__(self):
    """ Initializer for UAFundamentalParameter"""
            super(UAFundamentalParameter, self).__init__()
            self.activeEmissionParameterIndex = 0
            """ Which database record shall be used. An enumeration from EBV document"""
            self.scanPattern = 0
            """ The type of scan pattern, If not used, zero. An enumeration from EBV document"""
            self.beamCenterAzimuthHorizontal = 0
            """ center azimuth bearing of th emain beam. In radians."""
            self.azimuthalBeamwidthHorizontal = 0
            """ Horizontal beamwidth of th emain beam Meastued at the 3dB down point of peak radiated power. In radians."""
            self.beamCenterDepressionElevation = 0
            """ center of the d/e angle of th emain beam relative to the stablised de angle of the target. In radians."""
            self.beamwidthDownElevation = 0
            """ vertical beamwidth of the main beam. Meastured at the 3dB down point of peak radiated power. In radians."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class TwoByteChunk( object ):
"""16 bit piece of data
"""

    def __init__(self):
    """ Initializer for TwoByteChunk"""
            super(TwoByteChunk, self).__init__()
            otherParameters =  [ 0, 0]
            """ two bytes of arbitrary data"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DirectedEnergyDamage( object ):
"""Damage sustained by an entity due to directed energy. Location of the damage based on a relative x,y,z location from the center of the entity. Section 6.2.15.2
"""

    def __init__(self):
    """ Initializer for DirectedEnergyDamage"""
            super(DirectedEnergyDamage, self).__init__()
            self.recordType = 4500
            """ DE Record Type."""
            self.recordLength = 40
            """ DE Record Length (bytes)."""
            self.padding = 0
            """ padding."""
            damageLocation = Vector3Float();
            """ location of damage, relative to center of entity"""
            self.damageDiameter = 0
            """ Size of damaged area, in meters."""
            self.temperature = -273.15
            """ average temp of the damaged area, in degrees celsius. If firing entitty does not model this, use a value of -273.15"""
            self.componentIdentification = 0
            """ enumeration"""
            self.componentDamageStatus = 0
            """ enumeration"""
            self.componentVisualDamageStatus = 0
            """ enumeration"""
            self.componentVisualSmokeColor = 0
            """ enumeration"""
            fireEventID = EventIdentifier();
            """ For any component damage resulting this field shall be set to the fire event ID from that PDU."""
            self.padding2 = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ExplosionDescriptor( object ):
"""Explosion of a non-munition. Section 6.2.19.3
"""

    def __init__(self):
    """ Initializer for ExplosionDescriptor"""
            super(ExplosionDescriptor, self).__init__()
            explodingObject = EntityType();
            """ Type of the object that exploded. See 6.2.30"""
            self.explosiveMaterial = 0
            """ Material that exploded. Can be grain dust, tnt, gasoline, etc. Enumeration"""
            self.padding = 0
            """ padding"""
            self.explosiveForce = 0
            """ Force of explosion, in equivalent KG of TNT"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ClockTime( object ):
"""Time measurements that exceed one hour are represented by this record. The first field is the hours since the unix epoch (Jan 1 1970, used by most Unix systems and java) and the second field the timestamp units since the top of the hour. Section 6.2.14
"""

    def __init__(self):
    """ Initializer for ClockTime"""
            super(ClockTime, self).__init__()
            self.hour = 0
            """ Hours in UTC"""
            self.timePastHour = 0
            """ Time past the hour"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SecondaryOperationalData( object ):
"""Additional operational data for an IFF emitting system and the number of IFF Fundamental Parameter Data records Section 6.2.76.
"""

    def __init__(self):
    """ Initializer for SecondaryOperationalData"""
            super(SecondaryOperationalData, self).__init__()
            self.operationalData1 = 0
            """ additional operational characteristics of the IFF emitting system. Each 8-bit field will vary depending on the system type."""
            self.operationalData2 = 0
            """ additional operational characteristics of the IFF emitting system. Each 8-bit field will vary depending on the system type."""
            self.numberOfIFFFundamentalParameterRecords = 0
            """ the number of IFF Fundamental Parameter Data records that follow"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class UaPdu( DistributedEmissionsFamilyPdu ):
""" Information about underwater acoustic emmissions. This requires manual cleanup.  The beam data records should ALL be a the finish, rather than attached to each emitter system. Section 7.6.4. UNFINISHED
"""

    def __init__(self):
    """ Initializer for UaPdu"""
            super(UaPdu, self).__init__()
            emittingEntityID = EntityID();
            """ ID of the entity that is the source of the emission"""
            eventID = EventIdentifier();
            """ ID of event"""
            self.stateChangeIndicator = 0
            """ This field shall be used to indicate whether the data in the UA PDU represent a state update or data that have changed since issuance of the last UA PDU"""
            self.pad = 0
            """ padding"""
            self.passiveParameterIndex = 0
            """ This field indicates which database record (or file) shall be used in the definition of passive signature (unintentional) emissions of the entity. The indicated database record (or  file) shall define all noise generated as a function of propulsion plant configurations and associated  auxiliaries."""
            self.propulsionPlantConfiguration = 0
            """ This field shall specify the entity propulsion plant configuration. This field is used to determine the passive signature characteristics of an entity."""
            self.numberOfShafts = 0
            """  This field shall represent the number of shafts on a platform"""
            self.numberOfAPAs = 0
            """ This field shall indicate the number of APAs described in the current UA PDU"""
            self.numberOfUAEmitterSystems = 0
            """ This field shall specify the number of UA emitter systems being described in the current UA PDU"""
            shaftRPMs = []
            """ shaft RPM values. THIS IS WRONG. It has the wrong class in the list."""
            apaData = []
            """ apaData. THIS IS WRONG. It has the worng class in the list."""
            emitterSystems = []
            """ THIS IS WRONG. It has the wrong class in the list."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IntercomControlPdu( RadioCommunicationsFamilyPdu ):
""" Detailed inofrmation about the state of an intercom device and the actions it is requestion         of another intercom device, or the response to a requested action. Required manual intervention to fix the intercom parameters,        which can be of varialbe length. Section 7.7.5 UNFINSISHED
"""

    def __init__(self):
    """ Initializer for IntercomControlPdu"""
            super(IntercomControlPdu, self).__init__()
            self.controlType = 0
            """ control type"""
            self.communicationsChannelType = 0
            """ control type"""
            sourceEntityID = EntityID();
            """ Source entity ID"""
            self.sourceCommunicationsDeviceID = 0
            """ The specific intercom device being simulated within an entity."""
            self.sourceLineID = 0
            """ Line number to which the intercom control refers"""
            self.transmitPriority = 0
            """ priority of this message relative to transmissons from other intercom devices"""
            self.transmitLineState = 0
            """ current transmit state of the line"""
            self.command = 0
            """ detailed type requested."""
            masterEntityID = EntityID();
            """ eid of the entity that has created this intercom channel."""
            self.masterCommunicationsDeviceID = 0
            """ specific intercom device that has created this intercom channel"""
            self.intercomParametersLength = 0
            """ number of intercom parameters"""
            intercomParameters = []
            """ ^^^This is wrong the length of the data field is variable. Using a long for now."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SignalPdu( RadioCommunicationsFamilyPdu ):
""" Detailed information about a radio transmitter. This PDU requires manually written code to complete. The encodingScheme field can be used in multiple        ways, which requires hand-written code to finish. Section 7.7.3. UNFINISHED
"""

    def __init__(self):
    """ Initializer for SignalPdu"""
            super(SignalPdu, self).__init__()
            self.encodingScheme = 0
            """ encoding scheme used, and enumeration"""
            self.tdlType = 0
            """ tdl type"""
            self.sampleRate = 0
            """ sample rate"""
            self.dataLength = 0
            """ length od data"""
            self.samples = 0
            """ number of samples"""
            data = []
            """ list of eight bit values"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EnvironmentType( object ):
"""Description of environmental data in environmental process and gridded data PDUs. Section 6.2.32
"""

    def __init__(self):
    """ Initializer for EnvironmentType"""
            super(EnvironmentType, self).__init__()
            self.entityKind = 0
            """ Kind of entity"""
            self.domain = 0
            """ Domain of entity (air, surface, subsurface, space, etc)"""
            self.entityClass = 0
            """ class of environmental entity"""
            self.category = 0
            """ category of entity"""
            self.subcategory = 0
            """ subcategory of entity"""
            self.specific = 0
            """ specific info based on subcategory field"""
            self.extra = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class TotalRecordSets( object ):
"""Total number of record sets contained in a logical set of one or more PDUs. Used to transfer ownership, etc Section 6.2.88
"""

    def __init__(self):
    """ Initializer for TotalRecordSets"""
            super(TotalRecordSets, self).__init__()
            self.totalRecordSets = 0
            """ Total number of record sets"""
            self.padding = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MineEntityIdentifier( object ):
"""The unique designation of a mine contained in the Minefield Data PDU. No espdus are issued for mine entities.  Section 6.2.55 
"""

    def __init__(self):
    """ Initializer for MineEntityIdentifier"""
            super(MineEntityIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """ """
            self.mineEntityNumber = 0
            """ """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Relationship( object ):
"""The relationship of the part entity to its host entity. Section 6.2.74.
"""

    def __init__(self):
    """ Initializer for Relationship"""
            super(Relationship, self).__init__()
            self.nature = 0
            """ the nature or purpose for joining of the part entity to the host entity and shall be represented by a 16-bit enumeration"""
            self.position = 0
            """ the position of the part entity with respect to the host entity and shall be represented by a 16-bit enumeration"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RemoveEntityReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.2: Removal of an entity , reliable. COMPLETE
"""

    def __init__(self):
    """ Initializer for RemoveEntityReliablePdu"""
            super(RemoveEntityReliablePdu, self).__init__()
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding"""
            self.pad2 = 0
            """ padding"""
            self.requestID = 0
            """ Request ID"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EEFundamentalParameterData( object ):
"""Contains electromagnetic emmission regeneration parameters that are variable throught a scenario. Section 6.2.22.
"""

    def __init__(self):
    """ Initializer for EEFundamentalParameterData"""
            super(EEFundamentalParameterData, self).__init__()
            self.frequency = 0
            """ center frequency of the emission in hertz."""
            self.frequencyRange = 0
            """ Bandwidth of the frequencies corresponding to the fequency field."""
            self.effectiveRadiatedPower = 0
            """ Effective radiated power for the emission in DdBm. For a radar noise jammer, indicates the peak of the transmitted power."""
            self.pulseRepetitionFrequency = 0
            """ Average repetition frequency of the emission in hertz."""
            self.pulseWidth = 0
            """ Average pulse width  of the emission in microseconds."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class CreateEntityPdu( SimulationManagementFamilyPdu ):
"""Section 7.5.2. Create a new entity. COMPLETE
"""

    def __init__(self):
    """ Initializer for CreateEntityPdu"""
            super(CreateEntityPdu, self).__init__()
            originatingID = EntityID();
            """ Identifier for the request"""
            receivingID = EntityID();
            """ Identifier for the request"""
            self.requestID = 0
            """ Identifier for the request.  See 6.2.75"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class JammingTechnique( object ):
"""Jamming technique. Section 6.2.49
"""

    def __init__(self):
    """ Initializer for JammingTechnique"""
            super(JammingTechnique, self).__init__()
            self.kind = 0
            self.category = 0
            self.subcategory = 0
            self.specific = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RadioCommunicationsFamilyPdu( Pdu ):
""" Abstract superclass for radio communications PDUs. Section 7.7
"""

    def __init__(self):
    """ Initializer for RadioCommunicationsFamilyPdu"""
            super(RadioCommunicationsFamilyPdu, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DatumSpecification( object ):
"""List of fixed and variable datum records. Section 6.2.18 
"""

    def __init__(self):
    """ Initializer for DatumSpecification"""
            super(DatumSpecification, self).__init__()
            self.numberOfFixedDatums = 0
            """ Number of fixed datums"""
            self.numberOfVariableDatums = 0
            """ Number of variable datums"""
            fixedDatumIDList = []
            """ variable length list fixed datums"""
            variableDatumIDList = []
            """ variable length list variable datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DirectedEnergyAreaAimpoint( object ):
"""DE Precision Aimpoint Record. NOT COMPLETE. Section 6.2.20.2
"""

    def __init__(self):
    """ Initializer for DirectedEnergyAreaAimpoint"""
            super(DirectedEnergyAreaAimpoint, self).__init__()
            self.recordType = 4001
            """ Type of Record enumeration"""
            self.recordLength = 0
            """ Length of Record"""
            self.padding = 0
            """ Padding"""
            self.beamAntennaPatternRecordCount = 0
            """ Number of beam antenna pattern records"""
            self.directedEnergyTargetEnergyDepositionRecordCount = 0
            """ Number of DE target energy depositon records"""
            beamAntennaParameterList = []
            """ list of beam antenna records. See 6.2.9.2"""
            directedEnergyTargetEnergyDepositionRecordList = []
            """ list of DE target deposition records. See 6.2.21.4"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Vector3Float( object ):
"""Three floating point values, x, y, and z. Section 6.2.95
"""

    def __init__(self):
    """ Initializer for Vector3Float"""
            super(Vector3Float, self).__init__()
            self.x = 0
            """ X value"""
            self.y = 0
            """ y Value"""
            self.z = 0
            """ Z value"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SeesPdu( DistributedEmissionsFamilyPdu ):
""" SEES PDU, supplemental emissions entity state information. Section 7.6.6 COMPLETE
"""

    def __init__(self):
    """ Initializer for SeesPdu"""
            super(SeesPdu, self).__init__()
            orginatingEntityID = EntityID();
            """ Originating entity ID"""
            self.infraredSignatureRepresentationIndex = 0
            """ IR Signature representation index"""
            self.acousticSignatureRepresentationIndex = 0
            """ acoustic Signature representation index"""
            self.radarCrossSectionSignatureRepresentationIndex = 0
            """ radar cross section representation index"""
            self.numberOfPropulsionSystems = 0
            """ how many propulsion systems"""
            self.numberOfVectoringNozzleSystems = 0
            """ how many vectoring nozzle systems"""
            propulsionSystemData = []
            """ variable length list of propulsion system data"""
            vectoringSystemData = []
            """ variable length list of vectoring system data"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Expendable( object ):
"""An entity's expendable (chaff, flares, etc) information. Section 6.2.36
"""

    def __init__(self):
    """ Initializer for Expendable"""
            super(Expendable, self).__init__()
            expendable = EntityType();
            """ Type of expendable"""
            self.station = 0
            self.quantity = 0
            self.expendableStatus = 0
            self.padding = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IntercomSignalPdu( RadioCommunicationsFamilyPdu ):
""" Actual transmission of intercome voice data. Section 7.7.5. COMPLETE
"""

    def __init__(self):
    """ Initializer for IntercomSignalPdu"""
            super(IntercomSignalPdu, self).__init__()
            entityID = EntityID();
            """ entity ID"""
            self.communicationsDeviceID = 0
            """ ID of communications device"""
            self.encodingScheme = 0
            """ encoding scheme"""
            self.tdlType = 0
            """ tactical data link type"""
            self.sampleRate = 0
            """ sample rate"""
            self.dataLength = 0
            """ data length"""
            self.samples = 0
            """ samples"""
            data = []
            """ data bytes"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IOCommunicationsNode( object ):
"""A communications node that is part of a simulted communcations network. Section 6.2.49.2
"""

    def __init__(self):
    """ Initializer for IOCommunicationsNode"""
            super(IOCommunicationsNode, self).__init__()
            self.recordType = 5501
            self.recordLength = 16
            self.communcationsNodeType = 0
            self.padding = 0
            communicationsNodeID = CommunicationsNodeID();

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ModulationType( object ):
"""Information about the type of modulation used for radio transmission. 6.2.59 
"""

    def __init__(self):
    """ Initializer for ModulationType"""
            super(ModulationType, self).__init__()
            self.spreadSpectrum = 0
            """ This field shall indicate the spread spectrum technique or combination of spread spectrum techniques in use. Bit field. 0=freq hopping, 1=psuedo noise, time hopping=2, reamining bits unused"""
            self.majorModulation = 0
            """ the major classification of the modulation type. """
            self.detail = 0
            """ provide certain detailed information depending upon the major modulation type"""
            self.radioSystem = 0
            """ the radio system associated with this Transmitter PDU and shall be used as the basis to interpret other fields whose values depend on a specific radio system."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LinearSegmentParameter( object ):
"""The specification of an individual segment of a linear segment synthetic environment object in a Linear Object State PDU Section 6.2.52
"""

    def __init__(self):
    """ Initializer for LinearSegmentParameter"""
            super(LinearSegmentParameter, self).__init__()
            self.segmentNumber = 0
            """ the individual segment of the linear segment """
            self.segmentModification = 0
            """  whether a modification has been made to the point object’s location or orientation"""
            self.generalSegmentAppearance = 0
            """ general dynamic appearance attributes of the segment. This record shall be defined as a 16-bit record of enumerations. The values defined for this record are included in Section 12 of SISO-REF-010."""
            self.specificSegmentAppearance = 0
            """ This field shall specify specific dynamic appearance attributes of the segment. This record shall be defined as a 32-bit record of enumerations."""
            segmentLocation = Vector3Double();
            """ This field shall specify the location of the linear segment in the simulated world and shall be represented by a World Coordinates record """
            segmentOrientation = EulerAngles();
            """ orientation of the linear segment about the segment location and shall be represented by a Euler Angles record """
            self.segmentLength = 0
            """ length of the linear segment, in meters, extending in the positive X direction"""
            self.segmentWidth = 0
            """ The total width of the linear segment, in meters, shall be specified by a 16-bit unsigned integer. One-half of the width shall extend in the positive Y direction, and one-half of the width shall extend in the negative Y direction."""
            self.segmentHeight = 0
            """ The height of the linear segment, in meters, above ground shall be specified by a 16-bit unsigned integer."""
            self.segmentDepth = 0
            """ The depth of the linear segment, in meters, below ground level """
            self.padding = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SimulationAddress( object ):
"""A Simulation Address record shall consist of the Site Identification number and the Application Identification number. Section 6.2.79 
"""

    def __init__(self):
    """ Initializer for SimulationAddress"""
            super(SimulationAddress, self).__init__()
            self.site = 0
            """ A site is defined as a facility, installation, organizational unit or a geographic location that has one or more simulation applications capable of participating in a distributed event. """
            self.application = 0
            """ An application is defined as a software program that is used to generate and process distributed simulation data including live, virtual and constructive data."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SystemIdentifier( object ):
"""The ID of the IFF emitting system. NOT COMPLETE. Section 6.2.87
"""

    def __init__(self):
    """ Initializer for SystemIdentifier"""
            super(SystemIdentifier, self).__init__()
            self.systemType = 0
            """ general type of emitting system, an enumeration"""
            self.systemName = 0
            """ named type of system, an enumeration"""
            self.systemMode = 0
            """ mode of operation for the system, an enumeration"""
            changeOptions = ChangeOptions();
            """ status of this PDU, see section 6.2.15"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class TrackJamData( object ):
""" Track-Jam data Section 6.2.89
"""

    def __init__(self):
    """ Initializer for TrackJamData"""
            super(TrackJamData, self).__init__()
            entityID = EntityID();
            """ the entity tracked or illumated, or an emitter beam targeted with jamming"""
            self.emitterNumber = 0
            """ Emitter system associated with the entity"""
            self.beamNumber = 0
            """ Beam associated with the entity"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class CreateEntityReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.1: creation of an entity , reliable. COMPLETE
"""

    def __init__(self):
    """ Initializer for CreateEntityReliablePdu"""
            super(CreateEntityReliablePdu, self).__init__()
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding"""
            self.pad2 = 0
            """ padding"""
            self.requestID = 0
            """ Request ID"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AggregateType( object ):
"""Identifies the type and organization of an aggregate. Section 6.2.5
"""

    def __init__(self):
    """ Initializer for AggregateType"""
            super(AggregateType, self).__init__()
            self.aggregateKind = 0
            """ Grouping criterion used to group the aggregate. Enumeration from EBV document"""
            self.domain = 0
            """ Domain of entity (air, surface, subsurface, space, etc) Zero means domain does not apply."""
            self.country = 0
            """ country to which the design of the entity is attributed"""
            self.category = 0
            """ category of entity"""
            self.subcategory = 0
            """ subcategory of entity"""
            self.specificInfo = 0
            """ specific info based on subcategory field. specific is a reserved word in sql."""
            self.extra = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SimulationManagementPduHeader( object ):
"""First part of a simulation management (SIMAN) PDU and SIMAN-Reliability (SIMAN-R) PDU. Sectionn 6.2.81
"""

    def __init__(self):
    """ Initializer for SimulationManagementPduHeader"""
            super(SimulationManagementPduHeader, self).__init__()
            pduHeader = PduHeader();
            """ Conventional PDU header"""
            originatingID = SimulationIdentifier();
            """ IDs the simulation or entity, etiehr a simulation or an entity. Either 6.2.80 or 6.2.28"""
            receivingID = SimulationIdentifier();
            """ simulation, all simulations, a special ID, or an entity. See 5.6.5 and 5.12.4"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class BeamData( object ):
"""Describes the scan volue of an emitter beam. Section 6.2.11.
"""

    def __init__(self):
    """ Initializer for BeamData"""
            super(BeamData, self).__init__()
            self.beamAzimuthCenter = 0
            """ Specifies the beam azimuth an elevation centers and corresponding half-angles to describe the scan volume"""
            self.beamAzimuthSweep = 0
            """ Specifies the beam azimuth sweep to determine scan volume"""
            self.beamElevationCenter = 0
            """ Specifies the beam elevation center to determine scan volume"""
            self.beamElevationSweep = 0
            """ Specifies the beam elevation sweep to determine scan volume"""
            self.beamSweepSync = 0
            """ allows receiver to synchronize its regenerated scan pattern to that of the emmitter. Specifies the percentage of time a scan is through its pattern from its origion."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RemoveEntityPdu( SimulationManagementFamilyPdu ):
"""Section 7.5.3 The removal of an entity from an exercise shall be communicated with a Remove Entity PDU. COMPLETE
"""

    def __init__(self):
    """ Initializer for RemoveEntityPdu"""
            super(RemoveEntityPdu, self).__init__()
            originatingID = EntityID();
            """ Identifier for originating entity(or simulation)"""
            receivingID = EntityID();
            """ Identifier for the receiving entity(or simulation)"""
            self.requestID = 0
            """ This field shall identify the specific and unique start/resume request being made by the SM"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ResupplyReceivedPdu( LogisticsFamilyPdu ):
"""Section 7.4.4. Receipt of supplies is communicated by issuing Resupply Received PDU. COMPLETE
"""

    def __init__(self):
    """ Initializer for ResupplyReceivedPdu"""
            super(ResupplyReceivedPdu, self).__init__()
            receivingEntityID = EntityID();
            """ Entity that is receiving service.  Shall be represented by Entity Identifier record (see 6.2.28)"""
            supplyingEntityID = EntityID();
            """ Entity that is supplying.  Shall be represented by Entity Identifier record (see 6.2.28)"""
            self.numberOfSupplyTypes = 0
            """ How many supplies are taken by receiving entity"""
            self.padding1 = 0
            """ padding"""
            self.padding2 = 0
            """ padding"""
            supplies = []
            """ Type and amount of supplies for each specified supply type.  See 6.2.85 for supply quantity record."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class WarfareFamilyPdu( Pdu ):
"""abstract superclass for fire and detonation pdus that have shared information. Section 7.3 COMPLETE
"""

    def __init__(self):
    """ Initializer for WarfareFamilyPdu"""
            super(WarfareFamilyPdu, self).__init__()
            firingEntityID = EntityID();
            """ ID of the entity that shot"""
            targetEntityID = EntityID();
            """ ID of the entity that is being shot at"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class StopFreezeReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.4: Stop freeze simulation, relaible. COMPLETE
"""

    def __init__(self):
    """ Initializer for StopFreezeReliablePdu"""
            super(StopFreezeReliablePdu, self).__init__()
            realWorldTime = ClockTime();
            """ time in real world for this operation to happen"""
            self.reason = 0
            """ Reason for stopping/freezing simulation"""
            self.frozenBehavior = 0
            """ internal behvior of the simulation while frozen"""
            self.requiredReliablityService = 0
            """ reliablity level"""
            self.pad1 = 0
            """ padding"""
            self.requestID = 0
            """ Request ID"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EventReportReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.11: reports the occurance of a significatnt event to the simulation manager. Needs manual     intervention to fix padding in variable datums. UNFINISHED.
"""

    def __init__(self):
    """ Initializer for EventReportReliablePdu"""
            super(EventReportReliablePdu, self).__init__()
            self.eventType = 0
            """ Event type"""
            self.pad1 = 0
            """ padding"""
            self.numberOfFixedDatumRecords = 0
            """ Fixed datum record count"""
            self.numberOfVariableDatumRecords = 0
            """ variable datum record count"""
            fixedDatumRecords = []
            """ Fixed datum records"""
            variableDatumRecords = []
            """ Variable datum records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MinefieldResponseNackPdu( MinefieldFamilyPdu ):
"""proivde the means to request a retransmit of a minefield data pdu. Section 7.9.5 COMPLETE
"""

    def __init__(self):
    """ Initializer for MinefieldResponseNackPdu"""
            super(MinefieldResponseNackPdu, self).__init__()
            minefieldID = EntityID();
            """ Minefield ID"""
            requestingEntityID = EntityID();
            """ entity ID making the request"""
            self.requestID = 0
            """ request ID"""
            self.numberOfMissingPdus = 0
            """ how many pdus were missing"""
            missingPduSequenceNumbers = []
            """ PDU sequence numbers that were missing"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EngineFuel( object ):
"""Information about an entity's engine fuel. Section 6.2.24.
"""

    def __init__(self):
    """ Initializer for EngineFuel"""
            super(EngineFuel, self).__init__()
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

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class CollisionElasticPdu( EntityInformationFamilyPdu ):
"""Information about elastic collisions in a DIS exercise shall be communicated using a Collision-Elastic PDU. Section 7.2.4. COMPLETE
"""

    def __init__(self):
    """ Initializer for CollisionElasticPdu"""
            super(CollisionElasticPdu, self).__init__()
            issuingEntityID = EntityID();
            """ This field shall identify the entity that is issuing the PDU and shall be represented by an Entity Identifier record (see 6.2.28)"""
            collidingEntityID = EntityID();
            """ This field shall identify the entity that has collided with the issuing entity. This field shall be a valid identifier of an entity or server capable of responding to the receipt of this Collision-Elastic PDU. This field shall be represented by an Entity Identifier record (see 6.2.28)."""
            collisionEventID = EventIdentifier();
            """ This field shall contain an identification generated by the issuing simulation application to associate related collision events. This field shall be represented by an Event Identifier record (see 6.2.34)."""
            self.pad = 0
            """ some padding"""
            contactVelocity = Vector3Float();
            """ This field shall contain the velocity at the time the collision is detected at the point the collision is detected. The velocity shall be represented in world coordinates. This field shall be represented by the Linear Velocity Vector record [see 6.2.95 item c)]"""
            self.mass = 0
            """ This field shall contain the mass of the issuing entity and shall be represented by a 32-bit floating point number representing kilograms"""
            locationOfImpact = Vector3Float();
            """ This field shall specify the location of the collision with respect to the entity with which the issuing entity collided. This field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""
            self.collisionIntermediateResultXX = 0
            """ These six records represent the six independent components of a positive semi-definite matrix formed by pre-multiplying and post-multiplying the tensor of inertia, by the anti-symmetric matrix generated by the moment arm, and shall be represented by 32-bit floating point numbers (see 5.3.4.4)"""
            self.collisionIntermediateResultXY = 0
            """ tensor values"""
            self.collisionIntermediateResultXZ = 0
            """ tensor values"""
            self.collisionIntermediateResultYY = 0
            """ tensor values"""
            self.collisionIntermediateResultYZ = 0
            """ tensor values"""
            self.collisionIntermediateResultZZ = 0
            """ tensor values"""
            unitSurfaceNormal = Vector3Float();
            """ This record shall represent the normal vector to the surface at the point of collision detection. The surface normal shall be represented in world coordinates. This field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""
            self.coefficientOfRestitution = 0
            """ This field shall represent the degree to which energy is conserved in a collision and shall be represented by a 32-bit floating point number. In addition, it represents a free parameter by which simulation application developers may “tune” their collision interactions."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IOEffect( object ):
"""Effect of IO on an entity. Section 6.2.49.3
"""

    def __init__(self):
    """ Initializer for IOEffect"""
            super(IOEffect, self).__init__()
            self.recordType = 5500
            self.recordLength = 16
            self.ioStatus = 0
            self.ioLinkType = 0
            ioEffect = EntityID();
            self.ioEffectDutyCycle = 0
            self.ioEffectDuration = 0
            self.ioProcess = 0
            self.padding = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SimulationIdentifier( object ):
"""The unique designation of a simulation when using the 48-bit identifier format shall be specified by the Sim- ulation Identifier record. The reason that the 48-bit format is required in addition to the 32-bit simulation address format that actually identifies a specific simulation is because some 48-bit identifier fields in PDUs may contain either an Object Identifier, such as an Entity ID, or a Simulation Identifier. Section 6.2.80
"""

    def __init__(self):
    """ Initializer for SimulationIdentifier"""
            super(SimulationIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """ Simulation address """
            self.referenceNumber = 0
            """ This field shall be set to zero as there is no reference number associated with a Simulation Identifier."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ActionRequestPdu( SimulationManagementFamilyPdu ):
"""Section 7.5.7. Request from simulation manager to a managed entity to perform a specified action. COMPLETE
"""

    def __init__(self):
    """ Initializer for ActionRequestPdu"""
            super(ActionRequestPdu, self).__init__()
            originatingID = EntityID();
            """ Identifier for originating entity(or simulation)"""
            receivingID = EntityID();
            """ Identifier for the receiving entity(or simulation)"""
            self.requestID = 0
            """ identifies the request being made by the simulaton manager"""
            self.actionID = 0
            """ identifies the particular action being requested(see Section 7 of SISO-REF-010)."""
            self.numberOfFixedDatumRecords = 0
            """ Number of fixed datum records"""
            self.numberOfVariableDatumRecords = 0
            """ Number of variable datum records"""
            fixedDatums = []
            """ variable length list of fixed datums"""
            variableDatums = []
            """ variable length list of variable length datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class GridAxisDescriptorVariable( object ):
"""Grid axis descriptor fo variable spacing axis data. NOT COMPLETE. Need padding to 64 bit boundary.
"""

    def __init__(self):
    """ Initializer for GridAxisDescriptorVariable"""
            super(GridAxisDescriptorVariable, self).__init__()
            self.domainInitialXi = 0
            """ coordinate of the grid origin or initial value"""
            self.domainFinalXi = 0
            """ coordinate of the endpoint or final value"""
            self.domainPointsXi = 0
            """ The number of grid points along the Xi domain axis for the enviornmental state data"""
            self.interleafFactor = 0
            """ interleaf factor along the domain axis."""
            self.axisType = 0
            """ type of grid axis"""
            self.numberOfPointsOnXiAxis = 0
            """ Number of grid locations along Xi axis"""
            self.initialIndex = 0
            """ initial grid point for the current pdu"""
            self.coordinateScaleXi = 0
            """ value that linearly scales the coordinates of the grid locations for the xi axis"""
            self.coordinateOffsetXi = 0.0
            """ The constant offset value that shall be applied to the grid locations for the xi axis"""
            xiValues = []
            """ list of coordinates"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SupplyQuantity( object ):
""" A supply, and the amount of that supply. Section 6.2.86
"""

    def __init__(self):
    """ Initializer for SupplyQuantity"""
            super(SupplyQuantity, self).__init__()
            supplyType = EntityType();
            """ Type of supply"""
            self.quantity = 0
            """ the number of units of a supply type. """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SilentEntitySystem( object ):
"""information abou an enitity not producing espdus. Section 6.2.79
"""

    def __init__(self):
    """ Initializer for SilentEntitySystem"""
            super(SilentEntitySystem, self).__init__()
            self.numberOfEntities = 0
            """ number of the type specified by the entity type field"""
            self.numberOfAppearanceRecords = 0
            """ number of entity appearance records that follow"""
            entityType = EntityType();
            """ Entity type"""
            appearanceRecordList = []
            """ Variable length list of appearance records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AcknowledgePdu( SimulationManagementFamilyPdu ):
"""Section 7.5.6. Acknowledge the receipt of a start/resume, stop/freeze, or RemoveEntityPDU. COMPLETE
"""

    def __init__(self):
    """ Initializer for AcknowledgePdu"""
            super(AcknowledgePdu, self).__init__()
            originatingID = EntityID();
            """ Identifier for originating entity(or simulation)"""
            receivingID = EntityID();
            """ Identifier for the receiving entity(or simulation)"""
            self.acknowledgeFlag = 0
            """ type of message being acknowledged"""
            self.responseFlag = 0
            """ Whether or not the receiving entity was able to comply with the request"""
            self.requestID = 0
            """ Request ID that is unique"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DistributedEmissionsFamilyPdu( Pdu ):
"""Section 5.3.7. Electronic Emissions. Abstract superclass for distirubted emissions PDU
"""

    def __init__(self):
    """ Initializer for DistributedEmissionsFamilyPdu"""
            super(DistributedEmissionsFamilyPdu, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ActionResponseReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.7: Response from an entity to an action request PDU. COMPLETE
"""

    def __init__(self):
    """ Initializer for ActionResponseReliablePdu"""
            super(ActionResponseReliablePdu, self).__init__()
            self.requestID = 0
            """ request ID"""
            self.responseStatus = 0
            """ status of response"""
            self.numberOfFixedDatumRecords = 0
            """ Fixed datum record count"""
            self.numberOfVariableDatumRecords = 0
            """ variable datum record count"""
            fixedDatumRecords = []
            """ Fixed datum records"""
            variableDatumRecords = []
            """ Variable datum records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SimulationManagementWithReliabilityFamilyPdu( Pdu ):
"""Section 5.3.12: Abstract superclass for reliable simulation management PDUs
"""

    def __init__(self):
    """ Initializer for SimulationManagementWithReliabilityFamilyPdu"""
            super(SimulationManagementWithReliabilityFamilyPdu, self).__init__()
            originatingEntityID = EntityID();
            """ Object originatig the request"""
            receivingEntityID = EntityID();
            """ Object with which this point object is associated"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EventIdentifier( object ):
"""Identifies an event in the world. Use this format for every PDU EXCEPT the LiveEntityPdu. Section 6.2.34.
"""

    def __init__(self):
    """ Initializer for EventIdentifier"""
            super(EventIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """ Site and application IDs"""
            self.eventNumber = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ActionRequestReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.6: request from a simulation manager to a managed entity to perform a specified action. COMPLETE
"""

    def __init__(self):
    """ Initializer for ActionRequestReliablePdu"""
            super(ActionRequestReliablePdu, self).__init__()
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding"""
            self.pad2 = 0
            """ padding"""
            self.requestID = 0
            """ request ID"""
            self.actionID = 0
            """ request ID"""
            self.numberOfFixedDatumRecords = 0
            """ Fixed datum record count"""
            self.numberOfVariableDatumRecords = 0
            """ variable datum record count"""
            fixedDatumRecords = []
            """ Fixed datum records"""
            variableDatumRecords = []
            """ Variable datum records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class BlankingSector( object ):
"""The Blanking Sector attribute record may be used to convey persistent areas within a scan volume where emitter power for a specific active emitter beam is reduced to an insignificant value. Section 6.2.21.2
"""

    def __init__(self):
    """ Initializer for BlankingSector"""
            super(BlankingSector, self).__init__()
            self.recordType = 3500
            self.recordLength = 40
            self.padding = 0
            self.emitterNumber = 0
            self.beamNumber = 0
            self.stateIndicator = 0
            self.padding2 = 0
            self.leftAzimuth = 0
            self.rightAzimuth = 0
            self.lowerElevation = 0
            self.upperElevation = 0
            self.residualPower = 0
            self.padding3 = 0
            self.padding4 = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DesignatorPdu( DistributedEmissionsFamilyPdu ):
"""Section 5.3.7.2. Handles designating operations. COMPLETE
"""

    def __init__(self):
    """ Initializer for DesignatorPdu"""
            super(DesignatorPdu, self).__init__()
            designatingEntityID = EntityID();
            """ ID of the entity designating"""
            self.codeName = 0
            """ This field shall specify a unique emitter database number assigned to  differentiate between otherwise similar or identical emitter beams within an emitter system."""
            designatedEntityID = EntityID();
            """ ID of the entity being designated"""
            self.designatorCode = 0
            """ This field shall identify the designator code being used by the designating entity """
            self.designatorPower = 0
            """ This field shall identify the designator output power in watts"""
            self.designatorWavelength = 0
            """ This field shall identify the designator wavelength in units of microns"""
            designatorSpotWrtDesignated = Vector3Float();
            """ designtor spot wrt the designated entity"""
            designatorSpotLocation = Vector3Double();
            """ designtor spot wrt the designated entity"""
            self.deadReckoningAlgorithm = 0
            """ Dead reckoning algorithm"""
            self.padding1 = 0
            """ padding"""
            self.padding2 = 0
            """ padding"""
            entityLinearAcceleration = Vector3Float();
            """ linear accelleration of entity"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IsPartOfPdu( EntityManagementFamilyPdu ):
""" The joining of two or more simulation entities is communicated by this PDU. Section 7.8.5 COMPLETE
"""

    def __init__(self):
    """ Initializer for IsPartOfPdu"""
            super(IsPartOfPdu, self).__init__()
            orginatingEntityID = EntityID();
            """ ID of entity originating PDU"""
            receivingEntityID = EntityID();
            """ ID of entity receiving PDU"""
            relationship = Relationship();
            """ relationship of joined parts"""
            partLocation = Vector3Float();
            """ location of part; centroid of part in host's coordinate system. x=range, y=bearing, z=0"""
            namedLocationID = NamedLocationIdentification();
            """ named location"""
            partEntityType = EntityType();
            """ entity type"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LaunchedMunitionRecord( object ):
"""Identity of a communications node. Section 6.2.50
"""

    def __init__(self):
    """ Initializer for LaunchedMunitionRecord"""
            super(LaunchedMunitionRecord, self).__init__()
            fireEventID = EventIdentifier();
            self.padding = 0
            firingEntityID = EventIdentifier();
            self.padding2 = 0
            targetEntityID = EventIdentifier();
            self.padding3 = 0
            targetLocation = Vector3Double();

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IFFFundamentalParameterData( object ):
"""Fundamental IFF atc data. Section 6.2.45
"""

    def __init__(self):
    """ Initializer for IFFFundamentalParameterData"""
            super(IFFFundamentalParameterData, self).__init__()
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
            systemSpecificData =  [ 0, 0, 0]
            """ System-specific data"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class FundamentalOperationalData( object ):
"""Basic operational data for IFF. Section 6.2.40.
"""

    def __init__(self):
    """ Initializer for FundamentalOperationalData"""
            super(FundamentalOperationalData, self).__init__()
            self.systemStatus = 0
            """ system status"""
            self.dataField1 = 0
            """ data field 1"""
            self.informationLayers = 0
            """ eight boolean fields"""
            self.dataField2 = 0
            """ enumeration"""
            self.parameter1 = 0
            """ parameter, enumeration"""
            self.parameter2 = 0
            """ parameter, enumeration"""
            self.parameter3 = 0
            """ parameter, enumeration"""
            self.parameter4 = 0
            """ parameter, enumeration"""
            self.parameter5 = 0
            """ parameter, enumeration"""
            self.parameter6 = 0
            """ parameter, enumeration"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IntercomCommunicationsParameters( object ):
"""Intercom communcations parameters. Section 6.2.47.  This requires hand coding
"""

    def __init__(self):
    """ Initializer for IntercomCommunicationsParameters"""
            super(IntercomCommunicationsParameters, self).__init__()
            self.recordType = 0
            """ Type of intercom parameters record"""
            self.recordLength = 0
            """ length of record"""
            self.recordSpecificField = 0
            """ This is a placeholder."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityType( object ):
"""Identifies the type of Entity
"""

    def __init__(self):
    """ Initializer for EntityType"""
            super(EntityType, self).__init__()
            self.entityKind = 0
            """ Kind of entity"""
            self.domain = 0
            """ Domain of entity (air, surface, subsurface, space, etc)"""
            self.country = 0
            """ country to which the design of the entity is attributed"""
            self.category = 0
            """ category of entity"""
            self.subcategory = 0
            """ subcategory of entity"""
            self.specific = 0
            """ specific info based on subcategory field. Renamed from specific because that is a reserved word in SQL."""
            self.extra = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Munition( object ):
"""An entity's munition (e.g., bomb, missile) information shall be represented by one or more Munition records. For each type or location of munition, this record shall specify the type, location, quantity and status of munitions that an entity contains. Section 6.2.60 
"""

    def __init__(self):
    """ Initializer for Munition"""
            super(Munition, self).__init__()
            munitionType = EntityType();
            """  This field shall identify the entity type of the munition. See section 6.2.30."""
            self.station = 0
            """ the station or launcher to which the munition is assigned. See Annex I"""
            self.quantity = 0
            """ the quantity remaining of this munition."""
            self.munitionStatus = 0
            """  the status of the munition. It shall be represented by an 8-bit enumeration. """
            self.padding = 0
            """ padding """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class StandardVariableSpecification( object ):
"""Does not work, and causes failure in anything it is embedded in. Section 6.2.83
"""

    def __init__(self):
    """ Initializer for StandardVariableSpecification"""
            super(StandardVariableSpecification, self).__init__()
            self.numberOfStandardVariableRecords = 0
            """ Number of static variable records"""
            standardVariables = []
            """ variable length list of standard variables, The class type and length here are WRONG and will cause the incorrect serialization of any class in whihc it is embedded."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Vector2Float( object ):
"""Two floating point values, x, y
"""

    def __init__(self):
    """ Initializer for Vector2Float"""
            super(Vector2Float, self).__init__()
            self.x = 0
            """ X value"""
            self.y = 0
            """ y Value"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Environment( object ):
"""Incomplete environment record; requires hand coding to fix. Section 6.2.31.1
"""

    def __init__(self):
    """ Initializer for Environment"""
            super(Environment, self).__init__()
            self.environmentType = 0
            """ type"""
            self.length = 0
            """ length, in bits, of the record"""
            self.index = 0
            """ identifies the sequntially numbered record index"""
            self.padding = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AcousticEmitter( object ):
""" information about a specific UA emmtter. Section 6.2.2.
"""

    def __init__(self):
    """ Initializer for AcousticEmitter"""
            super(AcousticEmitter, self).__init__()
            self.acousticSystemName = 0
            """ the system for a particular UA emitter, and an enumeration"""
            self.acousticFunction = 0
            """ The function of the acoustic system"""
            self.acousticIDNumber = 0
            """ The UA emitter identification number relative to a specific system"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AngularVelocityVector( object ):
"""Angular velocity measured in radians per second out each of the entity's own coordinate axes. Order of measurement is angular velocity around the x, y, and z axis of the entity. The positive direction is determined by the right hand rule. Section 6.2.7
"""

    def __init__(self):
    """ Initializer for AngularVelocityVector"""
            super(AngularVelocityVector, self).__init__()
            self.x = 0
            """ velocity about the x axis"""
            self.y = 0
            """ velocity about the y axis"""
            self.z = 0
            """ velocity about the zaxis"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AggregateMarking( object ):
"""Specifies the character set used in the first byte, followed by up to 31 characters of text data. Section 6.2.4. 
"""

    def __init__(self):
    """ Initializer for AggregateMarking"""
            super(AggregateMarking, self).__init__()
            self.characterSet = 0
            """ The character set"""
            characters =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            """ The characters"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DataFilterRecord( object ):
"""identify which of the optional data fields are contained in the Minefield Data PDU or requested in the Minefield Query PDU. This is a 32-bit record. For each field, true denotes that the data is requested or present and false denotes that the data is neither requested nor present. Section 6.2.16
"""

    def __init__(self):
    """ Initializer for DataFilterRecord"""
            super(DataFilterRecord, self).__init__()
            self.bitFlags = 0
            """ Bitflags field"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class IntercomIdentifier( object ):
"""Unique designation of an attached or unattached intercom in an event or exercirse. Section 6.2.48
"""

    def __init__(self):
    """ Initializer for IntercomIdentifier"""
            super(IntercomIdentifier, self).__init__()
            self.siteNumber = 0
            self.applicationNumber = 0
            self.referenceNumber = 0
            self.intercomNumber = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class StorageFuel( object ):
"""Information about an entity's engine fuel. Section 6.2.84.
"""

    def __init__(self):
    """ Initializer for StorageFuel"""
            super(StorageFuel, self).__init__()
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

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class StopFreezePdu( SimulationManagementFamilyPdu ):
"""Section 7.5.5. Stop or freeze an enity (or exercise). COMPLETE
"""

    def __init__(self):
    """ Initializer for StopFreezePdu"""
            super(StopFreezePdu, self).__init__()
            originatingID = EntityID();
            """ Identifier for originating entity(or simulation)"""
            receivingID = EntityID();
            """ Identifier for the receiving entity(or simulation)"""
            realWorldTime = ClockTime();
            """ real-world(UTC) time at which the entity shall stop or freeze in the exercise"""
            self.reason = 0
            """ Reason the simulation was stopped or frozen (see section 7 of SISO-REF-010) represented by an 8-bit enumeration"""
            self.frozenBehavior = 0
            """ Internal behavior of the entity(or simulation) and its appearance while frozen to the other participants"""
            self.padding1 = 0
            """ padding"""
            self.requestID = 0
            """ Request ID that is unique"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Sensor( object ):
"""An entity's sensor information.  Section 6.2.77.
"""

    def __init__(self):
    """ Initializer for Sensor"""
            super(Sensor, self).__init__()
            self.sensorTypeSource = 0
            """  the source of the Sensor Type field """
            self.sensorOnOffStatus = 0
            """ the on/off status of the sensor"""
            self.sensorType = 0
            """ the sensor type and shall be represented by a 16-bit enumeration. """
            self.station = 0
            """  the station to which the sensor is assigned. A zero value shall indi- cate that this Sensor record is not associated with any particular station and represents the total quan- tity of this sensor for this entity. If this field is non-zero, it shall either reference an attached part or an articulated part"""
            self.quantity = 0
            """ quantity of the sensor """
            self.padding = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityStatePdu( EntityInformationFamilyPdu ):
"""Represents the postion and state of one entity in the world. Section 7.2.2. COMPLETE
"""

    def __init__(self):
    """ Initializer for EntityStatePdu"""
            super(EntityStatePdu, self).__init__()
            entityID = EntityID();
            """ Unique ID for an entity that is tied to this state information"""
            self.forceId = 0
            """ What force this entity is affiliated with, eg red, blue, neutral, etc"""
            self.numberOfVariableParameters = 0
            """ How many variable parameters are in the variable length list. In earlier versions of DIS these were known as articulation parameters"""
            entityType = EntityType();
            """ Describes the type of entity in the world"""
            alternativeEntityType = EntityType();
            entityLinearVelocity = Vector3Float();
            """ Describes the speed of the entity in the world"""
            entityLocation = Vector3Double();
            """ describes the location of the entity in the world"""
            entityOrientation = EulerAngles();
            """ describes the orientation of the entity, in euler angles"""
            self.entityAppearance = 0
            """ a series of bit flags that are used to help draw the entity, such as smoking, on fire, etc."""
            deadReckoningParameters = DeadReckoningParameters();
            """ parameters used for dead reckoning"""
            marking = EntityMarking();
            """ characters that can be used for debugging, or to draw unique strings on the side of entities in the world"""
            self.capabilities = 0
            """ a series of bit flags"""
            variableParameters = []
            """ variable length list of variable parameters. In earlier DIS versions this was articulation parameters."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MunitionReload( object ):
"""indicate weapons (munitions) previously communicated via the Munition record. Section 6.2.61 
"""

    def __init__(self):
    """ Initializer for MunitionReload"""
            super(MunitionReload, self).__init__()
            munitionType = EntityType();
            """  This field shall identify the entity type of the munition. See section 6.2.30."""
            self.station = 0
            """ the station or launcher to which the munition is assigned. See Annex I"""
            self.standardQuantity = 0
            """ the standard quantity of this munition type normally loaded at this station/launcher if a station/launcher is specified."""
            self.maximumQuantity = 0
            """ the maximum quantity of this munition type that this station/launcher is capable of holding when a station/launcher is specified """
            self.standardQuantityReloadTime = 0
            """ numer of seconds of sim time required to reload the std qty"""
            self.maximumQuantityReloadTime = 0
            """ the number of seconds of sim time required to reload the max possible quantity"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityManagementFamilyPdu( Pdu ):
""" Managment of grouping of PDUs, and more. Section 7.8
"""

    def __init__(self):
    """ Initializer for EntityManagementFamilyPdu"""
            super(EntityManagementFamilyPdu, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class StorageFuelReload( object ):
"""For each type or location of Storage Fuel, this record shall specify the type, location, fuel measure- ment units, reload quantity and maximum quantity for storage fuel either for the whole entity or a specific storage fuel location (tank). Section 6.2.85.
"""

    def __init__(self):
    """ Initializer for StorageFuelReload"""
            super(StorageFuelReload, self).__init__()
            self.standardQuantity = 0
            """  the standard quantity of this fuel type normally loaded at this station/launcher if a station/launcher is specified. If the Station/Launcher field is set to zero, then this is the total quantity of this fuel type that would be present in a standard reload of all appli- cable stations/launchers associated with this entity."""
            self.maximumQuantity = 0
            """ the maximum quantity of this fuel type that this sta- tion/launcher is capable of holding when a station/launcher is specified. This would be the value used when a maximum reload was desired to be set for this station/launcher. If the Station/launcher field is set to zero, then this is the maximum quantity of this fuel type that would be present on this entity at all stations/launchers that can accept this fuel type."""
            self.standardQuantityReloadTime = 0
            """ the seconds normally required to reload the standard quantity of this fuel type at this specific station/launcher. When the Station/Launcher field is set to zero, this shall be the time it takes to perform a standard quantity reload of this fuel type at all applicable stations/launchers for this entity."""
            self.maximumQuantityReloadTime = 0
            """ the seconds normally required to reload the maximum possible quantity of this fuel type at this station/launcher. When the Station/Launcher field is set to zero, this shall be the time it takes to perform a maximum quantity load/reload of this fuel type at all applicable stations/launchers for this entity."""
            self.fuelMeasurementUnits = 0
            """ the fuel measurement units. Enumeration"""
            self.fuelType = 0
            """ Fuel type. Enumeration"""
            self.fuelLocation = 0
            """ Location of fuel as related to entity. See section 14 of EBV document"""
            self.padding = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ExpendableReload( object ):
"""An entity's expendable (chaff, flares, etc) information. Section 6.2.37
"""

    def __init__(self):
    """ Initializer for ExpendableReload"""
            super(ExpendableReload, self).__init__()
            expendable = EntityType();
            """ Type of expendable"""
            self.station = 0
            self.standardQuantity = 0
            self.maximumQuantity = 0
            self.standardQuantityReloadTime = 0
            self.maximumQuantityReloadTime = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class StartResumePdu( SimulationManagementFamilyPdu ):
"""Section 7.5.4. Start or resume an exercise. COMPLETE
"""

    def __init__(self):
    """ Initializer for StartResumePdu"""
            super(StartResumePdu, self).__init__()
            originatingID = EntityID();
            """ Identifier for originating entity(or simulation)"""
            receivingID = EntityID();
            """ Identifier for the receiving entity(or simulation)"""
            realWorldTime = ClockTime();
            """ This field shall specify the real-world time (UTC) at which the entity is to start/resume in the exercise. This information shall be used by the participating simulation applications to start/resume an exercise synchronously. This field shall be represented by a Clock Time record (see 6.2.16)."""
            simulationTime = ClockTime();
            """ The reference time within a simulation exercise. This time is established ahead of time by simulation management and is common to all participants in a particular exercise. Simulation time may be either Absolute Time or Relative Time. This field shall be represented by a Clock Time record (see 6.2.16)"""
            self.requestID = 0
            """ Identifier for the specific and unique start/resume request"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class TransmitterPdu( RadioCommunicationsFamilyPdu ):
"""Detailed information about a radio transmitter. This PDU requires manually written code to complete, since the modulation parameters are of variable length. Section 7.7.2 UNFINISHED
"""

    def __init__(self):
    """ Initializer for TransmitterPdu"""
            super(TransmitterPdu, self).__init__()
            radioReferenceID = EntityID();
            """ ID of the entitythat is the source of the communication"""
            self.radioNumber = 0
            """ particular radio within an entity"""
            radioEntityType = EntityType();
            """ Type of radio"""
            self.transmitState = 0
            """ transmit state"""
            self.inputSource = 0
            """ input source"""
            self.variableTransmitterParameterCount = 0
            """ count field"""
            antennaLocation = Vector3Double();
            """ Location of antenna"""
            relativeAntennaLocation = Vector3Float();
            """ relative location of antenna"""
            self.antennaPatternType = 0
            """ antenna pattern type"""
            self.antennaPatternCount = 0
            """ atenna pattern length"""
            self.frequency = 0
            """ frequency"""
            self.transmitFrequencyBandwidth = 0
            """ transmit frequency Bandwidth"""
            self.power = 0
            """ transmission power"""
            modulationType = ModulationType();
            """ modulation"""
            self.cryptoSystem = 0
            """ crypto system enumeration"""
            self.cryptoKeyId = 0
            """ crypto system key identifer"""
            self.modulationParameterCount = 0
            """ how many modulation parameters we have"""
            self.padding2 = 0
            """ padding2"""
            self.padding3 = 0
            """ padding3"""
            modulationParametersList = []
            """ variable length list of modulation parameters"""
            antennaPatternList = []
            """ variable length list of antenna pattern records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ElectronicEmissionsPdu( DistributedEmissionsFamilyPdu ):
"""Section 5.3.7.1. Information about active electronic warfare (EW) emissions and active EW countermeasures shall be communicated using an Electromagnetic Emission PDU. NOT COMPLETE
"""

    def __init__(self):
    """ Initializer for ElectronicEmissionsPdu"""
            super(ElectronicEmissionsPdu, self).__init__()
            emittingEntityID = EntityID();
            """ ID of the entity emitting"""
            eventID = EventIdentifier();
            """ ID of event"""
            self.stateUpdateIndicator = 0
            """ This field shall be used to indicate if the data in the PDU represents a state update or just data that has changed since issuance of the last Electromagnetic Emission PDU [relative to the identified entity and emission system(s)]."""
            self.numberOfSystems = 0
            """ This field shall specify the number of emission systems being described in the current PDU."""
            self.paddingForEmissionsPdu = 0
            """ padding"""
            self.systemDataLength = 0
            """  this field shall specify the length of this emitter system's data in 32-bit words."""
            self.numberOfBeams = 0
            """ the number of beams being described in the current PDU for the emitter system being described. """
            emitterSystem = EmitterSystem();
            """  information about a particular emitter system and shall be represented by an Emitter System record (see 6.2.23)."""
            location = Vector3Float();
            """ the location of the antenna beam source with respect to the emitting entity's coordinate system. This location shall be the origin of the emitter coordinate system that shall have the same orientation as the entity coordinate system. This field shall be represented by an Entity Coordinate Vector record see 6.2.95 """
            systems = []
            """ Electronic emmissions systems THIS IS WRONG. It has the WRONG class type and will cause problems in any marshalling."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityIdentifier( object ):
"""Entity Identifier. Unique ID for entities in the world. Consists of an simulation address and a entity number. Section 6.2.28.
"""

    def __init__(self):
    """ Initializer for EntityIdentifier"""
            super(EntityIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """ Site and application IDs"""
            self.entityNumber = 0
            """ Entity number"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DirectedEnergyTargetEnergyDeposition( object ):
"""DE energy depostion properties for a target entity. Section 6.2.20.4
"""

    def __init__(self):
    """ Initializer for DirectedEnergyTargetEnergyDeposition"""
            super(DirectedEnergyTargetEnergyDeposition, self).__init__()
            targetEntityID = EntityID();
            """ Unique ID of the target entity."""
            self.padding = 0
            """ padding"""
            self.peakIrradiance = 0
            """ Peak irrandiance"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityID( object ):
"""more laconically named EntityIdentifier
"""

    def __init__(self):
    """ Initializer for EntityID"""
            super(EntityID, self).__init__()
            self.siteID = 0
            """ Site ID"""
            self.applicationID = 0
            """ application number ID"""
            self.entityID = 0
            """ Entity number ID"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ResupplyOfferPdu( LogisticsFamilyPdu ):
"""Information used to communicate the offer of supplies by a supplying entity to a receiving entity. Section 7.4.3 COMPLETE
"""

    def __init__(self):
    """ Initializer for ResupplyOfferPdu"""
            super(ResupplyOfferPdu, self).__init__()
            receivingEntityID = EntityID();
            """ Field identifies the Entity and respective Entity Record ID that is receiving service (see 6.2.28), Section 7.4.3"""
            supplyingEntityID = EntityID();
            """ Identifies the Entity and respective Entity ID Record that is supplying  (see 6.2.28), Section 7.4.3"""
            self.numberOfSupplyTypes = 0
            """ How many supplies types are being offered, Section 7.4.3"""
            self.padding1 = 0
            """ padding"""
            self.padding2 = 0
            """ padding"""
            supplies = []
            """ A Reord that Specifies the type of supply and the amount of that supply for each of the supply types in numberOfSupplyTypes (see 6.2.85), Section 7.4.3"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EngineFuelReload( object ):
"""For each type or location of engine fuell, this record specifies the type, location, fuel measurement units, and reload quantity and maximum quantity. Section 6.2.25.
"""

    def __init__(self):
    """ Initializer for EngineFuelReload"""
            super(EngineFuelReload, self).__init__()
            self.standardQuantity = 0
            """ standard quantity of fuel loaded"""
            self.maximumQuantity = 0
            """ maximum quantity of fuel loaded"""
            self.standardQuantityReloadTime = 0
            """ seconds normally required to to reload standard qty"""
            self.maximumQuantityReloadTime = 0
            """ seconds normally required to to reload maximum qty"""
            self.fuelMeasurmentUnits = 0
            """ Units of measure"""
            self.fuelLocation = 0
            """ fuel  location as related to the entity"""
            self.padding = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class UnattachedIdentifier( object ):
"""The unique designation of one or more unattached radios in an event or exercise Section 6.2.91
"""

    def __init__(self):
    """ Initializer for UnattachedIdentifier"""
            super(UnattachedIdentifier, self).__init__()
            simulationAddress = SimulationAddress();
            """ See 6.2.79"""
            self.referenceNumber = 0
            """ Reference number"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AttributePdu( EntityInformationFamilyPdu ):
"""Information about individual attributes for a particular entity, other object, or event may be communicated using an Attribute PDU. The Attribute PDU shall not be used to exchange data available in any other PDU except where explicitly mentioned in the PDU issuance instructions within this standard. See 5.3.6 for the information requirements and issuance and receipt rules for this PDU. Section 7.2.6. INCOMPLETE
"""

    def __init__(self):
    """ Initializer for AttributePdu"""
            super(AttributePdu, self).__init__()
            originatingSimulationAddress = SimulationAddress();
            """ This field shall identify the simulation issuing the Attribute PDU. It shall be represented by a Simulation Address record (see 6.2.79)."""
            self.padding1 = 0
            """ Padding"""
            self.padding2 = 0
            """ Padding"""
            self.attributeRecordPduType = 0
            """ This field shall represent the type of the PDU that is being extended or updated, if applicable. It shall be represented by an 8-bit enumeration."""
            self.attributeRecordProtocolVersion = 0
            """ This field shall indicate the Protocol Version associated with the Attribute Record PDU Type. It shall be represented by an 8-bit enumeration."""
            self.masterAttributeRecordType = 0
            """ This field shall contain the Attribute record type of the Attribute records in the PDU if they all have the same Attribute record type. It shall be represented by a 32-bit enumeration."""
            self.actionCode = 0
            """ This field shall identify the action code applicable to this Attribute PDU. The Action Code shall apply to all Attribute records contained in the PDU. It shall be represented by an 8-bit enumeration."""
            self.padding3 = 0
            """ Padding"""
            self.numberAttributeRecordSet = 0
            """ This field shall specify the number of Attribute Record Sets that make up the remainder of the PDU. It shall be represented by a 16-bit unsigned integer."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityTypeVP( object ):
"""Association or disassociation of two entities.  Section 6.2.94.5
"""

    def __init__(self):
    """ Initializer for EntityTypeVP"""
            super(EntityTypeVP, self).__init__()
            self.recordType = 3
            """ the identification of the Variable Parameter record. Enumeration from EBV"""
            self.changeIndicator = 0
            """ Indicates if this VP has changed since last issuance"""
            entityType = EntityType();
            """ """
            self.padding = 0
            """ padding"""
            self.padding1 = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class MinefieldFamilyPdu( Pdu ):
""" Abstract superclass for PDUs relating to minefields. Section 7.9
"""

    def __init__(self):
    """ Initializer for MinefieldFamilyPdu"""
            super(MinefieldFamilyPdu, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class BeamStatus( object ):
"""Information related to the status of a beam. This is contained in the beam status field of the electromagnitec emission PDU. The first bit determines whether the beam is active (0) or deactivated (1). Section 6.2.12.
"""

    def __init__(self):
    """ Initializer for BeamStatus"""
            super(BeamStatus, self).__init__()
            self.beamState = 0
            """ First bit zero means beam is active, first bit = 1 means deactivated. The rest is padding."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EnvironmentGeneral( object ):
""" Information about a geometry, a state associated with a geometry, a bounding volume, or an associated entity ID. NOTE: this class requires hand coding. 6.2.31
"""

    def __init__(self):
    """ Initializer for EnvironmentGeneral"""
            super(EnvironmentGeneral, self).__init__()
            self.environmentType = 0
            """ Record type"""
            self.length = 0
            """ length, in bits"""
            self.index = 0
            """ Identify the sequentially numbered record index"""
            self.padding1 = 0
            """ padding"""
            self.geometry = 0
            """ Geometry or state record"""
            self.padding2 = 0
            """ padding to bring the total size up to a 64 bit boundry"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SetDataReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.9: initializing or chaning internal state information, reliable. Needs manual intervention to fix     padding on variable datums. UNFINISHED
"""

    def __init__(self):
    """ Initializer for SetDataReliablePdu"""
            super(SetDataReliablePdu, self).__init__()
            self.requiredReliabilityService = 0
            """ level of reliability service used for this transaction"""
            self.pad1 = 0
            """ padding"""
            self.pad2 = 0
            """ padding"""
            self.requestID = 0
            """ Request ID"""
            self.numberOfFixedDatumRecords = 0
            """ Fixed datum record count"""
            self.numberOfVariableDatumRecords = 0
            """ variable datum record count"""
            fixedDatumRecords = []
            """ Fixed datum records"""
            variableDatumRecords = []
            """ Variable datum records"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Vector3Double( object ):
"""Three double precision floating point values, x, y, and z. Used for world coordinates Section 6.2.97.
"""

    def __init__(self):
    """ Initializer for Vector3Double"""
            super(Vector3Double, self).__init__()
            self.x = 0
            """ X value"""
            self.y = 0
            """ y Value"""
            self.z = 0
            """ Z value"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class GridAxis( object ):
"""Grid axis record for fixed data. Section 6.2.41
"""

    def __init__(self):
    """ Initializer for GridAxis"""
            super(GridAxis, self).__init__()
            self.domainInitialXi = 0
            """ coordinate of the grid origin or initial value"""
            self.domainFinalXi = 0
            """ coordinate of the endpoint or final value"""
            self.domainPointsXi = 0
            """ The number of grid points along the Xi domain axis for the enviornmental state data"""
            self.interleafFactor = 0
            """ interleaf factor along the domain axis."""
            self.axisType = 0
            """ type of grid axis"""
            self.numberOfPointsOnXiAxis = 0
            """ Number of grid locations along Xi axis"""
            self.initialIndex = 0
            """ initial grid point for the current pdu"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class Pdu( PduSuperclass ):
"""Adds some fields to the the classic PDU
"""

    def __init__(self):
    """ Initializer for Pdu"""
            super(Pdu, self).__init__()
            self.pduStatus = 0
            """ PDU Status Record. Described in 6.2.67. This field is not present in earlier DIS versions """
            self.padding = 0
            """ zero-filled array of padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class RecordSpecification( object ):
"""This record shall specify the number of record sets contained in the Record Specification record and the record details. Section 6.2.73.
"""

    def __init__(self):
    """ Initializer for RecordSpecification"""
            super(RecordSpecification, self).__init__()
            self.numberOfRecordSets = 0
            """ The number of record sets"""
            recordSets = []
            """ variable length list record specifications."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class VariableDatum( object ):
"""the variable datum type, the datum length, and the value for that variable datum type. NOT COMPLETE. Section 6.2.93
"""

    def __init__(self):
    """ Initializer for VariableDatum"""
            super(VariableDatum, self).__init__()
            self.variableDatumID = 0
            """ Type of variable datum to be transmitted. 32 bit enumeration defined in EBV"""
            self.variableDatumLength = 0
            """ Length, IN BITS, of the variable datum."""
            self.variableDatumBits = 0
            """ Variable datum. This can be any number of bits long, depending on the datum."""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EventReportPdu( SimulationManagementFamilyPdu ):
""" Reports occurance of a significant event to the simulation manager. Section 7.5.12. COMPLETE
"""

    def __init__(self):
    """ Initializer for EventReportPdu"""
            super(EventReportPdu, self).__init__()
            self.eventType = 0
            """ Type of event"""
            self.padding1 = 0
            """ padding"""
            self.numberOfFixedDatumRecords = 0
            """ Number of fixed datum records"""
            self.numberOfVariableDatumRecords = 0
            """ Number of variable datum records"""
            fixedDatums = []
            """ variable length list of fixed datums"""
            variableDatums = []
            """ variable length list of variable length datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class PointObjectStatePdu( SyntheticEnvironmentFamilyPdu ):
""": Inormation abut the addition or modification of a synthecic enviroment object that is anchored to the terrain with a single point. Section 7.10.4 COMPLETE
"""

    def __init__(self):
    """ Initializer for PointObjectStatePdu"""
            super(PointObjectStatePdu, self).__init__()
            objectID = EntityID();
            """ Object in synthetic environment"""
            referencedObjectID = EntityID();
            """ Object with which this point object is associated"""
            self.updateNumber = 0
            """ unique update number of each state transition of an object"""
            self.forceID = 0
            """ force ID"""
            self.modifications = 0
            """ modifications"""
            objectType = ObjectType();
            """ Object type"""
            objectLocation = Vector3Double();
            """ Object location"""
            objectOrientation = EulerAngles();
            """ Object orientation"""
            self.objectAppearance = 0
            """ Object apperance"""
            requesterID = SimulationAddress();
            """ requesterID"""
            receivingID = SimulationAddress();
            """ receiver ID"""
            self.pad2 = 0
            """ padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EventIdentifierLiveEntity( object ):
"""Identifies an event in the world. Use this format for ONLY the LiveEntityPdu. Section 6.2.34.
"""

    def __init__(self):
    """ Initializer for EventIdentifierLiveEntity"""
            super(EventIdentifierLiveEntity, self).__init__()
            self.siteNumber = 0
            self.applicationNumber = 0
            self.eventNumber = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class PduHeader( object ):
"""Not used. The PDU Header Record is directly incoroporated into the PDU class. Here for completness only. Section 6.2.66
"""

    def __init__(self):
    """ Initializer for PduHeader"""
            super(PduHeader, self).__init__()
            self.protocolVersion = 7
            """ The version of the protocol. 5=DIS-1995, 6=DIS-1998, 7=DIS-2009."""
            self.exerciseID = 0
            """ Exercise ID"""
            self.pduType = 0
            """ Type of pdu, unique for each PDU class"""
            self.protocolFamily = 0
            """ value that refers to the protocol family, eg SimulationManagement, etc"""
            self.timestamp = 0
            """ Timestamp value"""
            self.pduLength = 0
            """ Length, in bytes, of the PDU. Changed name from length to avoid use of Hibernate QL reserved word."""
            self.pduStatus = 0
            """ PDU Status Record. Described in 6.2.67. This field is not present in earlier DIS versions """
            self.padding = 0
            """ zero filled array of padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class PduSuperclass( object ):
"""The superclass for all PDUs, including classic and Live Entity (LE) PDUs. This incorporates the PduHeader record, section 7.2.2
"""

    def __init__(self):
    """ Initializer for PduSuperclass"""
            super(PduSuperclass, self).__init__()
            self.protocolVersion = 7
            """ The version of the protocol. 5=DIS-1995, 6=DIS-1998, 7=DIS-2009."""
            self.exerciseID = 0
            """ Exercise ID"""
            self.pduType = 0
            """ Type of pdu, unique for each PDU class"""
            self.protocolFamily = 0
            """ value that refers to the protocol family, eg SimulationManagement, et"""
            self.timestamp = 0
            """ Timestamp value"""
            self.length = 0
            """ Length, in bytes, of the PDU"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class CommunicationsNodeID( object ):
"""Identity of a communications node. Section 6.2.48.4
"""

    def __init__(self):
    """ Initializer for CommunicationsNodeID"""
            super(CommunicationsNodeID, self).__init__()
            entityID = EntityID();
            self.elementID = 0

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class DataPdu( SimulationManagementFamilyPdu ):
""" Information issued in response to a data query pdu or a set data pdu is communicated using a data pdu. Section 7.5.11 COMPLETE
"""

    def __init__(self):
    """ Initializer for DataPdu"""
            super(DataPdu, self).__init__()
            self.requestID = 0
            """ ID of request"""
            self.padding1 = 0
            """ padding"""
            self.numberOfFixedDatumRecords = 0
            """ Number of fixed datum records"""
            self.numberOfVariableDatumRecords = 0
            """ Number of variable datum records"""
            fixedDatums = []
            """ variable length list of fixed datums"""
            variableDatums = []
            """ variable length list of variable length datums"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class ExpendableDescriptor( object ):
"""Burst of chaff or expendible device. Section 6.2.19.4
"""

    def __init__(self):
    """ Initializer for ExpendableDescriptor"""
            super(ExpendableDescriptor, self).__init__()
            expendableType = EntityType();
            """ Type of the object that exploded"""
            self.padding = 0
            """ Padding"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class PropulsionSystemData( object ):
"""contains information describing the propulsion systems of the entity. This information shall be provided for each active propulsion system defined. Section 6.2.68
"""

    def __init__(self):
    """ Initializer for PropulsionSystemData"""
            super(PropulsionSystemData, self).__init__()
            self.powerSetting = 0
            """ powerSetting"""
            self.engineRpm = 0
            """ engine RPMs"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class LiveEntityIdentifier( object ):
"""The unique designation of each entity in an event or exercise that is contained in a Live Entity PDU. Section 6.2.54 
"""

    def __init__(self):
    """ Initializer for LiveEntityIdentifier"""
            super(LiveEntityIdentifier, self).__init__()
            liveSimulationAddress = LiveSimulationAddress();
            """ Live Simulation Address record (see 6.2.54) """
            self.entityNumber = 0
            """ Live entity number """

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class FastEntityStatePdu( EntityInformationFamilyPdu ):
"""Represents the postion and state of one entity in the world. This is identical in function to entity state pdu, but generates less garbage to collect in the Java world. Section 7.2.2. COMPLETE
"""

    def __init__(self):
    """ Initializer for FastEntityStatePdu"""
            super(FastEntityStatePdu, self).__init__()
            self.site = 0
            """ The site ID"""
            self.application = 0
            """ The application ID"""
            self.entity = 0
            """ the entity ID"""
            self.forceId = 0
            """ what force this entity is affiliated with, eg red, blue, neutral, etc"""
            self.numberOfVariableParameters = 0
            """ How many variable (nee articulation) parameters are in the variable length list"""
            self.entityKind = 0
            """ Kind of entity"""
            self.domain = 0
            """ Domain of entity (air, surface, subsurface, space, etc)"""
            self.country = 0
            """ country to which the design of the entity is attributed"""
            self.category = 0
            """ category of entity"""
            self.subcategory = 0
            """ subcategory of entity"""
            self.specific = 0
            """ specific info based on subcategory field"""
            self.extra = 0
            self.altEntityKind = 0
            """ Kind of entity"""
            self.altDomain = 0
            """ Domain of entity (air, surface, subsurface, space, etc)"""
            self.altCountry = 0
            """ country to which the design of the entity is attributed"""
            self.altCategory = 0
            """ category of entity"""
            self.altSubcategory = 0
            """ subcategory of entity"""
            self.altSpecific = 0
            """ specific info based on subcategory field"""
            self.altExtra = 0
            self.xVelocity = 0
            """ X velo"""
            self.yVelocity = 0
            """ y Value"""
            self.zVelocity = 0
            """ Z value"""
            self.xLocation = 0
            """ X value"""
            self.yLocation = 0
            """ y Value"""
            self.zLocation = 0
            """ Z value"""
            self.psi = 0
            self.theta = 0
            self.phi = 0
            self.entityAppearance = 0
            """ a series of bit flags that are used to help draw the entity, such as smoking, on fire, etc."""
            self.deadReckoningAlgorithm = 0
            """ enumeration of what dead reckoning algorighm to use"""
            otherParameters =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            """ other parameters to use in the dead reckoning algorithm"""
            self.xAcceleration = 0
            """ X value"""
            self.yAcceleration = 0
            """ y Value"""
            self.zAcceleration = 0
            """ Z value"""
            self.xAngularVelocity = 0
            """ X value"""
            self.yAngularVelocity = 0
            """ y Value"""
            self.zAngularVelocity = 0
            """ Z value"""
            marking =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            """ characters that can be used for debugging, or to draw unique strings on the side of entities in the world"""
            self.capabilities = 0
            """ a series of bit flags"""
            variableParameters = []
            """ variable length list of variable parameters. In earlier versions of DIS these were known as articulation parameters"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class SeparationVP( object ):
"""Physical separation of an entity from another entity.  Section 6.2.94.6
"""

    def __init__(self):
    """ Initializer for SeparationVP"""
            super(SeparationVP, self).__init__()
            self.recordType = 2
            """ the identification of the Variable Parameter record. Enumeration from EBV"""
            self.reasonForSeparation = 0
            """ Reason for separation. EBV"""
            self.preEntityIndicator = 0
            """ Whether the entity existed prior to separation EBV"""
            self.padding1 = 0
            """ padding"""
            parentEntityID = EntityID();
            """ ID of parent"""
            self.padding2 = 0
            """ padding"""
            self.stationLocation = 0
            """ Station separated from"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EmitterSystem( object ):
"""This field shall specify information about a particular emitter system. Section 6.2.23.
"""

    def __init__(self):
    """ Initializer for EmitterSystem"""
            super(EmitterSystem, self).__init__()
            self.emitterName = 0
            """ Name of the emitter, 16 bit enumeration"""
            self.emitterFunction = 0
            """ function of the emitter, 8 bit enumeration"""
            self.emitterIDNumber = 0
            """ emitter ID, 8 bit enumeration"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class PduStatus( object ):
"""PDU Status. These are a series of bit fields. Represented here as just a byte. Section 6.2.67
"""

    def __init__(self):
    """ Initializer for PduStatus"""
            super(PduStatus, self).__init__()
            self.pduStatus = 0
            """ Bit fields. The semantics of the bit fields depend on the PDU type"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class EntityInformationFamilyPdu( Pdu ):
"""Section 5.3.3. Common superclass for EntityState, Collision, collision-elastic, and entity state update PDUs. This should be abstract. COMPLETE
"""

    def __init__(self):
    """ Initializer for EntityInformationFamilyPdu"""
            super(EntityInformationFamilyPdu, self).__init__()

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class PduContainer( object ):
"""Used for XML compatability. A container that holds PDUs
"""

    def __init__(self):
    """ Initializer for PduContainer"""
            super(PduContainer, self).__init__()
            self.numberOfPdus = 0
            """ Number of PDUs in the container list"""
            pdus = []
            """ record sets"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack



class AcknowledgeReliablePdu( SimulationManagementWithReliabilityFamilyPdu ):
"""Section 5.3.12.5: Ack receipt of a start-resume, stop-freeze, create-entity or remove enitty (reliable) pdus. COMPLETE
"""

    def __init__(self):
    """ Initializer for AcknowledgeReliablePdu"""
            super(AcknowledgeReliablePdu, self).__init__()
            self.acknowledgeFlag = 0
            """ ack flags"""
            self.responseFlag = 0
            """ response flags"""
            self.requestID = 0
            """ Request ID"""

    def _pack(self):
        print pack


    def _unpack(self):

        print unpack


