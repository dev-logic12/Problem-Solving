'''
문자열로 만들고 
int로 받아서 하나씩 더하기 
더한 값을 더하기 
'''

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)    
    return answer