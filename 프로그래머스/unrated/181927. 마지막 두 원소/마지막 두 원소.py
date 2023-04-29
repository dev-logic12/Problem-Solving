def solution(num_list):
    answer = num_list
    if int(num_list[-1]) > int(num_list[-2]):
        answer.append(int(num_list[-1]) - int(num_list[-2]))
    else:
        answer.append(int(num_list[-1]*2))
    return answer
