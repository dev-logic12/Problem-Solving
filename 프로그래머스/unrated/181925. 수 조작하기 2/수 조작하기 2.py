def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        if int(numLog[i+1])-int(numLog[i]) == 1:
            answer += 'w'
        elif int(numLog[i+1]) - int(numLog[i]) == -1:
            answer += 's'
        elif int(numLog[i+1]) -int(numLog[i]) == 10:
            answer += 'd'
        elif int(numLog[i+1]) - int(numLog[i]) == -10:
            answer+= 'a'
    return answer