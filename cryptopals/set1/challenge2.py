# fixed xor
import sys
from binascii import unhexlify

def bytes_xor(a,b):
    return bytes([x^y for (x,y) in zip(a,b)])

#print(bytes_xor(unhexlify(sys.argv[1]),unhexlify(sys.argv[2])))
