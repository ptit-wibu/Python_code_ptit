def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i,0) + 1
    for i in cnt:
        if cnt[i] & 1 == 1:
            print(i)
            return
for _ in range(int(input())):
    solve()

'''
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2

'''