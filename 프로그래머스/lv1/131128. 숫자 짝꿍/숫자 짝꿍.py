def solution(x, y):
    answer = ''

    for i in range(9, -1,-1):
        answer += (str(i)*min(x.count(str(i)), y.count(str(i))))
    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer 