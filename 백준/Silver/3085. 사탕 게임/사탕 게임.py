import sys
input = sys.stdin.readline

N = int(input())
board = [list(input()) for _ in range(N)]
maxCnt = 0

def check():
    global maxCnt
    for i in range(N):
        cnt = 1     # 행을 검사
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1

        cnt = 1     # 열을 검사
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1

for i in range(N):
    for j in range(N):
        # 오른쪽과 바꿈
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 아래쪽과 바꿈
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(maxCnt)

#return 최대 사탕의 개수 




