def solution(n):
    answer = ''

    while(n >= 1):
        rest = n%3
        n = n//3
        answer += str(rest)
    #int(value, base)
    return int(answer, 3)
