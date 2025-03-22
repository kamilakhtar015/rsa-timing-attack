# core/rsa_core.py

from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

# -------------------------------
# Generate RSA Key Pair
# -------------------------------
def generate_rsa_keypair(key_size=1024):  # Default to 1024-bit for security
    key = RSA.generate(key_size)
    public_key = (key.e, key.n)   # (e, n)
    private_key = (key.d, key.n)  # (d, n)
    return public_key, private_key

# -------------------------------
# RSA Encryption: c = m^e mod n
# -------------------------------
def encrypt_message(message: bytes, public_key: tuple) -> int:
    e, n = public_key
    m = bytes_to_long(message)
    if m >= n:
        raise ValueError("Message too large for the RSA modulus.")
    c = pow(m, e, n)
    return c

# -------------------------------
# RSA Decryption (Timing-Vulnerable)
# -------------------------------
def decrypt_message(ciphertext: int, private_key: tuple) -> bytes:
    d, n = private_key
    m = square_and_multiply(ciphertext, d, n)  # Uses a timing-leaky method
    return long_to_bytes(m)

# -------------------------------
# Square-and-Multiply (Timing Attack Target)
# -------------------------------
def square_and_multiply(base, exponent, modulus):
    """ Performs modular exponentiation using Square-and-Multiply (timing-leaky). """
    result = 1
    base = base % modulus
    for bit in bin(exponent)[2:]:  # Convert exponent to binary
        result = (result * result) % modulus  # Always performed
        if bit == '1':
            result = (result * base) % modulus  # Only when bit is 1
    return result
