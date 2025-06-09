#start code with DucLN
import sys

def snt(s):
    if s<2: 
        return False
    elif s == 2:
        return True
    elif s % 2 == 0:
        return False
    else:
        for i in range(3,int(s**0.5)+1 , 2):
            if s % i == 0:
                return False
    return True

def check(s):
    if snt(len(s)) == False:
        return "NO"
    cnt = 0
    other = 0
    for i in s:
        if i in {'2', '3', '5', '7'}:
            cnt+=1
        else:
            other +=1
    if other >= cnt:
        return "NO"
    return "YES"

for _ in range (int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sys.stdout.write(check(s) + "\n")