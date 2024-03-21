def solution(arr, n):
    answer = []
    for i in range(len(arr)):
        if len(arr) %2 ==1:
            if i %2 == 0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
        else:
            if i %2 == 1:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    return answer
        
    








# def solution(arr, n):
#     answer = []
#     for i in range(len(arr)):
#         if len(arr) % 2 == 1:  # arr의 길이가 홀수인 경우
#             if i % 2 == 0:  # 짝수 인덱스에 대해
#                 answer.append(arr[i] + n)
#             else:
#                 answer.append(arr[i])
#         else:  # arr의 길이가 짝수인 경우
#             if i % 2 == 1:  # 홀수 인덱스에 대해
#                 answer.append(arr[i] + n)
#             else:
#                 answer.append(arr[i])
#     return answer





# arr = [49, 12, 100, 276, 33]	
# n = 27
# print(solution(arr, n))
