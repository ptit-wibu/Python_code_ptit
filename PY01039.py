#start code with DucLN
import sys


def check(s):
    set_check = set(s)
    return len(set_check) <= 2

def check1(s):
    i = s[0]
    j = s[1]
    for k in range(len(s)):
        if k%2==0:
            if s[k] != i:
                return False
        else:
            if s[k] != j:
                return False
    return True
for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    
    if check(s) == True and check1(s) == True:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
    

