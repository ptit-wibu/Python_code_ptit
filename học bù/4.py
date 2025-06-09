import sys

s = sys.stdin.readline().strip()
z = s
while(len(z) != 1):
    n = len(z)//2
    a = z[:n]
    b = z[n:]
    res = int(a)+int(b)
    #print(a)
    #print(b)
    z = str(res)
    print(res)
    