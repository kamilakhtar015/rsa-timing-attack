# rsa-timing-attack

# RSA Timing Attack Simulation

This project demonstrates a **timing side-channel attack** on the RSA encryption algorithm. By observing how long it takes the receiver to decrypt various ciphertexts, an attacker can infer patterns that may potentially leak information about the private key.

---

<<<<<<< HEAD
## Project Structure -- 
=======
### 📁 Project Structure
>>>>>>> my-local-changes

```text
rsa_timing_attack/
<<<<<<< HEAD

       ├── core/                  # Core RSA logic (key generation, encryption, decryption)
       
            ├── rsa_core.py
     

       ├── network/               # Network-based simulation of all actors
    
           ├── sender.py          # Sends encrypted messages to the receiver
   
           ├── receiver.py        # Decrypts messages and responds with an ACK
   
           ├── attacker.py        # Sends crafted ciphertexts and measures response time
   
           ├── public_key.txt     # Public key used by sender and attacker


       ├── logs/                  # Stores results of the timing attack
    
           ├──timing_results.txt


       ├── analyze_attack.py      # Analyzes and visualizes timing data from the attack
       
       ├── requirements.txt       # Python dependencies
       
       ├── README.md              # Project documentation (you’re reading it!)

=======
├── core/                 # Core RSA logic (key generation, encryption, decryption)
│   └── rsa_core.py
├── network/              # Network-based simulation of all actors
│   ├── sender.py         # Sends encrypted messages to the receiver
│   ├── receiver.py       # Decrypts messages and responds with an ACK
│   ├── attacker.py       # Sends crafted ciphertexts and measures response time
│   └── public_key.txt    # Public key used by sender and attacker
├── logs/                 # Stores results of the timing attack
│   └── timing_results.txt
├── analyze_attack.py     # Analyzes and visualizes timing data from the attack
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (you’re reading it!)
>>>>>>> my-local-changes


---

## 📖 How It Works

This project simulates a basic cryptographic environment involving three actors:

1. **Receiver**
   - Generates an RSA key pair
   - Starts a server that listens for incoming encrypted messages
   - Decrypts messages and returns an ACK

2. **Sender**
   - Reads the public key
   - Encrypts a plaintext message
   - Sends it to the Receiver

3. **Attacker**
   - Reads the same public key
   - Sends multiple crafted ciphertexts
   - Measures the **time taken** by the receiver to decrypt each one
   - Logs this timing information for later analysis

4. **Analyzer**
   - Reads the timing results
   - Produces statistics and a graph showing decryption time per ciphertext

---

<<<<<<< HEAD
## 🔁 Workflow Diagram

```mermaid

graph TD
    A[Receiver] -->|Generates RSA Keys| B[Public Key File]
    C[Sender] -->|Reads Public Key| B
    C -->|Sends Encrypted Message| A
    D[Attacker] -->|Reads Public Key| B
    D -->|Sends Crafted Ciphertexts| A
    D -->|Measures Response Time| E[Logs]
    F[Analyzer] -->|Reads Logs| E
    F -->|Visualizes Data| G[Graph + Stats]
=======
>>>>>>> my-local-changes


⚙️ How to Run
1. Install Requirements
Make sure you are using Python 3.9+ and have pip installed.
    pip install -r requirements.txt


2. . Run the Components
In separate terminals (or tabs):

✅ Start the Receiver (Server)
    python network/receiver.py

✅ Send a Message to Receiver
    python network/sender.py

✅ Run the Timing Attack
    python network/attacker.py

✅ Analyze and Visualize the Attack
    python analyze_attack.py
<<<<<<< HEAD

=======
>>>>>>> my-local-changes    
