#start code with DucLn
import sys

a = [0] * 93
a[0] = 0
a[1] = 1
def sinh():
    for i in range (2,93):
        a[i] = a[i-1] + a[i-2]

sinh()
for _ in range(int(sys.stdin.readline())):
    x,y = map(int, sys.stdin.readline().strip().split())
    for i in range(x,y+1):
        sys.stdout.write(str(a[i])+" ")
    sys.stdout.write("\n")