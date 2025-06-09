import sys

n = int(sys.stdin.readline())
res = []
for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    res.append(s)
sum = int(sys.stdin.readline())
s1 = 0
s2 = 0
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            s1 += res[i][j]
        elif j > n-i-1:
            s2 += res[i][j]
if abs(s1 - s2) <= sum:
    print("YES")
else:
    print("NO")
print(abs(s1-s2))
