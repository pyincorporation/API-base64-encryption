from cryptography.fernet import Fernet
import base64

# Generate a Fernet key
key = Fernet.generate_key()

# Create a Fernet cipher object using the key
cipher = Fernet(key)

# Define the text to be encrypted
text = "Comfort Care will be hosting our 1st Annual Fundraising Dinner on Saturday, November 11 2023, an evening to bring community members together to celebrate diversity and the efforts that make Wyndham more inclusive. A Fundraiser and Award Night to honor and recognise Wyndham's champions in inclusivity and diversity. Join us for an evening of cultural performances, networking, and an opportunity to share a meal with fellow advocates of diversity and inclusion. All proceeds from the Wyndham Inclusion Dinner will support the Comfort Care Foundation Feed the Needy food program."

# Encrypt the text using Fernet encryption
encrypted_data = cipher.encrypt(text.encode())

# Base64 encode the encrypted data
base64_encoded = base64.b64encode(encrypted_data)

# Calculate the length of the base64-encoded ciphertext
ciphertext_length = len(base64_encoded)

print("Ciphertext Length:", ciphertext_length)
