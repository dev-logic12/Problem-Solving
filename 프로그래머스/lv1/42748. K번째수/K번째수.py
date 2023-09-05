def solution(array, commands):
    answer = []
    list = []
    for i in commands:
        list = array[i[0] - 1:i[1]]
        list = sorted(list)
        answer.append(list[i[2]-1])

    return answer