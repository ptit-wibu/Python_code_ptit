import datetime
from datetime import datetime
import sys

class Gamer:
    def __init__(self, ma, ten, gio_vao, gio_ra):
        self.ma = ma
        self.ten = ten
        self.gio_vao = datetime.strptime(gio_vao, "%H:%M")
        self.gio_ra = datetime.strptime(gio_ra, "%H:%M")
        self.thoi_gian_choi = int((self.gio_ra - self.gio_vao).total_seconds() // 60)


    def __lt__(self, other):
        return self.thoi_gian_choi > other.thoi_gian_choi

    def __str__(self):
        gio = self.thoi_gian_choi // 60
        phut = self.thoi_gian_choi % 60
        return f"{self.ma} {self.ten} {gio} gio {phut} phut"    
    
n = int(sys.stdin.readline())
danh_sach = []
for _ in range(n):
    danh_sach.append(Gamer(sys.stdin.readline().strip(), sys.stdin.readline().strip(), sys.stdin.readline().strip(), sys.stdin.readline().strip()))

danh_sach.sort()
for i in danh_sach:
    #sys.stdin.write(str(i) + "\n")
    print(i)