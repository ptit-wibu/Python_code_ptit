def solve():
    s = input()
    while len(s) != 1:
        n = len(s)
        a = s[0:n//2]
        b = s[n//2:]
        sum = int(a) + int(b)
        s = str(sum)
        print(s)

solve()
'''
123456
'''