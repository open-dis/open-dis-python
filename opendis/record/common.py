"""Common record types used across multiple protocol families"""

from opendis.record import base, bitfield
from opendis.stream import DataInputStream, DataOutputStream
from opendis.types import (
    enum8,
    enum16,
    enum32,
    bf_enum,
    bf_int,
    bf_uint,
    float32,
    float64,
    struct8,
    uint8,
    uint16,
    uint32,
)

from . import symbolic_names as sym

__all__ = [
    "Vector3Float",
    "WorldCoordinates",
    "EntityIdentifier",
    "EulerAngles",
    "SimulationAddress",
    "EventIdentifier",
]


class EntityIdentifier(base.Record):
    """Section 6.2.28 Entity Identifier record
    
    Unique designation of each entity in an event or exercise that is not
    contained in a Live Entity PDU.
    """

    def __init__(self,
                 simulationAddress: "SimulationAddress | None" = None,
                 entityNumber: uint16 = 0):
        self.simulationAddress = simulationAddress or SimulationAddress()
        self.entityNumber = entityNumber
    
    def marshalledSize(self) -> int:
        return self.simulationAddress.marshalledSize() + 2

    def serialize(self, outputStream: DataOutputStream) -> None:
        self.simulationAddress.serialize(outputStream)
        outputStream.write_uint16(self.entityNumber)

    def parse(self, inputStream: DataInputStream) -> None:
        self.simulationAddress.parse(inputStream)
        self.entityNumber = inputStream.read_uint16()


class EulerAngles(base.Record):
    """6.2.32 Euler Angles record

    Three floating point values representing an orientation, psi, theta,
    and phi, aka the euler angles, in radians.
    These angles shall be specified with respect to the entity's coordinate
    system.
    """

    def __init__(self,
                 psi: float32 = 0.0,
                 theta: float32 = 0.0,
                 phi: float32 = 0.0):  # in radians
        self.psi = psi
        self.theta = theta
        self.phi = phi

    def marshalledSize(self) -> int:
        return 12

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_float32(self.psi)
        outputStream.write_float32(self.theta)
        outputStream.write_float32(self.phi)

    def parse(self, inputStream: DataInputStream) -> None:
        self.psi = inputStream.read_float32()
        self.theta = inputStream.read_float32()
        self.phi = inputStream.read_float32()


class EventIdentifier(base.Record):
    """6.2.33 Event Identifier record
    
    Identifies an event in the world. Use this format for every PDU EXCEPT
    the LiveEntityPdu.
    """
    # TODO: Distinguish EventIdentifier and LiveEventIdentifier

    def __init__(self,
                 simulationAddress: "SimulationAddress | None" = None,
                 eventNumber: uint16 = 0):
        self.simulationAddress = simulationAddress or SimulationAddress()
        """Site and application IDs"""
        self.eventNumber = eventNumber

    def marshalledSize(self) -> int:
        return self.simulationAddress.marshalledSize() + 2

    def serialize(self, outputStream: DataOutputStream) -> None:
        self.simulationAddress.serialize(outputStream)
        outputStream.write_unsigned_short(self.eventNumber)

    def parse(self, inputStream: DataInputStream) -> None:
        self.simulationAddress.parse(inputStream)
        self.eventNumber = inputStream.read_unsigned_short()


class SimulationAddress(base.Record):
    """6.2.80 Simulation Address record
    
    Simulation designation associated with all object identifiers except
    those contained in Live Entity PDUs.
    """

    def __init__(self,
                 site: uint16 = 0,
                 application: uint16 = 0):
        self.site = site
        """A site is defined as a facility, installation, organizational unit or a geographic location that has one or more simulation applications capable of participating in a distributed event."""
        self.application = application
        """An application is defined as a software program that is used to generate and process distributed simulation data including live, virtual and constructive data."""

    def marshalledSize(self) -> int:
        return 4

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_unsigned_short(self.site)
        outputStream.write_unsigned_short(self.application)

    def parse(self, inputStream: DataInputStream) -> None:
        self.site = inputStream.read_unsigned_short()
        self.application = inputStream.read_unsigned_short()


class Vector3Float(base.Record):
    """6.2.96 Vector record
    
    Vector values for entity coordinates, linear acceleration, and linear
    velocity shall be represented using a Vector record. This record shall
    consist of three fields, each a 32-bit floating point number.
    The unit of measure represented by these fields shall depend on the
    information represented.
    """

    def __init__(self, x: float32 = 0.0, y: float32 = 0.0, z: float32 = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def marshalledSize(self) -> int:
        return 12

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_float(self.x)
        outputStream.write_float(self.y)
        outputStream.write_float(self.z)

    def parse(self, inputStream: DataInputStream) -> None:
        self.x = inputStream.read_float()
        self.y = inputStream.read_float()
        self.z = inputStream.read_float()


class WorldCoordinates(base.Record):
    """6.2.98 World Coordinates record

    Location of the origin of the entity's or object's coordinate system,
    target locations, detonation locations, and other points shall be specified
    by a set of three coordinates: X, Y, and Z, represented by 64-bit floating
    point numbers.
    """

    def __init__(self, x: float64 = 0.0, y: float64 = 0.0, z: float64 = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def marshalledSize(self) -> int:
        return 24

    def serialize(self, outputStream: DataOutputStream) -> None:
        outputStream.write_float64(self.x)
        outputStream.write_float64(self.y)
        outputStream.write_float64(self.z)

    def parse(self, inputStream: DataInputStream) -> None:
        self.x = inputStream.read_float64()
        self.y = inputStream.read_float64()
        self.z = inputStream.read_float64()


