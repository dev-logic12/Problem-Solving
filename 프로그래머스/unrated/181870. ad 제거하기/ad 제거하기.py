def solution(strArr):
    answer = []
    for i in strArr:
        if 'ad' not in i:
            answer.append(i)
    return answer

# strArr = ["and","notad","abcd"]	
# print(solution(strArr))