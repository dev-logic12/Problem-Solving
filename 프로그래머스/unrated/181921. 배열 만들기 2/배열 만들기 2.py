def solution(l, r):
    answer = []
    for num in range(l, r+1):
        num_str = str(num)
        if all(char in '05' for char in num_str):
            answer.append(num)
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)


# def solution(l, r):
#     answer = []
#     while 1<=l<=r:
#         i = 1 
#         if l <= i <= r:
#             for num in 
#         answer.append(i)
#         answer.sort()
#     if answer == []:
#         return -1
#     return answer