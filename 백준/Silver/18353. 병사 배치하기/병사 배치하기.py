import sys 

n = int(sys.stdin.readline())

soldiers = list(map(int, sys.stdin.readline().split()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))