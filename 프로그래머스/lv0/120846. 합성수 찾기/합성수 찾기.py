
def solution(n):
    answer = 0
    for i in range(3,n+1) :
        temp = 1
        for j in range(1,i) :
            if i % j == 0 :
                temp += 1

        if temp > 2 :
            answer += 1
    return answer