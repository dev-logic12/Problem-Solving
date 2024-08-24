def solution(myString, pat):
    alter = myString.replace('A', 'b').replace('B', 'a')
    return 1 if pat.lower() in alter else 0 