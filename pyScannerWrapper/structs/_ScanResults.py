from dataclasses import dataclass


@dataclass
class ScanResults:
    scanner_name: str
    results: list
