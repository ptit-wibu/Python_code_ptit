#start code with DucLn

import sys

nums = []
def check(s):
    res = str(s)
    for i in res:
        if (ord(i) - ord('0'))%2 != 0:
            return False
    return True

def sinh():
    st = 2
    while st <= 1000:
        if check(st) == True:
            s = str(st) + str(st)[::-1]
            nums.append(int(s))
        st +=2

nums.sort()
sinh()
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    for res in nums:
        if res < n:
            sys.stdout.write(str(res) + " ")
        else:
            break
    sys.stdout.write("\n")