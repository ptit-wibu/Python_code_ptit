n,m = map(int, input().split())
a = list(input().split())
b = list(input().split())
res1 = set(a)
res2 = set(b)
print(*sorted(res1.intersection(res2)))
print(*sorted(res1-res2))
print(*sorted(res2-res1))
'''
5 6
1 2 3 4 5
3 4 5 6 7 8

'''