def solution(strArr):
    answer = []
    for i in strArr:   
        if i in strArr[0::2]:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
    return answer

strArr = ["AAA","BBB","CCC","DDD"]	
print(solution(strArr))