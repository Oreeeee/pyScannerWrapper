class BaseScanner:
    # Public
    input_ip_list: list
    input_port_list: list
    scanner_args: str
    input_file: str
    results: dict = {}
    running: bool = False

    # Private
    __scanner_name: str
    __default_args: str
    __should_yield: bool

    def __init__(self):
        pass

    def scan(self) -> None:
        pass

    def scan_yielder(self) -> None:
        pass
