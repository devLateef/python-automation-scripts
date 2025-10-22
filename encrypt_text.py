from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
text = 'I love python'
encrypted = cipher.encrypt(text.encode())
decrypted = cipher.decrypt(encrypted).decode()

print(f"Key: {key}")
print(f"Cipher text: {encrypted}")
print(f"Plain text: {decrypted}")