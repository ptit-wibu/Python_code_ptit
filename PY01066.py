import sys

def check(s,z):
    for i in range(1,len(s),1):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(z[i]) - ord(z[i-1])):
            return "NO"
    return "YES"

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    z = s[::-1]
    sys.stdout.write(check(s,z) + "\n")