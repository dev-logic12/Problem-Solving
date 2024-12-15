def solution(num_list):
    if len(num_list)>10: 
        return sum(num_list)
    a = 1
    for x in num_list:
        a *= x
    return a