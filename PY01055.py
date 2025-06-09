#start code with DucLN

import sys

def check(s):
    if len(s) & 1 == 0:
        return "NO"
    if s[0] == s[1]:
        return "NO"
    res = s[::2]
    if len(set(res)) != 1:
        return "NO"
    return "YES"

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sys.stdout.write(check(s) + "\n")