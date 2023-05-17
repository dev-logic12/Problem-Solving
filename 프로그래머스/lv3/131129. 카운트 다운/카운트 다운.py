def solution(target):
    dp = [[float('inf'), 0] for _ in range(300000)]

    targetList = [i + 1 for i in range(20)]

    dp[0][0] = 0

    for i in range(target):
        def check(addIdx, count):
            if dp[i + addIdx][0] >= dp[i][0] + 1:
                if dp[i + addIdx][0] == dp[i][0] + 1:
                    dp[i + addIdx][1] = max(dp[i + addIdx][1], dp[i][1] + count)
                else:
                    dp[i + addIdx] = [dp[i][0] + 1, dp[i][1] + count]

        for j in targetList:
            for v, c in [[1, 1], [2, 0], [3, 0]]:
                check(j * v, c)

        check(50, 1)

    return dp[target]
