# breaking repeating key XOR

def test_english(inputs):
    char_sets = list(range(97,122)) + [32]
    return sum([x in char_sets for x in inputs]) / len(inputs)

def single_character_xor(msg):
    n = len(msg)
    tests = []
    for i in range(256):
        key = bytes(chr(i)*n,'utf-8')
        score = test_english(bytes_xor(msg, key))
        tests.append({'score':score,'key':chr(i)})
    return sorted(tests,key=lambda x:x['score'], reverse=True)[0]

import base64,sys
from challenge2 import bytes_xor

KEYSIZE = 2 # to 40

def hd(w1,w2):
    # hamming distance between two words
    b_w1 = ''.join(format(x, '8b') for x in w1)
    b_w2 = ''.join(format(x, '8b') for x in w2)
    return sum([x != y for (x,y) in zip(b_w1,b_w2)])

with open("6.txt") as f:
        cipher = base64.b64decode(f.read())
        datas = []
        while(KEYSIZE != 41):
            distances = []
            parts = [cipher[i:i+KEYSIZE] for i in range(0, len(cipher), KEYSIZE)]
            for i in range(0,len(parts)-1):
                distances.append(hd(parts[i],parts[i+1])/KEYSIZE)
            findings = {'key':KEYSIZE,'avg':sum(distances)/len(distances)}
            datas.append(findings)
            KEYSIZE += 1
        keylength = sorted(datas,key=lambda x:x ['avg'])[0]['key']
        key = b''
        for i in range(keylength):
            block = b''
            for j in range(i, len(cipher), keylength):
                block += bytes([cipher[j]])
            #print(block)
            key += bytes(single_character_xor(block)['key'],'utf-8')
        print(key)
