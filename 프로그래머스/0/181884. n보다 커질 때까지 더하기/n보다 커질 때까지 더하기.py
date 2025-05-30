def solution(numbers, n):
    sum = 0
    for e in numbers:
        if sum > n:
            return sum
        else:
            sum += e
    return sum