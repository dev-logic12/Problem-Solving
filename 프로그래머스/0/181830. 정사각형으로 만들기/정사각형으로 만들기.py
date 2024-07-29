def solution(arr):
    answer = []

    countMax = max(len(arr), max(len(row) for row in arr))
    i = 0
    while i < countMax:
        if i < len(arr):
            answer.append(arr[i] + [0] * (countMax - len(arr[i])))
        else:
            answer.append([0] * countMax)
        i += 1

    return answer
