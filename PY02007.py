import sys
res = 0
cnt = [0] * 42
while True:
    a = list(map(int, sys.stdin.readline().split()))
    res += len(a)
    ans = 0
    for i in a:
        cnt[i%42]+=1
    if res == 10:
        break
for i in cnt:
    if i != 0:
        ans+=1
sys.stdout.write(str(ans))