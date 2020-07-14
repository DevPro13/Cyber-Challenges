# An ECB / CBC Detection Oracle
import os 
from random import randrange
import ten 

def randomKEY():
    return os.urandom(16)

def encryption_oracle(msg, mode, key=randomKEY()):
    MSG =  os.urandom(randrange(5,11)) + msg + os.urandom(randrange(5,11))
    if mode=="CBC":
        res = ten.encrypt_aes_128_cbc(MSG, os.urandom(16), key)
    else:
        import nine
        MSG = nine.PKCS(MSG,16)
        res = ten.encrypt_aes_128_ebc(MSG, key)
    return res

def test_ecb_128(ctxt): 
    num_blocks = len(ctxt)//16
    return len(set([ctxt[i*16:(i+1)*16] for i in range(num_blocks)])) < num_blocks

if randrange(0,2):
   cipher = encryption_oracle(b"A"*50, mode="ECB")
else:
   cipher = encryption_oracle(b"A"*50, mode="CBC") 
print(['ECB' if test_ecb_128(cipher) else 'CBC'])




