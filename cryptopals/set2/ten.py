# CBC Mode
''' 
allows irregular sized messages

each cipher block is added to next plain text block before the next call
first block is added to a fake 0th ciphertext block called initialization vector or IV
'''
def bxor(b1, b2): # use xor for bytes
    parts = []
    for b1, b2 in zip(b1, b2):
        parts.append(bytes([b1 ^ b2]))
    return b''.join(parts)

def split_blocks(msg, blocksize):
    return [msg[i:i+blocksize] for i in range(0, len(msg), blocksize)]

def encrypt_aes_128_ebc(msg, key):
    cipher_config = AES.new(key, AES.MODE_ECB)
    cipher = cipher_config.encrypt(msg)    
    return cipher

def decrypt_aes_128_ebc(cipher, key):
    cipher_config = AES.new(key, AES.MODE_ECB)
    msg = cipher_config.decrypt(cipher)    
    return msg

def encrypt_aes_128_cbc(msg, IV, key):
    msg = nine.PKCS(msg, 16)
    blocks = split_blocks(msg, 16)  
    res = b''
    for block in blocks:
        to_encrypt = bxor(block, IV)
        cipher = encrypt_aes_128_ebc(to_encrypt, key)
        res += cipher
        IV = cipher
    return res

def decrypt_aes_128_cbc(cipher, IV, key):
    blocks = split_blocks(cipher, 16)  
    res = b''
    for block in blocks:
        to_decrypt =  decrypt_aes_128_ebc(block, key)
        msg = bxor(to_decrypt, IV)
        res += msg
        IV = block
    return res


import os 
from Crypto.Cipher import AES
import nine
'''
message = b"THIS IS A MESSAGE That needs work"
key = b"YELLOW SUBMARINE"

IV = b'\x00'*16

cip = encrypt_aes_128_cbc(message, IV, key)
r_msg = decrypt_aes_128_cbc(cip, IV, key)

print(decrypt_aes_128_ebc(encrypt_aes_128_ebc(message,key),key) == message)
print(r_msg)
'''
