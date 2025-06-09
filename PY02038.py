n = int(input())
a = list()
cot = [0 for i in range(n)]
hang = [0 for i in range(n)]
for i in range(n):
    a.append(input())

for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            hang[i] += 1
            cot[j] += 1
sum = 0
for i in range(n):
    sum += hang[i] * (hang[i] - 1) / 2
    sum += cot[i] * (cot[i] - 1) / 2
print(int(sum))
'''
4
CC..
C..C
.CC.
.CC.

'''