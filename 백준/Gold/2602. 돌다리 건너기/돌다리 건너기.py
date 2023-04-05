import sys  # sys 모듈 import

# 입력 값을 처리하기 위한 함수 정의
input = lambda: sys.stdin.readline().rstrip()

# 첫번째 문자열 값
target = input()

# 두번째 문자열 값
s1 = input()

# 세번째 문자열 값
s2 = input()

# dp 배열 초기화
dp = [[[0] * 2 for _ in range(len(target))] for _ in range(len(s1))]

# 첫번째 열 초기화
for i in range(len(s1)):
    if s1[i] == target[0]:
        dp[i][0][0] = 1
    if s2[i] == target[0]:
        dp[i][0][1] = 1

# dp 배열 갱신
for i in range(len(s1)):
    for j in range(1, len(target)):
        if s1[i] == target[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j-1][1]

        if s2[i] == target[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j-1][0]

# dp 배열의 값을 모두 더해서 answer에 저장
answer = 0
for i in range(len(s1)):
    answer += (dp[i][len(target)-1][0] + dp[i][len(target)-1][1])

# 결과 출력
print(answer)
