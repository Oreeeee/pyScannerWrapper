from pyScannerWrapper.exceptions import *
from .structs import ScanResults
import shutil


class BaseScanner:
    # Public variables
    input_ip_list: list
    input_port_list: list
    scanner_args: str
    input_file: str
    results: ScanResults = None
    running: bool = False
    yield_results: bool = False

    # Private variables
    __scanner_name: str
    __default_args: str

    # Public methods
    def scan(self) -> None:
        """
        This method will scan with the provided scanner.
        It doesn't return anything, and will instead set the results property of the class.
        If yielding is enabled, it will in addition yield the IP:Port of the server if a online target is found.
        It is up to the inheriting class to override this method.
        """
        pass
    
    # Private methods
    def scanner_path_verify(self) -> None:
        """
        This method will check is the scanner present in PATH. If it isn't, it will throw ScannerNotFoundException.
        """
        if shutil.which(self.__scanner_name) == None:
            raise ScannerNotFoundException(f"{self.__scanner_name} not found in PATH")
