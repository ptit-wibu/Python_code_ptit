#start code with DucLN
import bisect
import sys
from bisect import bisect_left
nums = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160,
        25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280,
        720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
#nums.sort()
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    '''
    ans = 0
    for i in range(0,len(nums)):
        if nums[i] >= n:
            ans = nums[i]
            break
    print(ans)
    '''
    print(nums[bisect_left(nums,n)])