import sys

chuso = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def doi_co_so(N,b):
    if N == 0:
        return "0"
    kq = "" 
    while N>0:
        N,r = divmod(N,b)
        kq = chuso[r] + kq
    return kq

for _ in range(int(sys.stdin.readline())):
    N , b = map(int, sys.stdin.readline().strip().split())
    print(doi_co_so(N,b))