import re
import sys

text = sys.stdin.read()
sens = re.split(r'[.?!]', text)

for i in sens:
    i = i.strip()
    if i:
        res = re.sub('[^a-zA-Z0-9,:]', ' ',i).split()
        ans = ' '.join(res).lower()
        ans = ans.capitalize()
        print(ans)