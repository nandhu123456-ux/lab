from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Take user input
text = input("Enter plaintext: ")
key = input("Enter key (16, 24, or 32 characters): ").encode()

if len(key) not in (16, 24, 32):
    print("Key must be exactly 16, 24, or 32 bytes.")
else:
    # Encryption
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())

    print("Encrypted (Hex):", ciphertext.hex())

    # Decryption using the same key and nonce
    decipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    plaintext = decipher.decrypt_and_verify(ciphertext, tag)

    print("Decrypted:", plaintext.decode())