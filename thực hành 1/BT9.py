import sys

cnt =0 
for i in (sys.stdin.readline().strip()):
    if i == '4' or i == '7':
        cnt+=1
if cnt in {4,7}:
    sys.stdout.write("YES")
else:
    sys.stdout.write("NO")