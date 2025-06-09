#start code with DucLn
'''
def check(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    return True
'''

def check(s):
    for i, val in enumerate(s[1:], 1):
        if val < s[i-1]:
            return False
    return True
t = int(input())
while t>0:
    t-=1
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")