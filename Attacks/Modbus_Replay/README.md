# Modbus TCP Replay Attack

This attack demonstrates a replay vulnerability in the Modbus TCP protocol.

A previously captured legitimate Modbus Write command is replayed and
accepted again by the PLC, showing the absence of replay protection.

- Protocol: Modbus TCP
- Function Code: 06 (Write Single Register)
- Security Impact: Integrity and Safety violation
