x = ",LQ?2>6QiQFD6C]EIEQ[QA2DDQiQFD6C]EIEQN."
res = ''
for i in range(len(x)):
    j = ord(x[i])
    if (j >=33 and j <= 126):
        res += chr(33+((j+14)%94))
    else: 
        res += x[i]
print(res)
