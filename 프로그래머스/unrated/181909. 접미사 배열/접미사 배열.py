def solution(my_string):
    answer = []
    answer1 = ''
    for i in range(len(my_string)):
        answer1 = my_string[i:]
        answer.append(answer1)
    
    answer.sort()
    return answer