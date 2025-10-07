"""Base classes for all Record types."""

__all__ = ["Record", "StandardVariableRecord", "VariableRecord"]

from abc import abstractmethod
from typing import Any, Protocol, TypeGuard, runtime_checkable

from opendis.stream import DataInputStream, DataOutputStream
from opendis.types import enum32


@runtime_checkable
class Record(Protocol):
    """Base class for all Record types with fixed sizes."""

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
    """Base class for all Record types with variable sizes."""

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
              bytelength: int) -> None:
        """Parse the record from the input stream.

        If bytelength is provided, it indicates the expected length of the record. Some records may require this information to parse correctly.
        """
        if not self.is_positive_int(bytelength):
            raise ValueError(
                f"bytelength must be a non-negative integer, got {bytelength!r}"
            )
        # TODO: Implement padding handling


@runtime_checkable
class StandardVariableRecord(VariableRecord):
    """6.2.83 Standard Variable (SV) Record

    This base class defines the interface for DIS records with variable sizes.
    First SV record of a Standard Variable Specification record shall start on
    a 64-bit boundary.
    Padding shall be explicitly included in each record as necessary to make
    the record length a multiple of 8 octets (64 bits) so that the following
    record is automatically aligned. The record length requirement may be
    achieved by placing padding fields anywhere in the SV record as deemed appropriate, not necessarily at the end of the record.
    """
    recordType: enum32  # [UID 66]

    @staticmethod
    def is_positive_int(value: Any) -> TypeGuard[int]:
        """Check if a value is a positive integer."""
        return isinstance(value, int) and value >= 0

    @property
    def recordLength(self) -> int:
        return self.marshalledSize()

    @abstractmethod
    def serialize(self, outputStream: DataOutputStream) -> None:
        """Serialize the record to the output stream."""
        super().serialize(outputStream)
        outputStream.write_uint32(self.recordType)
        outputStream.write_uint32(self.recordLength)

    @abstractmethod
    def parse(self,
              inputStream: DataInputStream,
              bytelength: int) -> None:
        """Parse the record from the input stream.

        If bytelength is provided, it indicates the expected length of the record. Some records may require this information to parse correctly.
        Assume that recordType and recordLength have already been read from the
        stream.
        recordLength will usually be passed to this method to assist in parsing.
        """
        # Validate bytelength
        super().parse(inputStream, bytelength)
        if not bytelength % 8 == 0:
            raise ValueError(
                f"bytelength must be a multiple of 8, got {bytelength!r}"
            )
        # TODO: Implement padding handling
