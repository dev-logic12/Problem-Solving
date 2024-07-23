def solution(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    size = max(rows, cols)
    
    for i in range(rows):
        arr[i].extend([0] * (size - cols))
    
    for i in range(rows, size):
        arr.append([0] * size)
    
    return arr
