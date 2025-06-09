import sys
import bisect

hamming = set()
lim = int(1e18)
for i in range(65):
    n2 = 1 << i
    if n2 > lim:
        break
    for j in range(40):
        n3 = 3 ** j
        if n2 * n3 > lim:
            break
        for k in range(28):
            n5 = 5 ** k
            if n2 * n3 * n5 > lim:
                break
            hamming.add(n2 * n3 * n5)
hamming = sorted(hamming)

def find_position(a, v):
    pos = bisect.bisect_left(a, v)
    if pos != len(a) and a[pos] == v:
        return pos + 1
    return 'Not in sequence'

for _ in range(int(sys.stdin.readline())):
    sys.stdout.write(str(find_position(hamming, int(sys.stdin.readline()))) + "\n")