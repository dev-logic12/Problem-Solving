def solution(my_string, is_suffix):
    answer = my_string.endswith(is_suffix)
    return 1 if answer else 0