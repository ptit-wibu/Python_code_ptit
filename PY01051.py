#start code with DucLN

import sys

def check(s):
    if len(s) == 1:
        return "NO"
    if s != s[::-1]:
        return "NO"
    return "YES"
    
for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sum = 0
    for j in s:
        if j.isdigit():
            sum += (ord(j) - ord('0'))
    sys.stdout.write(check(str(sum)) + "\n")
        