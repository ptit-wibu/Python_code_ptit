import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().strip().split())))

k = int(sys.stdin.readline())

top , down = 0 , 0

for i in range(n):
    for j in range(n):
        if j > n-i-1:
            top += a[i][j]
        elif j <n-i-1:
            down += a[i][j]

if abs(top-down) <= k:
    sys.stdout.write("YES\n")
else:
    sys.stdout.write("NO\n")
sys.stdout.write(str(abs(top-down)))