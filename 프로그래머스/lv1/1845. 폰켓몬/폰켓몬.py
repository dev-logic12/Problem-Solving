'''
123 2 2 
234 3 3
23 3 2
set(nums) >= len(nums)-> len(nums)
< set(nums)


'''


def solution(nums):
    answer = set(nums)
    if len(answer) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(answer)
















# def solution(nums):
#     num = set(nums)
#     for i in range(len(nums)):
#         if len(num) >= len(nums)//2:
#             return len(nums)//2
#         else: 
#             return len(num)