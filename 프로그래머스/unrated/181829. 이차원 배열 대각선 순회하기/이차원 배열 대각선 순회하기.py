def solution(board, k):
    m = len(board)
    n = len(board[0])
    total_sum = 0
    
    for i in range(m):
        for j in range(n):
            if i + j <= k:
                total_sum += board[i][j]
    
    return total_sum
