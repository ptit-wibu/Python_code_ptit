import sys
import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def cong (self, other):
        ucln = math.gcd(self.mau, other.mau)
        bcnn = int((self.mau * other.mau)/ucln)
        res = int(self.tu * (bcnn/self.mau) +  other.tu * (bcnn/other.mau))
        tmp = math.gcd(bcnn, res)
        bcnn /= tmp
        res /= tmp
        return f"{int(res)}/{int(bcnn)}"
    
a = list(map(int, input().split()))
ps1 = PhanSo(a[0], a[1])
ps2 = PhanSo(a[2], a[3])
print(ps1.cong(ps2))
    