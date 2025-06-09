#start code with DucLN
import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    n = 1
    for i in s:
        if i != '0':
            n*=(ord(i) - ord('0')) 
        else:
            continue
    sys.stdout.write(str(n) + "\n")