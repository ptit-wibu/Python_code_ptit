n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 1
for i in range(1, len(a)):
    if a[i] - a[i-1] > k:
        cnt+=1
print(cnt)

'''
7 1
2 6 1 7 3 4 9

'''