import sys

n = sys.stdin.readline().strip()
cnt = 0
if len(n) == 1:
    sys.stdout.write("1")
else:
    while len(n)>1:
        sum = 0
        for i in n:
            sum += (ord(i) - ord('0'))
        cnt+=1
        n = str(sum)
    sys.stdout.write(str(cnt))
