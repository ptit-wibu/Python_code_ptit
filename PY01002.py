'''
a = input().replace(" ","")
b = int(a[0])
c = int(a[2])
d = int(a[4])
if b + c == d:
    print("YES")
else:
    print("NO")
    '''
a = input() # 1 + 2 = 3
b = int(a[0]) # =1
c = int(a[4]) # =2
d = int(a[8]) # =3
if b + c == d: 
    print("YES")
else:
    print("NO")
