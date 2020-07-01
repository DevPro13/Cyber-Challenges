# Detect AES in ECB mode

from binascii import hexlify, unhexlify
from collections import Counter

with open('8.txt') as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    
blockarrays = []

for line in lines:
    blocks = [line[i:i+16] for i in range(0,len(line),16)]
    blockarrays.append(blocks)


for blocks in blockarrays:
    counts = Counter(blocks)
    x = counts.most_common()
    repeated = [i for i in x if i[1] > 1]
    if repeated:
        print(''.join(blocks))
