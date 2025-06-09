import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    #res = s[len(s)-2:]
    #print(res)
    print("YES" if s[len(s)-2:] == "86" else "NO")