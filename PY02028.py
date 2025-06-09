import sys

def snt(n):
    if n<2: 
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3 , int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def solve(arr):
    primes = [x for x in arr if snt(x)]
    primes.sort()

    result = []
    primes_index = 0

    for i in arr:
        if snt(i):
            result.append(primes[primes_index])
            primes_index+=1
        else:
             result.append(i)

    return result

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))

res = solve(a)
sys.stdout.write(' '.join(map(str, res)))

