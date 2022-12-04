def solution(n):
    s = 0
    for i in range(2, n+1, 2):
        s += i
    return s 