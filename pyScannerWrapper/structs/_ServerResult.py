from dataclasses import dataclass


@dataclass
class ServerResult:
    ip: str
    port: int
    status: str
    time_discovered: str
