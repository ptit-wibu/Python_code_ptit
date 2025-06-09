'''
s = input()
print(s.upper())
'''

s = input()
ans = ""
for i in range(0,len(s)):
    x = ord(s[i])
    if x>=97 and x<=122:
        x-=32
        #print(chr(x))
        ans += chr(x)
    else:
        #print(s[i])
        ans += s[i]
print(ans)