import string

def decryption(ct):
    pt = []
    for char in ct:
        pt.append((179 * (char - 18)) % 256)
    return bytes(pt)

ct = file.open()