
def solution(nums):
    a = len(set(nums))
    b = len(nums)//2 
    if a >= b:
        return b
    else: 
        return a 