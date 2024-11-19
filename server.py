from flask import Flask, request, jsonify
from encryption import generate_key, decrypt_data

app = Flask(__name__)

# Password and salt for key generation (shared secret)
PASSWORD = "securepassword"
SALT = b'somesaltvalue'

@app.route('/receive', methods=['POST'])
def receive_data():
    # Get encrypted data from the client
    data = request.json
    iv = bytes.fromhex(data['iv'])
    ciphertext = bytes.fromhex(data['ciphertext'])

    # Generate the encryption key
    key = generate_key(PASSWORD, SALT)

    # Decrypt the data
    plaintext = decrypt_data(key, iv, ciphertext)
    return jsonify({"message": "Data received and decrypted successfully", "data": plaintext})

if __name__ == '__main__':
    app.run(debug=True)
