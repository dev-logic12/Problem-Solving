def solution(board, k):

    total_sum = 0  # 결과 값을 저장할 변수
    rows, cols = len(board), len(board[0])  # 행(row)과 열(column)의 크기

    # 각 행을 순회
    for i in range(rows):
        # 현재 행에서 열의 범위를 결정 (k - i와 cols - 1 중 더 작은 값까지 탐색)
        max_col = min(k - i, cols - 1)
        for j in range(max_col + 1):
            total_sum += board[i][j]  # 해당 값을 누적

    return total_sum
