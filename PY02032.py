s = input()
if len(s) & 1 ==1:
    s = s[:len(s)-1]
a = list()
for i in range(0,len(s),2):
    tmp = int(s[i:i+2])
    if tmp not in a:
        a.append(tmp)
a.sort()
print(*a)
'''
124356141111434356149

'''