import sys

for _ in range (int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    #print(a)
    #print(b)
    a.sort()
    b.sort()
    cnt = 0
    for i in range(n-1):
        if a[i] > b[i]:
            cnt += 1
    if cnt > 1:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")