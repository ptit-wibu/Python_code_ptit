import sys

def solve(n):
    cnt = 1
    while n!=1:
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1
        cnt+=1
        if cnt >= 100000:
            break
    return cnt

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    sys.stdout.write(str(solve(n)) + "\n")