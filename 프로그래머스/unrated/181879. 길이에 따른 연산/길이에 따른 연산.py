from functools import reduce

def solution(num_list):
    list_length = len(num_list)

    if list_length >= 11:
        return sum(num_list)
    else:
        return reduce(lambda x, y: x * y, num_list, 1)
