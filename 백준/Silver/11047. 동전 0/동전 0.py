n, k = map(int, input().split())
coins = []  # 동전의 가치를 저장할 리스트
cnt = 0 

for i in range(n):
    coin = int(input())  # 동전의 가치를 입력받음
    coins.append(coin)  # 동전의 가치를 coins 리스트에 저장
coins.sort(reverse=True)  # coins 리스트를 가치가 큰 순서대로 정렬

for coin in coins:
    if coin <= k:
        cnt += k // coin  # 현재 동전으로 만들 수 있는 개수를 cnt에 더함
        k %= coin  # k를 현재 동전으로 만들고 남은 나머지로 갱신

print(cnt)
