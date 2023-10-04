def solution(name, yearning, photo):
    answer = []

    for n in photo:
        score = 0
        for n in n:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)

    return answer