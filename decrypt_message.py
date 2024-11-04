from cryptography.fernet import Fernet

# Load the key from the file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

# Create a Fernet instance with the loaded key
f = Fernet(key)

# Token (the encrypted message) you want to decrypt
# token = b"YOUR_ENCRYPTED_TOKEN_HERE"

token = b"gAAAAABnKCGtwupDwr8V__REgBpiB-UylBO83zlIhjszrAAos9Xk4Jd-Szu91SYdml9FxSKzK2NQ3qmOVkAtBcsFi4hBArAH59vlRP-coJ1HfwoUEtRsBLiT8dXPpz58TCZ7UFxxJUlh"

# Decrypt the message
decrypted_message = f.decrypt(token)
print("Decrypted:", decrypted_message.decode())
