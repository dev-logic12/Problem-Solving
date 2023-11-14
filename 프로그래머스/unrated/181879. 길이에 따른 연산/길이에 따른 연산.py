def solution(num_list):
    answer = 0
    answer1 = 1
    for i in num_list:
        if len(num_list)>=11:
            answer += i 
        else:
            answer1 *= i
    return answer if len(num_list) >= 11 else answer1
    # return if num_list len(num_list)>11 else num_list