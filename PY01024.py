#start code with DucLN
import math
def check(s):
    sum = 0
    for i in range(len(s)-1):
        if abs(int(s[i]) - int(s[i+1]))!= 2:
            return False
        sum += int(s[i])
    sum += int(s[len(s)-1])
    return sum % 10 == 0

t = int(input())
while t!=0:
    t-=1
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
