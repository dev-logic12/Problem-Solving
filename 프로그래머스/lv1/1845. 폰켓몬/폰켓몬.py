'''
1,2,3 2 2 
2,3,4 3 3 
2,3 3 2 
len(nums)//2 
len(set(nums))

'''


def solution(nums):
    return min(len(set(nums)), len(nums)//2)