def solution(num_list):
    answer = 0
    answer1 = 0 
    for i in range(len(num_list)):
        if num_list[i] % 2 != 0:
            answer += int(num_list[i])
        else:
            answer1 += int(num_list[i])
    return max(answer, answer1)


# num_list = [4, 2, 6, 1, 7, 6]	
# print(solution(num_list))