import sys
def solve():
    message = sys.stdin.readline().strip()
    if len(message) <=100:
        print(message)
        return
    shorten_ver = message[:100]
    if message[99] != ' ' and message[100] != ' ':
        res = shorten_ver.rfind(' ')
        if res != -1:
            shorten_ver = shorten_ver[:res]
    print(shorten_ver.strip())

for _ in range (int(sys.stdin.readline())):
    solve()