import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg_my.enc','w')
f.write(ct.hex())
f.close()


def decryption(ct):
    pt = []
    for char in ct:
        pt.append((179 * (char - 18)) % 256)
    return bytes(pt)