from pyScannerWrapper.core import BaseScanner


class Masscan(BaseScanner):
    scanner_name = "masscan"

    def __init__(self):
        self.scanner_path_verify()

    def scan(self) -> None:
        pass
