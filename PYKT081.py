import sys

def solve():
    ip = sys.stdin.readline().strip()
    res = list(ip.split("."))
    if len(res) < 4:
        return "NO\n"
    for i in res:
        if i.isdigit():
            if int(i) < 0 or int(i) > 255:
                return "NO\n"
        else:
            return "NO\n"
    return "YES\n"

for _ in range(int(sys.stdin.readline())):
    sys.stdout.write(solve())

'''
2
192.168.1.1
256.255.255.255

'''