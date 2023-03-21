'''
1,2,3,1이 완성되면 
cnt를 하나씩 올리고 
마지막에 cnt를 리턴하기 
'''


def solution(ingredient):
    answer = []
    cnt = 0 
    for i in ingredient:
        answer.append(i)
        if answer[-4:] == [1,2,3,1]:
            cnt += 1 
            for _ in range(4):
                answer.pop()
    return cnt