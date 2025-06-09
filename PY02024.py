'''
import sys

def mul(x):
    res = 1
    for i in str(x):
        res *= int(i)
    return res

def digit_sum(x):
    return (mul(x),x)


n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort(key=digit_sum, reverse=False)
    for i in a:
        sys.stdout.write(str(i) + " ")
    sys.stdout.write("\n")
'''
import sys

def mul(x):
    res = 1
    for i in str(x):
        res *= int(i)
    return res

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().strip().split()))
    a.sort(key=lambda x:(mul(x), x))
    for i in a:
        sys.stdout.write(str(i) + " ")
    print()


'''
1
8
143 43 22 99 7 9 1111 10000000

'''
