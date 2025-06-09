t = int(input())
while t!=0:
    t-=1
    s = input()
    check = True
    for c in s:
        if c != '4' and c!= '7':
            print("NO")
            check = False
            break
    if check == True:
        print("YES")