import sys
import math

a = set()
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    a.add(s)
sys.stdout.write(str(len(a)))