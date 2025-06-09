import sys
import math
def sieve():
    prime = [True] * (1000001)
    prime[0] = prime[1] = False
    for i in range (2, 1001,1):
        if prime[i]:
            for j in range (i*i, 1000001, i):
                prime[j] = False
    primes =  {x for x in range(1000001) if prime[x]}
    return primes

snt = sieve()
def check(s,n):
    if int(str(s)[::-1]) == s:
        return False
    if int(str(s)[::-1]) not in snt:
        return False
    if int(str(s)[::-1]) < s or int(str(s)[::-1]) >=n:
        return False
    return True

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
   # print(snt)
    ans = ""
    for i in snt:
        if check(i,n) == True:
            ans += (str(i) + " " + str(i)[::-1] + " ")
    ans = ans.strip()
    sys.stdout.write(ans + "\n")
