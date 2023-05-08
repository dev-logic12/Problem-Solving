def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer += i.replace('a', 'A')
        elif i == 'A':
            answer += i 
        elif i.isupper() == True:
            answer += i.lower()
        else:
            answer += i 
    return answer