import subprocess
import threading

from pyScannerWrapper.core import BaseScanner
from pyScannerWrapper.core.structs import ScanResults


class Masscan(BaseScanner):
    scanner_name = "masscan"

    def __init__(self):
        self.scanner_path_verify()

    def scan(self) -> None:
        # Initialize results
        self.results = ScanResults(
            scanner_name=self.scanner_name,
            start_time=None,
            end_time=None,
            time_took=None,
            args="",
            results=[],
        )
