import sys

for _ in range(int(sys.stdin.readline())):
    ok = True
    n = int(sys.stdin.readline())
    a = sorted(list(map(int, sys.stdin.readline().strip().split())))
    b = sorted(list(map(int, sys.stdin.readline().strip().split())))
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
    if(ok):
        sys.stdout.write("YES" + "\n")
    else:
        sys.stdout.write("NO" + "\n")
        