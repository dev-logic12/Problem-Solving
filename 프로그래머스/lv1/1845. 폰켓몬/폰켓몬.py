def solution(nums):
    num = set(nums)
    for i in range(len(nums)):
        if len(num) >= len(nums)//2:
            return len(nums)//2
        else: 
            return len(num)