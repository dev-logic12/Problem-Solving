def solution(n, lost, reserve):
    answer = [1]*(n+2)
    cnt = 0 
    for i in range(1,n+1):
        if i in lost:
            answer[i] -=1 
        if i in reserve:
            answer[i] += 1 
    for i in range(1, n+1):
        if answer[i] == 2:
            if answer[i-1] == 0:
                answer[i] -= 1 
                answer[i-1] += 1 
            elif answer[i+1] == 0:
                answer[i] -= 1 
                answer[i+1] +=1 
    for i in range(1, len(answer)-1):
        if answer[i] >= 1:
            cnt += 1 
    return cnt 