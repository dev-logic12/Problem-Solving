def solution(nums):
    a = len(set(nums))
    b = len(nums)//2
    return min(a, b)
    # if a >= b:
    #     return b 
    # elif a <= b:
    #     return a
