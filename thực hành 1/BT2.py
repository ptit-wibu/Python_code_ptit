import sys

n = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().strip().split()]  
ans = 10**9

for i in a:
    res = 0
    for j in a:
        res += abs(i-j)
    if (ans > res):
        ans = res
        index = i
sys.stdout.write(str(ans) + " " + str(index))