# PKCS#7 padding 
# Public Key Cryptography Standards
# Padding to encrypt different sized message blocks 

def PKCS(msg, block_length):
    pad_len =  block_length - (len(msg) % block_length) 
    #if pad_len == 0:
    #   pad_len = block_length
    return msg + pad_len * b"\x04"


