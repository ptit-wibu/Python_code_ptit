import sys

while True:
    a = list(map(int, sys.stdin.readline().strip().split()))
    if a == [0,0,0,0]:
        break
    cnt = 0
    while len(set(a)) > 1:
        b = []
        for i in range(3):
            b.append(abs(a[i+1] - a[i]))
        b.append(abs(a[3] - a[0]))
        a = b
        cnt +=1
    sys.stdout.write(str(cnt) +"\n")