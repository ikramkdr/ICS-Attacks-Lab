# Modbus TCP Write Injection Attack

## Overview
This experiment demonstrates a Modbus TCP write injection attack targeting a simulated PLC.
The goal is to force an actuator to change state by writing unauthorized values into Modbus registers.

---

## Hardware Setup
- ESP32: acting as a low-cost PLC
- DHT11: temperature sensor
- Built-in LED (GPIO D2): actuator (cooling system)

---

## Software Requirements

### On the PLC
- Arduino IDE
- Modbus TCP library for ESP32
- DHT11 sensor library

### On the Attacker Machine
- Python 3
- pyModbusTCP

Install Python dependencies:
```bash
pip install pyModbusTCP
