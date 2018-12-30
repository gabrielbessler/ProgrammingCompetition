import sys
from math import floor
from math import log

for x in range(1,200):
    #using left shift seems to have to processing impact
    #print(-x - 1 + 2^(1 + (floor(log(x,2)))))
    ans = []
    for a in range(1,x):
        if x ^ a > x:
            ans.append(a)
    print(ans)
