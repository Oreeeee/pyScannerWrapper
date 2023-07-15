from distutils.core import setup
from pathlib import Path

from pyScannerWrapper import __version__ as ver

# Load README from README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyScannerWrapper",
    version=ver,
    description="Easy-to-use Python wrapper for various port scanners.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Oreeeee",
    license="MIT",
    url="https://github.com/Oreeeee/pyScannerWrapper",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=[
        "pyScannerWrapper",
        "pyScannerWrapper.core",
        "pyScannerWrapper.structs",
        "pyScannerWrapper.exceptions",
        "pyScannerWrapper.scanners",
    ],
)
