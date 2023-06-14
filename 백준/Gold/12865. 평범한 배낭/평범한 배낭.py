def recur(cur, w):
    global ans

    if w > m:  # 무게 제한을 초과한 경우
        return -9999999

    if cur == n:  # 마지막 아이템까지 확인한 경우
        return 0

    if dp[cur][w] != -1:  # 이미 계산한 경우
        return dp[cur][w]

    # 현재 아이템을 선택한 경우와 선택하지 않은 경우 중 더 큰 가치를 선택하여 저장
    dp[cur][w] = max(recur(cur + 1, w + arr[cur][0]) + arr[cur][1], recur(cur + 1, w))

    return dp[cur][w]

n, m = map(int, input().split())  # 아이템 개수(n)와 무게 제한(m)을 입력받음
arr = [list(map(int, input().split())) for i in range(n)]  # 각 아이템의 무게와 가치를 입력받음

dp = [[-1 for _ in range(100010)] for j in range(n)]  # 메모이제이션을 위한 배열 초기화

ans = recur(0, 0)  # 재귀 함수 호출

print(ans)  # 최대 가치 출력
