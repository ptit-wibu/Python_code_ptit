import sys

def tinh_diem_cc(res):
    v = 0
    m = 0
    for i in res:
        if i == 'v':
            v += 1
        elif i == 'm':
            m += 1
    cc = 10 - v * 2 - m
    return cc if cc > 0 else 0

class Student():
    def __init__(self,ma,ten,lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.cc = 10
    def __str__(self):
        return f"{self.ma} {self.ten} {self.lop} {self.cc} {'' if self.cc > 0 else 'KDDK'}"

a = list()
for _ in range (int(input())):
    a.append(Student(input(), input(), input()))

data = sys.stdin.read().split("\n")
#print(data)
for i in data:
    res = list(i.split())
    #print(res)
    if not res:
        continue
    for j in a:
        if j.ma == res[0]:
            j.cc = tinh_diem_cc(res[1])
            break
for i in a:
    print(i)
'''
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm

'''