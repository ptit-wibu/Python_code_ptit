def solve():
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res1 = set(a)
    res2 = set(b)
    ans = res1.difference(res2)
    return len(ans) == 0

if solve() == True:
    print("YES")
else:
    print("NO")

'''
12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5

'''