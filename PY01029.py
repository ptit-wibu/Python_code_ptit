#start code with DucLN

import math
t = int(input())
while t!= 0:
    t-=1
    s = input().strip()
    a = int(s)
    b = int(s[::-1])
    if math.gcd(a,b) == 1:
        print("YES")
    else:
        print("NO")