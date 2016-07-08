#python

import time
t=time.time()
for i in range(0,5):
    tt=time.localtime(t)
    out=time.strftime("%Y%m%d%H%M%S",tt)
    t+=1
    print(out)
