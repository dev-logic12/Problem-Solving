def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        answer1 = i[s:s+l]
        num = int(answer1)
        if num > k:
            answer.append(num)
    return answer


