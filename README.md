# RSA Timing Attack Simulation

This project demonstrates a **timing side-channel attack** against RSA encryption.  
By measuring decryption times of crafted ciphertexts, an attacker can infer bits of the private key.

It includes a **web-based simulation** for visualizing sender, receiver, and attacker behavior.

---

## Project Structure

```
rsa-timing-attack/
├── core/                  # Core RSA functionality (keygen, encrypt, decrypt)
│   └── rsa_core.py
├── network/               # Socket-based communication modules
│   ├── sender.py          # Sends encrypted messages
│   ├── receiver.py        # Receives and decrypts messages
│   ├── attacker.py        # Launches timing attacks
│   └── public_key.txt     # Public key for sender/attacker
├── web/                   # Web interface for simulation
│   ├── app.py             # Flask app
│   ├── templates/         # HTML pages
│   │   ├── index.html
│   │   ├── sender.html
|   |   |── attacker.html
│   │   └── receiver.html
│   └── static/            # CSS and JavaScript
│       ├── style.css
├── logs/                  # Timing attack logs
│   └── timing_results.txt
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/pallasite99/rsa-timing-attack.git
cd rsa-timing-attack
```

### 2. (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

### Option 1: Command-Line Simulation

1. **Start the receiver**:

    ```bash
    python network/receiver.py
    ```

2. **Start the sender** (in a new terminal):

    ```bash
    python network/sender.py
    ```

3. **Start the attacker** (in another terminal):

    ```bash
    python network/attacker.py
    ```

4. **Analyze timing data**:

    ```bash
    python analyze_attack.py
    ```

---

### Option 2: Web-Based Simulation (Flask)

1. **Navigate to the `web/` directory**:

    ```bash
    cd web
    ```

2. **Run the Flask server**:

    ```bash
    python app.py
    ```

3. **Open your browser** and go to:

    ```
    http://localhost:5000
    ```

    You will find pages to simulate:
    - Sender
    - Receiver
    - Attacker
    - Real-time timing visualizations

---

## Features

| Feature | Description |
|:--------|:------------|
| **Core RSA** | Key generation, encryption, and decryption |
| **Sender** | Encrypts and sends random messages |
| **Receiver** | Decrypts incoming messages and responds |
| **Attacker** | Sends crafted ciphertexts and measures decryption timing |
| **Analyzer** | Parses and plots timing data for analysis |
| **Web UI** | Flask app with real-time controls and timing charts |
| **Constant-Time Toggle** | Web UI supports constant-time decryption mode to mitigate timing attacks |

---

## Requirements

- Python 3.8+
- Flask
- Matplotlib
- Numpy

All dependencies can be installed via:

```bash
pip install -r requirements.txt
```

---

## Contact

For questions, feedback, or contributions, please open an issue at [github.com/pallasite99/rsa-timing-attack/issues](https://github.com/pallasite99/rsa-timing-attack/issues).
