def check(start,end,n):
    return n == (end- start)

def solve():
    m, n = map(int, input().split())
    a = list()
    vi_tri = list()
    for i in range(m):
        a.append(list(map(int, input().split())))

    ans = 0
    start = min(min(row) for row in a)
    end = max(max(row) for row in a)
    for i in range(m):
        for j in range(n):
            if check(start, end, a[i][j]):
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
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77

'''