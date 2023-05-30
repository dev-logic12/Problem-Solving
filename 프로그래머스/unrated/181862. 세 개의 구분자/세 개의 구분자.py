import re 

def solution(myStr):
    answer = re.split('[a|b|c]', myStr)
    answer = list(filter(lambda a: a, answer))
    return answer if answer else ['EMPTY']