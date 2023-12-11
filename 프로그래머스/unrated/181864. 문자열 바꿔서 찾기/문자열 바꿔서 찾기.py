def solution(myString, pat):
    answer = myString.replace('A', 'b').replace('B', 'a')
    return 1 if pat.lower() in answer else 0 