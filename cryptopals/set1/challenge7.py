# AES in ECB mode 

from base64 import b64decode
from Crypto.Cipher import AES
from binascii import hexlify, unhexlify

with open('7.txt') as f:
    msg = b64decode(f.read())

key = b"YELLOW SUBMARINE"

cipher_config = AES.new(key, AES.MODE_ECB)

recovered = cipher_config.decrypt(msg)

print("Decrypted Mesg", recovered)

print("Hex Form", hexlify(recovered))
