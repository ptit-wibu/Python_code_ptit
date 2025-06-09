import sys

s1 = set(list(sys.stdin.readline().strip().lower().split()))
s2 = set(list(sys.stdin.readline().strip().lower().split()))

ans1 = s1.union(s2)
ans2 = s1.intersection(s2)

res1 = list(ans1)
res1.sort()
res2 = list(ans2)
res2.sort()
print(*res1)
print(*res2)

'''
Lap trinh huong doi tuong
Ngon ngu lap trinh C++

'''