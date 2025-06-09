import sys
def snt(n):
    if n < 2 :
        return False
    elif n == 2:
        return True
    elif n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def solve():
    m, n = map(int, input().split())
    a = list()
    vi_tri = list()
    for i in range(m):
        a.append(list(map(int, input().split())))

    ans = 0
    for i in range(m):
        for j in range(n):
            if snt(a[i][j]) and a[i][j] > ans:
                ans = a[i][j]
    for i in range(m):
        for j in range(n):
            if a[i][j] == ans:
                vi_tri.append((i, j))
    if ans == 0:
        print("NOT FOUND")
        return
    print(ans)
    for i in vi_tri:
        print(f"Vi tri [{i[0]}][{i[1]}]")
solve()
'''
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29

'''