#start code wih DucLn
import sys

def check(s):
    for i in range (len(s)):
        if s[i] == '\n':
            continue
        if s[i] != '0' and s[i] != '1' and s[i] != '2':
            return "NO"
    return "YES"
    
for i in range(int(sys.stdin.readline())):
    sys.stdout.write(check(sys.stdin.readline()) + "\n")