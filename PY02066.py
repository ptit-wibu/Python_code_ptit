import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.read().split()))
#print(a)
lim = max(a)
res = set(a)
ans = list()
for i in range(1,lim+1):
    if i not in res:
        ans.append(i)
if len(ans) == 0:
    print("Excellent!")
else:
    for i in ans:
        print(i)
'''
7
4 5 7 8 9
10 11
'''
