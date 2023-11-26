def solution(a, b):
    answer = int(str(a)+str(b))
    answer1 = int(str(b)+str(a))
    return answer if answer>answer1 else answer1