def solution(myString, pat):
    myString1 = myString.lower()
    pat1 = pat.lower()
    return 1 if pat1 in myString1 else 0