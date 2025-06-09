P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while 1!=0:
    s = input().lstrip()
    if s[0] == '0':
        break
    else:
        token = s.split()
        res = int(token[0])
        a = str(token[1])
        ans = ""
        word = 0
        for i in range(len(a)):
            if a[i] == '_':
                word = (26 + res)%28
            elif a[i] == '.':
                word = (27 + res)%28
            else:
                word = (ord(a[i]) - 65 + res)%28
            ans += P[word]
        print("".join(reversed(ans)))
    