import sys

def Try(n, a, b, c):
    if n == 1:
        sys.stdout.write(a + " -> " + c + "\n")
        return
    Try(n-1,a,c,b)
    Try(1,a,b,c)
    Try(n-1,b,a,c)

Try(int(sys.stdin.readline()), "A", "B", "C")