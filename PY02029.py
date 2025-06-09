m,n = map(int, input().split())
a = list(map(int, input().split()))

res = dict()
for i in a:
    res[i] = res.get(i,0) + 1

ans = sorted(res.items(), key=lambda x: (-x[1], x[0]))
#print(ans)
nhat = ans[0]
stt = nhat[0]
so_phieu = nhat[1]

nhi = None
for i in ans:
    tmp = i
    if tmp[1] < so_phieu:
        nhi = i
        break

if nhi == None:
    print("NONE")
else:
    print(nhi[0])

'''
10 4
2 3 1 2 3 4 1 2 3 2

8 4
1 2 3 4 4 3 2 1

'''
