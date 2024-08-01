def solution(myString):
    answer = []
    olen = []
    answer = myString.split('x')
    for i in answer:
        olen.append(len(i))
    return olen