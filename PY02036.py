import math
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
for i in range(0, len(arr)-1):
    for j in range(i+1, len(arr)):
        if math.gcd(arr[i], arr[j]) == 1:
            print (f"{arr[i]} {arr[j]}")