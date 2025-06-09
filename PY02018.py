import sys

n = int(sys.stdin.readline().strip())
a = map(int, sys.stdin.readline().strip().split())

a = sorted(a)
res = 1
for i in a:
    if i > res:
        break
    elif i == res:
        res +=1
sys.stdout.write(str(res))