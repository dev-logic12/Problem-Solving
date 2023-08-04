from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    queue = deque()
    queue.append((0, 0))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[0][0] = True
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    maps[ny][nx] = maps[y][x] + 1
                    
    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]
