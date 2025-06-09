s = input()
if len(s) & 1 == 1:
    s = s[:len(s)-1]
res = dict()
for i in range(0,len(s), 2):
    tmp = s[i:i+2]
    res[int(tmp)] = res.get(int(tmp),0) + 1
for i in res:
    print(f"{i} {res[i]}")
'''
124356141111434356149

'''