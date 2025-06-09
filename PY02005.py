import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
res = len(a)
cnt = 0
for i in range (0,res-1):
    for j in range(i+1, res):
        if a[i] > a[j]:
            #print(str(a[i]) + " " + str(a[j]))
            cnt += 1
sys.stdout.write(str(cnt))