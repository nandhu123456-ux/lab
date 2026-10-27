# Diffie-Hellman Key Exchange

p = int(input("Enter prime number (p): "))
g = int(input("Enter generator (g): "))

# Private keys
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

# Calculate public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)

# Calculate shared secret
alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)

print("Alice's shared secret:", alice_secret)
print("Bob's shared secret:", bob_secret)

if alice_secret == bob_secret:
    print("Key exchange successful!")
else:
    print("Key exchange failed!")