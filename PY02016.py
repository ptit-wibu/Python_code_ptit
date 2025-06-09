'''
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().strip().split()))
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i,0) + 1
    sorted_cnt = sorted(cnt.items(), key = lambda x: (-x[1], x[0]))
    #print(sorted_cnt)
    ans = sorted_cnt[0]
    key, val = ans
    if val > int(n//2):
        sys.stdout.write(str(key) + "\n")
    else:
        sys.stdout.write("NO" + "\n")
'''

import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = map(int, sys.stdin.readline().strip().split())
    cnt = dict()
    for i in a:
        cnt[i] = cnt.get(i,0) + 1
    sorted_cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    '''đang là tuple'''
    ans = sorted_cnt[0]
    key, val = ans
    if val > int(n//2):
        sys.stdout.write(str(key) + "\n")
    else:
        sys.stdout.write("NO\n")

'''
2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4

'''


