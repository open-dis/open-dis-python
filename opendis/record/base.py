"""Base classes for all Record types."""

__all__ = ["Record", "VariableRecord"]

from abc import abstractmethod
from typing import Any, Protocol, TypeGuard, runtime_checkable

from opendis.stream import DataInputStream, DataOutputStream


@runtime_checkable
class Record(Protocol):
    """Base class for all Record types.
    
    This base class defines the interface for DIS records with fixed sizes.
    """

    @abstractmethod
    def marshalledSize(self) -> int:
        """Return the size (in bytes) of the record when serialized."""

    @abstractmethod
    def serialize(self, outputStream: DataOutputStream) -> None:
        """Serialize the record to the output stream."""

    @abstractmethod
    def parse(self, inputStream: DataInputStream) -> None:
        """Parse the record from the input stream."""


@runtime_checkable
class VariableRecord(Protocol):
    """Base class for all Variable Record types.

    This base class defines the interface for DIS records with variable sizes.
    """

    @staticmethod
    def is_positive_int(value: Any) -> TypeGuard[int]:
        """Check if a value is a positive integer."""
        return isinstance(value, int) and value >= 0

    @abstractmethod
    def marshalledSize(self) -> int:
        """Return the size (in bytes) of the record when serialized."""

    @abstractmethod
    def serialize(self, outputStream: DataOutputStream) -> None:
        """Serialize the record to the output stream."""

    @abstractmethod
    def parse(self,
              inputStream: DataInputStream,
              bytelength: int | None = None) -> None:
        """Parse the record from the input stream.

        If bytelength is provided, it indicates the expected length of the record. Some records may require this information to parse correctly.
        """
