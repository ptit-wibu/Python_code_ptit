'''
class Triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a = math.sqrt(pow((self.x1-self.x2), 2) + pow((self.y1-self.y2),2))
        self.b = math.sqrt(pow((self.x2-self.x3), 2) + pow((self.y2-self.y3),2))
        self.c = math.sqrt(pow((self.x3-self.x1), 2) + pow((self.y3-self.y1),2))
        self.chuvi = self.a + self.b + self.c
    def __str__(self):
        if self.a + self.b <= self.c or self.b + self.c <= self.a or self.c + self.a <= self.b:
            return "INVALID"
        else:
            return f"{self.chuvi:.3f}"
        
for _ in range(int(sys.stdin.readline())):
    tmp = list(map(float, sys.stdin.readline().strip().split()))
    triangle = Triangle(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5])
    if triangle.a + triangle.b <= triangle.c or triangle.b + triangle.c <= triangle.a or triangle.c + triangle.a <= triangle.b:
        print("INVALID")
    else:
        print(f"{round(triangle.chuvi,3):.3f}")
    #print(triangle)

import sys
import math

class Triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a = math.sqrt(pow((self.x1-self.x2), 2) + pow((self.y1-self.y2),2))
        self.b = math.sqrt(pow((self.x2-self.x3), 2) + pow((self.y2-self.y3),2))
        self.c = math.sqrt(pow((self.x3-self.x1), 2) + pow((self.y3-self.y1),2))
        self.chuvi = self.a + self.b + self.c
    def __str__(self):
        if self.a + self.b <= self.c or self.b + self.c <= self.a or self.c + self.a <= self.b:
            return "INVALID"
        else:
            return f"{self.chuvi:.3f}"
        
for _ in range(int(sys.stdin.readline())):
    tmp = list(map(float, sys.stdin.readline().strip().split()))
    triangle = Triangle(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5])
    if triangle.a + triangle.b <= triangle.c or triangle.b + triangle.c <= triangle.a or triangle.c + triangle.a <= triangle.b:
        print("INVALID")
    else:
        print(f"{round(triangle.chuvi,3):.3f}")
    #print(triangle)

'''
import sys
import math
def dis(a,b):
    return math.sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2))

t = int(input())
l = []
for i in range(t):
    l.extend([float(x) for x in input().split()])
i = 0
for j in range(t):
    a = dis([l[i], l[i+1]], [l[i+2], l[i+3]])
    b = dis([l[i+2], l[i+3]], [l[i+4], l[i+5]])
    c = dis([l[i+4], l[i+5]], [l[i], l[i+1]])
    i+=6
    if max([a,b,c])*2 >= a+b+c:
        print("INVALID")
    else:
        print(f"{round(a+b+c,3):.3f}")