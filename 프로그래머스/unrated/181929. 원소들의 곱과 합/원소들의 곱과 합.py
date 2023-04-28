def solution(num_list):
    answer = 1
    sum = 0 
    for i in num_list:
        answer *= i
        sum += i 
    if answer < sum**2:
        return 1 
    elif answer > sum**2:
        return 0
        