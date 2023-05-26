def solution(num_list):
    even = 0
    odd = 0 
    for i in range(len(num_list)):
        if i % 2 != 0:
            odd += int(num_list[i])
        else:
            even += int(num_list[i])
    return max(even, odd)


# num_list = [4, 2, 6, 1, 7, 6]	
# print(solution(num_list))