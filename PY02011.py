import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
cost = 1e9
index = -1

for i in range(n):
    tmp = a[i]
    sum = 0
    for j in range(n):
        sum += abs(tmp - a[j])
    #print(sum, a[i])
    if sum < cost:
        cost = sum
        index = i

print(f"{cost} {a[index]}")
'''
8
13 5 8 7 9 15 26 34

'''