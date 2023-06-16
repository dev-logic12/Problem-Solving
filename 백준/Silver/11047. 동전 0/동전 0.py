n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]
cnt = 0
coins.reverse()
for coin in coins:
    cnt += k // coin
    k%= coin
print(cnt)