msg = 'odaeeuzsftqdgnuoazxvymiumq'
for i in range(27):
    print(''.join([chr(((ord(c)+i-97)%26)+97) for c in msg]))
    
