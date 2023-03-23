def solution(answers):
    answer = []
    p1 = [1,2,3,4,5] * 2000
    p2 = [2,1,2,3,2,4,2,5] * 1250
    p3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    c1, c2, c3 = 0, 0, 0

    for i in range(len(answers)):
        if p1[i] == answers[i]:
            c1 += 1 
        if p2[i] == answers[i]:
            c2 += 1 
        if p3[i] == answers[i]:
            c3 += 1 
    max_count = max(c1, c2, c3)
    if max_count == c1:
        answer.append(1)
    if max_count == c2:
        answer.append(2)
    if max_count == c3:
        answer.append(3)
    return answer
