import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    if (s[0] == s[-1]):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")