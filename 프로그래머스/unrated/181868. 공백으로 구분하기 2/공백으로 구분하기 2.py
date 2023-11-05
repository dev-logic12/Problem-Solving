def solution(my_string):
    answer = my_string.split(' ')
    answer1 = []
    for i in answer:
        if i != '':
            answer1.append(i)
    return answer1
