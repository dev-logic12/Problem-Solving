import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = [input() for _ in range(n)]
change_chess = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j) % 2 and chess[i][j] != 'B':
            change_chess[i][j] = 1
        elif not (i+j) % 2 and chess[i][j] != 'W':
            change_chess[i][j] = 1

res = []
for i in range(n-7):
    for j in range(m-7):
        cnt = sum([sum(change_chess[i+k][j:j+8]) for k in range(8)])
        res += [cnt, 64-cnt]
print(min(res))