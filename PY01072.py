from itertools import permutations
from itertools import combinations
import sys

n,k = map(int, sys.stdin.readline().strip().split())
my_list = list(map(int, sys.stdin.readline().strip().split()))

res =sorted(set(my_list))
per = combinations(res, k)
for i in per:
    sys.stdout.write(" ".join(map(str,i)) + "\n")