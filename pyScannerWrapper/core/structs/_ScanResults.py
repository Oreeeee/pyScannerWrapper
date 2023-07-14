from dataclasses import dataclass


@dataclass
class ScanResults:
    scanner_name: str
    start_time: str
    end_time: str
    time_took: int
    args: str
    results: list
