import sys


def sieve(lim, prime):
    prime[0] = prime[1] = False
    for i in range (2,int(lim**0.5) + 1):
        if prime[i]:
            for j in range (i*i, lim+1, i):
                prime[j] = False
    return set([i for i, val in enumerate(prime) if val])

snt = sieve(1000000, [True]*1000001)
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] in snt:
            print("1", end= " ")
        else:
            print("0", end = " ")
    print()