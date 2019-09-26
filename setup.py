import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='opendis',
      version='1.0',
      author='Don McGregor',
      author_email='mcgredo@nps.edu',
      description='implementation of DIS, IEEE-1278.1',
      url='https://github.com/open-dis/open-dis-python',
      license='BSD',
      keywords = "dis distributed interactive simulation",
      packages=['opendis'],
      long_description=read('README.md'),
      install_requires=['numpy'],
      classifiers=[
         "Development Status :: 3 - Alpha",
         "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
         "License :: OSI Approved :: BSD License"
         ],
      zip_safe=False)
