def solution(n):
    # n x n 크기의 배열 생성
    array = [[0] * n for _ in range(n)]

    # 배열 내에서 이동할 방향을 정의 (시계방향: 오른쪽, 아래, 왼쪽, 위)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 현재 위치와 이동 방향 초기화
    x, y = 0, 0
    direction = 0

    # 배열에 값을 채워 나감
    for i in range(1, n * n + 1):
        array[x][y] = i

        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 다음 위치가 배열 범위를 벗어나거나 이미 값이 채워진 경우 방향을 변경
        if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]

        # 다음 위치로 이동
        x, y = nx, ny

    return array
