import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# dp1[i][j] : i 포함해서 j까지의 구간합
# dp2[i][j] : i 포함 안하고 j까지의 구간합
dp1 = [[0]+[-1e9]*M for _ in range(N+1)]
dp2 = [[0]+[-1e9]*M for _ in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    for j in range(1, min((i+1)//2, M)+1):
        dp2[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j-1]) + num

print(max(dp1[N][M], dp2[N][M]))