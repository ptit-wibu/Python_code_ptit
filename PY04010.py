import sys
from decimal import Decimal, ROUND_HALF_UP
class ThiSinh():
    def __init__(self, ten, dob ,a,b,c ):
        self.ten = ten
        self.dob = dob
        self.diem = Decimal(a+b+c)
    def __str__(self):
        return f"{self.ten} {self.dob} {self.diem:.1f}"

ts = ThiSinh(sys.stdin.readline().strip(), sys.stdin.readline().strip(), Decimal(sys.stdin.readline().strip()),Decimal(sys.stdin.readline().strip()),Decimal(sys.stdin.readline().strip()))
print(ts)
'''
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5

'''