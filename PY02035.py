s = input()
n = int(input())
if len(s) & 1 == 1:
    s = s[:len(s)-1]
res = dict()
for i in range(0,len(s), 2):
    tmp = s[i:i+2]
    res[int(tmp)] = res.get(int(tmp),0) + 1
ans = sorted(res.items(), key=lambda x: (x[0]))
ok = None
for i in ans:
    if i[1] >=n:
        print(f"{i[0]} {i[1]}")
        ok = 1
if ok == None:
    print("NOT FOUND")
'''
124356141111434356149
2

124356141111434356149
10

'''