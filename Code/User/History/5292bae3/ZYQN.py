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
message = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
encrypted_message = encryption(message)
decrypted_message = decryption(message.encode())

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message.decode())
