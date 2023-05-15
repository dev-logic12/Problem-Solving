def solution(e, starts):
    answer = []
    multiples = [0] * (e + 1)

    for i in range(1, int(e ** 0.5) + 1):
        for j in range(i, e // i + 1):
            product = i * j
            multiples[product] += (2 if i != j else 1)

    counts = [0] * (e + 1)
    max_count = 0

    for idx in range(e, 0, -1):
        if multiples[idx] >= max_count:
            max_count = multiples[idx]
            counts[idx] = idx
        else:
            counts[idx] = counts[idx + 1]

    for start in starts:
        answer.append(counts[start])
    return answer
