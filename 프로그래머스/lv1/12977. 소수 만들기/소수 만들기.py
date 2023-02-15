
from itertools import combinations

def solution(nums):

    arrs = list(combinations(nums, 3))
    cnt = 0

    for arr in arrs:
        tmp = 0
        sum_ = sum(arr)
        for i in range(2, sum_):
            if sum_ % i == 0:
                tmp += 1
        
        if tmp == 0:
            cnt += 1

    return cnt