import sys

def solve():
    m,n = map(int, input().split())
    a = list()
    for i in range(m):
        a.append(list(map(int, input().split())))
    if m > n:
        res = m - n
        abandon = list()
        index = 1
        while res != 0:
            abandon.append(index)
            index+=2
            res -=1
        for i in range (m):
            if i + 1 not in abandon:
                for j in range(n):
                    print(a[i][j], end=' ')
                print()
    elif m < n:
        res = n - m
        abandon = list()
        index = 2
        while(res != 0):
            abandon.append(index)
            index +=2
            res-=1
        for i in range (m):
            ok = None
            for j in range(n):
                if j+1 not in abandon:
                    print(a[i][j], end=' ')
            print()
    else:
        for i in range(m):
            print(*a[i])
solve()

'''
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9

4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7

'''