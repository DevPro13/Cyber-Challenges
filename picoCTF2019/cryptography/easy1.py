key = "SOLVECRYPTO"
cipher = "UFJKXQZQUNB"

for k,c in zip(key, cipher):
    print(chr(((ord(c)-ord(k)+26)%26)+65),end='')


