import sys

def sieve(lim, prime):
    prime[0] = prime[1] = False
    for i in range (2,int(lim**0.5) + 1):
        if prime[i]:
            for j in range (i*i, lim+1, i):
                prime[j] = False
    return set([i for i, val in enumerate(prime) if val])

snt = sieve(1000000, [True]*1000001)
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
cnt = {}
for i in a:
    if i in snt:
        cnt[i] = cnt.get(i,0) + 1

for k in cnt.keys():
    sys.stdout.write(str(k) + " " + str(cnt[k]) + "\n")