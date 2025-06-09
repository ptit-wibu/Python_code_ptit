#start code with DucLN
import sys
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    n = 0
    for i in s:
        n += (ord(i) - ord('0'))
    if n % 3 == 0:
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")
    sys.stdout.write("\n")