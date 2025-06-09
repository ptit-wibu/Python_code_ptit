import sys
import math
for _ in range(int(sys.stdin.readline())):
    a = map(int, sys.stdin.readline().strip().split())
    a = sorted(a)
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if math.gcd(a[i], a[j]) == 1:
                sys.stdout.write(str(a[i]) + " " + str(a[j]) + "\n")