def solution(n):
    # 초기화: n x n 크기의 배열을 0으로 초기화
    answer = [[0] * n for _ in range(n)]
    
    # 방향 벡터: 우(0,1), 하(1,0), 좌(0,-1), 상(-1,0)
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    x, y, m = 0, 0, 0  # 시작 위치와 방향 초기화
    for i in range(1, n**2 + 1):
        answer[y][x] = i  # 현재 위치에 값을 넣기
        # 다음 위치 계산
        next_y, next_x = y + move[m][0], x + move[m][1]
        
        # 다음 위치가 경계 바깥이거나 이미 숫자가 채워져 있는 경우 방향 전환
        if not (0 <= next_y < n and 0 <= next_x < n and answer[next_y][next_x] == 0):
            m = (m + 1) % 4  # 방향 전환
            
        # 새로운 위치로 이동
        y, x = y + move[m][0], x + move[m][1]
    
    return answer

# 테스트 예제
print(solution(3))  # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(solution(4))  # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
