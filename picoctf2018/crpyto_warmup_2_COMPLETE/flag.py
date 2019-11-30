#ignore symbols and check case
cipher = "cvpbPGS{guvf_vf_pelcgb!}"
for i in cipher.lower():
	# print(chr((ord(i)+13)%122 - 1))
	x = ord(i) + 13
	if x > 122:
		print(chr(x%122 - 1 + ord('a')))
	else:
		print(chr(x))
