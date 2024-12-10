# Securing Data Transmission for Remote Model Training

This project demonstrates securing data transmission between a client and server during remote model training. It now includes features for encryption, decryption, and monitoring encrypted communication using additional tools.

---

## **Project Overview**

The goal of this project is to:

- Securely transmit and process sensitive data using AES encryption over HTTPS.
- Provide packet monitoring to detect and analyze encrypted data traffic.
- Monitor filesystem changes for enhanced security insights.

---

## **Features**

1. **Data Encryption and Decryption**:
   - Uses AES encryption with derived keys (PBKDF2HMAC) for secure data handling.
   - Encrypts data before transmission and decrypts it upon receipt.

2. **Secure HTTPS Communication**:
   - All data transmissions between client and server are encrypted using HTTPS.
   - SSL/TLS certificates are utilized for secure connections.

3. **Packet Monitoring**:
   - Captures and analyzes network packets using `pyshark`.
   - Detects encrypted traffic and logs details for security purposes.

4. **File System Monitoring**:
   - Tracks changes in monitored directories.
   - Logs file deletions for enhanced security auditing.

---

## **Requirements**

- **Python 3.x**
- Libraries:
  - `flask` (for the server)
  - `requests` (for client communication)
  - `cryptography` (for AES encryption and decryption)
  - `pyshark` (for network packet monitoring)
  - `watchdog` (for filesystem monitoring)
  
Install the required libraries with:

```bash
pip install flask requests cryptography pyshark watchdog
```

---

## **Setting Up the Project**

1. **Clone the Repository**:
   - Clone or download the project files.

2. **Set Up Python Environment**:
   - Install the required libraries listed above.

3. **Generate SSL Certificates**:
   - Use the following command to create certificates for HTTPS communication:
     ```bash
     openssl req -new -x509 -keyout server.key -out server.crt -days 365
     ```
   - Place `server.crt` and `server.key` in the project directory.

4. **Set Environment Variables**:
   - Configure sensitive data like passwords and salts in environment variables.

---

## **How to Run the Project**

### **Step 1: Start the Server**
```bash
python server.py
```
Expected output:
```
Server running and waiting for encrypted client data...
```

### **Step 2: Send Encrypted Data Using the Client**
```bash
python client.py
```

### **Step 3: Monitor Network Traffic**
- Start packet monitoring on a specific interface (e.g., Wi-Fi):
  ```bash
  python monitor.py
  ```
- Captured packets are saved to `output.pcap`.

### **Step 4: Monitor File Changes**
- Run the file system monitoring script:
  ```bash
  python monitor.py
  ```

---

## **Code Explanation**

1. **Encryption and Decryption**:
   - `encryption.py` contains functions for key derivation, AES encryption, and decryption.

2. **Client**:
   - Encrypts data using `encryption.py` and sends it securely to the server.

3. **Server**:
   - Decrypts received data and logs responses.

4. **Packet Monitoring**:
   - Captures and logs network packets.
   - Analyzes encrypted traffic.

5. **File System Monitoring**:
   - Tracks and logs file deletions in specified directories.

---

## **Troubleshooting**

- **SSL Verification Errors**:
  - For self-signed certificates, disable verification in the client (development only):
    ```python
    requests.post(SERVER_URL, json=data, verify=False)
    ```

- **Packet Monitoring Permissions**:
  - Run packet monitoring with elevated privileges:
    ```bash
    sudo python monitor.py
    ```

---

## **Future Improvements**

1. **Enhanced Security**:
   - Use production-grade certificates and enforce strong encryption standards.

2. **Authentication**:
   - Add user authentication to secure endpoints further.

3. **Real-World Integration**:
   - Extend functionality for real machine learning workflows.

4. **Custom Alerts**:
   - Trigger notifications for unusual packet or filesystem activity.