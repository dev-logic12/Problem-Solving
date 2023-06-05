def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    # 행의 수가 더 많은 경우
    if row_len > col_len:
        diff = row_len - col_len
        for i in range(row_len):
            for _ in range(diff):
                arr[i].append(0)

    # 열의 수가 더 많은 경우
    elif col_len > row_len:
        diff = col_len - row_len
        for _ in range(diff):
            arr.append([0] * col_len)

    return arr

