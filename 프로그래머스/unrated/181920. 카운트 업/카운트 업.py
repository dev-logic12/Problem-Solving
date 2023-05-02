def solution(start, end):
    answer = []
    for i in range(51):
        answer.append(i)
    return answer[start:end+1]