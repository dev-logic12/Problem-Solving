def solution(common):
    answer = 0
    for i in range(len(common)):
        if common[i+1] - common[i] == common[i+2] - common[i+1]:
            return common[-1] + int(common[i+2] - common[i+1])
        else:
            return common[-1]*int(common[i+1]//common[i])