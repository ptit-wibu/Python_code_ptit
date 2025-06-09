t = int(input())

a = []
num = 2
def check(n):
    for i in n:
        if int(i)%2 == 1:
            return False
    return True
    
while num < 889:
    if(check(str(num))):
        tmp = str(num)
        a.append(tmp + tmp[::-1])
    num+=2

while t>0:
    t -= 1
    s = input()
    ans = ''
    for i in a:
        if int(i) >= int(s):
            break
        ans += (i + ' ')
    print(ans.strip())