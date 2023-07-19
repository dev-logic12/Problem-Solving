def solution(arr):
    row = len(arr)
    col = len(arr[0])

    if row > col:
        diff = row - col
        for i in range(row):
            for _ in range(diff):
                arr[i].append(0)

    elif col > row:
        diff = col - row
        for _ in range(diff):
            arr.append([0] * col)

    return arr

