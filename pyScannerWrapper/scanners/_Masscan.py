from pyScannerWrapper.core import BaseScanner


class Masscan(BaseScanner):
    __scanner_name = "masscan"

    def __init__(self):
        self.__scanner_path_verify()

    def scan(self) -> None:
        pass
