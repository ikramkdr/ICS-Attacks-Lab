# Attacks in an Industrial Control System (ICS)

## Authors
- KADRI Ikram
- HOUACINE Yousra

## Academic Context
This project was developed as part of a university course on Network / Industrial Control System Security.
All activities were carried out strictly for educational purposes.

## Project Description
This project presents an experimental analysis of cyber attacks targeting Industrial Control Systems (ICS).
The objective is to study how network-based attacks impact availability, integrity, and operator visibility
in industrial environments.

Due to the critical nature of real ICS infrastructures, all experiments were conducted on simulated systems
within a controlled local laboratory environment.

## Simulation Disclaimer
⚠️ **Important Notice**  
This project does **NOT** target real industrial infrastructures.
All PLCs, HMIs, and services used in this work are simulated or low-cost educational devices
(ESP32, local web servers) deployed on a local network only.

## Implemented Attacks
- Slowloris Attack (HTTP Denial of Service)
- Modbus TCP Write Injection
- Modbus TCP Read 
- Replay Attack 

## Experimental Environment
- Operating System: Windows 10
- Network: Local network / localhost
- Protocols: HTTP, Modbus TCP (port 502)
- Tools: Python, Flask, pyModbusTCP, Arduino IDE, Wireshark
## Installation

### Python Dependencies
Install all required Python libraries using:

```bash
pip install -r requirements.txt

```


