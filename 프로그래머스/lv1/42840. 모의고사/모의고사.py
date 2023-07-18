def solution(answers):
    answer = []
    s1 = [1,2,3,4,5] * 2000
    s2 = [2,1,2,3,2,4,2,5] * 1250
    s3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    p1, p2, p3 = 0, 0, 0

    for i in range(len(answers)):
        if s1[i] == answers[i]:
            p1 += 1 
        if s2[i] == answers[i]:
            p2 += 1 
        if s3[i] == answers[i]:
            p3 += 1 
    count = max(p1, p2, p3)
    if count == p1:
        answer.append(1)
    if count == p2:
        answer.append(2)
    if count == p3:
        answer.append(3)
    return answer
