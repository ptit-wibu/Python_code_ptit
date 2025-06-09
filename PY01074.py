import sys
import math

MAX_N = int(2e6) + 1
a = [0] * MAX_N

for i in range(2, int(math.sqrt(2e6)) + 1):
    if a[i] == 0:
       a[i] = i
       for j in range (i, int(2e6)//i + 1):
           a[i*j] = i
for i in range (4,int(2e6)):
    a[i] += a[i//a[i]] if a[i] else i
res = 0
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    res += a[n]

sys.stdout.write(str(res) + "\n")