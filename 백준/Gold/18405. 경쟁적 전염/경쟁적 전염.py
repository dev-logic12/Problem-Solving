from collections import deque
n, k = map(int, input().split())
gragh = []
data = []

for i in range(n):
    gragh.append(list(map(int, input().split())))
    for j in range(n):
        if gragh[i][j] != 0:
            data.append((gragh[i][j], 0, i, j))
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if gragh[nx][ny] == 0:
                gragh[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
print(gragh[target_x -1][target_y -1])
