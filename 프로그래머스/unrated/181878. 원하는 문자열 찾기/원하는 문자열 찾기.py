def solution(myString, pat):
    answer = 0
    myString1 = myString.lower()
    pat1 = pat.lower()
    for i in myString:
        if pat1 in myString1:
            return 1 
        else:
            return 0
    return answer