s = input()
hoa = 0
thuong = 0
for x in s:
    if x >= 'a' and x <= 'z':
        thuong+=1
    elif x >= 'A' and x<='Z':
        hoa+=1
if thuong >= hoa:
    print(s.lower())
else:
    print(s.upper())