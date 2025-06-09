import sys
import string
import re
'''
  s = s.replace(',', ' ')
    s = s.replace('.', ' ')
    s = s.replace('?', ' ')
    s = s.replace('!', ' ')
    s = s.replace(':', ' ')
    s = s.replace(';', ' ')
    s = s.replace('-', ' ')
    s = s.replace('/', ' ')
    s = s.replace('(', ' ')
    s = s.replace(')', ' ')
'''
'''
   s = sys.stdin.readline().strip().lower() + ' '
   word = ''
   for char in s:
        if char.isalnum():
            word += char
        else:
            if word != '':
                if word in ans:
                    ans[word] +=1
                else:
                    ans[word] = 1
                word = ''
ans = sorted(ans.items(), key = lambda x:(-x[1], x[0]))
for i in ans:
    print(i[0], i[1])
'''
ans = dict()
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip().lower()
    s = re.sub(r'[^\w\s]', ' ', s)
    for i in s.split():
        ans[i] = ans.get(i,0) + 1
#res = {k: v for k, v in sorted(ans.items(), key = lambda item: (-item[1], item[0]))}
ans = sorted(ans.items(), key = lambda x:(-x[1], x[0]))
for i in ans:
    print(i[0], i[1])
