import string


def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption("Hi")
f = open('./msg_my.enc','w')
f.write(ct.hex())
f.close()


