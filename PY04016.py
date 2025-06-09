import datetime
import sys
from datetime import datetime

tien = [0, 25, 34, 50, 80]

class Hotel():
    def __init__(self,stt, ten, phong, vao, ra,dichvu):
        self.ma = f"KH{stt:02d}"
        self.ten = ten
        self.phong = phong
        self.vao = datetime.strptime(vao, "%d/%m/%Y")
        self.ra = datetime.strptime(ra, "%d/%m/%Y")
        self.dichvu = int(dichvu)
        self.so_ngay = self.tinh_so_ngay()
        self.thanh_tien = self.tinh_tien()
    def tinh_so_ngay(self):
        return (self.ra - self.vao).days + 1
    def tinh_tien(self):
        tang = int(self.phong[0])
        return tien[tang]*self.so_ngay + self.dichvu
    def __lt__(self, other):
        return self.thanh_tien > other.thanh_tien
    def __str__(self):
        return f"{self.ma} {self.ten} {self.phong} {self.so_ngay} {self.thanh_tien}"


res = list()
for i in range(int(input())):
    res.append(Hotel(i+1, input().strip(), input(), input().strip(), input().strip(), int(input())))
res.sort()
for i in res:
    print(i)