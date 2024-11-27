def solution(arr):
    n, m = len(arr), len(arr[0])
    if n > m:
        for row in arr:
            row.extend([0] * (n - m))
    elif n < m:
        arr.extend([[0] * m for _ in range(m - n)])
    return arr
