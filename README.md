# pyca/cryptography Explorer

This project is an exploration of the **pyca/cryptography** library, specifically focusing on symmetric encryption using **Fernet**. It demonstrates how to securely generate, store, use, and manage encryption keys, as well as encrypt and decrypt messages.

## Features

- **Key Generation**: Generate a key and save it to a file for later use.
- **Message Encryption**: Encrypt sensitive data using the saved key.
- **Message Decryption**: Decrypt encrypted data using the same key.

## Requirements

To run this project, you'll need:

- Python 3.6 or higher
- `cryptography` library

You can install the required library using the following command:

```bash
pip install cryptography
```

## Project Structure

The project consists of three Python files:

1. **`generate_key.py`**:
   - Generates a Fernet key and saves it in a file (`secret.key`).
   - Run this script first to create the key for encryption and decryption.

2. **`encrypt_message.py`**:
   - Loads the key from the `secret.key` file and encrypts a message.
   - The encrypted message (token) is displayed.

3. **`decrypt_message.py`**:
   - Loads the key from the `secret.key` file and decrypts the encrypted message (token).
   - The original message is displayed.

## How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/LahcenEzzara/pyca-cryptography-explorer.git
   cd pyca-cryptography-explorer
   ```

2. **Generate a Key**

   Run the `generate_key.py` script to generate a new encryption key and save it to `secret.key`:

   ```bash
   python generate_key.py
   ```

3. **Encrypt a Message**

   Use the `encrypt_message.py` script to encrypt a message:

   ```bash
   python encrypt_message.py
   ```

   The script will display the encrypted message (token).

4. **Decrypt a Message**

   To decrypt the encrypted message, run the `decrypt_message.py` script and replace `YOUR_ENCRYPTED_TOKEN_HERE` in the script with the encrypted token:

   ```bash
   python decrypt_message.py
   ```

   The original message will be displayed.

## Security Considerations

- Always keep the encryption key (`secret.key`) secure. Anyone with access to this key can decrypt your encrypted data.
- Never share the key publicly or commit it to version control.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy exploring the **pyca/cryptography** library!