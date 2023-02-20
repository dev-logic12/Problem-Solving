def solution(n):
    if n == 1:
        return 1
    for i in range(1, int(n**0.5)+1):
        if n == i**2:
            return 1
    return 2
