def solution(my_string, alp):
    answer = my_string.replace(alp, alp.swapcase())
    return answer