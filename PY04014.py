import sys
from decimal import Decimal, ROUND_HALF_UP
class hocsinh():
    def __init__(self,stt, ten, diem):
        self.ma = f"HS{stt:02d}"
        self.ten = ten
        self.diem = diem
        self.diemtb = self.tinhdiemtb()
        self.xeploai = self.tinhxeploai()

    def tinhxeploai(self):
        dtb = self.diemtb
        if dtb >= 9:
            return "XUAT SAC"
        elif dtb >= 8:
            return "GIOI"
        elif dtb >= 7:
            return "KHA"
        elif dtb >= 5:
            return "TB"
        else:
            return "YEU"

    def tinhdiemtb(self):
        sum = self.diem[0]*2 + self.diem[1]*2
        for i in range(2,10):
            sum += self.diem[i]
        diem = sum/12
        return diem.quantize(Decimal('0.1'), ROUND_HALF_UP)

    def __str__(self):
        return f"{self.ma} {self.ten} {self.diemtb:.1f} {self.xeploai}\n"

    def __lt__(self, other):
        if self.diemtb != other.diemtb:
            return self.diemtb > other.diemtb
        return self.ma < other.ma
res = list()
n = int(sys.stdin.readline())
for i in range(1, n + 1):
    res.append(hocsinh(i, input(), list(map(Decimal, input().split()))))
res.sort()
for i in res:
    print(i)

'''
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0

'''