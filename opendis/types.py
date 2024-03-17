"""types.py

This module contains type aliases to document the size of attributes required/
used by classes in dis7.py and elsewhere. It should not import other modules in
the opendis package.

Note: if imported directly, this may shadow the `types` built-in Python module,
which is rarely used.
"""

# Type aliases (for readability)
enum8 = int
enum16 = int
enum32 = int
int8 = int
int16 = int
int32 = int
int64 = int
uint8 = int
uint16 = int
uint32 = int
uint64 = int
float32 = float
float64 = float
struct8 = bytes
struct16 = bytes
struct32 = bytes
char8 = str
char16 = str
