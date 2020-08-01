#!/usr/bin/env python

import base64
import binascii

h = binascii.hexlify
b = base64.b64encode

c = b'37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067'

def enc(f):
    e = b(f)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
    c = h(bytearray(z))
    return c


from binascii import unhexlify
c = unhexlify(c)
u_c = c[::-1]

print("u_c: ",u_c)
r = []
i = 0
o = u_c[i] ^ 90 # base64 "f" = "Z" => 90

r.append(o)

while i < len(u_c)-1:
    i += 1
    o = u_c[i] ^ o
    r.append(o)

from base64 import b64decode
print(b64decode(bytearray(r)[::-1]))

# flag{tyrannosauras_xor_in_reverse}
