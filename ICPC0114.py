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
    sum = 0
    for i in s:
        sum += (ord(i) - ord('0'))
        if i not in {'2', '3', '5', '7'}:
            return "No"
    if snt(sum) == "NO":
        return "No"
    if(snt(int(s))) == "NO":
        return "No"
    if(snt(int(s[::-1]))) == "NO":
        return "No"
    return "Yes"

for _ in range (int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sys.stdout.write(check(s))