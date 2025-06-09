s = input()
if len(s) & 1 == 1:
    s = s[:len(s)-1:]
a = dict()
for i in range(0,len(s),2):
    tmp = int(s[i:i+2])
    a[tmp] = a.get(tmp, 0) + 1

#print(res)
for i in a:
    print(i, end=" ")
'''
124356141111434356149
'''
