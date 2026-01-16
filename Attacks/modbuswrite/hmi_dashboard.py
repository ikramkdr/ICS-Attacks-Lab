from flask import Flask, render_template
from pyModbusTCP.client import ModbusClient
import time
import threading

"""
Industrial HMI Simulation - Modbus TCP
-------------------------------------
This Flask-based dashboard simulates an industrial HMI.
It continuously reads Modbus registers from a PLC and
displays system status, alarms, and actuator states.

"""


app = Flask(__name__)

modbus_client = ModbusClient(host="192.168.1.137", port=502, auto_open=True, auto_close=True)

dashboard_data = {
    "temperature": 40,
    "valve_status": "OPEN",
    "weather": "UNKNOWN", # FIXED: Added weather here
    "status_message": "System Normal",
    "css_class": "normal"
}

def read_modbus_registers():
    while True:
        try:
            # FIXED: Read 3 registers instead of 2 to get the Weather (Reg 2)
            regs = modbus_client.read_holding_registers(0, 3) 
            
            if regs:
                dashboard_data["temperature"] = regs[0]
                dashboard_data["valve_status"] = "OPEN" if regs[1] == 1 else "CLOSED"
                
                # FIXED: Accessing the 3rd register (index 2)
                dashboard_data["weather"] = "It is Cold , dont forget your coat" if regs[2] == 1 else "SUNNY"

                # Logic for alerts
                if dashboard_data["temperature"] > 100 or (dashboard_data["valve_status"] == "CLOSED" and dashboard_data["temperature"] > 45):
                    dashboard_data["status_message"] = "CRITICAL: SYSTEM COMPROMISED!"
                    dashboard_data["css_class"] = "critical"
                elif dashboard_data["temperature"] > 40: # Adjusted for your 49°C test
                    dashboard_data["status_message"] = "WARNING: Logic Inconsistency Detected"
                    dashboard_data["css_class"] = "warning"
                else:
                    dashboard_data["status_message"] = "System Normal"
                    dashboard_data["css_class"] = "normal"
            else:
                dashboard_data["status_message"] = "Modbus PLC Offline"
                dashboard_data["css_class"] = "offline"

        except Exception as e:
            print(f"Modbus Read Error: {e}")
            dashboard_data["status_message"] = "Connection Error"
            dashboard_data["css_class"] = "offline"
            
        time.sleep(1)

modbus_thread = threading.Thread(target=read_modbus_registers)
modbus_thread.daemon = True
modbus_thread.start()

@app.route('/')
def index():
    return render_template('index.html', data=dashboard_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)