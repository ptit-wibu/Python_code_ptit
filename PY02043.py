import sys

def solve():
    a = input()
    b = input()
    cnt = 0
    start_pos = 0
    while 1!=0:
        pos = a.find(b,start_pos)
        if pos != -1:
            cnt+=1
            start_pos = pos + len(b)
        else:
            break
    return cnt
for _ in range(int(input())):
    print(solve())

'''
2
1212121112211221121
121
2222222222322292
2222

'''