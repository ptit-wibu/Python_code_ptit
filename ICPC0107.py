#start code with DucLN
import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    p ,q = map(str,s.split())
    if q > p:
        p,q = q,p
    s = sys.stdin.readline().strip().split()
    if len(s) > 1:
        x1 = s[0]
        x2 = s[1]
    else:
        x1 = s[0]
        x2 = sys.stdin.readline().strip()
    a1 = x1
    a2 = x2
    x1 = x1.replace(p,q)
    x2 = x2.replace(p,q)
    a1 = a1.replace(q,p)
    a2 = a2.replace(q,p)
    sum1 = int(x1) + int(x2)
    sum2 = int(a1) + int(a2)
    sys.stdout.write(str(sum1) + " " + str(sum2) + "\n")
