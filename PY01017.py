#start code with DucLN

t = int(input())
while t!=0:
    t-=1
    s = input()
    s += " "
    cnt = 1
    for i in range(len(s)-1):
        if s[i+1] != s[i]:
            print(str(cnt)+""+s[i], end='')
            cnt = 1
        else:
            cnt+=1
    print()
