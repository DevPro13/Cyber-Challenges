f = open("incident.raw",'rb')
lines = f.readlines()

pngdata = b""

def swap_order(d, wsz=4, gsz=2 ):
    d = d.decode('utf-8')
    d = "".join(["".join([m[i:i+gsz] for i in range(wsz-gsz,-gsz,-gsz)]) for m in [d[i:i+wsz] for i in range(0,len(d),wsz)]])
    return d.encode('ascii')

from binascii import hexlify

for line in lines:
    data = line.replace(b'\n',b'')
    if data:
        pngdata += data[-36:-4]
        print(pngdata)
        input()


