def solution(n):
    arr = [[0] * n for _ in range(n)]
    
    return [[1 if bi == i else b for bi, b in enumerate(a)] for i, a in enumerate(arr)]

