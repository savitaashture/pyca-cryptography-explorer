from cryptography.fernet import Fernet

# Load the key from the file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

# Create a Fernet instance with the loaded key
f = Fernet(key)

# Token (the encrypted message) you want to decrypt
token = b"YOUR_ENCRYPTED_TOKEN_HERE"

# Decrypt the message
decrypted_message = f.decrypt(token)
print("Decrypted:", decrypted_message.decode())
