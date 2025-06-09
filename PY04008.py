import sys
for _ in range (int(sys.stdin.readline())):
    m,n = map(int, sys.stdin.readline().strip().split())
    a = list()
    b = [[0 for i in range(m)] for j in range(n)]
    for i in range (m):
        a.append(list(map(int, sys.stdin.readline().strip().split())))
    for i in range (n):
        for j in range(m):
            b[i][j] = a[j][i]
    c = [[0 for i in range(m)] for j in range(m)]
    for i in range (m):
        for j in range(m):
            sum = 0
            for k in range (n):
                sum += a[i][k]*b[k][j]
            c[i][j] = sum
    for i in range (m):
        for j in range(m):
            sys.stdout.write(str(c[i][j]) + ' ')
        sys.stdout.write("\n")
'''
1
2  2
1  2
3  4

'''