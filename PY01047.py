#start code with DucLn

import sys
import math
def snt(s):
    if s<2: 
        return "NO"
    elif s == 2:
        return "YES"
    elif s % 2 == 0:
        return "NO"
    else:
        for i in range(3, int(math.sqrt(s))+1,2):
            if s % i == 0:
                return "NO"
    return "YES"

for i in range(int(sys.stdin.readline())):
    #print(int(sys.stdin.readline()[-4::]))
    print(snt(int(sys.stdin.readline().strip()[-4::])))