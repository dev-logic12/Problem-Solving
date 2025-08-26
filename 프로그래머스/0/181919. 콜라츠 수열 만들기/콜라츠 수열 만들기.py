def solution(n):
    answer = [n]
    append = answer.append   
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        append(n)
    return answer
