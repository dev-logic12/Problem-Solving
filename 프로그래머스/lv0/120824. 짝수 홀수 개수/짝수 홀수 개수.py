def solution(num_list):
    even = list(filter(lambda x : x % 2 == 0, num_list))
    return [len(even), len(num_list)-len(even)]