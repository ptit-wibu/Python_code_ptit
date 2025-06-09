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
    a = int(s[0:3])
    b = int(s[-3:])
    if snt(a) == "YES" and snt(b) == "YES":
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")
    sys.stdout.write("\n")