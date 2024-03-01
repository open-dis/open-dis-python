import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='opendis',
    version='1.0',
    author='Don McGregor',
    author_email='mcgredo@nps.edu',
    description='implementation of DIS, IEEE-1278.1',
    url='https://github.com/open-dis/open-dis-python',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator"
     ],
)
