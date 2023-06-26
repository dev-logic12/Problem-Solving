from collections import deque

def calculate_cost(current_direction, next_direction, current_cost):
    # 현재 방향과 다음 방향이 동일한 경우 또는 상하 혹은 좌우 방향인 경우 100을 추가한 비용 반환
    if (current_direction in ('R', 'L') and next_direction in ('L', 'R')) or (current_direction in ('D', 'U') and next_direction in ('D', 'U')):
        return current_cost + 100
    # 그 외의 경우 600을 추가한 비용 반환
    return current_cost + 600

def bfs(start_x, start_y, initial_cost, initial_direction):
    queue = deque([(start_x, start_y, initial_cost, initial_direction)])
    checked = [[0 for _ in range(N)] for _ in range(N)]
    checked[start_x][start_y] = 1
    while queue:
        x, y, cost, current_direction = queue.popleft()
        # 목적지에 도착한 경우 최소 비용을 answer에 추가하고 다음으로 넘어감
        if x == N-1 and y == N-1:
            answer.append(cost)
            continue
        # 상하좌우 방향 탐색
        for i, j, d in [(0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')]:
            new_x, new_y, new_cost = x+i, y+j, calculate_cost(current_direction, d, cost)
            # 새로운 좌표가 범위를 벗어나거나 벽인 경우 무시
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N or new_board[new_x][new_y]:
                continue
            # 새로운 좌표의 방문 여부를 확인하고, 비용이 더 작은 경우에만 큐에 추가
            if not checked[new_x][new_y] or checked[new_x][new_y] > new_cost:
                checked[new_x][new_y] = new_cost
                queue.append((new_x, new_y, new_cost, d))

def solution(board):
    global N, checked, new_board, answer
    answer = []
    N = len(board)
    new_board = [board[i][:] for i in range(N)]
    # 오른쪽 방향과 아래쪽 방향에서 시작하는 BFS 탐색
    bfs(0, 0, 0, 'R')
    bfs(0, 0, 0, 'D')
    # answer 리스트에서 최소 비용 반환
    return min(answer)
