#start code with DucLn

t = int(input())
while t!= 0:
    t-=1
    n = int(input())
    if n%2==1:
        ans = 0
        for i in range(1,n+1,2):
            ans += (1/i)
        print(f"{ans:.6f}")
    else:
        ans = 0
        for i in range (2,n+1,2):
            ans += (1/i)
        print(f"{ans:.6f}")
