#start code with DucLN
import sys
import math
def snt(s):
    if s<2: 
        return False
    elif s == 2:
        return True
    elif s % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(s))+1,2):
            if s % i == 0:
                return False
    return True

def check(s):
    if snt(len(s)) == False:
        return "NO"
    prime = 0
    other = 0
    for i in s:
        if (ord(i) - ord('0')) in {2,3,5,7}:
            prime +=1
        else:
            other +=1
    if prime > other: 
        return "YES"
    else:
        return "NO"


for i in range(int(sys.stdin.readline())):
    sys.stdout.write(check(sys.stdin.readline().strip()) + "\n")
    