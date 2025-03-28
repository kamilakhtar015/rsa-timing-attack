# network/attacker.py

import os
import sys
import socket
import time
import random
from core.rsa_core import encrypt_message

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# -------------------------------
# Configuration
# -------------------------------
HOST = '127.0.0.1'
PORT = 5001
BUFFER_SIZE = 4096
PUBLIC_KEY_FILE = os.path.join(os.path.dirname(__file__), 'public_key.txt')
NUM_TESTS = 50
LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
LOG_FILE = os.path.join(LOGS_DIR, 'timing_results.txt')

# -------------------------------
# Load Public Key
# -------------------------------
def load_public_key():
    with open(PUBLIC_KEY_FILE, 'r') as f:
        e = int(f.readline().strip())
        n = int(f.readline().strip())
    return (e, n)

# -------------------------------
# Measure Response Time
# -------------------------------
def measure_decryption_time(ciphertext: int):
    ciphertext_bytes = ciphertext.to_bytes((ciphertext.bit_length() + 7) // 8, byteorder='big')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        start = time.perf_counter()
        s.sendall(ciphertext_bytes)
        ack = s.recv(BUFFER_SIZE)
        end = time.perf_counter()

    if ack == b'ACK':
        return end - start
    return None

# -------------------------------
# Run the Attack
# -------------------------------
def run_attack():
    os.makedirs(LOGS_DIR, exist_ok=True)
    public_key = load_public_key()
    e, n = public_key
    results = []

    print(f"[Attacker] Sending {NUM_TESTS} crafted ciphertexts to measure response time...\n")

    for i in range(NUM_TESTS):
        random_msg = random.randint(1, n - 1)
        m_bytes = random_msg.to_bytes((random_msg.bit_length() + 7) // 8, byteorder='big')
        ciphertext = encrypt_message(m_bytes, public_key)

        response_time = measure_decryption_time(ciphertext)

        if response_time is not None:
            results.append((ciphertext, response_time))
            print(f"[Attacker] #{i+1:02} | Time: {response_time*1000:.3f} ms")

    # Save full results to log file
    with open(LOG_FILE, 'w') as f:
        for ct, rt in results:
            f.write(f"{ct},{rt}\n")

    # Print top 5 slowest responses
    results.sort(key=lambda x: x[1], reverse=True)
    print("\n🔍 Top 5 Slowest Decryptions:")
    for i, (ct, rt) in enumerate(results[:5]):
        print(f"#{i+1} | Time: {rt*1000:.3f} ms | Ciphertext Head: {str(ct)[:10]}...")

    print(f"\n✅ Timing results saved to: {LOG_FILE}")

# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    run_attack()
