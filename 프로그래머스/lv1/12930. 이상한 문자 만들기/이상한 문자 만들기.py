def solution(s):
    answer = []
    new_list = s.split(' ')

    for i in range(len(new_list)):
        result = ''
        for j in range(len(new_list[i])):
            if j % 2 == 0:
                result += new_list[i][j].upper()
            else:
                result += new_list[i][j].lower()
        answer.append(result)
    return ' '.join(answer)