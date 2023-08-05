def solution(n, lost, reserve):
    member = [1]*(n+2)
    cnt = 0 
    for i in range(1, n+1):
        if i in lost:
            member[i] -= 1 
        if i in reserve:
            member[i] += 1 
    for i in range(1, n+1):
        if member[i] == 2:
            if member[i-1] == 0:
                member[i-1] += 1 
                member[i] -= 1 
            elif member[i+1] == 0:
                member[i+1] += 1 
                member[i] -= 1 
    for i in range(1, n+1):
        if member[i] >= 1:
            cnt += 1 
    return cnt