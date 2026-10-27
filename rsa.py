# RSA Encryption and Decryption

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17  # Public exponent

# Find private exponent d
for d in range(1, phi):
    if (e * d) % phi == 1:
        break

message = input("Enter message: ")

# Encryption
cipher = []

for ch in message:
    m = ord(ch)
    c = pow(m, e, n)
    cipher.append(c)

print("Encrypted message:", cipher)

# Decryption
plain = ""

for c in cipher:
    m = pow(c, d, n)
    plain += chr(m)

print("Decrypted message:", plain)