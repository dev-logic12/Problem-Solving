def solution(array, commands):
    result = []
    for i, j, k in commands:
        answer = array[i-1:j]
        result.append(sorted(answer)[k-1])
    return result