import sys

s = sys.stdin.readline().strip().split(".")
if(s[1].lower() == "py"):
    sys.stdout.write("yes")
else:
    sys.stdout.write("no")