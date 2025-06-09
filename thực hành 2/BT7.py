import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
ans = 0
for i in range(0,n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            ans +=1
sys.stdout.write(str(ans))