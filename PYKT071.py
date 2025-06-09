import pickle
from collections import Counter

def khong_giam(n):
    s = str(n)
    if len(s) < 2:
        return False
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def solve():
    with open ("DATA1.in", "rb") as f:
        list1 = pickle.load(f)
    with open ("DATA2.in", "rb") as f:
        list2 = pickle.load(f)

    count1 = Counter(n for n in list1 if khong_giam(n))
    count2 = Counter(n for n in list2 if khong_giam(n))

    key1 = set(count1.keys())
    key2 = set(count2.keys())

    chung = key1.intersection(key2)
    sort_res = sorted(list(chung))
    for i in sort_res:
        print(f"{i} {count1[i]} {count2[i]}")

solve()