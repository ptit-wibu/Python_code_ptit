from datetime import datetime
import sys
class MonThi:
    def __init__(self, ma_mon, ten_mon):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon

class CaThi:
    def __init__(self,stt, ma_mon, ngay_thi, gio_thi,nhom_thi):
        self.ma_ca = f"T{stt:03d}"
        self.ma_mon = ma_mon
        self.ngay_thi = datetime.strptime(ngay_thi, '%d/%m/%Y')
        self.gio_thi = datetime.strptime(gio_thi, '%H:%M')
        self.nhom_thi = nhom_thi
    def __lt__(self, other):
        if self.ngay_thi != other.ngay_thi:
            return self.ngay_thi < other.ngay_thi
        if self.gio_thi != other.gio_thi:
            return self.gio_thi < other.gio_thi
        return self.ma_mon < other.ma_mon
    
    def hien_thi(self,ten_mon_dict):
        ten_mon = ten_mon_dict.get(self.ma_mon)
        return f"{self.ma_ca} {self.ma_mon} {ten_mon} {self.ngay_thi.strftime('%d/%m/%Y')} {self.gio_thi.strftime('%H:%M')} {self.nhom_thi}"
    
a,b = map(int, sys.stdin.readline().strip().split())
ds_mon = []
for _ in range(a):
    ds_mon.append(MonThi(input(), input()))

ten_mon_dict = {mon.ma_mon: mon.ten_mon for mon in ds_mon}
ds_ca = []
for i in range(1,b+1):
    tmp = input().split()
    ds_ca.append(CaThi(i,tmp[0], tmp[1], tmp[2], tmp[3]))
ds_ca.sort()
for i in ds_ca:
    print(i.hien_thi(ten_mon_dict))