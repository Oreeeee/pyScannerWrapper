# pyScannerWrapper -- WORK IN PROGRESS --
Easy-to-use Python wrapper for various port scanners. (WIP)

# Supported scanners
- Masscan

# Planned scanners planned to be added
- Nmap
- RustScan

# Usage
## masscan
```python
from pyScannerWrapper.scanners import Masscan
from pyScannerWrapper.structs import *

# Initialize masscan object
mas = Masscan()

# Change some properties
mas.input_ip_list = ["192.168.0.0/16", "10.0.0.0/8"]
mas.input_port_list = ["22", "80", "443", "8080"]
mas.args = "--rate 10000"
mas.sudo = True # Required on Unix systems

# Normal example
mas.scan()
print(mas.output)

# Yielding example
results = mas.scan_yielder()
for result in results:
    print(result)
```
