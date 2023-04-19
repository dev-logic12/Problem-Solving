def solution(board, skill):
    # 보드 크기 설정
    R, C = len(board) + 1, len(board[0]) + 1
    # diff 리스트 초기화
    diff = [[0] * C for _ in range(R)]

    # 각 스킬 적용
    for t, r1, c1, r2, c2, d in skill:
        d *= -1 if t == 1 else 1
        set_diff(diff, r1, c1, r2, c2, d)

    # diff 리스트 누적합 계산
    for i in range(1, R):
        diff[i][0] += diff[i - 1][0]
        diff[0][i] += diff[0][i - 1]

    # 보드의 양수 칸 개수 계산
    ans = 0
    for i in range(1, R):
        for j in range(1, C):
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
            ans += 1 if board[i - 1][j - 1] + diff[i - 1][j - 1] > 0 else 0
    return ans

def set_diff(diff, r1, c1, r2, c2, d):
    # diff 리스트 갱신
    diff[r1][c1] += d
    diff[r2 + 1][c2 + 1] += d
    diff[r2 + 1][c1] -= d
    diff[r1][c2 + 1] -= d
