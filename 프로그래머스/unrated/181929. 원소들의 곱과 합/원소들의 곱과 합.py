def solution(num_list):
    answer = 1
    answer1 = 0 
    for num in num_list:
        answer1 += num
        answer *= num
    return 1 if answer <= answer1*answer1 else 0