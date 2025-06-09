'''
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    res = {}
    for i in range(n):
        s = int(sys.stdin.readline())
        if s in res:
            res[s] += 1
        else:
            res.setdefault(s,1)
    max_value = max(res.values())
    ans = None
    for key, val in res.items():
        if val == max_value:
            if ans == None or key < ans:
                ans = key
    sys.stdout.write(str(ans) + "\n")
'''
import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    res = {}
    for i in range(n):
        tmp = int(sys.stdin.readline())
        res[tmp] = res.get(tmp,0) + 1
    cnt = sorted(res.items(), key=lambda x: (-x[1], x[0]))
    ans = cnt[0]
    key, val = ans
    sys.stdout.write(str(key) + "\n")

'''
3
3
999
999
19
4
13
333
333
13
3
11
12
13

'''