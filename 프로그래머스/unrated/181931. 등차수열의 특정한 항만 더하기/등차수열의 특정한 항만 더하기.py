def solution(a, d, included):
    result = 0 
    for i in range(len(included)):
        if included[i]:
            result += a + (i*d)
    return result 
    # answer = a + 4*d
    # for i in included:
    #     if included[i] == 'true':
    #         answer += included[i]
    # return answer