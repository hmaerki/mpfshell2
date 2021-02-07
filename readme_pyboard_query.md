# Query for the required board

One could specify in a configuration file which micropython board connects to which com port.

This modules allows find the required com port for example based on the expected hardware. Hence a configuration file is not required.

In the following example, we expect, that a `scanner_pyb_2020` and a `compact_2020` are connected:

```python
scanner = ConnectPyboard('scanner_pyb_2020')
compact = ConnectPyboard('compact_2012')
```

## Query micropython boards

The query uses three stages
* Query windows COM ports
* Connect to com port using mpfshell
* Read `config_identification.py` on the micropython boards flash.

To query, derive `BoardQueryBase` and overwrite the `select_*` methods.

There query will print all available boards

```python
BoardQueryBase.print_all(f=sys.stdout)
```

Sample output
```text
*** Board Query: Micropython boards found:
    Board Query COM8
      pyserial.description: USB Serial Device (COM8)
      pyserial.hwid: USB VID:PID=F055:9800 SER=2078379C304E LOCATION=1-2.1:x.1
      mpfshell.micropython_sysname: pyboard
      mpfshell.micropython_release: 1.10.0
      mpfshell.micropython_machine: PYBv1.1 with STM32F405RG
      config_identification.py.FILENAME: config_identification.py
      config_identification.py.FILECONTENT:
           #
           # Copy this file onto the pyboards flash of the pyboard and rename it to 'config_serial.py'
           #
           HWTYPE = 'scanner_pyb_2020' # or 'compact_2012', ...
           HWVERSION = '20201120'
           HWSERIAL = '20201120_01'
      config_identification.py.HWTYPE: scanner_pyb_2020
      config_identification.py.HWVERSION: 20201120
      config_identification.py.HWSERIAL: 20201120_01
    Board Query COM9
      pyserial.description: USB Serial Device (COM9)
      pyserial.hwid: USB VID:PID=F055:9800 SER=376439873535 LOCATION=1-1.2:x.1
      mpfshell-error: Failed to open "COM9"
      config_identification.py.FILENAME: config_identification.py
      config_identification.py.READ_ERROR: Failed to open "COM9"
    Board Query COM10
      pyserial.description: Silicon Labs CP210x USB to UART Bridge (COM10)
      pyserial.hwid: USB VID:PID=10C4:EA60 SER=9072266AC599E8118237B558C3E5CFBD LOCATION=1-3:x.1
      mpfshell.micropython_sysname: esp32
      mpfshell.micropython_release: 1.10.0
      mpfshell.micropython_machine: ESP32 module with ESP32
      config_identification.py.FILENAME: config_identification.py
      config_identification.py.READ_ERROR: Failed to read file: config_identification.py
```

You may query com-ports using `pyserial`
```bash
python -m serial.tools.list_ports -v
```

Example output
```text
COM3
    desc: Standard Serial over Bluetooth link (COM3)
    hwid: BTHENUM\{00001101-0000-1000-8000-00805F9B34FB}_LOCALMFG&0000\8&6CFA44B&1&000000000000_00000002
COM8   <== A pyboard
    desc: USB Serial Device (COM8)
    hwid: USB VID:PID=F055:9800 SER=2078379C304E LOCATION=1-2.1:x.1
COM10  <== A espressif esp32 development board
    desc: Silicon Labs CP210x USB to UART Bridge (COM10)
    hwid: USB VID:PID=10C4:EA60 SER=9072266AC599E8118237B558C3E5CFBD LOCATION=1-3:x.1
```

## Query and connect a micropython boards

There are three predefined queries.

Connect to `COM8`:
```python
board = ConnectComport('COM8')
```

Connect to the first `scanner_pyb_2020`:
```python
board = ConnectPyboard('scanner_pyb_2020')
```

Connect to multiple boards - slow and fast:
```python
import pyboard_query
# Slow
scanner = ConnectPyboard('scanner_pyb_2020')
compact = ConnectPyboard('compact_2012')

# Fast
scanner = pyboard_query.BoardQueryPyboard('scanner_pyb_2020')
compact = pyboard_query.BoardQueryPyboard('compact_2012')
pyboard_query.Connect([compact, scanner])
scanner.board  <== The query result
compact.board  <== The query result
```

## Return class: `Board`

* property `port`: The pyserial port object
* property `mpfshell`: The connected mpfshell. If `isinstance(mpfshell, str)`, this is the error message while connecting.
* property `identification`: See `Identification`

## Return class: `Identification`

This class corresponds to `config_identification.py` on the micropython boards flash.

Example `config_identification.py`:
```python
#
# Copy this file onto the pyboards flash of the pyboard and rename it to 'config_identification.py'
#

# The type of hardware connected to this pyboard
HWTYPE = 'scanner_pyb_2020' # or 'compact_2012', ...

# The hardware version as printed on the schematics
HWVERSION = '20201120'

# The serial number of this hardware
HWSERIAL = '20201120_01'
```

Properties of the class `Identification`:

* property `READ_ERROR`: The error message if not `None`.
* property `FILECONTENT`: The contents as above.
* property `HWTYPE`: `scanner_pyb_2020` in above example.
* property `HWVERSION`: `20201120` in above example.
* property `HWSERIAL`: `20201120_01` in above example.

Method of class `Identification`:

```python
print(self, f=sys.stdout)
```

This will print for example

```text
Board Query COM8
  pyserial.description: USB Serial Device (COM8)
  pyserial.hwid: USB VID:PID=F055:9800 SER=2078379C304E LOCATION=1-2.1:x.1
    mpfshell.micropython_sysname: pyboard
    mpfshell.micropython_release: 1.10.0
    mpfshell.micropython_machine: PYBv1.1 with STM32F405RG
  config_identification.py.FILENAME: config_identification.py
  config_identification.py.FILECONTENT:
       #
       # Copy this file onto the pyboards flash of the pyboard and rename it to 'config_serial.py'
       #
       HWTYPE = 'scanner_pyb_2020' # or 'compact_2012', ...
       HWVERSION = '20201120'
       HWSERIAL = '20201120_01'
  config_identification.py.HWTYPE: scanner_pyb_2020
  config_identification.py.HWVERSION: 20201120
  config_identification.py.HWSERIAL: 20201120_01
```
