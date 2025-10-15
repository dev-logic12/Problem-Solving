def solution(num_list):
    s = sum(num_list)
    p = 1
    for n in num_list:
        p *= n
    return int(p < s * s)
