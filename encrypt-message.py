from cryptography.fernet import Fernet

# Load the key from the file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

# Create a Fernet instance with the loaded key
f = Fernet(key)

# Encrypt a message
message = b"A really secret message. Not for prying eyes."
token = f.encrypt(message)
print("Encrypted:", token)
