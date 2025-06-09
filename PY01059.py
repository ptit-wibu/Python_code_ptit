import sys

def sum(s):
    res = 0
    for i in range(0,len(s),2):
        res += ord(s[i]) - ord('0')
    return str(res)

def mul(s):
    a = set()
    mul = 1
    for i in range (1, len(s), 2):
        if s[i] != '0':
            mul *= (ord(s[i]) - ord('0'))
        a.add(s[i])
    if len(a) == 1 and '0' in a:
        return '0'
    return str(mul)

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    sys.stdout.write(sum(s) + " " + mul(s) + "\n")