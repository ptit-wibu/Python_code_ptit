import sys
import math

a = { 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

for _ in range(int(sys.stdin.readline())):
    coso = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    #sys.stdout.write(res + "\n")
    if coso == 2:
        sys.stdout.write(s + "\n")
    elif coso == 4:
        ans = ""
        if len(s) % 2 == 1:
            s = '0' + s    
        for i in range (len(s)-2,-1,-2):
            num = s[i:i+2]
            ans =  str(int(num,2)) + ans
        sys.stdout.write(ans + "\n")
    elif coso == 8:
        ans = ""
        if len(s) % 3 == 1:
            s = '00' + s    
        elif len(s) % 3 == 2:
            s = "0" + s
        for i in range (len(s)-3,-1,-3):
            num = s[i:i+3]
            ans = str(int(num,2)) + ans
        sys.stdout.write(ans + "\n")
    elif coso == 16:
        ans = ""
        if len(s) % 4 == 1:
            s = '000' + s    
        elif len(s) % 4 == 2:
            s = "00" + s
        elif len(s) % 4 == 3:
            s = "0" + s
        for i in range (len(s)-4,-1,-4):
            num = s[i:i+4]
            if int(num,2) <10:
                ans = str(int(num,2)) + ans
            else:
                ans = a[int(num,2)] + ans
        sys.stdout.write(ans + "\n")