#start code with DucLN

t = int(input())
def check(s):
    x = s[::-1]
    for i in range (1,len(s),1):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(x[i]) - ord(x[i-1])):
            return False
    return True
while t!= 0:
    t-=1
    s = input()
    if check(s) == True:
        print("YES")
    else: 
        print("NO")