import sys

s = sys.stdin.readline().strip()
if len(s)%3 == 1:
    s = "00" + s
elif len(s)%3==2:
    s = "0" + s
#print(s)
res = int(s,2)
print(oct(res)[2:])