def create_table():
    a = []
    for i in range(256):
        k = i
        for j in range(8):
            if k & 1:
                k ^= 0x1db710640
            k >>= 1
        a.append(k)
    return a




crc_table = create_table()
print(hex(crc_update(b"The quick brown fox jumps over the lazy dog", 0)))
