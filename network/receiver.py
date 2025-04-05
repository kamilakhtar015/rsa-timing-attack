# network/receiver.py

import socket
import threading
import os
import sys


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.insert(0, PROJECT_ROOT)

from core.rsa_core import generate_rsa_keypair, decrypt_message

# -------------------------------
# Configuration
# -------------------------------
HOST = '127.0.0.1'
PORT = 5001
BUFFER_SIZE = 4096
PUBLIC_KEY_FILE = os.path.join(CURRENT_DIR, 'public_key.txt')  # Saves next to receiver.py

# -------------------------------
# Save Public Key to File
# -------------------------------
def save_public_key_to_file(public_key, filename=PUBLIC_KEY_FILE):
    e, n = public_key
    with open(filename, 'w') as f:
        f.write(f"{e}\n{n}")
    print(f"[Receiver] Public key saved to {filename}")

# -------------------------------
# Handle Client Connection
# -------------------------------
def handle_client(conn, addr, private_key):
    print(f"[Receiver] Connected with {addr}")
    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break

            ciphertext = int.from_bytes(data, byteorder='big')
            print(f"[Receiver] Received ciphertext: {ciphertext}")

            plaintext = decrypt_message(ciphertext, private_key)
            print(f"[Receiver] Decrypted message: {plaintext.decode(errors='ignore')}")

            conn.sendall(b'ACK')
            print(f"[Receiver] Sent ACK\n")

    except Exception as e:
        print(f"[Receiver] Error: {e}")
    finally:
        conn.close()
        print(f"[Receiver] Connection with {addr} closed.")

# -------------------------------
# Start Socket Server
# -------------------------------
def start_server():
    public_key, private_key = generate_rsa_keypair()
    print(f"[Receiver] Public Key (e, n): {public_key}")
    save_public_key_to_file(public_key)

    print(f"[Receiver] Starting server on {HOST}:{PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[Receiver] Waiting for connections...")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, private_key))
            thread.start()

# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    start_server()
