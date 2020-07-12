def switchBits(c, p1, p2):
    v = list(c)
    v[p1], v[p2] = v[p2], v[p1]
    return ''.join(v)
vals = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC0, 0xB4, 0xD1, 0xD2, 0x85, 0xA4, 0xA5, 0xC1, 0x85]
converted = []
for c in vals:
    c = format(c, '08b')
    c = switchBits(c, 6, 7)
    c = switchBits(c, 2, 5)
    c = switchBits(c, 3, 4)
    c = switchBits(c, 0, 1)
    c = switchBits(c, 4, 7)
    c = switchBits(c, 5, 6)
    c = switchBits(c, 0, 3)
    c = switchBits(c, 1, 2)
    converted.append(c)

print(''.join([chr(int(i,base=2)) for i in converted]))







