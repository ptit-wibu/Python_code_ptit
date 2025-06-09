import sys
import math

def snt(n):
    if n < 2: 
        return "NO"
    elif n == 2:
        return "YES"
    elif n%2==0:
        return "NO"
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n % i == 0:
                return "NO"
    return "YES"

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    res = s[-4::]
    #print(res)
    sys.stdout.write(snt(int(res)))