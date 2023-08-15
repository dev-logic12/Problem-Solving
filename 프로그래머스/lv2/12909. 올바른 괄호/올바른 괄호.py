def solution(s):
    answer = 0
    for c in s :
        if c == '(' : answer += 1
        elif c == ')' : answer -= 1
        if answer < 0 : return False
    return answer == 0
