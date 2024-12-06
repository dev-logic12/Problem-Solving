def solution(n):
    spiral = [[0] * n for _ in range(n)]  # 초기화
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위
    row, col = 0, 0  # 시작 위치
    direction_index = 0  # 방향 인덱스
    
    for num in range(1, n**2 + 1):
        spiral[row][col] = num
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        # 다음 위치가 경계를 벗어나거나 이미 채워져 있는 경우 방향 전환
        if not (0 <= next_row < n and 0 <= next_col < n and spiral[next_row][next_col] == 0):
            direction_index = (direction_index + 1) % 4  # 방향 전환
            next_row = row + directions[direction_index][0]
            next_col = col + directions[direction_index][1]
        
        row, col = next_row, next_col
    
    return spiral
