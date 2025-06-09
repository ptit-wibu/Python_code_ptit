import math
def solve(N,X,M):
    base = math.log(1+X/100)
    return math.ceil((math.log(M) - math.log(N))/base)

t = int(input())
while t!=0:
    t-=1
    s = input()
    N,X,M = map(float, s.split())
    print(solve(N,X,M))