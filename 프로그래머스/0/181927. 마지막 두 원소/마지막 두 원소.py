def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    if num_list[-1] > num_list[-2]:
        num_list.append(int(a-b))
    else:
        num_list.append(int(a)*2)
    return num_list