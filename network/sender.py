# network/sender.py

import socket
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.rsa_core import encrypt_message

# -------------------------------
# Configuration
# -------------------------------
HOST = '127.0.0.1'
PORT = 5001
BUFFER_SIZE = 4096
# PUBLIC_KEY_FILE = 'network/public_key.txt'
PUBLIC_KEY_FILE = os.path.join(os.path.dirname(__file__), 'public_key.txt')


# -------------------------------
# Load Public Key from File
# -------------------------------
def load_public_key_from_file(filename=PUBLIC_KEY_FILE):
    with open(filename, 'r') as f:
        e = int(f.readline().strip())
        n = int(f.readline().strip())
    return (e, n)

# -------------------------------
# Send Encrypted Message
# -------------------------------
def send_message(message: str):
    public_key = load_public_key_from_file()
    m_bytes = message.encode()
    ciphertext = encrypt_message(m_bytes, public_key)
    ciphertext_bytes = ciphertext.to_bytes((ciphertext.bit_length() + 7) // 8, byteorder='big')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[Sender] Connected to Receiver at {HOST}:{PORT}")

        s.sendall(ciphertext_bytes)
        print(f"[Sender] Sent encrypted message.")

        ack = s.recv(BUFFER_SIZE)
        if ack == b'ACK':
            print("[Sender] Received ACK from Receiver.\n")
        else:
            print("[Sender] No ACK received.")

# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    test_message = "Hello, Receiver! - This is my first message and lets try our connection"
    send_message(test_message)
