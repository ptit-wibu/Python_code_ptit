n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = max(int(a[0]*a[1]), int(a[0]*a[1]*a[2]), int(a[n-1]*a[n-2]), int(a[n-1]*a[n-2]*a[n-3]), int(a[0]*a[1]*a[n-1]))
print(ans)
'''
6
5 10 -2 3 5 2

'''