from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Take input
text = input("Enter plaintext: ").encode()
key = input("Enter key (exactly 8 bytes): ").encode()

if len(key) != 8:
    print("Key must be exactly 8 bytes.")
else:
    # Generate an 8-byte initialization vector
    iv = get_random_bytes(8)

    # Encryption
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(text, DES.block_size))

    print("Encrypted (Hex):", (iv + ciphertext).hex().upper())

    # Decryption
    decipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = unpad(
        decipher.decrypt(ciphertext),
        DES.block_size
    )

    print("Decrypted:", decrypted.decode())