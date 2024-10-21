def solution(n):
    answer = [[None] * n for _ in range(n)]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        next_y, next_x = y + move[m][0], x + move[m][1]
        if not (0 <= next_y < n and 0 <= next_x < n) or answer[next_y][next_x] is not None:
            m = (m + 1) % 4
        y, x = y + move[m][0], x + move[m][1]
    return answer
