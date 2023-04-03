import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# dp[i]는 i원을 만드는 경우의 수를 저장합니다.
dp = [0] * (k+1)
dp[0] = 1

# 동전의 가치를 하나씩 확인하면서 dp 테이블을 갱신합니다.
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

# k원을 만드는 경우의 수 출력
print(dp[k])
