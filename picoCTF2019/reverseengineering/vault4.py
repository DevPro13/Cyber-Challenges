    
bytess = [
106 , 85  , 53  , 116 , 95  , 52  , 95  , 98,  0x55, 0x6e, 0x43, 0x68, 0x5f,0x30, 0x66, 0x5f,142, 0131, 0164, 063 , 0163, 0137, 063 , 0141, '7' , '2' ,'4' , 'c' , '8' , 'f' , '9' , '2' ,
]
passw = []
for e in bytess:
    passw.append(e)
for e in passw:
    if isinstance(e, basestring):
        print(e)
    else:
        print(chr(e))
