# convert hex to base64
import sys
from binascii import unhexlify
from base64 import b64encode

print(b64encode(unhexlify(sys.argv[1])))
