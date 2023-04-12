import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 그래프 생성 및 초기화
graph = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

# dp 배열 생성 및 초기화
dp = [[0] * M for _ in range(N)]
dp[0][0] = graph[0][0] # 시작 위치 초기화

# 첫 행 초기화
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + graph[0][j]

# 첫 열 초기화
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + graph[i][0]

# dp 배열 채우기
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + graph[i][j]

# 결과 출력
print(dp[N-1][M-1])

