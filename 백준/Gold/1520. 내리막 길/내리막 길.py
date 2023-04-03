import sys

sys.setrecursionlimit(10**6) # recursion limit 를 설정해줍니다.

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)] # -1 로 초기화

dx = [-1, 0, 1, 0] # 상하좌우
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x == n-1 and y == m-1: # 종료 조건
        return 1

    if dp[x][y] != -1: # 이미 계산한 값이면 바로 반환
        return dp[x][y]

    dp[x][y] = 0 # 처음에는 0으로 초기화

    for i in range(4): # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m: # 지도를 벗어나지 않는 경우
            if graph[x][y] > graph[nx][ny]: # 현재 위치의 값이 더 클 경우
                dp[x][y] += dfs(nx, ny) # dp 값 갱신

    return dp[x][y]

print(dfs(0, 0)) # (0, 0) 에서 시작
