from flask import Flask, request, jsonify
from encryption import generate_key, decrypt_data
import os

app = Flask(__name__)

# Use environment variables for sensitive data
PASSWORD = os.getenv('ENCRYPTION_PASSWORD', 'securepassword')
SALT = os.getenv('ENCRYPTION_SALT', b'somesaltvalue')

@app.route('/receive', methods=['POST'])
def receive_data():
    # Validate input
    data = request.json
    if not data or 'iv' not in data or 'ciphertext' not in data:
        return jsonify({"error": "Invalid input data"}), 400

    try:
        # Convert received data
        iv = bytes.fromhex(data['iv'])
        ciphertext = bytes.fromhex(data['ciphertext'])

        # Generate key and decrypt
        key = generate_key(PASSWORD, SALT)
        plaintext = decrypt_data(key, iv, ciphertext)

        return jsonify({"message": "Data received and decrypted successfully", "data": plaintext})

    except Exception as e:
        return jsonify({"error": f"Decryption failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
