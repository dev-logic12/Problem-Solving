from collections import deque

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    row, col = map(int, input().split())
    apples.append((row, col))
    
l = int(input())
moves = []
for _ in range(l):
    x, c = input().split()
    moves.append((int(x), c))

# 동, 남, 서, 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 초기 뱀의 위치와 방향 설정
snake = deque([(1, 1)])
direction = 0

time = 0
move_idx = 0

while True:
    time += 1
    
    # 다음 칸 위치
    ny = snake[0][0] + dy[direction]
    nx = snake[0][1] + dx[direction]
    
    # 벽에 부딪히거나 자기 자신의 몸에 부딪힌 경우
    if ny < 1 or ny > n or nx < 1 or nx > n or (ny, nx) in snake:
        break
    
    # 다음 칸에 사과가 있는 경우
    if (ny, nx) in apples:
        apples.remove((ny, nx))
    else:
        snake.pop()
    
    snake.appendleft((ny, nx))
    
    # 방향 전환
    if move_idx < l and time == moves[move_idx][0]:
        if moves[move_idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        move_idx += 1
        
print(time)
