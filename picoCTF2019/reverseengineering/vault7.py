x = """
return x[0] == 1096770097
            && x[1] == 1952395366
                        && x[2] == 1600270708
                                    && x[3] == 1601398833
                                                && x[4] == 1716808014
                                                            && x[5] == 1734305335
                                                                        && x[6] == 962749284
                                                                                    && x[7] == 828584245

"""
import re
reg = "== (\d+)"
vals = re.findall(reg,x)
from binascii import unhexlify
print(''.join([(unhexlify(hex(int(v))[2:])).decode('ascii') for v in vals]))
