def solution(str_list, ex):
    answer = [s for s in str_list if ex not in s]
    return "".join(answer)