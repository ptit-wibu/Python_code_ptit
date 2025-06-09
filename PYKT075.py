import sys

class Contact():
    def __init__(self,ten,sdt,ngay):
        self.ten = ten
        self.sdt = sdt
        self.ngay = ngay
        self.name = self.ten.split()[-1]
    def __lt__(self, other):
        if self.name != other.name:
            return self.name < other.name
        return self.ten < other.ten
    def __str__(self):
        return f"{self.ten}: {self.sdt} {self.ngay}"

with open("SOTAY.txt", "r") as vao:
    data = vao.read()
res = data.split("\n")
#print(res)
i = 0
cur_date = None
ans = list()
while i < len(res):
    if res[i][:4:] == "Ngay":
        cur_date = res[i][5:]
        i+=1
    elif len(res[i]) > 0:
        ten = res[i]
        i+=1
        sdt = res[i]
        ans.append(Contact(ten, sdt, cur_date))
        i+=1
    else:
        i+=1
ans.sort()
with open ("DIENTHOAI.txt", "w") as ra:
    for i in ans:
        ra.write(str(i) + "\n")

