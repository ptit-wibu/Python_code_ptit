# start code with DucLn
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
def check (s):
    sum = 0
    for i in range(len(s)):
        sum += (ord(s[i]) - ord('0'))
        if i & 1 == 0:
            if (ord(s[i]) - ord('0')) & 1 != 0:
                return "NO"
        else:
            if (ord(s[i]) - ord('0')) & 1 == 0:
                return "NO"
    if snt(sum) == "NO":
        return "NO"
    return "YES"
for _ in range (int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sys.stdout.write(check(s) + "\n")