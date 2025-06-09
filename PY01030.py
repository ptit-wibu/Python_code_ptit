#start code with DucLN
import math

n, k = map (int, input().split())
duoi =  pow(10,k-1)
tren = pow(10,k)

ans = []
for i in range(duoi,tren):
    if math.gcd(n,i) == 1:
        ans.append(i)

for i in range(0, len(ans), 10):
    print(" ".join(map(str, ans[i:i+10])))