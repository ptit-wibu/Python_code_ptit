#start code with DucLN
import sys
gth = [1]
def sinh():
    n = 1
    for i in range(1,10):
        n*=i
        gth.append(n)
sinh()
for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().strip()
    res = 0
    for i in n:
        res += int(gth[ord(i) - ord('0')])
    if res == int(n):
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")