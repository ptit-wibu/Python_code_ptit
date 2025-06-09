import sys

for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    a = ""
    for i in s:
        if i.isalpha():
            a += ' '
        else:
            a += i
    n = a.split()
    k = []
    for res in n:
        k.append(int(res))
    #print(n)
    k.sort(reverse=True)
    sys.stdout.write(str(k[0]) + "\n")