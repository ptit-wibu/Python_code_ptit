#start code with DucLN
import sys

for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    sys.stdout.write(str(a.count(b)) + "\n")