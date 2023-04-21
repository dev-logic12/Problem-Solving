def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer1 = array[i-1:j]
        answer.append(sorted(answer1)[k-1])
    return answer