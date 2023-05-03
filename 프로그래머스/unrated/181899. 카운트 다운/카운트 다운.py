def solution(start, end):
    answer = []
    answer1 = []
    for i in range(0, 51):
        answer.append(i)
    answer1 = answer[end: start+1]
    answer1.sort(reverse = True)
    return answer1

# start = 10 
# end = 3 
# print(solution(start, end))