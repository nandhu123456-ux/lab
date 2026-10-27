def rc4(data, key):
    S = list(range(256))
    j = 0

    # Step 1: Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Step 2: Generate keystream and encrypt/decrypt
    i = j = 0
    result = []

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)

    return bytes(result)


text = input("Enter plaintext: ").encode()
key = input("Enter key: ").encode()

if not key:
    print("Key cannot be empty!")
else:
    # Encryption
    cipher = rc4(text, key)
    print("Encrypted (Hex):", cipher.hex().upper())

    # Decryption
    decrypted = rc4(cipher, key)
    print("Decrypted:", decrypted.decode())