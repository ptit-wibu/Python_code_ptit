
def chuanhoa(s):
    return ' '.join(word.capitalize() for word in s.strip().lower().split())

def tinh_diem_uu_tien(dtoc, kvuc):
    uu_tien = 0
    if kvuc == "1":
        uu_tien += 1.5
    elif kvuc == "2":
        uu_tien +=1.0
    
    if dtoc.lower() != "kinh":
        uu_tien += 1.5
    return uu_tien

def trang_thai(diem):
    return "Do" if diem >= 20.5 else "Truot"

n = int(input())
danh_sach = []

for i in range(n):
    ma = f"TS{i+1:02}"
    ten = input().strip()
    diem = float(input())
    dan_toc = input().strip()
    khu_vuc = input().strip()

    ho_ten = chuanhoa(ten)
    uu_tien = tinh_diem_uu_tien(dan_toc,khu_vuc)
    tong_diem = diem + uu_tien
    ket_qua = trang_thai(tong_diem)
    danh_sach.append((ma,ho_ten,tong_diem,ket_qua))

danh_sach.sort(key=lambda x: (-x[2], x[0]))
for ts in danh_sach:
    print(f"{ts[0]} {ts[1]} {ts[2]:.1f} {ts[3]}")