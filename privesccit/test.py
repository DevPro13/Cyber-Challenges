from base64 import b64decode

with open("b64.txt","r") as f:
    cipher = f.read()

for i in range(50):
    cipher = b64decode(cipher)

print(cipher)
