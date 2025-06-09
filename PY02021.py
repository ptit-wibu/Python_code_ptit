import sys

def solve():
    a,b,c = map(int, sys.stdin.readline().split())
    a1 = list(map(int, sys.stdin.readline().split()))
    b1 = list(map(int, sys.stdin.readline().split()))
    c1 = list(map(int, sys.stdin.readline().split()))
    i,j,k = 0,0,0
    ans = list()
    while i<len(a1) and j < len(b1) and k < len(c1):
        if a1[i] == b1[j] and b1[j] == c1[k]:
            ans.append(a1[i])
            i+=1
            j+=1
            k+=1
        elif a1[i] < b1[j]:
            i+=1
        elif b1[j] < c1[k]:
            j+=1
        elif c1[k] < a1[i]:
            k+=1
    if len(ans) == 0:
        print("NO")
        return
    for i in ans:
        print(i, end=" ")
    print()
for _ in range(int(input())):
    solve()
'''
3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9

'''