import requests

payload = ''
flag = ''
while True:
    r = requests.get('http://10.10.169.100:3000/{}'.format(payload))
    res = r.text
    print(res)
    payload = res[-3]
    flag += res[10] 
    if res == '{"value":"end","next":"end"}':
        break

print(flag)
