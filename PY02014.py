import sys
import bisect
from bisect import bisect_left,bisect_right

lim = 10005
prime = [True]*lim

def sieve():
    prime[0] = prime[1] = False
    for i in range(2, int(lim**0.5) + 1):
        if prime[i]:
            for j in range(i*i, lim, i):
                prime[j] = False
    return [x for x in range(lim) if prime[x]]

def solve():
    prime_num = sieve()
    n = int(input())
    a = list(map(int, input().split()))
    cost = 0
    for i in a:
        if prime[i]:
            continue
        idx = bisect_left(prime_num, i)
        p2 = prime_num[idx]
        p1 = prime_num[idx-1]

        cost_num = min(abs(p2-i), abs(p1-i))
        if cost_num > cost:
            cost = cost_num
    print(cost)

solve()
'''
8
13 5 8 7 9 15 26 34

'''