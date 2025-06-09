from itertools import permutations
import sys

s = sys.stdin.readline().strip()
res = permutations(s)
for i in res:
    sys.stdout.write("".join(i) + "\n")