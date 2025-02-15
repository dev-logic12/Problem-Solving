def solution(n):
    answer = [[]]
    del answer[0]
    for i in range(n):
        answer.append(n*[0])

    for i in range(n):
        answer[i][i] = 1

    return answer