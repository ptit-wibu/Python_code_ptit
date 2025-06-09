'''
import sys

n = int(sys.stdin.readline())
a = list(map(float, sys.stdin.readline().split()))
a = sorted(a)
sum = 0
cnt = 0
for i in a:
    if i != a[0] and i != a[-1]:
        sum += i
        cnt += 1

sys.stdout.write("{:.2f}\n".format(sum/cnt))
'''

import sys
n = int(sys.stdin.readline())
a = list(map(float, sys.stdin.readline().strip().split()))
a.sort()
sum = 0
cnt = 0
for i in a:
    if i != a[0] and i != a[-1]:
        sum += i
        cnt += 1
ans = sum/cnt
sys.stdout.write(f"{ans:.2f}" + "\n")

'''
6
6.75 8 9.2 7.25 7.75 6.75

'''