def solution(nums):
    answer = 0 
    num = set(nums)
    for i in nums: 
        if len(num) >= len(nums)//2:
            answer = len(nums)//2
        else:
            answer = len(num)
    return answer 