def solution(num_list):
    answer = 1
    answer1 = 0 
    for i in num_list:
        answer *= i
        answer1 += i 
    return 1 if answer< answer1*answer1 else 0  