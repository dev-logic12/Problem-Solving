def solution(n):
    answer = [n]  # 초기값인 n을 answer에 추가합니다.
    
    while n != 1:  # n이 1이 아닐 때까지 반복합니다.
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        answer.append(n)
        
    return answer


# def solution(n):
#     answer = []
#     while n <= 1000:
#         if n%2 == 0:
#             n//2 
#             answer.append(n)
#             if n == 1:
#                 break
#         else:
#             3*n+1 
#             answer.append(n)
#             if n == 1:
#                 break
#     return answer 
