def solution(myString, pat):
    answer = int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString) 
    return answer