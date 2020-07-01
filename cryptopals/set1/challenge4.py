# detect single-character XOR

def test_english(inputs):
    char_sets = list(range(97,122)) + [32]
    if (sum([x in char_sets for x in inputs]) / len(inputs) > 0.7):
            print(inputs)

from challenge2 import bytes_xor
import sys
from binascii import unhexlify

with open("4.txt",'rb') as f:
    ciphers = f.readlines()
    for cipher in ciphers: 
        cipher =  unhexlify(cipher[:-1])
        n = len(cipher)
        for i in range(256):
            key = bytes(chr(i) * n,'utf-8')
            test_english(bytes_xor(cipher, key))
