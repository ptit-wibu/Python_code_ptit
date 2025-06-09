import string
t = int(input())
while t>0:
    t-=1
    s = input()
    #print(s[0:2])
    #print(s[-2:])
    if s[0:2] == s[-2:]:
        print("YES")
    else:
        print("NO")