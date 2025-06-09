import math
t = int(input())
while t!=0:
    t-=1
    n = int(input())
    count = 0
    for i in range(1,n):
        if math.gcd(i,n) == 1:
            count+=1
    if count <2:
        print("NO")
        #continue
    elif count == 2:
        print("YES")
    elif count % 2 == 0:
        print("NO")
    else:
        check = True
        for i in range(3,int(math.sqrt(count)),2):
            if count%i==0:
                check = False
                break
        if check==True:
            print("YES")
        else:
            print("NO")