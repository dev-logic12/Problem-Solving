def solution(board, k):
    answer = 0
    n, m = len(board), len(board[0])

    for i in range(n):
        sum_j = min(k - i, m - 1)
        for j in range(sum_j + 1):
            answer += board[i][j]

    return answer
