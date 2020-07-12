buf = 'jU5t_a_sna_3lpm12gb44_u_4_m1r240' 
passw = ' ' * len(buf)
buf_pass = {}
i = 0
while i < 8:
    buf_pass[i] = i
    i += 1
while i < 16:
    buf_pass[i] = 23 - i
    i += 1
while i < 32:
    buf_pass[i] = 46 - i
    i += 2
i = 31
while i >= 17:
    buf_pass[i] = i
    i -= 2
ans = sorted([(buf[k],v) for k,v in buf_pass.items()], key = lambda x:x[1])
print(''.join([v for v,_ in ans]))

