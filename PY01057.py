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

def check(s):
    for i in range(len(s)):
        if s[i] in {'2', '3', '5', '7'}:
            if snt(i) == "NO" :
                return "NO"
        else:
            if snt(i) == 'YES':
                return "NO"
    return "YES"
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sys.stdout.write(check(s))
