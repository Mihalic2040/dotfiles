def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * ord(char) + 18) % 256)
    return bytes(ct)

def decryption(ct):
    pt = []
    for char in ct:
        pt.append((179 * (char - 18)) % 256)
    return bytes(pt)

# Example usage:
message = "Hi"
encrypted_message = encryption(message)
decrypted_message = decryption(encrypted_message)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message.decode())
