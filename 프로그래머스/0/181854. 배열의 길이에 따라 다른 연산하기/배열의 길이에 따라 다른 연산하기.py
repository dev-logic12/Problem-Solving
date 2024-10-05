def solution(arr, n):
    answer = 0 if len(arr) % 2 else 1
    for i in range(answer, len(arr), 2):
        arr[i] += n
    return arr
