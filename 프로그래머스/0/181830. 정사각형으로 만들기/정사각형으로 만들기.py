def solution(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    
    if rows > cols:
        for i in range(rows):
            arr[i].extend([0] * (rows - cols))
    elif cols > rows:
        for i in range(cols - rows):
            arr.append([0] * cols)
    
    return arr
