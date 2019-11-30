def generateKey(string, key):
	for i in range(len(string) - len(key)):
		key += key[i%len(key)]
	return key

def decrypt(cipher, key):
	original = ""
	for idx, val in enumerate(cipher):
		original += chr(((ord(val) - ord(key[idx]) + 26) % 26) + ord('a'))
	return original

print(decrypt('llkjmlmpadkkc','thisisalilkey'))

