# Slowloris Denial-of-Service Attack

## 1. Objective

This attack demonstrates a **Slowloris Denial-of-Service (DoS)** attack targeting an
HTTP service used as a **simulation of an ICS web interface / HMI**.

The objective is to show how an attacker can exhaust server resources by maintaining
a large number of **incomplete HTTP connections**, leading to severe service degradation
or denial of service.

This is a **controlled simulation for academic purposes only**.

---

## 2. Attack Principle

Slowloris exploits the fact that many HTTP servers allocate a thread or socket
for each incoming connection.

Instead of sending full HTTP requests, the attacker:
- Opens a large number of TCP connections
- Sends **incomplete HTTP headers**
- Periodically sends small header fragments to keep connections alive

As a result:
- Server sockets remain occupied
- Legitimate clients experience long delays or complete service unavailability

---

## 3. Target Description

- **Target service**: Local HTTP server (ICS / HMI simulation)
- **Protocol**: HTTP over TCP
- **Port**: 8080
- **Environment**: Local host (127.0.0.1)

The server is first tested under **normal conditions** to establish a baseline.

---

## 4. Attack Script Overview

The provided Python script performs the attack in three phases:

### Phase 1 – Connection Flood
- Opens hundreds to thousands of TCP connections
- Sends partial HTTP headers (`GET / HTTP/1.1`, `Host:`)

### Phase 2 – Connection Maintenance
- Periodically sends fake header lines
- Prevents the server from closing connections

### Phase 3 – Cleanup
- Closes all sockets after the attack duration

The attack intensity is controlled by the `NUM_SOCKETS` parameter.

---


## 5. How to Run the Attack

### Step 1 – Start the HTTP Server

Start a local HTTP server on port 8080.
This server represents an ICS web interface / HMI.

```bash
python -m http.server 8080
```
### Step 2 – Launch the Attack

```bash
python slowloris.py
```
