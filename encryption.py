from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from os import urandom

# Encryption and decryption helper functions
def generate_key(password: str, salt: bytes, iterations: int = 100000, key_length: int = 32):
    """
    Derive a symmetric encryption key from a password and salt.

    :param password: The input password (string).
    :param salt: A unique salt value (bytes).
    :param iterations: Number of iterations for PBKDF2 (default: 100,000).
    :param key_length: Length of the derived key (default: 32 bytes for AES-256).
    :return: Derived key (bytes).
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_length,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_data(key: bytes, plaintext: str):
    """
    Encrypt plaintext data using AES encryption (CFB mode).

    :param key: The symmetric encryption key (bytes).
    :param plaintext: The plaintext string to encrypt.
    :return: A tuple containing the IV (bytes) and ciphertext (bytes).
    """
    try:
        iv = urandom(16)  # Generate a random initialization vector (IV)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return iv, ciphertext
    except Exception as e:
        raise ValueError(f"Encryption failed: {e}")

def decrypt_data(key: bytes, iv: bytes, ciphertext: bytes):
    """
    Decrypt ciphertext data using AES decryption (CFB mode).

    :param key: The symmetric encryption key (bytes).
    :param iv: The initialization vector used during encryption (bytes).
    :param ciphertext: The ciphertext to decrypt (bytes).
    :return: The decrypted plaintext string.
    """
    try:
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode()
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")
