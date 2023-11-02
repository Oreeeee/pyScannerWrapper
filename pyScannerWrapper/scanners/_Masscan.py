import queue
import subprocess
import threading
import time

from scanf import scanf

from pyScannerWrapper.core import BaseScanner
from pyScannerWrapper.structs import ScanResults, ServerResult


class Masscan(BaseScanner):
    scanner_name = "masscan"
    queue = queue.Queue()

    def __init__(self):
        self.scanner_path_verify()

    def scan_internal(self) -> None:
        # Initialize results
        self.results = ScanResults(
            scanner_name=self.scanner_name,
            results=[],
        )

        # Add input file
        if self.input_file != "":
            self.scanner_args = f"{self.scanner_args} -iL {input_file}"

        # Ports
        mass_ports: str = ",".join(self.input_port_list)
        self.scanner_args = f"{self.scanner_args} -p{mass_ports}"

        # IP List
        if self.input_ip_list != []:
            mass_ips: str = " ".join(self.input_ip_list)
            self.scanner_args = f"{self.scanner_args} {mass_ips}"

        # Make running attribute True
        self.running = True

        # Start masscan
        # We only care about stdout in here, that's where masscan shows the hits
        # stderr and stdin can be /dev/null
        self.scanner_process = subprocess.Popen(
            self.make_command(),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )

        # Start the parsing thread
        threading.Thread(target=self.scanner_parser).start()

    def scanner_parser(self) -> None:
        while self.running:
            for line in iter(self.scanner_process.stdout.readline, b""):
                line = line.decode("UTF-8").strip()
                parsed_line: tuple = scanf("Discovered open port %s on %s", s=line)

                ip: str = parsed_line[1]
                port: int = int(parsed_line[0].replace("/tcp", ""))

                self.queue.put(ServerResult(ip=ip, port=int(port)))
