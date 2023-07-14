import queue
import shutil
import subprocess
import time

from pyScannerWrapper.exceptions import *

from .structs import ScanResults


class BaseScanner:
    input_ip_list: list = []
    input_port_list: list = []
    scanner_args: str = ""
    input_file: str = ""
    results: ScanResults = None
    running: bool = False
    scanner_name: str = ""
    default_args: str = ""
    merged_args: str = ""
    queue = None
    scanner_process: subprocess.Popen = None

    def scan_internal(self) -> None:
        """
        This method will scan with the provided scanner.
        It shouldn't be executed by the user.
        It is up to the inheriting class to override this method.
        """
        pass

    def scan_yielder(self) -> any:
        """
        This method will start scanning and yield the results from the queue
        """
        self.scan_internal()
        while self.running:
            try:
                result = self.queue.get_nowait()
                yield result
            except queue.Empty:
                pass
            self.poll_scanner_process()
            time.sleep(0.01)

    def scan(self) -> None:
        """
        This method will start scanning and add the results
        """
        self.scan_internal()
        while self.running:
            try:
                result = self.queue.get_nowait()
                self.results.results.append(result)
            except queue.Empty:
                pass
            self.poll_scanner_process()
            time.sleep(0.01)

    def merge_args(self, additional_args: str) -> None:
        """
        This method merges additional args, user-provided args and default arguments of the inheriting class and
        sets the merged_args attribute of the class to it.
        """
        self.merged_args = f"{additional_args} {self.scanner_args} {self.default_args}"

    def scanner_parser(self) -> None:
        """
        This method will open a subprocess of the scanner in another thread and yield the parsed IP:Port
        to the caller scan() method.
        It is up to the inheriting class to override this method.
        """
        pass

    def poll_scanner_process(self) -> None:
        """
        This method is called in every iteration of scan_yielder() or scan_noyield() method, to check is the scanner still running.
        It will set running attribute to False if it isn't
        """
        if self.scanner_process.poll() != None:
            self.running = False

    def scanner_path_verify(self) -> None:
        """
        This method will check is the scanner present in PATH. If it isn't, it will throw ScannerNotFoundException.
        """
        if shutil.which(self.scanner_name) == None:
            raise ScannerNotFoundException(f"{self.scanner_name} not found in PATH")
