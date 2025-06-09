import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().strip().split()
res = 0
for i in range (1,len(a)):
    if a[i] != a[i-1]:
        res +=1
sys.stdout.write(str(res))