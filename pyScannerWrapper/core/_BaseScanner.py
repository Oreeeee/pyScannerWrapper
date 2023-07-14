from .structs import ScanResults


class BaseScanner:
    # Public variables
    input_ip_list: list
    input_port_list: list
    scanner_args: str
    input_file: str
    results: ScanResults = None
    running: bool = False

    # Private variables
    __scanner_name: str
    __default_args: str
    __should_yield: bool

    # Public methods
    def __init__(self):
        pass

    def scan(self) -> None:
        """
        This method will scan with the provided scanner.
        It doesn't return anything, and will instead set the results property of the class.
        If yielding is enabled, it will in addition yield the IP:Port of the server if a online target is found.
        It is up to the inheriting class to override this method.
        """
        pass

    def scan_yielder(self) -> None:
        pass
