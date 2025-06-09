import sys

def solve():
    n = int(input())
    a = list()
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp)
    res = [0]*n
    if n == 2:
        res[0] = a[0][1]//2
        res[1] = a[0][1]//2
    else:
        res[0] = (a[0][1] + a[0][2] - a[1][2])//2
        for i in range(1,n):
            res[i] = a[0][i] - res[0]
    print(*res)
solve()
'''
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0

2
0 2
2 0

'''
