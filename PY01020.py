#start code with DucLn

t = int(input())
while t!=0:
    t-=1
    s = input()
    #print(s[-2:][::-1])
    if s[-2:] != "86":
        print("NO")
    else:
        print("YES")