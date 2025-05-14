def solution(picture, k):
    answer = []
    for i in picture:
        solution = ''
        for j in i:
            solution += j * k
        for _ in range(k):
            answer.append(solution) 
    return answer