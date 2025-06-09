#start to code by DucLn

a, k, n = map(int, input().split())
res = int(n/k)
flag = False
for i in range (1,res+1):
    if i*k-a > 0:
        print(i*k-a, end=' ')
        flag = True
    else:
        continue
if flag == False:
    print("-1")