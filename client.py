import requests
from encryption import generate_key, encrypt_data
import os

# Use environment variables for sensitive data
PASSWORD = os.getenv('ENCRYPTION_PASSWORD', 'securepassword')
SALT = os.getenv('ENCRYPTION_SALT', b'somesaltvalue')
SERVER_URL = "http://127.0.0.1:5000/receive"

def send_data(plaintext: str):
    try:
        # Generate the encryption key
        key = generate_key(PASSWORD, SALT)

        # Encrypt the data
        iv, ciphertext = encrypt_data(key, plaintext)

        # Send the encrypted data to the server
        response = requests.post(SERVER_URL, json={
            "iv": iv.hex(),
            "ciphertext": ciphertext.hex()
        })

        # Handle server response
        response.raise_for_status()
        print("Server response:", response.json())

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with server: {e}")

if __name__ == '__main__':
    sample_data = "Hi Calvin, welcome to Adams State University."
    send_data(sample_data)

