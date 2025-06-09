import sys

def check(s):
    for i in range(1,len(s)):
        if s[i-1] > s[i]:
            return "NO"
    return "YES"

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sys.stdout.write(check(s) + "\n")