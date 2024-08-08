def solution(board, k):
    answer = 0
    n, m = len(board), len(board[0])

    for i in range(n):
        max_j = min(m - 1, k - i)
        for j in range(max_j + 1):
            answer += board[i][j]
    
    return answer
