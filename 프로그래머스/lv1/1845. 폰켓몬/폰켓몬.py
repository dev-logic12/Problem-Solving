def solution(nums):
    answer = 0
    num = len(set(nums))
    arr = len(nums)//2
    for i in range(len(nums)):
        if num>= arr:
            return arr
        else:
            return num