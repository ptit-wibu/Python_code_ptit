import sys

def solve():
    n = int(sys.stdin.readline())
    bac = [0] * (n+1)

    for _ in range(n-1):
        a,b = map(int, sys.stdin.readline().strip().split())
        bac[a] +=1
        bac[b] +=1

    cnt_deg1 = 0
    cnt_degN1 = 0
    for i in range(1,n+1):
        if bac[i] == 1:
            cnt_deg1 +=1
        elif bac[i] == n-1:
            cnt_degN1 +=1
        else:
            return False
    return cnt_deg1 == n-1 and cnt_degN1 == 1

if solve() == True:
    sys.stdout.write("Yes")
else:
    sys.stdout.write("No")
