import math
n = input()
c_4 = 0
c_7 = 0
for c in n:
    if c == '4':
        c_4+=1
    elif c=='7':
        c_7+=1
if(c_4 + c_7 == 4 or c_4 + c_7 == 7):
    print("YES")
else:
    print("NO")