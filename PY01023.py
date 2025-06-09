#start code with DucLN

import math
t = int(input())
while t != 0:
    t-=1
    n = int(input())
    m = n
    ans = "1"
    for i in range (2, math.ceil(math.sqrt(m))):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt+=1
                n//=i
            ans += (f" * {int(i)}^{cnt}")
    if n!=1:
        ans += (f" * {n}^1")
    print(ans.rstrip())