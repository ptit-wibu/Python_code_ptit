import sys

res = set()
for _ in range(int(sys.stdin.readline())):
    res.add(sys.stdin.readline().strip())
sys.stdout.write(str(len(res)))