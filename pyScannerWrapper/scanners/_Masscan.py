import queue
import subprocess
import threading
import time

from pyScannerWrapper.core import BaseScanner
from pyScannerWrapper.core.structs import ScanResults, ServerResult


class Masscan(BaseScanner):
    scanner_name = "masscan"
    queue = queue.Queue()

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

        self.merge_args("")

        # Make running attribute True
        self.running = True

        # Start masscan
        # We only care about stdout in here, that's where masscan shows the hits
        # stderr and stdin can be /dev/null
        proc = subprocess.Popen(
            f"{self.scanner_name} {self.merged_args}".split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
        )

        # Start the parsing thread
        threading.Thread(target=self.scanner_parser, args=(proc,)).start()

        while self.running:
            # Poll the results
            try:
                result = self.queue.get_nowait()
                self.results.results.append(result)
            except queue.Empty:
                pass

            # Check is masscan dead
            if proc.poll() != None:
                # Stop running
                self.running = False

            time.sleep(0.5)  # Sleep to not use the CPU 100%

    def scanner_parser(self, proc: subprocess.Popen) -> None:
        while self.running:
            for line in iter(proc.stdout.readline, b""):
                line = line.decode("UTF-8").strip()

                ip: str = ""
                port: str = ""

                # Get the IP
                ip = line[::-1]  # Reverse the line
                ip = ip[: ip.find(" ")]  # Remove everything after first space
                ip = ip[::-1]  # Reverse the string

                # Get the port
                port = line.replace(
                    "Discovered open port ", ""
                )  # Remove open port prefix
                port = port[: port.find("/")]  # Remove everything after the slash

                # Assign a ServerResult value
                result = ServerResult(
                    ip=ip, port=int(port), status="open", time_discovered=None
                )

                # Add these values to queue
                self.queue.put(result)
