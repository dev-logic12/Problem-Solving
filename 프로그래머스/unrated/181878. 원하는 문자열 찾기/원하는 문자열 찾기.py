def solution(myString, pat):
    answer = 0
    a = myString.upper()
    b = pat.upper()
    if b in a:
        return 1 
    else:
        return 0
