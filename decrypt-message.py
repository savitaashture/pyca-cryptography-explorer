from cryptography.fernet import Fernet

# Load the key from the file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

# Create a Fernet instance with the loaded key
f = Fernet(key)

# Token (the encrypted message) you want to decrypt
token = b"gAAAAABnGaYpXRg-IjkUHlADlQnuFAuG1UNdG3NhqnPKSZ2pHpsb0DL-YOGMLvYCv7Tr4kqBR8Gn4VpJBYwC4KWOBO2FoIQAFbPZwHrvAJEee--V6glOiv4qjNQRgtKO-5uWsstgLBl3"

# Decrypt the message
decrypted_message = f.decrypt(token)
print("Decrypted:", decrypted_message.decode())
