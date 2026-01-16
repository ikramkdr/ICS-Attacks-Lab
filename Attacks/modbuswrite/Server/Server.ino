#include <ESP8266WiFi.h>
#include <ModbusIP_ESP8266.h>
#include "DHT.h"

/*
 * Vulnerable PLC Simulation - Modbus TCP
 * -------------------------------------
 * This code simulates an industrial PLC using an ESP8266.
 * It exposes Modbus holding registers without authentication
 * and demonstrates how a Modbus write injection attack can
 * manipulate control logic.
 *
 * Educational purpose only.
 */

// --- Hardware Configuration ---
#define DHTPIN 4        // D2 pin
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// --- WiFi Configuration ---
const char* ssid = "";
const char* password = "";

// --- Modbus Server ---
ModbusIP mb;

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Built-in LED used as actuator (cooling system)
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH); // OFF

  // Connect to WiFi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nPLC CONNECTED");
  Serial.println(WiFi.localIP());

  // Start Modbus TCP server
  mb.server();

  // Modbus Holding Registers
  mb.addHreg(0, 0); // Register 0: Temperature value
  mb.addHreg(1, 0); // Register 1: Actuator state (0=OFF, 1=ON)
}

void loop() {
  // Handle Modbus communication
  mb.task();

  static uint32_t lastRead = 0;
  if (millis() - lastRead > 2000) {
    lastRead = millis();

    float t = dht.readTemperature();

    // --- SENSOR UPDATE CONDITION ---
    // The register is updated with real sensor data
    // ONLY if it has not been overwritten by an attack (>40)
    if (mb.Hreg(0) < 40) {
      if (!isnan(t)) {
        mb.Hreg(0, (int)t);
      }
    }

    // --- VULNERABLE CONTROL LOGIC ---
    // The PLC decision is based on Register 0.
    // If an attacker writes 49 into Reg 0, the PLC
    // will falsely detect an over-temperature condition.
    if (mb.Hreg(0) > 29) {
      mb.Hreg(1, 1); // Actuator ON
      Serial.println("PLC Logic: Temperature > 29 detected in register. Cooling activated.");
    } else {
      mb.Hreg(1, 0); // Actuator OFF
    }
  }

  // Physical actuator action
  digitalWrite(LED_BUILTIN, (mb.Hreg(1) == 1) ? LOW : HIGH);
}
