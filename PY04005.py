import sys
import math

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.a = math.hypot(x1 - x2, y1 - y2)
        self.b = math.hypot(x2 - x3, y2 - y3)
        self.c = math.hypot(x3 - x1, y3 - y1)
        self.chuvi = self.a + self.b + self.c

    def is_valid(self):
        return self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b

    def __str__(self):
        if not self.is_valid():
            return "INVALID"
        else:
            return f"{self.chuvi:.3f}"

inputs = sys.stdin.read().strip().split()
t = int(inputs[0])
numbers = list(map(float, inputs[1:]))

results = []
for i in range(t):
    x1, y1 = numbers[i*6], numbers[i*6+1]
    x2, y2 = numbers[i*6+2], numbers[i*6+3]
    x3, y3 = numbers[i*6+4], numbers[i*6+5]
    triangle = Triangle(x1, y1, x2, y2, x3, y3)
    results.append(str(triangle))

for res in results:
    print(res)