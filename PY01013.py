import math

def check(n):
    if n <2:
        return False
    elif n == 2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))):
            if(n % i == 0):
                return False
    return True

t = int(input())
while t>0:
    t-=1
    a,b = map(int, input().split())
    ucln = math.gcd(a,b)
    res = 0
    for i in str(ucln):
        res += int(i)
    if check(res) == True:
        print("YES")
    else:
        print("NO")
    