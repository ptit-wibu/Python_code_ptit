def snt(n):
    if n<2:
        return False
    elif n == 2:
        return True
    elif n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

ans = list()
for i in a:
    if i not in ans:
        ans.append(i)
sum = 0
for i in ans:
    sum+=i
tmp = 0
ok = None
for i in range(len(ans)):
    tmp+=ans[i]
    if snt(tmp) and snt(sum - tmp):
        print(i)
        ok = 1
        break
if ok == None:
    print("NOT FOUND")
'''
10
3 6 7 3 5 7 3 6 6 7

10
3 6 7 3 4 7 3 6 4 4
'''