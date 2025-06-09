import sys

def check(s,z):
    n = len(s)
    for i in range(0, n-2):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(z[i]) - ord(z[i+1])):
            return "NO"
    return "YES"

t = int (sys.stdin.readline())
for _ in range(t):
    s =  sys.stdin.readline().strip()
    z = s[::-1]
    sys.stdout.write(check(s,z) + "\n")
