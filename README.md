## open-dis-python

A Python implementation of the Distributed Interactive Simulation (DIS) standard.

## Installation

For installation instructions and how to run the provided simple example,
refer to the python [README](src/main/python/README.md).

### Git Submodules

This uses a git submodule to hold a XML description of they protocol messages. If
you regenerate the source code (you probably shouldn't) make sure the submodule
is loaded with

```
$ git submodule init
$ git submodule update
```
