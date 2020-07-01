# single-byte xor cipher

def test_english(inputs):
    char_sets = list(range(97,122)) + [32]
    if (sum([x in char_sets for x in inputs]) / len(inputs) > 0.8):
            print(inputs)

from challenge2 import bytes_xor
import sys
from binascii import unhexlify

cipher = unhexlify(sys.argv[1])
n = len(cipher)

for i in range(256):
    key = bytes(chr(i) * n,'utf-8')
    test_english(bytes_xor(cipher, key))

