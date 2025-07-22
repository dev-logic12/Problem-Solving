from math import prod

def solution(num_list):
    answer = sum(num_list) if len(num_list) >= 11 else prod(num_list)
    return answer 