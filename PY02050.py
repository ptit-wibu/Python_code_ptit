import sys
def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().strip().split()))
    stack = list()
    result = list()

    for i in range(n):
        while stack and stack[-1][0] <= a[i]:
            stack.pop()
        if not stack:
            result.append(i+1)
        else:
            result.append(i - stack[-1][1])
        stack.append((a[i], i))
    sys.stdout.write(" ".join(map(str,result)) + "\n")

for _ in range(int(sys.stdin.readline())):
    solve()

'''
1
7
100 80 60 70 60 75 85

'''