from math import factorial

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if factorial(i) > n:
            return i-1
        elif factorial(i) == n:
            return i
        
            