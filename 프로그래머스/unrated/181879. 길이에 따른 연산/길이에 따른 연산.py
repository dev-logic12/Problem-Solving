from math import prod
def solution(num_list):
    answer = 0
    for i in num_list:
        if len(num_list) >= 11:
            answer = sum(num_list)
        else:
            answer = prod(num_list)
    return answer