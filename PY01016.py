#start code with DucLn

t = int(input())
while t!=0:
    t-=1
    s = input()
    for i in range(1,len(s),2):
        cnt = int(s[i])
        while cnt !=0:
            cnt -=1
            print(s[i-1], end='')
    print()