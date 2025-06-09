import sys

def sieve(lim, prime):
    prime[0] = prime[1] = False
    for i in range (2,int(lim**0.5) + 1):
        if prime[i]:
            for j in range (i*i, lim+1, i):
                prime[j] = False
    #return [i for i, val in enumerate(prime) if val]

#print(res)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    cnt= 0
    res = [True] * (n+1)
    sieve(n,res)
    for i in range(2,n-6+1):
        if res[i] and res[i+2] and res[i+6]:
           #print(i, i+2, i+6)
           cnt+=1
        elif res[i] and res[i+4] and res[i+6]:
            #print(i, i+4, i+6)
            cnt+=1
    sys.stdout.write(str(cnt) + "\n")