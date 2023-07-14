from distutils.core import setup

from pyScannerWrapper import __version__ as ver

setup(
    name="pyScannerWrapper",
    version=ver,
    description="Easy-to-use Python wrapper for various port scanners. (WIP)",
    author="Oreeeee",
    packages=[
        "pyScannerWrapper",
        "pyScannerWrapper.core",
        "pyScannerWrapper.core.structs",
        "pyScannerWrapper.exceptions",
        "pyScannerWrapper.scanners",
    ],
)
