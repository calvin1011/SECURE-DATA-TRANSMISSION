import requests
from encryption import generate_key, encrypt_data

# Password and salt for key generation (shared secret)
PASSWORD = "securepassword"
SALT = b'somesaltvalue'

SERVER_URL = "http://127.0.0.1:5000/receive"

def send_data(plaintext: str):
    # Generate the encryption key
    key = generate_key(PASSWORD, SALT)

    # Encrypt the data
    iv, ciphertext = encrypt_data(key, plaintext)

    # Send the encrypted data to the server
    response = requests.post(SERVER_URL, json={
        "iv": iv.hex(),
        "ciphertext": ciphertext.hex()
    })

    print("Server response:", response.json())

if __name__ == '__main__':
    sample_data = "Hi Calvin, welcome to Adams State University."
    send_data(sample_data)
