def solution(myString):
    answer = []
    answer1 = []
    answer = myString.split('x')
    for i in answer:
        answer1.append(len(i))
    return answer1