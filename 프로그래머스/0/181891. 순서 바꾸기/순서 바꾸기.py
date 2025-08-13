def solution(num_list, n):
    n %= len(num_list)  
    num_list[:] = num_list[n:] + num_list[:n]
    return num_list
