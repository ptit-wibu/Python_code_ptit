#start code with DucLN
import sys
import math

for _ in range(int(sys.stdin.readline())):
    d,m = map(int, sys.stdin.readline().strip().split())
    if m == 1:
        if d < 20:
            sys.stdout.write("Ma Ket\n")
        else:
            sys.stdout.write("Bao Binh\n")
    elif m == 2:
        if d < 19:
            sys.stdout.write("Bao Binh\n")
        else:
            sys.stdout.write("Song Ngu\n")
    elif m == 3:
        if d < 21:
            sys.stdout.write("Song Ngu\n")
        else:
            sys.stdout.write("Bach Duong\n")
    elif m == 4:
        if d < 20:
            sys.stdout.write("Bach Duong\n")
        else:
            sys.stdout.write("Kim Nguu\n")
    elif m == 5:
        if d < 21:
            sys.stdout.write("Kim Nguu\n")
        else:
            sys.stdout.write("Song Tu\n")
    elif m == 6:
        if d < 21:
            sys.stdout.write("Song Tu\n")
        else:
            sys.stdout.write("Cu Giai\n")
    elif m == 7:
        if d < 23:
            sys.stdout.write("Cu Giai\n")
        else:
            sys.stdout.write("Su Tu\n")
    elif m == 8:
        if d < 23: 
            sys.stdout.write("Su Tu\n")
        else:
            sys.stdout.write("Xu Nu\n")
    elif m == 9:
        if d < 23:
            sys.stdout.write("Xu Nu\n")
        else:
            sys.stdout.write("Thien Binh\n")
    elif m == 10:
        if d <23:
            sys.stdout.write("Thien Binh\n")
        else:
            sys.stdout.write("Thien Yet\n")
    elif m == 11:
        if d < 23:
            sys.stdout.write("Thien Yet\n")
        else:
            sys.stdout.write("Nhan Ma\n")
    else:
        if d < 22:
            sys.stdout.write("Nhan Ma\n")
        else:
            sys.stdout.write("Ma Ket\n")