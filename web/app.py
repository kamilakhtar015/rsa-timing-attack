import os
import sys
import time
import random
from flask import Flask, render_template, request, jsonify

# Fix Python path to access core/ from web/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.rsa_core import generate_rsa_keypair, encrypt_message, decrypt_message

app = Flask(__name__)
app.secret_key = "rsa-attack-ui"

# Globals
public_key = None
private_key = None
timing_log = []
receiver_log = []

# --- Utility ---
def save_public_key_to_file(e, n):
    with open('../network/public_key.txt', 'w') as f:
        f.write(f"{e}\n{n}")

def load_public_key_from_file():
    with open('../network/public_key.txt', 'r') as f:
        e = int(f.readline().strip())
        n = int(f.readline().strip())
    return (e, n)

# --- Page Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receiver')
def receiver_page():
    return render_template('receiver.html')

@app.route('/sender')
def sender_page():
    return render_template('sender.html')

@app.route('/attacker')
def attacker_page():
    return render_template('attacker.html')

# --- API Routes ---
@app.route('/start-receiver', methods=['POST'])
def start_receiver():
    global public_key, private_key, receiver_log
    public_key, private_key = generate_rsa_keypair()
    save_public_key_to_file(*public_key)
    receiver_log = ["✅ Receiver started and ready to accept messages."]
    return jsonify({
        "message": "Receiver started.",
        "public_key": public_key
    })

@app.route('/receiver-logs')
def receiver_logs():
    return jsonify({"logs": receiver_log})

@app.route('/send-message', methods=['POST'])
def send_message():
    global public_key, receiver_log
    public_key = load_public_key_from_file()
    message = request.form['message']
    ciphertext = encrypt_message(message.encode(), public_key)
    decrypted = decrypt_message(ciphertext, private_key)
    receiver_log.append(f"🔐 Received Ciphertext: {str(ciphertext)[:20]}...")
    receiver_log.append(f"🔓 Decrypted Message: {decrypted.decode(errors='ignore')}")
    return jsonify({"ciphertext": str(ciphertext)})

@app.route('/run-attacker', methods=['POST'])
def run_attacker():
    global public_key, private_key, timing_log
    e, n = load_public_key_from_file()
    results = []

    for i in range(20):
        msg = random.randint(1, n - 1)
        msg_bytes = msg.to_bytes((msg.bit_length() + 7) // 8, 'big')
        ciphertext = encrypt_message(msg_bytes, (e, n))

        start = time.perf_counter()
        decrypt_message(ciphertext, (private_key[0], private_key[1]))
        end = time.perf_counter()

        results.append({
            "id": i + 1,
            "ciphertext": str(ciphertext)[:12] + "...",
            "time": round(end - start, 6)
        })

    timing_log = results
    return jsonify({"results": results})

@app.route('/analyze', methods=['POST'])
def analyze():
    return jsonify({"data": timing_log})

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
