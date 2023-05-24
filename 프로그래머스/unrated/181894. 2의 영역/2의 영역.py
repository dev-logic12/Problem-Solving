def solution(arr):
    try:
        start = arr.index(2)
        end = len(arr) - arr[::-1].index(2) -1
        return arr[start:end+1]
    except ValueError:
        return [-1]
