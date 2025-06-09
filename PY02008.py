import sys

limit = int(1e6)
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if is_prime[start]:
            for i in range(start * start, limit + 1, start):
                is_prime[i] = False
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

res = sieve(limit)

n, x = map (int , sys.stdin.readline().strip().split())
sys.stdout.write(str(x) + ' ')
for i in range(n):
    x = x + res[i]
    sys.stdout.write(str(x) + ' ')