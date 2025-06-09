#start code with DucLN
import sys
import math
for _ in range (int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    sys.stdout.write(str(math.gcd(a,b)) + "\n")
