import sys


class Luong_Mua():
    def __init__(self,ten, start, end, lgmua):
        self.ten = ten
        self.start = start
        self.end = end
        self.lgmua = lgmua
        self.thoigian = self.tinhthoigian()
    def tinhthoigian(self):
        a = self.start.split(":")
        b = self.end.split(":")
        return int(b[0])*60 + int(b[1]) - int(a[0])*60 - int(a[1])


res = {}
for _ in range(int(sys.stdin.readline())):
    ts = Luong_Mua(input(), input(), input(), int(input()))
    if ts.ten not in res:
        res[ts.ten] = (ts.thoigian, ts.lgmua)
    else:
        res[ts.ten] = (res[ts.ten][0] + ts.thoigian, res[ts.ten][1] + ts.lgmua)

id = 1
for i in res:
    sys.stdout.write(f"T{id:02d} {i} {(res[i][1] * 60 / res[i][0]):.2f}\n")
    id+=1

'''
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35

'''