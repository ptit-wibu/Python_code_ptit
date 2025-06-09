import sys
def solve(a):
    sorted(a)
    n = len(a)
    cnt = 0

    for i in range (n-2):
        if i > 0 and a[i] == a[i-1]:
            continue
        l,r = i+1, n-1
        while l<r:
            total = a[i] + a[l] + a[r]
            if total == 0:
                cnt+=1
                l+=1
                r-=1

                while l< r and a[l] == a[l-1]:
                    l+=1
                while l < r and a[r] == a[r+1]:
                    r+=1
            elif total < 0:
                l+=1
            else: 
                r-=1
    return cnt

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(a))