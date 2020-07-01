# repeating-key XOR

from binascii import hexlify

msg = b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = b"ICE"
n = len(msg)
keystream = (key*n)[:n]

from challenge2 import bytes_xor

print(hexlify(bytes_xor(msg,keystream)))
