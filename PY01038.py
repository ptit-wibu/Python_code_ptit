#start code with DucLN
import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    cnt = 0
    while True:
        if n % 7 == 0:
            sys.stdout.write(str(n))
            sys.stdout.write("\n")
            break
        if cnt > 1000:
            sys.stdout.write("-1\n")
            break
        cnt+=1
        n = n + int(str(n)[::-1])