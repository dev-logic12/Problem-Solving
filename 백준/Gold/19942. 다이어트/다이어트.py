def recur(idx, p, f, c, v, price):
    global answer, used, answer_used

    if p >= protein and f >= fat and c >= carbo and v >= vitamin and answer > price:
        answer = price
        answer_used = used[:]

    if idx == n:
        return

    used.append(idx + 1)
    recur(idx + 1, p + ing[idx][0], f + ing[idx][1], c + ing[idx][2], v + ing[idx][3], price + ing[idx][4])
    used.pop()
    recur(idx + 1, p, f, c, v, price)


n = int(input())
protein, fat, carbo, vitamin = map(int, input().split())
ing = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')
used = []
answer_used = []

recur(0, 0, 0, 0, 0, 0)

answer_used.sort()

if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)
