# Modbus Write Attack – Register Manipulation

## 1. Objective

This attack demonstrates a **Modbus Write vulnerability** in an ICS/SCADA‑like environment.
The goal is to show how an attacker can **manipulate Modbus registers** to alter the
behavior of a PLC without authentication.


---

## 2. System Description

The simulated system is composed of:

- **PLC**: ESP8266 acting as a Modbus TCP server  
- **Sensor**: DHT11 temperature sensor connected to **pin D2**
- **HMI**: Python-based dashboard displaying system values
- **Attacker**: Python script performing Modbus Write operations

### PLC Logic 

- Holding Register 0 → Temperature value
- Holding Register 1 → Actuator state (e.g., air conditioning / LED)
- If `Register 0 > 29`, the PLC activates the actuator


---

## 3. Attack Description

The attacker exploits the Modbus protocol by **writing a forged temperature value**
directly into the PLC holding register.

Instead of modifying the physical sensor, the attacker sends a Modbus Write command:
- Writing a high value (e.g., `49`) into **Holding Register 0**

As a result:
- The PLC believes the temperature is critical
- The actuator is activated even if the real temperature is normal

This represents a **false data injection attack** on an ICS.

---

## 4. Prerequisites

### Hardware
- ESP8266
- DHT11 sensor connected to **pin D2**
- Wi‑Fi network

### Software
- Python 3.x
- Required Python libraries (see `requirements.txt`)
- Arduino IDE (to flash the ESP8266)

---

## 5. How to Run the Attack

### Step 1 – Start the PLC (ESP8266)

1. Flash the Arduino code to the ESP8266
2. Ensure:
   - DHT11 is connected to **D2**
   - ESP8266 is connected to your Wi‑Fi network
3. Open the serial monitor and note the **PLC IP address**

The ESP8266 now acts as a **Modbus TCP server**

---

### Step 2 – Launch the HMI

run:

```bash
python hmi_dashboard.py
```
### This dashboard:

1. Displays temperature values
2. Displays actuator state
3. Communicates with the PLC via Modbus TCP

---

### Step 3 – Launch the Modbus Write Attack

From the attack directory, run:

```bash
python modbuswrite.py
```
### This script:

1. Connects to the PLC
2. Writes a forged value into Holding Register 0
3. Triggers the PLC control logic
