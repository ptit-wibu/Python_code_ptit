#start code with DucLn
import sys

def find_Top(s):
    for i in range (1,len(s)):
        if s[i] == s[i-1]:
            return -1
        if s[i] < s[i-1]:
            return i
    return -1
def solution(s):
    if len(s) < 3: 
        return "NO"
    id = find_Top(s)
    if id == -1:
        return "NO"
    for i in range (id + 1, len(s)):
        if s[i] >= s[i-1]:
            return "NO"
    return "YES"    

for i in range (int(sys.stdin.readline())):
    sys.stdout.write(solution(sys.stdin.readline())+"\n")
