import sys

s = sys.stdin.readline().strip()
result = ""
if len(s) % 3 == 1:
    s = "00" + s
elif len(s) % 3 == 2:
    s = "0" + s
for i in range(0, len(s)-1, 3):
    result += str(int(s[i:i+3],2))
    #print(s[i:i+3])
print(result)